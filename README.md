# Zig Study

Comprehensive reference materials, resource maps, and AI agent skill files for Zig 0.16.0 and 0.17.0.

## Contents

```
zig-study/
├── zig-0.16.0-resource-map/    # Full reference for Zig 0.16.0
├── zig-0.17.0-resource-map/    # Full reference for Zig 0.17.0
└── zig/                        # LLM agent skill (SKILL.md + references)
```

### zig-0.16.0-resource-map

Deep-dive documentation for Zig 0.16.0 — release facts, std.Io architecture, language changes, stdlib modules, build system, migration cheat sheet, and extracted function signatures (~9,000 pub fn signatures).

### zig-0.17.0-resource-map

Changes from 0.16.0 to 0.17.0 — breaking changes, stdlib diffs, migration guide, and API diff showing added/removed function signatures between versions.

### zig/ (SKILL.md)

An AI coding agent skill (compatible with Claude Code, OpenCode, Codex) for mastering Zig 0.16/0.17. Lean entry point (243 lines) with 13 progressive-disclosure reference files covering critical patterns, language reference, std.Io, process, allocators, collections, encoding, crypto, build system, common errors, idioms, migration, and key function signatures.

## Purpose

- **Resource maps**: Comprehensive, grep-friendly documentation of the Zig 0.16.0 and 0.17.0 standard libraries, with function signatures extracted directly from the installed stdlib source
- **Skill file**: Enables LLM coding agents to write correct, idiomatic Zig code by providing version-pinned patterns, WRONG→CORRECT code examples, error→fix tables, and best practices

## Usage

### As reference documentation

Browse the markdown files in each resource-map directory. Each file covers a specific topic (I/O, language changes, build system, etc.).

### As an LLM agent skill

Copy the `zig/` directory to your agent's skills path:

| Agent | Destination |
|-------|-------------|
| OpenCode | `.opencode/skills/zig/` or `~/.config/opencode/skills/zig/` |
| Claude Code | `.claude/skills/zig/` |
| Codex | `.agents/skills/zig/` |

### Zig versions covered

| Version | Status | Location |
|---------|--------|----------|
| 0.16.0 | Stable release | `zig-0.16.0-resource-map/` |
| 0.17.0 | Dev release | `zig-0.17.0-resource-map/` |

## Stats

- 31 markdown files
- ~24,000 lines of documentation
- ~17,000 extracted function signatures (across both versions)
- Function signatures generated from actual installed stdlib source

## License

MIT
