#!/usr/bin/env python3
"""Generate Zig stdlib function-signature tables + HTML viewer.

Usage:
    python3 tools/gen.py --zig <zvm-root>/0.17.0/zig

Walks <zig>/lib/std, extracts every `pub fn` signature, groups them by
module, and writes:
  - <repo>/zig-<ver>-resource-map/NN-function-signatures.md
  - <repo>/zig-<ver>-resource-map/functions.html

The output is stamped with the exact `zig version` so docs stay pinned to
the compiler they were generated against.
"""
import argparse
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


def extract_sigs(text):
    """Return list of (name, full_signature) for every `pub fn` in `text`."""
    out = []
    i = 0
    n = len(text)
    while i < n:
        idx = text.find("pub", i)
        if idx < 0:
            break
        if idx > 0 and (text[idx - 1].isalnum() or text[idx - 1] == "_"):
            i = idx + 3
            continue
        rest = text[idx + 3 :]
        m = re.match(r"\s+(?:inline\s+|extern\s+)?fn\s+([A-Za-z_]\w*)\s*\(", rest)
        if not m:
            i = idx + 3
            continue
        name = m.group(1)
        p = text.find("(", idx)
        if p < 0:
            i = idx + 3
            continue
        depth = 0
        j = p
        in_str = None
        while j < n:
            c = text[j]
            if in_str:
                if c == "\\":
                    j += 2
                    continue
                if c == in_str:
                    in_str = None
            elif c == '"' or c == "'":
                in_str = c
            elif c == "(":
                depth += 1
            elif c == ")":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        k = j + 1
        while k < n and text[k] not in "{;":
            k += 1
        sig = text[idx:k]
        sig = re.sub(r"\s+", " ", sig).strip()
        out.append((name, sig))
        i = j + 1
    return out


def collect(std_dir):
    modules = []
    for root, _, files in os.walk(std_dir):
        for fn in files:
            if not fn.endswith(".zig"):
                continue
            if fn.endswith("_test.zig"):
                continue
            path = os.path.join(root, fn)
            rel = os.path.relpath(path, std_dir)[:-4]  # drop .zig
            base = os.path.basename(rel)
            if base in ("std", "zig"):
                continue
            label = rel.replace("/", " / ")
            try:
                text = open(path, encoding="utf-8", errors="ignore").read()
            except OSError:
                continue
            sigs = extract_sigs(text)
            if sigs:
                modules.append((label, sigs))
    modules.sort(key=lambda x: x[0].lower())
    return modules


def render_md(version, modules):
    lines = [
        f"# Zig {version} — Function Signatures",
        "",
        f"Source: `<zig-install-dir>/lib/std`  (generated against `{version}`)",
        "",
    ]
    for label, sigs in modules:
        lines.append(f"## {label}")
        lines.append("")
        lines.append("| Function | Signature |")
        lines.append("|----------|-----------|")
        for name, sig in sigs:
            lines.append(f"| `{name}` | `{sig}` |")
        lines.append("")
    return "\n".join(lines)


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITLE__</title>
<style>
:root { --bg:#f8f9fa; --fg:#212529; --muted:#6c757d; --border:#dee2e6;
  --card:#fff; --accent:#f7a41d; --hover:#e9ecef; --code:#f1f3f5; }
@media (prefers-color-scheme: dark) {
  :root { --bg:#0d1117; --fg:#c9d1d9; --muted:#8b949e; --border:#30363d;
    --card:#161b22; --accent:#f7a41d; --hover:#21262d; --code:#0d1117; } }
* { box-sizing:border-box; margin:0; padding:0; }
body { font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  background:var(--bg); color:var(--fg); line-height:1.5; font-size:14px; }
.topbar { position:sticky; top:0; z-index:100; background:var(--card);
  border-bottom:1px solid var(--border); padding:.6rem 1rem; display:flex;
  gap:.6rem; align-items:center; flex-wrap:wrap; }
.topbar h1 { font-size:1rem; font-weight:700; }
#search { flex:1; min-width:200px; padding:.4rem .6rem; border:1px solid var(--border);
  border-radius:6px; background:var(--code); color:var(--fg); }
.count { color:var(--muted); font-size:.85rem; }
section.mod { border-bottom:1px solid var(--border); }
.mod-header { padding:.5rem 1rem; background:var(--hover); cursor:pointer;
  display:flex; justify-content:space-between; align-items:center; }
.mod-header h2 { font-size:1rem; }
.sc { color:var(--muted); font-size:.8rem; }
.grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(420px,1fr));
  gap:.5rem; padding:.5rem 1rem; }
