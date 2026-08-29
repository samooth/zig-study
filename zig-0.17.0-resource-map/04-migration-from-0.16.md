# Zig 0.17.0 — Migration from 0.16.0

Side-by-side migration guide from Zig 0.16.0 to 0.17.0.

## Builtins

### `@enumFromInt` (still works) and new `@fromBackingInt`

```zig
// 0.16.0 and 0.17.0 — still works, no change required
const tag: MyTag = @enumFromInt(raw_u32);

// 0.17.0 — new alternative (optional)
const tag: MyTag = @fromBackingInt(@intCast(raw_u32));
```

### `@intFromEnum` (still works) and new `@backingInt`

```zig
// 0.16.0 and 0.17.0 — still works, no change required
const raw: u32 = @intFromEnum(tag);

// 0.17.0 — new alternative (optional)
const raw: u32 = @backingInt(tag);
```

### `@cImport` → Build System

```zig
// 0.16.0 (deprecated, still worked)
const c = @cImport({
    @cInclude("foo.h");
});

// 0.17.0 — build.zig only
const translate_c = b.addTranslateC(.{
    .root_source_file = b.path("src/c.h"),
    .target = target,
});
// Then in source:
const c = @import("c");
```

## Module Paths

| 0.16.0 | 0.17.0 |
|--------|--------|
| `std.builtin` | `std.lang` (or `std.builtin` — deprecated) |
| `std.builtin.OptimizeMode` | `std.lang.Optimize` |
| `std.gpu` | `std.spirv` |
| `std.Io.Uring` | `std.Io.Uring` (same name in both 0.16 and 0.17) |
| `std.heap.DebugAllocator` | `std.heap.SafeAllocator` |
| `std.heap.GeneralPurposeAllocator` | `std.heap.SafeAllocator` |

## Enum Variants

### OptimizeMode → Optimize (lowercased)

```zig
// 0.16.0
const mode: std.builtin.OptimizeMode = .Debug;
if (mode == .ReleaseSafe) { ... }

// 0.17.0
const mode: std.lang.Optimize = .debug;
if (mode == .safe) { ... }
```

### Error set patterns

```zig
// 0.16.0
if (builtin.mode == .Debug) { ... }

// 0.17.0
if (builtin.mode == .debug) { ... }
```

## Allocators

```zig
// 0.16.0
var gpa = std.heap.GeneralPurposeAllocator{};
defer _ = gpa.deinit();

// 0.17.0
var gpa = std.heap.SafeAllocator{};
defer _ = gpa.deinit();
// OR (DebugAllocator still works as deprecated alias):
var gpa = std.heap.DebugAllocator{};
```

## Type Introspection (`@typeInfo`)

### Pointer Attributes

```zig
// 0.16.0
const info = @typeInfo(*const u32);
if (info.Pointer.is_const) { ... }
const align_val = info.Pointer.alignment;

// 0.17.0
const info = @typeInfo(*const u32);
if (info.Pointer.attrs.@"const") { ... }
const align_val = info.Pointer.attrs.@"align";
```

### Struct Fields

```zig
// 0.16.0
for (@typeInfo(MyStruct).Struct.fields) |field| {
    _ = field.name;   // [:0]const u8
    _ = field.type;   // type
}

// 0.17.0
const info = @typeInfo(MyStruct).Struct;
for (info.field_names, info.field_types) |name, T| {
    _ = name;  // [:0]const u8
    _ = T;     // type
}
```

### Enum Fields

```zig
// 0.16.0
const info = @typeInfo(MyEnum).Enum;
_ = info.is_exhaustive;
for (info.fields) |field| { _ = field.name; }

// 0.17.0
const info = @typeInfo(MyEnum).Enum;
_ = info.mode == .exhaustive;
for (info.field_names) |name| { _ = name; }
```

### Fn Signatures

