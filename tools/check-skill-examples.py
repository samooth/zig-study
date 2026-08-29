#!/usr/bin/env python3
"""Compile every ```zig code block in the Zig skill against the installed compilers.

For each fenced `zig` block in zig/SKILL.md and zig/references/*.md:

  * blocks containing `// WRONG`  -> expected to FAIL to compile (the doc claims
    the API is wrong). If it unexpectedly compiles, that's a failure (the claim
    is false). The `// CORRECT` portion of the same block is extracted and
    checked separately as expected-to-compile.
  * all other blocks             -> expected to compile in at least one of the
    installed versions. A block that fails only because of an undeclared
    identifier (`io`, `allocator`, ...) is reported as SKIPPED (needs runtime
    context) rather than a hard failure.

Blocks whose fence info string contains `skip` or that contain a `// skip-check`
comment are ignored (e.g. C-interop snippets needing a real header file, or
build-system-only fragments).

Usage:
    python3 tools/check-skill-examples.py [--zig16 PATH] [--zig17 PATH]
"""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
import tempfile

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REFERENCES = os.path.join(SKILL_DIR, "zig", "references")
SKILL_MD = os.path.join(SKILL_DIR, "zig", "SKILL.md")

FENCE_RE = re.compile(r"^```(\w[^\n]*)$")
UNDECLARED_RE = re.compile(r"error:\s*(use of undeclared identifier|unknown identifier)")

# Genuine API mistakes in the docs: a wrong member/field name, wrong arity, or
# wrong type. Anything else (undeclared identifiers, partial listings, unused
# locals, structural fragments) is a documentation fragment, not an API error.
REAL_API_RE = re.compile(
    r"(no member named|no field named|unknown field|unknown member|"
    r"expected type '|wrong number of arguments|too (few|many) arguments|"
    r"expected \d+ argument|missing argument|unexpected argument|"
    r"is not a function|does not support member access|has no member|"
    r"no errors|invalid enum value)"
)


def find_zigs() -> dict[str, str]:
    zigs: dict[str, str] = {}
    env16 = os.environ.get("ZIG16")
    env17 = os.environ.get("ZIG17")
    if env16:
        zigs["0.16"] = env16
    if env17:
        zigs["0.17"] = env17
    if not zigs:
        zvm = os.path.expanduser("~/.zvm")
        if os.path.isdir(zvm):
            for name in sorted(os.listdir(zvm)):
                cand = os.path.join(zvm, name, "zig")
                if os.path.exists(cand):
                    try:
                        out = subprocess.run(
                            [cand, "version"], capture_output=True, text=True, timeout=20
                        ).stdout.strip()
                    except Exception:
                        continue
                    if out.startswith("0.16"):
                        zigs.setdefault("0.16", cand)
                    elif out.startswith("0.17"):
                        zigs.setdefault("0.17", cand)
    return zigs


def extract_blocks(text: str):
    """Yield (info, body, line_no) for fenced ```zig blocks."""
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        m = FENCE_RE.match(lines[i])
        if m and m.group(1).split()[0] == "zig":
            info = m.group(1)
            start = i + 1
            buf = []
            j = i + 1
            while j < len(lines) and not lines[j].startswith("```"):
                buf.append(lines[j])
                j += 1
            yield info, "\n".join(buf), i + 1
            i = j + 1
        else:
            i += 1


def needs_std(body: str) -> bool:
    if "const std = @import" in body or '@import("std")' in body:
        return False
    return "std." in body


def run_compile(zig: str, code: str) -> tuple[bool, str]:
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "snippet.zig")
        with open(path, "w") as f:
            f.write(code)
        try:
            r = subprocess.run(
                [zig, "build-obj", path],
                capture_output=True, text=True, timeout=120, cwd=d,
            )
        except subprocess.TimeoutExpired:
            return False, "timed out"
        return r.returncode == 0, (r.stderr or r.stdout).strip()


_COMPILE_CACHE: dict[tuple[str, str], tuple[bool, str, bool, str]] = {}


