---
name: zig
description: >-
  Zig programming language patterns and best practices for versions 0.16.x and 0.17.x.
  Use when writing, reviewing, debugging, or migrating Zig code, working with
  build.zig, build.zig.zon, comptime metaprogramming, or the std.Io interface.
  Covers language semantics, standard library, allocators, build system, and
  cross-compilation. Critical for avoiding outdated patterns from LLM training data.
license: MIT
compatibility:
  - claude-code
  - opencode
  - codex
metadata:
  version: "0.16.x / 0.17.x"
  language: "zig"
  category: "programming-language"
---

# Zig Programming Guide (0.16.x / 0.17.x)

## When To Use This Skill

- Writing new Zig code
- Debugging compilation errors
- Reviewing Zig code for correctness or idiomatic patterns
- Migrating from Zig 0.15.x or earlier
- Working with build.zig / build.zig.zon
- Comptime metaprogramming and type reflection

## Local Documentation First

Before guessing API shapes, check the local installation:

```bash
zig env              # shows std_dir, lib_dir, version
zig std              # opens stdlib docs in browser
```

Then grep the local stdlib for the actual API:

```bash
grep -rn "pub fn openFile" $(zig env | jq -r .std_dir)
```

The local source is always more authoritative than prose documentation.

## Version Detection

```bash
zig version
# 0.16.x → use std.Io (uppercase), std.process.Init, .name = .x in build.zig.zon
# 0.17.x → additionally: @fromBackingInt, std.lang (not std.builtin), .debug (not .Debug)
```

## Design Principles

1. **Type-First Development** — Define types before functions. Use comptime to enforce invariants.
2. **Make Illegal States Unrepresentable** — Use enums, packed structs, and optionals to eliminate invalid states.
3. **Memory Ownership** — Functions that allocate memory have an `Alloc` suffix or take an explicit `Allocator` parameter.
4. **Error Handling** — Use `try`/`catch`/`errdefer`. Never ignore errors. Prefer `errdefer` over `defer` for cleanup on error.
5. **Comptime Over Runtime** — Prefer comptime-known values. Use `comptime {}` blocks for compile-time computation.
6. **I/O as Interface** — All I/O functions take an `io: Io` parameter (0.16+). Never use global state.

## Top Breaking Changes (Quick Ref)

| Pattern | 0.15.x (old) | 0.16.x+ (new) |
|---------|--------------|----------------|
| Entry point | `pub fn main() !void` | `pub fn main(init: std.process.Init) !void` |
| Allocator | `GeneralPurposeAllocator` | `SafeAllocator` (0.17) or `DebugAllocator` (0.16) |
| C imports | `@cImport({ @cInclude("x.h"); })` | `b.addTranslateC` in build.zig |
| File open | `std.fs.openFile(path, flags)` | `std.Io.Dir.cwd().openFile(io, path, opts)` |
| ArrayList init | `ArrayList(T){}` | `ArrayList(T).empty` |
| String trim | `trimLeft` / `trimRight` | `trimStart` / `trimEnd` |
| Get cwd | `std.process.getCwd(buf)` | `std.process.currentPath(io, buf)` |
| Random | `std.crypto.random.bytes(buf)` | `io.random(buf)` |
| sleep | `std.time.sleep(ns)` | `io.sleep(timeout)` |
| Type info | `@typeInfo(T).Struct.fields` | `@typeInfo(T).Struct.field_names` (0.17) |
| Enum int | `@enumFromInt(x)` | `@fromBackingInt(@intCast(x))` (0.17) |
| OptimizeMode | `.Debug`, `.ReleaseSafe` | `.debug`, `.safe` (0.17 lowercase) |
| @Type | `@Type(...)` | Removed; use `@typeInfo`, `@Tuple`, etc. |
| build.zig.zon | `.name = "x"` | `.name = .x` + `.fingerprint = 0x...` |
| Thread.Pool | `std.Thread.Pool` | Removed; use `std.Io.Group` + `Io.async` |

## Critical Patterns

### Entry Point (Juicy Main)

