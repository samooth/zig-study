#!/usr/bin/env python3
"""Verify generated Zig signature tables against the installed stdlib.

Usage:
    python3 tools/verify.py --zig /home/t0m4s/.zvm/0.17.0/zig

Parses the generated <map>/NN-function-signatures.md and functions.html,
and checks that every listed function name actually exists in the
installed <zig>/lib/std. Also enforces a few hard rules (no IoUring
outside os.linux, no ThreadSafeAllocator/SbrkAllocator). Exits non-zero
if any mismatch is found.
"""
import argparse
import glob
import os
import re
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LABEL_TO_NUM = {"0.16.0": "09", "0.17.0": "05"}


def version_of(zig):
    out = subprocess.run([zig, "version"], capture_output=True, text=True)
    if out.returncode != 0:
        sys.exit(f"failed to run `{zig} version`")
    return out.stdout.strip()


def short_label(version):
    if version.startswith("0.16"):
        return "0.16.0"
    if version.startswith("0.17"):
        return "0.17.0"
    parts = version.split(".")
    return f"{parts[0]}.{parts[1]}.0"


def source_fns(std_dir):
    s = set()
    for path in glob.glob(os.path.join(std_dir, "**", "*.zig"), recursive=True):
        try:
            t = open(path, encoding="utf-8", errors="ignore").read()
        except OSError:
            continue
        for m in re.finditer(r"\bfn\s+([A-Za-z_]\w*)\s*\(", t):
            s.add(m.group(1).lower())
    return s


def listed_names(md_path, html_path):
    names = set()
    if md_path and os.path.exists(md_path):
        for line in open(md_path, encoding="utf-8", errors="ignore"):
            m = re.match(r"^\|\s*`([^`]+)`\s*\|", line)
            if m:
                names.add(m.group(1).lower())
    if html_path and os.path.exists(html_path):
        t = open(html_path, encoding="utf-8", errors="ignore").read()
        for m in re.finditer(r'data-name="([^"]+)"', t):
            names.add(m.group(1).lower())
        for m in re.finditer(r'data-n="([^"]+)"', t):
            names.add(m.group(1).lower())
    return names


def hard_rule_violations(md_path, html_path):
    violations = []
    texts = []
    for p in (md_path, html_path):
        if p and os.path.exists(p):
            texts.append(open(p, encoding="utf-8", errors="ignore").read())
    blob = "\n".join(texts)
    # The only legitimate `IoUring` is `os.linux.IoUring` (in any of its
    # separator spellings). The false form is the `Io` module's Uring.
    if re.search(r"std\.Io\.IoUring|Io / IoUring|Io---IoUring|Io___IoUring", blob):
        violations.append("found `Io.IoUring` (should be `Io.Uring`)")
    for bad in ("ThreadSafeAllocator", "SbrkAllocator"):
        if bad in blob:
            violations.append(f"found forbidden module `{bad}`")
    return violations


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--zig", required=True)
    args = ap.parse_args()

    version = version_of(args.zig)
    label = short_label(version)
    std_dir = os.path.join(os.path.dirname(os.path.abspath(args.zig)), "lib", "std")
    if not os.path.isdir(std_dir):
        sys.exit(f"std lib not found at {std_dir}")

    num = LABEL_TO_NUM.get(label)
    if not num:
        sys.exit(f"no signature-file slot for version {label}")
    map_dir = os.path.join(REPO, f"zig-{label}-resource-map")
    md_path = os.path.join(map_dir, f"{num}-function-signatures.md")
    html_path = os.path.join(map_dir, "functions.html")

    src = source_fns(std_dir)
    listed = listed_names(md_path, html_path)
    missing = sorted(n for n in listed if n not in src)
    violations = hard_rule_violations(md_path, html_path)

    print(f"[{version}] source pub fns: {len(src)} | listed: {len(listed)}")
    ok = True
    if missing:
        ok = False
        print(f"  FAIL: {len(missing)} listed functions not found in source:")
        for n in missing[:50]:
            print(f"    - {n}")
        if len(missing) > 50:
            print(f"    ... and {len(missing) - 50} more")
    if violations:
        ok = False
        for v in violations:
            print(f"  FAIL rule: {v}")
    if ok:
        print("  OK: all listed functions exist in source and no forbidden terms.")
        sys.exit(0)
    sys.exit(1)


if __name__ == "__main__":
    main()
