# Zig Study

Comprehensive reference materials, resource maps, and AI agent skill files for Zig.

## Contents

```
zig-study/
├── skills/                        # AI agent skills (SKILL.md each)
│   ├── zig-0.10/                  # skill for Zig 0.10.1   (SKILL.md + es/)
│   ├── zig-0.11/                  # skill for Zig 0.11.0   (SKILL.md + es/)
│   ├── zig-0.12/                  # skill for Zig 0.12.0   (SKILL.md + es/)
│   ├── zig-0.13/                  # skill for Zig 0.13.0   (SKILL.md + es/)
│   ├── zig-0.14/                  # skill for Zig 0.14.0   (SKILL.md + es/)
│   ├── zig/                       # skill for Zig 0.16.x / 0.17.x (SKILL.md + references/)
│   └── zig-multios/               # skill for cross-platform Zig (SKILL.md + es/)
├── zig-0.10.1-resource-map/       # Full reference for Zig 0.10.1
├── zig-0.11.0-resource-map/       # Full reference for Zig 0.11.0
├── zig-0.12.0-resource-map/       # Full reference for Zig 0.12.0
├── zig-0.13.0-resource-map/       # Full reference for Zig 0.13.0
├── zig-0.14.0-resource-map/       # Full reference for Zig 0.14.0
├── zig-0.16.0-resource-map/       # Full reference for Zig 0.16.0
├── zig-0.17.0-resource-map/       # Full reference for Zig 0.17.0
├── tools/                         # gen.py, verify.py, check-skill-examples.py
├── Makefile
└── README.md
```

### zig-0.16.0-resource-map

Deep-dive documentation for Zig 0.16.0 — release facts, std.Io architecture, language changes, stdlib modules, build system, migration cheat sheet, and extracted function signatures (~9,000 pub fn signatures).

### zig-0.17.0-resource-map

Changes from 0.16.0 to 0.17.0 — breaking changes, stdlib diffs, migration guide, and API diff showing added/removed function signatures between versions.

### Versioned resource maps (zig-0.10.1 … zig-0.14.0)

Full reference for each older stable release, generated directly from the installed stdlib source:

| Version | Location | Functions |
|---------|----------|-----------|
| 0.10.1 | `zig-0.10.1-resource-map/` | 5,128 `pub fn` signatures |
| 0.11.0 | `zig-0.11.0-resource-map/` | 5,947 `pub fn` signatures |
| 0.12.0 | `zig-0.12.0-resource-map/` | 6,160 `pub fn` signatures |
| 0.13.0 | `zig-0.13.0-resource-map/` | 6,180 `pub fn` signatures |
| 0.14.0 | `zig-0.14.0-resource-map/` | 7,176 `pub fn` signatures |

Each contains an `NN-function-signatures.md` table and an interactive `functions.html` viewer, both regenerated from the matching `<zig>/lib/std`.

### skills/zig/ (SKILL.md)

An AI coding agent skill (compatible with Claude Code, OpenCode, Codex) for mastering Zig 0.16/0.17. Lean entry point (243 lines) with 13 progressive-disclosure reference files covering critical patterns, language reference, std.Io, process, allocators, collections, encoding, crypto, build system, common errors, idioms, migration, and key function signatures.

### skills/zig-multios/ (SKILL.md)

An AI coding agent skill for **cross-platform Zig** (Windows, Linux, macOS, Android, WASM) on 0.16.x / 0.17.x. Covers `build.zig` cross-compilation, platform detection via `@import("builtin")`, the injected-module architecture pattern, per-OS gotchas, and memory handling across targets.

### Versioned skills (skills/zig-0.10 … skills/zig-0.14)

One skill per stable release for the older Zig toolchains installed under
`<zvm-root>/` (note: these are managed by **zvm**, not nvm). Each skill
is a lean `SKILL.md` entry point covering language semantics, std library
(pre-`std.Io` era), allocators, `build.zig`/`build.zig.zon`, and
cross-compilation for that exact version.

## Purpose

- **Resource maps**: Comprehensive, grep-friendly documentation of the Zig 0.16.0 and 0.17.0 standard libraries, with function signatures extracted directly from the installed stdlib source
- **Skill file**: Enables LLM coding agents to write correct, idiomatic Zig code by providing version-pinned patterns, WRONG→CORRECT code examples, error→fix tables, and best practices

## Usage

### As reference documentation

Browse the markdown files in each resource-map directory. Each file covers a specific topic (I/O, language changes, build system, etc.).

### As an LLM agent skill

Copy any skill folder from `skills/` to your agent's skills path:

| Agent | Destination |
|-------|-------------|
| OpenCode | `.opencode/skills/<skill-name>/` or `~/.config/opencode/skills/<skill-name>/` |
| Claude Code | `.claude/skills/<skill-name>/` |
| Codex | `.agents/skills/<skill-name>/` |

Example:

```bash
cp -r skills/zig ~/.config/opencode/skills/zig
cp -r skills/zig-multios ~/.config/opencode/skills/zig-multios
cp -r skills/zig-0.14 ~/.config/opencode/skills/zig-0.14
```

### Zig versions covered

| Version | Status | Location |
|---------|--------|----------|
| 0.10.1 | Stable release | `skills/zig-0.10/` |
| 0.11.0 | Stable release | `skills/zig-0.11/` |
| 0.12.0 | Stable release | `skills/zig-0.12/` |
| 0.13.0 | Stable release | `skills/zig-0.13/` |
| 0.14.0 | Stable release | `skills/zig-0.14/` |
| 0.16.0 | Stable release | `skills/zig/` + `zig-0.16.0-resource-map/` |
| 0.17.0 | Dev release | `skills/zig/` + `zig-0.17.0-resource-map/` |
| multi-OS | Cross-platform (0.16/0.17) | `skills/zig-multios/` |

## Stats

- 31 markdown files
- ~24,000 lines of documentation
- ~17,000 extracted function signatures (across both versions)
- Function signatures generated from actual installed stdlib source

## Regenerating the signature tables & HTML

The function-signature tables (`NN-function-signatures.md`) and `functions.html`
viewers are **generated**, not hand-written, and are git-ignored. They are
produced directly from the installed Zig standard library so they can never
drift from the compiler.

Each resource map is pinned to the exact Zig build it was generated against
(the version is stamped into the generated files). The current 0.17.0 docs
target `0.17.0-dev.1662+cc6f42302` (the dev snapshot installed via zvm).

```bash
# regenerate both versions (requires the matching zvm installs)
make gen

# regenerate + verify every listed function exists in the installed stdlib
make check
```

`tools/gen.py` extracts every `pub fn` from `<zig>/lib/std` and writes the
markdown table + HTML viewer; `tools/verify.py` parses those artifacts and
fails if any listed function is missing from (or any forbidden term appears
in) the installed stdlib. Run `make verify` in CI / pre-commit to catch
drift automatically.

## License

MIT