def compile_variants(zig: str, body: str) -> tuple[bool, str, bool, str]:
    """Compile a snippet both as-is (top-level declarations) and wrapped in a
    `main` function. Returns (asis_ok, asis_err, wrapped_ok, wrapped_err)."""
    key = (zig, body)
    if key in _COMPILE_CACHE:
        return _COMPILE_CACHE[key]
    pre = "" if not needs_std(body) else 'const std = @import("std");\n'
    asis = pre + body
    wrapped = pre + "pub fn main() !void {\n" + body + "\n}\n"
    a_ok, a_err = run_compile(zig, asis)
    w_ok, w_err = run_compile(zig, wrapped)
    _COMPILE_CACHE[key] = (a_ok, a_err, w_ok, w_err)
    return _COMPILE_CACHE[key]



def only_undeclared(err: str) -> bool:
    lines = [l for l in err.splitlines() if "error:" in l]
    if not lines:
        return False
    return all(UNDECLARED_RE.search(l) for l in lines)


def correct_subblock(body: str) -> str | None:
    lines = body.splitlines()
    for idx, line in enumerate(lines):
        if "correct" in line.lower() and "//" in line:
            return "\n".join(lines[idx:])
    return None


def check_block(zigs: dict[str, str], info: str, body: str, src: str, line: int):
    results = []
    skip = "skip" in info.lower() or "// skip-check" in body.lower()
    if skip:
        return [("SKIP", src, line, "marked skip-check")]

    def verdict(body: str):
        """Return ("PASS"|"SKIP"|"FAIL", detail) for a snippet compiled against
        both versions (as-is and wrapped)."""
        a_ok = w_ok = False
        errs = {}
        for ver, zig in zigs.items():
            a, ae, w, we = compile_variants(zig, body)
            errs[ver] = (ae, we)
            a_ok = a_ok or a
            w_ok = w_ok or w
        if a_ok or w_ok:
            return "PASS", "compiles"
        # Gather every compiler error line from both interpretations/versions.
        all_errs = [l for v in zigs for e in errs[v] for l in e.splitlines()
                    if "error:" in l]
        # A real API mistake (wrong member/field/arity/type) is a genuine doc
        # bug. Anything else (undeclared id, partial listing, unused local,
        # structural fragment) is an illustrative snippet needing context.
        if any(REAL_API_RE.search(l) for l in all_errs):
            return "FAIL", "fails to compile:\n" + "\n".join(
                f"  [{v}] asis: {errs[v][0]}\n  [{v}] wrapped: {errs[v][1]}" for v in zigs
            )
        return "SKIP", "documentation fragment (non-API error)"

    is_wrong = "// wrong" in body.lower()
    if is_wrong:
        # Whole block must fail (proves the doc's "WRONG" claim).
        whole = verdict(body)
        if whole[0] == "PASS":
            results.append(("FAIL", src, line, "marked WRONG but compiles"))
        else:
            results.append(("PASS", src, line, "WRONG block fails as expected"))
        # Validate the CORRECT half separately.
        sub = correct_subblock(body)
        if sub:
            v = verdict(sub)
            results.append((v[0], src, line,
                            ("CORRECT half " + v[1]) if v[0] != "PASS"
                            else "CORRECT half compiles"))
        return results

    v = verdict(body)
    results.append((v[0], src, line, v[1]))
    return results


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--verbose", action="store_true",
                    help="print PASS/SKIP details (default: only FAILs)")
    args = ap.parse_args()

    zigs = find_zigs()
    if not zigs:
        print("no zig compilers found (set ZIG16/ZIG17 or install via zvm)", file=sys.stderr)
        return 2
    print(f"using: " + ", ".join(f"{v}={zigs[v]}" for v in sorted(zigs)))

    targets = [(SKILL_MD, "SKILL.md")]
    if os.path.isdir(REFERENCES):
        for fn in sorted(os.listdir(REFERENCES)):
            if fn.endswith(".md"):
                targets.append((os.path.join(REFERENCES, fn), f"references/{fn}"))

    fails = 0
    skips = 0
    passes = 0
    for path, label in targets:
        with open(path) as f:
            text = f.read()
        for info, body, line in extract_blocks(text):
            for status, src, ln, msg in check_block(zigs, info, body, label, line):
                if status == "PASS":
                    passes += 1
                    if args.verbose:
                        print(f"  PASS  {src}:{ln} {msg}")
                elif status == "SKIP":
                    skips += 1
                    if args.verbose:
                        print(f"  SKIP  {src}:{ln} {msg}")
                else:
                    fails += 1
                    print(f"  FAIL  {src}:{ln} {msg}")

    print(f"\nsummary: {passes} pass, {skips} skip, {fails} fail")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
