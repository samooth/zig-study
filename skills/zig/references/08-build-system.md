# Build System Reference

build.zig and build.zig.zon for Zig 0.16+/0.17+.

## build.zig.zon

### 0.16+ Required Fields

```zig
.{
    .name = .my_project,        // enum literal, NOT string
    .fingerprint = 0xa1b2c3d4, // required in 0.16+
    .version = "0.1.0",
    .dependencies = .{},
    .paths = .{""},
}
```

### Dependencies

```zig
.{
    .dependencies = .{
        .dep_name = .{
            .url = "git+https://example.com/repo#commit-hash",
            .hash = "...",
        },
    },
}
```

Fetch with: `zig fetch --save git+https://example.com/repo`

## build.zig

### Basic Structure

```zig
const std = @import("std");

pub fn build(b: *std.Build) void {
    const target = b.standardTargetOptions(.{});
    const optimize = b.standardOptimizeOption(.{});

    // Module
    const mod = b.createModule(.{
        .root_source_file = b.path("src/main.zig"),
        .target = target,
        .optimize = optimize,
    });

    // Executable
    const exe = b.addExecutable(.{
        .name = "myapp",
        .root_module = mod,
    });

    b.installArtifact(exe);

    // Run step
    const run_cmd = b.addRunArtifact(exe);
    run_cmd.step.dependOn(b.getInstallStep());

    const run_step = b.step("run", "Run the app");
    run_step.dependOn(&run_cmd.step);

    // Test step
    const tests = b.addTest(.{
        .root_module = mod,
    });
    const run_tests = b.addRunArtifact(tests);

    const test_step = b.step("test", "Run tests");
    test_step.dependOn(&run_tests.step);
}
```

### Module Imports

```zig
const mod = b.createModule(.{
    .root_source_file = b.path("src/lib.zig"),
    .imports = &.{
        .{ .name = "std", .module = b.createModule(.{}) },
        .{ .name = "mydep", .module = dep_module },
    },
});

exe.root_module.addImport("mylib", mod);
```

### Linking

```zig
// Link libc (0.16+ style)
const mod = b.createModule(.{
    .root_source_file = b.path("src/main.zig"),
    .link_libc = true,
});

// Link system library
mod.linkSystemLibrary("z", .{});

// Link framework (macOS)
mod.linkFramework("CoreFoundation", .{});
```

### Translate C (replaces @cImport)

```zig
const translate_c = b.addTranslateC(.{
    .root_source_file = b.path("src/c.h"),
    .target = target,
    .optimize = optimize,
});
translate_c.linkSystemLibrary("glfw", .{});

const exe = b.addExecutable(.{
    .name = "myapp",
    .root_module = b.createModule(.{
        .root_source_file = b.path("src/main.zig"),
        .imports = &.{
            .{ .name = "c", .module = translate_c.createModule() },
        },
    }),
});
```

### Options

```zig
const target = b.standardTargetOptions(.{});
const optimize = b.standardOptimizeOption(.{});

// Custom option
const use_thing = b.option(bool, "use_thing", "Enable thing") orelse false;
```

### Install Artifacts

```zig
b.installArtifact(exe);
b.installFile(b.path("data/config.json"), "bin/config.json");
b.installDir(.{ .sub_path = "share", .dirname = b.path("data") });
```

### Temporary Files

```zig
// 0.16+ — automatic cleanup
const tmp = b.addTempFiles();
```

### Package Dependencies

```zig
const dep = b.dependency("my_dep", .{
    .target = target,
    .optimize = optimize,
});
exe.root_module.addImport("my_dep", dep.module("my_dep"));
```

### Build Options

| CLI Option | Description |
|-----------|-------------|
| `--fork=<path>` | Local package override |
| `--fetch[=mode]` | Fetch packages locally |
| `--test-timeout <timeout>` | Test timeout |
| `--error-style` | Error formatting |
| `--multiline-errors` | Multi-line errors |
| `-Doptimize=ReleaseFast` | Optimization level |
| `-Dtarget=aarch64-linux` | Cross-compile target |
| `--watch` | Incremental watch mode |

### Fuzzing

```zig
zig build test --fuzz -Doptimize=ReleaseSafe
```

## Common Patterns

### System Library Detection

```zig
// There is no b.findSystemLibrary; link a system library onto a module instead:
const mod = b.createModule(.{ .root_source_file = b.path("src/main.zig") });
mod.linkSystemLibrary("z", .{});
```

### Conditional Compilation

```zig
if (target.result.os.tag == .linux) {
    // Linux-specific steps
}
```

### Custom Step

```zig
const step = b.addSystemCommand(&.{"python3", "scripts/generate.py"});
step.addFileInput(b.path("input.txt"));
step.addFileOutput(b.path("output.zig"));
```
