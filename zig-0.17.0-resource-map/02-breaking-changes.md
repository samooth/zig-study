# Zig 0.17.0 — Breaking Changes from 0.16.0

Complete list of breaking changes when migrating from 0.16.0 to 0.17.0.

## Builtin Renames

### `@enumFromInt` → `@fromBackingInt`

```zig
// 0.16.0
const value: MyEnum = @enumFromInt(raw);

// 0.17.0
const value: MyEnum = @fromBackingInt(@intCast(raw));
```

### `@intFromEnum` → `@backingInt`

```zig
// 0.16.0
const raw: u32 = @intFromEnum(value);

// 0.17.0
const raw: u32 = @backingInt(value);
```

**Note:** These are used extensively in the stdlib. External code using these builtins must update.

## Module Renames

### `std.builtin` → `std.lang`

```zig
// 0.16.0
const optimize = std.builtin.OptimizeMode.Debug;

// 0.17.0
const optimize = std.lang.Optimize.debug;
// OR (deprecated alias still works):
const optimize = std.builtin.Optimize.debug;
```

### `std.gpu` → `std.spirv`

```zig
// 0.16.0
@import("std").gpu

// 0.17.0
@import("std").spirv
```

### `std.Io.IoUring` → `std.Io.Uring`

```zig
// 0.16.0
const backend = std.Io.IoUring{ ... };

// 0.17.0
const backend = std.Io.Uring{ ... };
```

## Enum Variant Changes

### OptimizeMode Variants Lowercased

```zig
// 0.16.0
switch (mode) {
    .Debug => ...,
    .ReleaseSafe => ...,
    .ReleaseFast => ...,
    .ReleaseSmall => ...,
}

// 0.17.0
switch (mode) {
    .debug => ...,
    .safe => ...,
    .fast => ...,
    .small => ...,
}
```

Old names (`.Debug`, `.ReleaseSafe`, etc.) are kept as deprecated aliases.

## Removed Builtins/Features

### `@cImport` Removed

```zig
// 0.16.0 (deprecated but worked)
const c = @cImport({
    @cInclude("stdio.h");
});

// 0.17.0 — must use build system
// build.zig:
const translate_c = b.addTranslateC(.{
    .root_source_file = b.path("src/c.h"),
    .target = target,
});
// src/main.zig:
const c = @import("c");
```

### `StackFallbackAllocator` Removed

```zig
// 0.16.0
var sfa = std.heap.stackFallback(1024, std.heap.page_allocator);
const allocator = sfa.get();

// 0.17.0 — use SmpAllocator or manual approach
const allocator = std.heap.SmpAllocator{};
```

### `std.Io.Threaded.ioBasic()` Removed

```zig
// 0.16.0
const basic_io = threaded.ioBasic();

// 0.17.0
const basic_io = threaded.io();
```

## Type System Changes

### `@typeInfo` Return Types Restructured

#### Pointer

```zig
// 0.16.0
info.Pointer.is_const
info.Pointer.is_volatile
info.Pointer.alignment
info.Pointer.address_space
info.Pointer.is_allowzero

// 0.17.0
info.Pointer.attrs.@"const"
info.Pointer.attrs.@"volatile"
info.Pointer.attrs.@"align"
info.Pointer.attrs.@"addrspace"
info.Pointer.attrs.@"allowzero"
```

#### Struct

```zig
// 0.16.0
info.Struct.fields  // []const StructField
info.Struct.decls   // []const Declaration

// 0.17.0
info.Struct.field_names  // []const [:0]const u8
info.Struct.field_types  // []const type
info.Struct.field_attrs  // []const FieldAttributes
info.Struct.decl_names   // []const [:0]const u8
```

#### Enum

```zig
// 0.16.0
info.Enum.fields      // []const EnumField
info.Enum.decls       // []const Declaration
info.Enum.is_exhaustive

// 0.17.0
info.Enum.field_names   // []const [:0]const u8
info.Enum.field_values  // []const comptime_int
info.Enum.decl_names    // []const [:0]const u8
info.Enum.mode          // .exhaustive or .nonexhaustive
```

#### Fn

```zig
// 0.16.0
info.Fn.calling_convention
info.Fn.is_var_args
info.Fn.params  // []const Param

// 0.17.0
info.Fn.attrs.@"callconv"
info.Fn.attrs.varargs
info.Fn.param_types  // []const ?type
info.Fn.param_attrs  // []const ParamAttributes
```

#### Union

```zig
// 0.16.0
info.Union.fields  // []const UnionField
info.Union.decls   // []const Declaration

// 0.17.0
info.Union.field_names   // []const [:0]const u8
info.Union.field_types   // []const type
info.Union.field_attrs   // []const FieldAttributes
info.Union.decl_names    // []const [:0]const u8
```

#### Opaque

```zig
// 0.16.0
info.Opaque.decls  // []const Declaration

// 0.17.0
info.Opaque.decl_names  // []const [:0]const u8
```

#### ErrorSet

```zig
// 0.16.0
info.ErrorSet  // ?[]const Error

// 0.17.0
info.ErrorSet  // struct { error_names: ?[]const [:0]const u8 }
```

## Allocator Changes

### `DebugAllocator` → `SafeAllocator`

```zig
// 0.16.0
var gpa = std.heap.DebugAllocator{};
defer _ = gpa.deinit();

// 0.17.0
var gpa = std.heap.SafeAllocator{};
defer _ = gpa.deinit();
```

Old name kept as deprecated alias.

## Quick Grep Safety Net

```bash
# Find all 0.16 patterns that need updating
rg "@cImport" --include "*.zig"
rg "@enumFromInt" --include "*.zig"
rg "@intFromEnum" --include "*.zig"
rg "\.Debug|\.ReleaseSafe|\.ReleaseFast|\.ReleaseSmall" --include "*.zig"
rg "std\.gpu" --include "*.zig"
rg "IoUring" --include "*.zig"
rg "StackFallbackAllocator" --include "*.zig"
rg "DebugAllocator" --include "*.zig"
rg "ioBasic" --include "*.zig"
rg "is_exhaustive" --include "*.zig"
rg "\.is_const|\.is_volatile|\.is_allowzero" --include "*.zig"
rg "\.fields\b.*StructField|\.fields\b.*EnumField|\.fields\b.*UnionField" --include "*.zig"
rg "\.decls\b.*Declaration" --include "*.zig"
```
