# Migration: 0.16 → 0.17

Key changes when upgrading from Zig 0.16.x to 0.17.x.

## Enum Builtins (not renamed)

Both the old and new builtins exist in 0.17 — the `*Backing*` variants were *added*, the
old ones were not removed:

| Works in all versions | Added in 0.17 |
|----------------------|---------------|
| `@enumFromInt(x)`    | `@fromBackingInt(@intCast(x))` |
| `@intFromEnum(e)`    | `@backingInt(e)` |

## Module Renames

| Old | New |
|-----|-----|
| `std.builtin` | `std.lang` (alias kept) |
| `std.builtin.OptimizeMode` | `std.lang.Optimize` |
| `std.gpu` | `std.spirv` |
| `std.Io.IoUring` | `std.Io.Uring` (note: it was always `Uring`, never `IoUring`) |
| `std.heap.DebugAllocator` | `std.heap.SafeAllocator` (both still exist in 0.17; not a rename) |

## Enum Variants Lowercased

```zig
// 0.16
.mode == .Debug
.mode == .ReleaseSafe

// 0.17
.mode == .debug
.mode == .safe
```

## @typeInfo Restructured

### Pointer

```zig
// 0.16
info.Pointer.is_const
info.Pointer.alignment

// 0.17
info.Pointer.attrs.@"const"
info.Pointer.attrs.@"align"
```

### Struct

```zig
// 0.16
for (@typeInfo(T).Struct.fields) |f| { _ = f.name; }

// 0.17
for (@typeInfo(T).Struct.field_names) |name| { ... }
```

### Enum

```zig
// 0.16
info.Enum.is_exhaustive

// 0.17
info.Enum.mode == .exhaustive
```

### Fn

```zig
// 0.16
info.Fn.calling_convention
info.Fn.is_var_args
for (info.Fn.params) |p| { _ = p.type; }

// 0.17
info.Fn.attrs.@"callconv"
info.Fn.attrs.varargs
for (info.Fn.param_types) |T| { ... }
```

## @cImport Removed

```zig
// 0.16 (deprecated, still worked)
const c = @cImport({ @cInclude("foo.h"); });

// 0.17 — must use build system
// build.zig:
const tc = b.addTranslateC(.{ .root_source_file = b.path("src/c.h") });
// main.zig:
const c = @import("c");
```

## StackFallbackAllocator Removed

```zig
// 0.16
var sfa = std.heap.stackFallback(1024, std.heap.page_allocator);

// 0.17
// Use SmpAllocator or manual approach
```

## Io Backend Changes

```zig
// 0.16 (macOS)
std.Io.Kqueue

// 0.17 (macOS)
std.Io.Dispatch  // Grand Central Dispatch
```

## Io VTable: crashHandler

New entry: `crashHandler: *const fn (?*anyopaque) void`

## New Features in 0.17

- `std.spirv` — expanded GPU intrinsics (barriers, image ops)
- `Io.fiber` — fiber/context switching (aarch64, riscv64, x86_64)
- `SafeAllocator` — new safe/leak-checking allocator (0.17; `DebugAllocator` still exists too)
- `BufferFirstAllocator` — try buffer first
- `std.Options.networking` — disable networking

## Quick Grep for Migration

```bash
rg "@enumFromInt" --include "*.zig"
rg "@intFromEnum" --include "*.zig"
rg "@cImport" --include "*.zig"
rg "std\.gpu" --include "*.zig"
rg "IoUring" --include "*.zig"
rg "DebugAllocator" --include "*.zig"
rg "StackFallbackAllocator" --include "*.zig"
rg "\.Debug\b|\.ReleaseSafe\b" --include "*.zig"
```
