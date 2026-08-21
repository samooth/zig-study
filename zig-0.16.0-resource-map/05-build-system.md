# Zig 0.16.0 — Build System Changes

## build.zig.zon Changes

### Fingerprint Required

`build.zig.zon` now requires a `fingerprint` field, and `name` must be an enum literal (not a string):

```zig
.{
    .name = .my_project,  // was: .name = "my_project"
    .fingerprint = 0xa1b2c3d4,  // NEW — required
    .version = "0.1.0",
    .dependencies = .{},
    .paths = .{""},
}
```

### New CLI Options

| Option | Description |
|--------|-------------|
| `--fork=<path>` | Local package override |
| `--fetch[=mode]` | Fetch packages into project-local directory |
| `--test-timeout <timeout>` | Unit test timeout |
| `--error-style` | Error message formatting |
| `--multiline-errors` | Multi-line error display |

## Build API Changes

### `b.addExecutable` Redesigned

No longer accepts `root_source_file` directly. Must create a module first:

```zig
// OLD
const exe = b.addExecutable(.{
    .name = "myapp",
    .root_source_file = b.path("src/main.zig"),
    .target = target,
    .optimize = optimize,
});

// NEW
const exe = b.addExecutable(.{
    .name = "myapp",
    .root_module = b.createModule(.{
        .root_source_file = b.path("src/main.zig"),
        .target = target,
        .optimize = optimize,
        .imports = &.{
            .{ .name = "dep", .module = dep_module },
        },
    }),
});
```

### `b.addTranslateC` for C Translation

Replaces `@cImport`. Handles system library linking:

```zig
const translate_c = b.addTranslateC(.{
    .root_source_file = b.path("src/c.h"),
    .target = target,
    .optimize = optimize,
});
translate_c.linkSystemLibrary("glfw", .{});
translate_c.linkSystemLibrary("epoxy", .{});

const exe = b.addExecutable(.{
    .name = "tetris",
    .root_module = b.createModule(.{
        .root_source_file = b.path("src/main.zig"),
        .target = target,
        .optimize = optimize,
        .imports = &.{
            .{
                .name = "c",
                .module = translate_c.createModule(),
            },
        },
    }),
});
```

### Temporary Files API

```zig
// OLD
const tmp_path = b.makeTempPath();
try b.addRemoveDirTree(tmp_path);

// NEW
const tmp_files = b.addTempFiles(&.{"*.tmp"});
// Build runner handles cleanup automatically
```

### Module System

Modules are now first-class:

```zig
const my_mod = b.createModule(.{
    .root_source_file = b.path("src/lib.zig"),
    .target = target,
    .optimize = optimize,
    .imports = &.{
        .{ .name = "std", .module = b.createModule(.{}) },
    },
});

exe.root_module.addImport("mylib", my_mod);
```

### Linking Changes

```zig
// OLD
exe.linkLibC();
exe.linkSystemLibrary("z");

// NEW — link_libc is a module option
const mod = b.createModule(.{
    .root_source_file = b.path("src/main.zig"),
    .link_libc = true,
});
mod.linkSystemLibrary("z", .{});
```

## Package Management

### Fetching Dependencies

```zig
// Add a dependency
zig fetch --save git+https://codeberg.org/ziglang/translate-c

// This adds to build.zig.zon:
// .dependencies = .{
//     .translate_c = .{
//         .url = "git+https://codeberg.org/ziglang/translate-c#<hash>",
//         .hash = "<hash>",
//     },
// },
```

### Using Dependencies

```zig
const translate_c_dep = b.dependency("translate_c", .{});

const t: Translator = .init(translate_c_dep, .{
    .c_source_file = .{ .cwd_relative = "/usr/include/zstd.h" },
    .target = target,
    .optimize = optimize,
});

t.linkSystemLibrary("zstd", .{});
exe.root_module.addImport("zstd", t.mod);
```

## Fuzzing

Built-in fuzzer support:

```zig
zig build test --fuzz -Doptimize=ReleaseSafe
```

## Watch Mode

Incremental compilation with file watching:

```zig
zig build --watch
```

## New Build Step Types

| Step | Purpose |
|------|---------|
| `WriteFile` | Generate source files |
| `CheckFile` | Verify file contents |
| `CheckObject` | Verify binary objects |
| `ObjCopy` | Copy/transform object files |
| `Fmt` | Format source files |
| `TranslateC` | C translation |
| `UpdateSourceFiles` | Batch source updates |

## Migration Checklist

- [ ] Add `fingerprint` to `build.zig.zon`
- [ ] Change `.name = "x"` to `.name = .x` in `build.zig.zon`
- [ ] Replace `root_source_file` with `root_module = b.createModule(...)`
- [ ] Replace `@cImport` with `b.addTranslateC`
- [ ] Replace `linkLibC()` with `link_libc = true` in module options
- [ ] Replace `b.makeTempPath()` with `b.addTempFiles`
- [ ] Update module imports to use `b.createModule` pattern