```zig
// 0.16.0
const info = @typeInfo(@TypeOf(myFn)).Fn;
_ = info.calling_convention;
_ = info.is_var_args;
for (info.params) |param| { _ = param.type; }

// 0.17.0
const info = @typeInfo(@TypeOf(myFn)).Fn;
_ = info.attrs.@"callconv";
_ = info.attrs.varargs;
for (info.param_types) |T| { _ = T; }
```

### Declarations

```zig
// 0.16.0
for (@typeInfo(T).Struct.decls) |decl| { _ = decl.name; }

// 0.17.0
for (@typeInfo(T).Struct.decl_names) |name| { _ = name; }
```

## Io Backend

```zig
// 0.16.0 (macOS)
const backend = std.Io.Kqueue{ ... };

// 0.17.0 (macOS — now uses Dispatch)
const backend = std.Io.Dispatch{ ... };

// 0.16.0 (Linux)
const backend = std.Io.Uring{ ... };

// 0.17.0 (Linux)
const backend = std.Io.Uring{ ... };
```

## Threaded Io

```zig
// 0.16.0 and 0.17.0 — `Threaded.io()` is unchanged (there was never an `ioBasic`)
const basic = threaded.io();
```

## SPIR-V / GPU

```zig
// 0.16.0
const gpu = @import("std").gpu;

// 0.17.0
const spirv = @import("std").spirv;

// New capabilities in 0.17.0:
spirv.workgroupBarrier();
spirv.controlBarrier(.workgroup, .device, .{ .acquire_release = true });
const size = spirv.imageQuerySize(image);
```

## ASCII

```zig
// 0.16.0 and 0.17.0 — dedicated module available in both versions
const ascii = @import("std").ascii;
if (ascii.isLowercase(c)) { ... }
```

## Quick Grep Safety Net

```bash
# Builtins
# NOTE: @enumFromInt / @intFromEnum still work in 0.17 — no update required.
# New alternatives @fromBackingInt / @backingInt were added but are optional.
rg "@cImport" --include "*.zig"

# Module paths
rg "std\.builtin\." --include "*.zig"
rg "std\.gpu" --include "*.zig"
# NOTE: std.Io.Uring is the correct name in both 0.16 and 0.17.
rg "DebugAllocator" --include "*.zig"
rg "StackFallbackAllocator" --include "*.zig"

# Enum variants
rg "\.Debug\b|\.ReleaseSafe\b|\.ReleaseFast\b|\.ReleaseSmall\b" --include "*.zig"

# Type introspection (old patterns)
rg "\.is_const\b|\.is_volatile\b|\.is_allowzero\b|\.is_var_args\b" --include "*.zig"
rg "\.is_exhaustive\b" --include "*.zig"
rg "\.calling_convention\b" --include "*.zig"
rg "\.fields\b.*StructField|\.fields\b.*EnumField|\.fields\b.*UnionField" --include "*.zig"
rg "\.decls\b.*Declaration" --include "*.zig"
rg "ioBasic" --include "*.zig"
# NOTE: ioBasic never existed; Threaded.io() is unchanged. Safe to ignore.
```

## Migration Checklist

- [ ] (Optional) Prefer new `@fromBackingInt`/`@backingInt`; old `@enumFromInt`/`@intFromEnum` still work
- [ ] Remove all `@cImport` usage, move to `b.addTranslateC`
- [ ] Update `std.builtin` → `std.lang` (or keep using deprecated alias)
- [ ] Update `.Debug`/`.ReleaseSafe` → `.debug`/`.safe`
- [ ] Update `std.gpu` → `std.spirv`
- [ ] `std.Io.Uring` is unchanged — no rename needed
- [ ] Update `DebugAllocator` → `SafeAllocator`
- [ ] Remove `StackFallbackAllocator` usage
- [ ] Update `@typeInfo` access patterns for Pointer/Struct/Enum/Fn/Union/Opaque/ErrorSet
- [ ] `Threaded.io()` is unchanged — no `ioBasic` change needed
- [ ] Test on target platform (macOS now uses Dispatch backend)