.card { border:1px solid var(--border); border-radius:6px; background:var(--card);
  padding:.4rem .6rem; }
.fn { display:flex; justify-content:space-between; align-items:center; gap:.5rem; }
.func-name { font-weight:600; }
.btn { border:1px solid var(--border); background:var(--code); color:var(--fg);
  border-radius:4px; padding:.1rem .5rem; cursor:pointer; font-size:.8rem; }
.btn:hover { background:var(--accent); color:#1a1a1a; }
.sig { font-family:ui-monospace,SFMono-Regular,Consolas,monospace; font-size:.82rem;
  color:var(--muted); margin-top:.2rem; word-break:break-all; }
.hidden { display:none; }
</style>
</head>
<body>
<div class="topbar">
  <h1>__TITLE__</h1>
  <input id="search" placeholder="Filter functions..." oninput="filter()">
  <span class="count" id="count"></span>
</div>
__BODY__
<script>
function filter() {
  const q = document.getElementById('search').value.toLowerCase();
  let shown = 0, total = 0;
  document.querySelectorAll('section.mod').forEach(sec => {
    let secShown = 0;
    sec.querySelectorAll('.card').forEach(c => {
      total++;
      const hit = c.getAttribute('data-n').toLowerCase().includes(q);
      c.classList.toggle('hidden', !hit);
      if (hit) { secShown++; shown++; }
    });
    sec.classList.toggle('hidden', secShown === 0);
  });
  document.getElementById('count').textContent = shown + ' / ' + total;
}
function cp(btn) {
  const sig = btn.getAttribute('data-sig');
  navigator.clipboard.writeText(sig).then(() => {
    const t = btn.textContent; btn.textContent = 'Copied';
    setTimeout(() => btn.textContent = t, 1000);
  });
}
document.getElementById('count').textContent = '0 / 0';
filter();
</script>
</body>
</html>
"""


def render_html(version, modules):
    sections = []
    for label, sigs in modules:
        sec_id = label.replace(" / ", "---")
        cards = []
        for name, sig in sigs:
            g = sig.lower()
            cards.append(
                f'    <div class="card" data-n="{name.lower()}">\n'
                f'      <div class="fn"><span class="func-name">{name}</span>'
                f'<button class="btn" onclick="cp(this)" data-sig="{sig}">Copy</button></div>\n'
                f'      <div class="sig">{sig}</div>\n'
                f"    </div>"
            )
        sections.append(
            f'<section class="mod" id="{sec_id}">\n'
            f'  <div class="mod-header" onclick="this.nextElementSibling.classList.toggle(\'hidden\')">'
            f"<h2>{label}</h2><span class=\"sc\">{len(sigs)}</span></div>\n"
            f'  <div class="grid">\n' + "\n".join(cards) + "\n  </div>\n</section>"
        )
    body = "\n".join(sections)
    return HTML_TEMPLATE.replace("__TITLE__", f"Zig {version} Standard Library — Function Signatures").replace(
        "__BODY__", body
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--zig", required=True, help="path to the zig binary")
    args = ap.parse_args()

    version = version_of(args.zig)
    label = short_label(version)
    std_dir = os.path.join(os.path.dirname(os.path.abspath(args.zig)), "lib", "std")
    if not os.path.isdir(std_dir):
        sys.exit(f"std lib not found at {std_dir}")

    num = LABEL_TO_NUM.get(label)
    if not num:
        sys.exit(f"no signature-file slot configured for version {label}")
    map_dir = os.path.join(REPO, f"zig-{label}-resource-map")
    if not os.path.isdir(map_dir):
        sys.exit(f"resource-map dir not found: {map_dir}")

    modules = collect(std_dir)
    total = sum(len(s) for _, s in modules)
    md_path = os.path.join(map_dir, f"{num}-function-signatures.md")
    html_path = os.path.join(map_dir, "functions.html")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(render_md(version, modules))
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(render_html(version, modules))
    print(f"[{version}] {len(modules)} modules, {total} functions")
    print(f"  wrote {md_path}")
    print(f"  wrote {html_path}")


if __name__ == "__main__":
    main()
