# Zig 0.16.0 Resource Map

A comprehensive reference for Zig 0.16.0 — its architecture, APIs, breaking changes, and migration paths.

**Release Date:** April 14, 2026 | **Dev Cycle:** 8 months | **Contributors:** 244 | **Commits:** 1183

## Documents

| File | Contents |
|------|----------|
| [01-release-overview.md](01-release-overview.md) | Release facts, highlights, and key themes |
| [02-io-as-interface.md](02-io-as-interface.md) | Deep dive into `std.Io` — the central abstraction |
| [03-language-changes.md](03-language-changes.md) | Language-level changes, builtins, and semantics |
| [04-standard-library.md](04-standard-library.md) | Standard library modules and their APIs |
| [05-build-system.md](05-build-system.md) | Build system changes, `build.zig.zon`, steps |
| [06-migration-cheat-sheet.md](06-migration-cheat-sheet.md) | Quick-reference migration from 0.15.x |
| [07-stdlib-map.md](07-stdlib-map.md) | File-by-file stdlib directory map |
| [08-useful-resources.md](08-useful-resources.md) | Links, tools, community resources |
| [09-function-signatures.md](09-function-signatures.md) | All pub fn signatures extracted from stdlib |

## Quick Start

```zig
// Zig 0.16.0 — "Juicy Main" entry point
const std = @import("std");

pub fn main(init: std.process.Init) !void {
    const gpa = init.gpa;
    const io = init.io;
    const args = try init.minimal.args.toSlice(init.arena.allocator());
    _ = gpa;
    _ = io;
    _ = args;
}
```

## Key Themes

1. **I/O as an Interface** — `std.Io` unifies all I/O (files, network, process, time, random) behind a single vtable
2. **Juicy Main** — `std.process.Init` dependency injection eliminates allocator/env boilerplate
3. **@cImport Deprecated** — C translation moves to `b.addTranslateC` in the build system
4. **@Type Removed** — Replaced by focused builtins (`@typeInfo`, `@typeName`, etc.)
5. **Unmanaged Containers** — `ArrayList`/`HashMap` variants consolidated; use `.empty` init
6. **New ELF Linker** — 66% faster incremental link times
7. **Self-hosted Backend Maturation** — Faster debug builds without LLVM

## Stdlib Location (this install)

```
lib/std/
```

Verify with: `zig env` → `std_dir`
