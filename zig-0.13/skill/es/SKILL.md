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

## Cuando usar este skill

- Escribiendo código Zig dirigido a **0.13.0** (compilador
  `<zvm-root>/0.13.0/zig`).
- Depurando errores de compilación en 0.13.0.
- Revisando código Zig 0.13.0 en busca de patrones anticuados de versiones
  posteriores.
- Migrando desde 0.12.x o anterior a 0.13.0.
- Trabajando con `build.zig` / `build.zig.zon` en el formato de 0.13.0.

> Nota: este skill cubre **0.13.0**, era **pre-`std.Io`**. Para 0.16.x / 0.17.x
> usa el skill `zig/` de este mismo repositorio.

## Versión objetivo y binary local

```bash
<zvm-root>/0.13.0/zig version   # 0.13.0
<zvm-root>/0.13.0/zig env       # std_dir, lib_dir, version
```

## Diferencias clave por versión (vista rápida)

| Característica | 0.12.x / 0.13.x (esta skill) | 0.14.0 | 0.16.x / 0.17.x (skill `zig`) |
|---|---|---|---|
| Punto de entrada | `pub fn main() !void` | igual | `pub fn main(init: std.process.Init) !void` |
| I/O archivos | `std.fs.cwd().openFile(...)` | igual | `std.Io.Dir.cwd().openFile(io, ...)` |
| I/O stdout | `std.io.getStdOut().writer()` | igual | `std.Io.File.stdout().writer(io, ...)` |
| Tiempo / sleep | `std.time.sleep(nanos)` | igual | `io.sleep(duration, clock)` |
| Aleatorio | `std.crypto.random.bytes(buf)` | igual | `io.random(buf)` |
| Allocator por defecto | `GeneralPurposeAllocator` | igual | `init.gpa` / `SafeAllocator` |
| ArrayList init | `ArrayList(T){}` | igual | `ArrayList(T).empty` |
| build.zig.zon | `.name = "x"` | + `.checksum` | `.name = .x` + `.fingerprint` |

## Reglas de oro (Zig 0.13.0)

1. **Allocator explícito.** Funciones que asignan reciben un `Allocator`.
2. **Error unions (`!`).** `try` para propagar, `errdefer` para limpieza ante error.
3. **Comptime sobre runtime.** Invariantes y generación de código en comptime.
4. **Tipos antes que funciones.** Define tipos con `struct`/`enum` antes de usarlos.

## Punto de entrada

```zig
pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();

    std.debug.print("hola, mundo\n", .{});
}
```

## Allocadores

```zig
const std = @import("std");

var gpa = std.heap.GeneralPurposeAllocator(.{}){};
defer _ = gpa.deinit();
const allocator = gpa.allocator();

var arena = std.heap.ArenaAllocator.init(allocator);
defer arena.deinit();
const tmp = arena.allocator();
```

## Archivos (API global pre-0.16)

```zig
const std = @import("std");

const file = try std.fs.cwd().openFile("datos.txt", .{});
defer file.close();

const contents = try file.readToEndAlloc(allocator, 1024 * 1024);
defer allocator.free(contents);
std.debug.print("contenido: {s}\n", .{contents});
```

## ArrayList y HashMap

```zig
const std = @import("std");

var lista = std.ArrayList(u32).init(allocator);
defer lista.deinit();
try lista.append(42);

var mapa = std.StringHashMap(u32).init(allocator);
defer mapa.deinit();
try mapa.put("clave", 99);
```

## Manejo de errores

```zig
const std = @import("std");

pub fn leer(path: []const u8, allocator: std.mem.Allocator) ![]u8 {
    const file = try std.fs.cwd().openFile(path, .{});
    errdefer file.close();
    return try file.readToEndAlloc(allocator, 1024 * 1024);
}
```

## build.zig y build.zig.zon (0.13.0)

**build.zig.zon:**

```zig
.{
    .name = "mi_app",
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
        .name = "mi_app",
        .root_source_file = b.path("src/main.zig"),
        .target = target,
        .optimize = optimize,
    });

    exe.root_module.link_libc = true;
    b.installArtifact(exe);
}
```

Comandos de cross-compilation:

```bash
zig build -Dtarget=x86_64-windows-gnu
zig build -Dtarget=x86_64-linux-musl
zig build -Dtarget=aarch64-macos
zig build -Dtarget=wasm32-wasi
```

## Detección de plataforma en compilación

```zig
const builtin = @import("builtin");

pub fn platformName() []const u8 {
    return switch (builtin.os.tag) {
        .windows => "Windows",
        .linux => if (builtin.abi == .android) "Android" else "Linux",
        .macos, .ios, .tvos, .watchos => "Apple",
        .freebsd, .netbsd, .openbsd => "BSD",
        .wasi, .emscripten => "Web",
        else => "Desconocido",
    };
}
```

## Referencias

- `tools/gen.py` — extrae `pub fn` de `<zig>/lib/std` y escribe las tablas de
  firmas + `functions.html` (regenera con
  `--zig <zvm-root>/0.13.0/zig`).
- `tools/verify.py` — verifica que las firmas generadas existan en el stdlib
  instalado.
- Instalación local: `<zvm-root>/0.13.0/lib/std` (fuente del stdlib).

> Tip: antes de inventar una firma, grepea el stdlib local:
> `grep -rn "pub fn readToEndAlloc" <zvm-root>/0.13.0/lib/std`
