---
name: zig-0.13
description: >-
  Zig 0.13.0 patterns and best practices. Use when writing, reviewing, debugging
  or migrating Zig 0.13.0 code. Covers language semantics, standard library
  (pre-std.Io era), allocators, build.zig/build.zig.zon, and cross-compilation.
license: MIT
compatibility:
  - claude-code
  - opencode
  - codex
metadata:
  version: "0.13.0"
  language: "zig"
  category: "programming-language"
---

# SKILL: Zig 0.13.0

## When to use this skill

- Writing new Zig code targeting **0.13.0** (compiler at
  `<zvm-root>/0.13.0/zig`).
- Debugging compilation errors in 0.13.0.
- Reviewing Zig 0.13.0 code for outdated patterns from later versions.
- Migrating from 0.12.x or earlier to 0.13.0.
- Working with `build.zig` / `build.zig.zon` in the 0.13.0 format.

> Note: this skill covers **0.13.0**, belonging to the **pre-`std.Io` era**.
> For 0.16.x / 0.17.x use the `zig/` skill in this same repository.

## Target version and local binary

```bash
<zvm-root>/0.13.0/zig version   # 0.13.0
<zvm-root>/0.13.0/zig env       # std_dir, lib_dir, version
```

## Key differences by version (quick view)

| Feature | 0.12.x / 0.13.x (this skill) | 0.14.0 | 0.16.x / 0.17.x (`zig` skill) |
|---|---|---|---|
| Entry point | `pub fn main() !void` | same | `pub fn main(init: std.process.Init) !void` |
| File I/O | `std.fs.cwd().openFile(...)` | same | `std.Io.Dir.cwd().openFile(io, ...)` |
| Stdout I/O | `std.io.getStdOut().writer()` | same | `std.Io.File.stdout().writer(io, ...)` |
| Time / sleep | `std.time.sleep(nanos)` | same | `io.sleep(duration, clock)` |
| Random | `std.crypto.random.bytes(buf)` | same | `io.random(buf)` |
| Default allocator | `GeneralPurposeAllocator` | same | `init.gpa` / `SafeAllocator` |
| ArrayList init | `ArrayList(T){}` | same | `ArrayList(T).empty` |
| build.zig.zon | `.name = "x"` | + `.checksum` | `.name = .x` + `.fingerprint` |

## Golden rules (Zig 0.13.0)

1. **Explicit allocator.** Functions that allocate receive an `Allocator`.
2. **Error unions (`!`).** `try` to propagate, `errdefer` to clean up on error.
3. **Comptime over runtime.** Invariants and code generation in comptime.
4. **Types before functions.** Define types with `struct`/`enum` before using them.

## Entry point

```zig
pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
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

var arena = std.heap.ArenaAllocator.init(allocator);
defer arena.deinit();
const tmp = arena.allocator();
```

## Files (pre-0.16 global API)

```zig
const std = @import("std");

const file = try std.fs.cwd().openFile("data.txt", .{});
defer file.close();

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

## build.zig and build.zig.zon (0.13.0)

**build.zig.zon:**

```zig
.{
    .name = "my_app",
    .version = "0.1.0",
    .dependencies = &.{},
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
  `--zig <zvm-root>/0.13.0/zig`).
- `tools/verify.py` — verifies generated artifacts exist in the installed
  stdlib.
- Local installation: `<zvm-root>/0.13.0/lib/std` (stdlib source).

> Tip: before inventing a signature, grep the local stdlib:
> `grep -rn "pub fn readToEndAlloc" <zvm-root>/0.13.0/lib/std`
