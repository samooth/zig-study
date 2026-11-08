---
name: zig-0.14
description: >-
  Zig 0.14.0 patterns and best practices. Use when writing, reviewing, debugging
  or migrating Zig 0.14.0 code. Covers language semantics, standard library
  (pre-std.Io era), allocators, build.zig/build.zig.zon, and cross-compilation.
  Zig 0.14.0 still uses the pre-0.16 global I/O API
  (std.fs.cwd, std.io.getStdOut, std.time.sleep, etc.).
license: MIT
compatibility:
  - claude-code
  - opencode
  - codex
metadata:
  version: "0.14.0"
  language: "zig"
  category: "programming-language"
---

# SKILL: Zig 0.14.0

## When to use this skill

- Writing new Zig code targeting **0.14.0** (compiler at
  `<zvm-root>/0.14.0/zig`).
- Debugging compilation errors in 0.14.0.
- Reviewing Zig 0.14.0 code for outdated patterns from later versions
  (0.16+ uses `std.Io`, `pub fn main(init: std.process.Init)`, etc.).
- Migrating from 0.13.x or earlier to 0.14.0.
- Working with `build.zig` / `build.zig.zon` in the 0.14.0 format.

> Note: this skill covers **0.14.0**, belonging to the **pre-`std.Io` era**.
> For 0.16.x / 0.17.x use the `zig/` skill in this same repository.

## Target version and local binary

```bash
<zvm-root>/0.14.0/zig version   # 0.14.0
<zvm-root>/0.14.0/zig env       # std_dir, lib_dir, version
```

## Key differences by version (quick view)

| Feature | 0.13.x / 0.14.x (this skill) | 0.16.x / 0.17.x (`zig` skill) |
|---|---|---|
| Entry point | `pub fn main() !void` | `pub fn main(init: std.process.Init) !void` |
| File I/O | `std.fs.cwd().openFile(...)` (global) | `std.Io.Dir.cwd().openFile(io, ...)` |
| Stdout I/O | `std.io.getStdOut().writer()` | `std.Io.File.stdout().writer(io, ...)` |
| Time / sleep | `std.time.sleep(nanos)` | `io.sleep(duration, clock)` |
| Random | `std.crypto.random.bytes(buf)` | `io.random(buf)` |
| Default allocator | `std.heap.GeneralPurposeAllocator` | `init.gpa` / `SafeAllocator` |
| ArrayList init | `ArrayList(T){}` | `ArrayList(T).empty` |
| build.zig.zon | `.name = "x"` | `.name = .x` + `.fingerprint` |
| `@enumFromInt/@intFromEnum` | standard | `@fromBackingInt/@backingInt` added in 0.17 |

## Golden rules (Zig 0.14.0)

1. **Assign an explicit allocator.** Functions that allocate receive an
   `Allocator` as first parameter (0.14 convention).
2. **Error unions (`!`).** Propagate errors with `try` and clean up with
   `errdefer`. Never ignore errors with `catch ignore` in production code.
3. **Do not assume persistent global I/O.** `std.io.getStdOut()` /
   `std.io.getStdErr()` exist in 0.14 but are considered legacy; pass
   `stdout`/`stderr` as parameters when possible to ease migration to 0.16+.
4. **Comptime over runtime.** Use `comptime {}` blocks and comptime-known
   values for invariants and code generation.
5. **build.zig.zon requires `.checksum`.** In 0.14 dependencies are declared in
   `build.zig.zon` with `.checksum` (content hash).

## Entry point

```zig
// CORRECT — 0.14.0 style (no Init, no mandatory global io)
pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator{};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();

    std.debug.print("hello, world\n", .{});
}
```

## Allocators

```zig
const std = @import("std");

var gpa = std.heap.GeneralPurposeAllocator(.{}){};
defer _ = gpa.deinit();
const allocator = gpa.allocator();

// For short-lived temporaries:
var arena = std.heap.ArenaAllocator.init(allocator);
defer arena.deinit();
const tmp = arena.allocator();
```

## Files (pre-0.16 global API)

```zig
const std = @import("std");

// Open for reading (0.14 global API)
const file = try std.fs.cwd().openFile("data.txt", .{});
defer file.close();

// Read entire contents
const contents = try file.readToEndAlloc(allocator, 1024 * 1024);
defer allocator.free(contents);
std.debug.print("contents: {s}\n", .{contents});
```

## ArrayList and HashMap

```zig
const std = @import("std");

var list = std.ArrayList(u32).init(allocator);
defer list.deinit();
try list.append(42);

var map = std.StringHashMap(u32).init(allocator);
defer map.deinit();
try map.put("key", 99);
```

## Error handling

```zig
const std = @import("std");

pub fn read(path: []const u8, allocator: std.mem.Allocator) ![]u8 {
    const file = try std.fs.cwd().openFile(path, .{});
    errdefer file.close();
    return try file.readToEndAlloc(allocator, 1024 * 1024);
}
```

## build.zig and build.zig.zon (0.14.0)

**build.zig.zon:**

```zig
.{
    .name = "my_app",
    .version = "0.1.0",
    .dependencies = &.{},
    .checksum = "...", // content hash required in 0.14
    .ref = .{
        .target = .native,
        .optimize = .ReleaseFast,
    },
}
```

**build.zig:**

```zig
const std = @import("std");

pub fn build(b: *std.Build) void {
    const target = b.standardTargetOptions(.{});
    const optimize = b.standardOptimizeOption(.{});

    const exe = b.addExecutable(.{
        .name = "my_app",
        .root_source_file = b.path("src/main.zig"),
        .target = target,
        .optimize = optimize,
    });

    exe.root_module.link_libc = true;
    b.installArtifact(exe);
}
```

Cross-compilation commands:

```bash
zig build -Dtarget=x86_64-windows-gnu
zig build -Dtarget=x86_64-linux-musl
zig build -Dtarget=aarch64-macos
zig build -Dtarget=wasm32-wasi
```

## Compile-time platform detection

```zig
const builtin = @import("builtin");

pub fn platformName() []const u8 {
    return switch (builtin.os.tag) {
        .windows => "Windows",
        .linux => if (builtin.abi == .android) "Android" else "Linux",
        .macos, .ios, .tvos, .watchos => "Apple",
        .freebsd, .netbsd, .openbsd => "BSD",
        .wasi, .emscripten => "Web",
        else => "Unknown",
    };
}
```

## References

- `tools/gen.py` — extracts `pub fn` from `<zig>/lib/std` and writes the
  signature tables + `functions.html` viewer (regenerate with
  `--zig <zvm-root>/0.14.0/zig`).
- `tools/verify.py` — verifies generated artifacts exist in the installed
  stdlib.
- Deep dive: `zig-0.16.0-resource-map/` and `zig-0.17.0-resource-map/` in this
  repo (conceptual reference only; signatures differ in 0.14.0).
- Local installation: `<zvm-root>/0.14.0/lib/std` (stdlib source).

> Tip: before inventing a signature, grep the local stdlib:
> `grep -rn "pub fn readToEndAlloc" <zvm-root>/0.14.0/lib/std`
