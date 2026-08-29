# Zig 0.17.0 Resource Map

A comprehensive reference for Zig 0.17.0 — changes from 0.16.0, new features, and migration paths.

**Version:** 0.17.0-dev.1662+cc6f42302 | **Source:** `<zig-install-dir>/lib/std/`

## Documents

| File | Contents |
|------|----------|
| [01-release-overview.md](01-release-overview.md) | Release facts and key themes |
| [02-breaking-changes.md](02-breaking-changes.md) | All breaking changes from 0.16.0 |
| [03-stdlib-changes.md](03-stdlib-changes.md) | New/removed/renamed modules |
| [04-migration-from-0.16.md](04-migration-from-0.16.md) | Side-by-side 0.16 → 0.17 migration |
| [05-function-signatures.md](05-function-signatures.md) | All pub fn signatures extracted from stdlib |
| [06-api-diff-from-0.16.md](06-api-diff-from-0.16.md) | Added/removed functions between versions |

## Quick Comparison: 0.16.0 vs 0.17.0

| Feature | 0.16.0 | 0.17.0 |
|---------|--------|--------|
| `@cImport` | Deprecated | **Removed** |
| `@enumFromInt` | Available | Still works; new `@fromBackingInt` added |
| `@intFromEnum` | Available | Still works; new `@backingInt` added |
| `std.builtin` | Primary module | Deprecated alias for `std.lang` |
| `OptimizeMode` | `.Debug`, `.ReleaseSafe` | `.debug`, `.safe` (lowercase) |
| `std.gpu` | Available | Renamed to `std.spirv` |
| `Io.Uring` | Available | `std.Io.Uring` in both 0.16 and 0.17 (low-level `os.linux.IoUring` is a separate type) |
| `StackFallbackAllocator` | Available | **Removed** |
| `DebugAllocator` | Primary | Deprecated alias for `SafeAllocator` |
| `std.ascii` | Available | Available in both 0.16 and 0.17 |
| `Io.Dispatch` | Available | Available in both 0.16 and 0.17 (macOS Grand Central Dispatch) |
| `Io.fiber` | Available | Available in both 0.16 and 0.17 (fiber/context switching) |
| `crashHandler` in VTable | Present | Present in both 0.16 and 0.17 |

## Stdlib Location

```
lib/std/
```

Verify with: `zig env` → `std_dir`
