# Common Error Messages and Fixes

Match compiler errors to their fixes. Organized by frequency.

## Container Init Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `expected 0 argument(s), found 1` on `ArrayList(T){}` | Old init syntax | Use `ArrayList(T).empty` |
| `no field named 'x' in struct '...'` on container init | Missing `.empty` | Add `.empty` suffix |
| `type 'ArrayList(u8)' has no field named ' allocator'` | Wrong init | Use `.empty` then `.deinit(allocator)` |

## I/O Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `expected 2 argument(s), found 1` on `openFile` | Missing `io` param | Add `io` as first argument |
| `no member named 'fs' in 'std'` | Using old fs API | Use `std.Io.Dir`, `std.Io.File` |
| `no member named 'cwd' in 'Io.Dir'` call wrong | Missing io | `Io.Dir.cwd()` then `.openFile(io, ...)` |
| `expected type '*const process.Environ.Map'` | Function needs env | Pass from `init.environ_map` |

## Allocator Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `no member named 'GeneralPurposeAllocator'` | Renamed | Use `DebugAllocator` (0.16) or `SafeAllocator` (0.17) |
| `type depends on itself for alignment` | Self-referential query | Remove `@alignOf(@This())` or restructure |

## @cImport Errors (0.17)

| Error | Cause | Fix |
|-------|-------|-----|
| `unused @cImport` or `@cImport removed` | @cImport removed in 0.17 | Use `b.addTranslateC` in build.zig |
| `undeclared identifier 'c'` | Missing translate-c module | Add translate-c step and `@import("c")` |

## Builtin Errors (0.17)

| Error | Cause | Fix |
|-------|-------|-----|
| `no builtin named 'enumFromInt'` | Renamed in 0.17 | Use `@fromBackingInt` |
| `no builtin named 'intFromEnum'` | Renamed in 0.17 | Use `@backingInt` |
| `no member named 'Debug' in enum` | Variants lowercased | Use `.debug`, `.safe`, `.fast`, `.small` |
| `no member named 'fields' in 'Struct'` | @typeInfo restructured | Use `.field_names`, `.field_types` |
| `no member named 'is_exhaustive' in 'Enum'` | Renamed | Use `.mode == .exhaustive` |
| `no member named 'is_const' in 'Pointer'` | Nested in attrs | Use `.attrs.@"const"` |
| `no member named 'calling_convention' in 'Fn'` | Nested in attrs | Use `.attrs.@"callconv"` |

## Build System Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `fingerprint field missing` | Required in build.zig.zon | Add `.fingerprint = 0x...` |
| `name must be an enum literal` | Old string name | Change `.name = "x"` to `.name = .x` |
| `root_source_file not accepted` | API changed | Use `root_module = b.createModule(...)` |
| `no member named 'linkLibC'` | Moved to module option | Set `link_libc = true` in `b.createModule` |

## Module Import Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `no member named 'Pool' in 'Thread'` | Thread.Pool removed | Use `std.Io.Group` + `Io.async` |
| `no member named 'fixedBufferStream'` | Old stream API | Use `Io.Reader.fixed(...)` or `Io.Writer.fixed(...)` |
| `no field named 'getCwd' in 'process'` | Renamed | Use `std.process.currentPath*` |
| `no member named 'gpu' in 'std'` (0.17) | Renamed | Use `std.spirv` |
| `no member named 'IoUring' in 'Io'` (0.17) | Renamed | Use `std.Io.Uring` |

## Time / Duration Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `no member named 'Instant' in 'time'` | Moved to Io | Use `std.Io.Timestamp` |
| `no member named 'Timer' in 'time'` | Moved to Io | Use `std.Io.Timestamp` |
| `'{D}' format specifier removed` | Type safety | Use `Io.Duration{ .nanoseconds = ns }` with `{f}` |

## Type Introspection Errors (0.17)

| Error | Cause | Fix |
|-------|-------|-----|
| `no member named 'is_var_args' in 'Fn'` | Restructured | Use `.attrs.varargs` |
| `no member named 'params' in 'Fn'` | Restructured | Use `.param_types` |
| `no member named 'decls' in 'Struct'` | Restructured | Use `.decl_names` |

## Networking Errors (0.17)

| Error | Cause | Fix |
|-------|-------|-----|
| `expected type 'IpAddress', found '*const IpAddress'` | Now takes pointer | Pass `&address` instead of `address` |

## Parameter Order Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `expected type 'usize', found 'T'` on `containsAtLeastScalar` | Param order swapped in 0.17 | Check new signature: `(T, list, element, minimum)` |

## General Debugging Tips

1. **Run `zig build` first** — captures all errors
2. **Check `zig env`** — verify std_dir and version
3. **Grep the stdlib** — `grep -rn "pub fn funcName" $(zig env | jq -r .std_dir)`
4. **Read the error carefully** — Zig errors usually tell you exactly what's wrong
5. **Check for deprecated aliases** — old names often still work temporarily
