# Zig 0.17.0 — Release Overview

## Release Facts

| Field | Value |
|-------|-------|
| Version | 0.17.0-dev.1662+cc6f42302 |
| Development Status | Dev release (not yet final) |
| Based on | 0.16.0 with continued evolution toward 1.0 |

## Key Themes

### 1. `@cImport` Fully Removed

The deprecated `@cImport` builtin from 0.16.0 is now completely gone. All C translation must go through the build system:

```zig
// Build system only
const translate_c = b.addTranslateC(.{
    .root_source_file = b.path("src/c.h"),
    .target = target,
});
```

### 2. New Enum Backing-Integer Builtins

No enum builtins were renamed. `@enumFromInt` and `@intFromEnum` are unchanged from 0.16, and two new builtins were added (all four coexist):

| Builtin | Purpose |
|---------|---------|
| `@enumFromInt` | Convert backing integer to enum (unchanged) |
| `@intFromEnum` | Convert enum to backing integer (unchanged) |
| `@fromBackingInt` | New: convert backing integer to enum |
| `@backingInt` | New: convert enum to backing integer |

### 3. `std.builtin` → `std.lang`

The language-provided types have been renamed from `std.builtin` to `std.lang`:

```zig
// 0.16.0
@import("std").builtin.OptimizeMode

// 0.17.0
@import("std").lang.Optimize  // or std.builtin.Optimize (deprecated alias)
```

### 4. OptimizeMode Variants Lowercased

```zig
// 0.16.0
.builtin.mode == .Debug
.builtin.mode == .ReleaseSafe

// 0.17.0
.lang.mode == .debug
.lang.mode == .safe
```

### 5. Io Backends

- **`Io.Dispatch`** — macOS Grand Central Dispatch backend (present since 0.16, alongside `Kqueue`)
- **`Io.fiber`** — Fiber/context switching support (aarch64, riscv64, x86_64; present since 0.16)
- **`crashHandler`** — VTable entry for crash handling (present since 0.16)

### 6. `std.spirv` — Expanded GPU Support

`std.gpu` renamed to `std.spirv` with significant new functionality:

- `Scope` enum (cross_device, device, workgroup, subgroup, invocation, queue_family, shader_call_khr)
- `MemorySemantics` packed struct
- `controlBarrier()`, `memoryBarrier()`, `workgroupBarrier()` functions
- `specConst()` for specialization constants
- `imageSampleImplicitLod()`, `imageQuerySize()`, `imageWrite()` — image operations

### 7. `SafeAllocator` — New Primary Debug Allocator

`DebugAllocator` is now a deprecated alias for `SafeAllocator`:

```zig
// 0.16.0
const allocator = std.heap.DebugAllocator{};

// 0.17.0
const allocator = std.heap.SafeAllocator{};
```

### 8. `std.ascii` Module

Dedicated ASCII character handling module with:
- Character classification (`isAlphanumeric`, `isControl`, etc.)
- Case conversion
- Character constants (control codes, whitespace)
- Validation functions

## Removed Features

| Feature | Replacement |
|---------|-------------|
| `@cImport` | `b.addTranslateC` in build system |
| `StackFallbackAllocator` | Use `SmpAllocator` or manual stack allocation |
| `std.gpu` | `std.spirv` |

## Type System Changes

The `@typeInfo` return types have been restructured:

- **Pointer**: `is_const`/`is_volatile`/`is_allowzero`/`address_space`/`alignment` → `attrs: Attributes`
- **Struct**: `fields`/`decls` → `field_names`/`field_types`/`field_attrs`/`decl_names`
- **Enum**: `fields`/`decls`/`is_exhaustive` → `field_names`/`field_values`/`decl_names`/`mode: Mode`
- **Fn**: `calling_convention`/`is_var_args`/`params` → `attrs: Attributes`/`param_types`/`param_attrs`
- **Union**: `fields`/`decls` → `field_names`/`field_types`/`field_attrs`/`decl_names`
- **Opaque**: `decls` → `decl_names`
- **ErrorSet**: `?[]const Error` → `struct { error_names: ?[]const [:0]const u8 }`

## Stdlib Location

```
lib/std/
```