```zig
// WRONG — old style, no io access
pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator{};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();
    // ... no way to do I/O without global state
}

// CORRECT — 0.16+ style
pub fn main(init: std.process.Init) !void {
    const gpa = init.gpa;
    const io = init.io;
    const arena = init.arena;
    const args = try init.minimal.args.toSlice(arena.allocator());
    _ = gpa;
    _ = args;
}
```

### File I/O

```zig
// WRONG — old global fs API
const file = try std.fs.cwd().openFile("data.txt", .{});

// CORRECT — Io-based
const file = try std.Io.Dir.cwd().openFile(io, "data.txt", .{});
defer file.close(io);
var reader = file.reader(io, &.{});
```

### ArrayList

```zig
// WRONG — old init
var list = std.ArrayList(u8){};

// CORRECT — 0.16+ init
var list = std.ArrayList(u8).empty;
defer list.deinit(allocator);
try list.append(allocator, 42);
```

### HashMap

```zig
// WRONG
var map = std.StringHashMap(u32){};

// CORRECT
var map = std.StringHashMap(u32).empty;
defer map.deinit(allocator);
try map.put(allocator, "key", value);
```

### Error Handling

```zig
// WRONG — ignoring errors
const file = std.fs.cwd().openFile("x", .{}) catch return;

// CORRECT — propagate or handle
const file = std.Io.Dir.cwd().openFile(io, "x", .{}) catch |err| {
    log.err("failed to open: {}", .{err});
    return err;
};
defer file.close(io);
```

### C Interop (0.17+)

```zig
// WRONG — @cImport removed in 0.17
const c = @cImport({ @cInclude("foo.h"); });

// CORRECT — build system approach
// build.zig:
const translate_c = b.addTranslateC(.{
    .root_source_file = b.path("src/c.h"),
    .target = target,
});
// main.zig:
const c = @import("c");
```

## Common Idioms

### Arena for Temporary Allocations

```zig
var arena = std.heap.ArenaAllocator.init(gpa);
defer arena.deinit();
const alloc = arena.allocator();
// All allocations freed at once when arena deinitializes
```

### Testing

```zig
const std = @import("std");

test "basic assertion" {
    const io = std.testing.io;
    const result = try myFunction(io, 42);
    try std.testing.expectEqual(@as(u32, 42), result);
}
```

### JSON Parsing

```zig
const parsed = try std.json.parseFromSlice(MyStruct, allocator, json_bytes, .{});
defer parsed.deinit();
const value = parsed.value;
```

### Deferred Cleanup

```zig
var resource = try acquireResource();
defer resource.deinit(); // always runs

// For error-only cleanup:
var resource2 = try acquireResource();
errdefer resource2.deinit(); // only runs on error
try doSomething(resource2);  // if this fails, resource2 is cleaned up
```

## Verification Workflow

After making changes, always run:

```bash
zig build                    # check compilation
zig build test               # run tests
zig build -Doptimize=ReleaseFast test  # optimized test
zig fmt src/                 # format code
```

## References

- [Critical Patterns](references/01-critical-patterns.md) — WRONG→CORRECT for top 20 gotchas
- [Language Reference](references/02-language-reference.md) — Builtins, syntax, type system
- [std.Io Reference](references/03-stdlib-io.md) — File, Dir, Reader, Writer, net
- [Process Reference](references/04-stdlib-process.md) — Init, Child, Args, Environ
- [Allocator Reference](references/05-stdlib-allocators.md) — Heap allocators and patterns
- [Collections Reference](references/06-stdlib-collections.md) — ArrayList, HashMap, etc.
- [Encoding Reference](references/06-stdlib-encoding.md) — fmt, json, zon, compress
- [Crypto Reference](references/07-stdlib-crypto.md) — AEAD, hashing, TLS
- [Build System](references/08-build-system.md) — build.zig, build.zig.zon, packages
- [Common Errors](references/09-common-errors.md) — Error message → fix table
- [Idioms & Patterns](references/10-idioms-patterns.md) — Best practices and patterns
- [Migration 0.16→0.17](references/11-migration-016-to-017.md) — What changed between versions
- [Function Signatures](references/12-function-signatures.md) — Key API signatures
