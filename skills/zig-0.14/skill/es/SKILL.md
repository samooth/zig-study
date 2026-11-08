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

## Cuando usar este skill

- Escribiendo código Zig nuevo dirigido a **0.14.0** (compilador
  `<zvm-root>/0.14.0/zig`).
- Depurando errores de compilación en 0.14.0.
- Revisando código Zig 0.14.0 en busca de patrones anticuados de versiones
  posteriores (0.16+ usa `std.Io`, `pub fn main(init: std.process.Init)`,
  etc.).
- Migrando desde 0.13.x o anterior a 0.14.0.
- Trabajando con `build.zig` / `build.zig.zon` en el formato de 0.14.0.

> Nota: este skill cubre **0.14.0**, que pertenece a la era **pre-`std.Io`**.
> Para 0.16.x / 0.17.x usa el skill `zig/` de este mismo repositorio.

## Versión objetivo y binary local

```bash
<zvm-root>/0.14.0/zig version   # 0.14.0
<zvm-root>/0.14.0/zig env       # std_dir, lib_dir, version
```

## Diferencias clave por versión (vista rápida)

| Característica | 0.13.x / 0.14.x (esta skill) | 0.16.x / 0.17.x (skill `zig`) |
|---|---|---|
| Punto de entrada | `pub fn main() !void` | `pub fn main(init: std.process.Init) !void` |
| I/O archivos | `std.fs.cwd().openFile(...)` (global) | `std.Io.Dir.cwd().openFile(io, ...)` |
| I/O stdout | `std.io.getStdOut().writer()` | `std.Io.File.stdout().writer(io, ...)` |
| Tiempo / sleep | `std.time.sleep(nanos)` | `io.sleep(duration, clock)` |
| Aleatorio | `std.crypto.random.bytes(buf)` | `io.random(buf)` |
| Allocator por defecto | `std.heap.GeneralPurposeAllocator` | `init.gpa` / `SafeAllocator` |
| ArrayList init | `ArrayList(T){}` | `ArrayList(T).empty` |
| build.zig.zon | `.name = "x"` | `.name = .x` + `.fingerprint` |
| `@enumFromInt/@intFromEnum` | estándar | `@fromBackingInt/@backingInt` añadido en 0.17 |

## Reglas de oro (Zig 0.14.0)

1. **Asigna un allocator explícito.** Las funciones que asignan reciben un
   `Allocator` como primer parámetro (convención de 0.14).
2. **Error unions (`!`).** Propaga errores con `try` y limpia con `errdefer`.
   Nunca ignores errores con `catch ignore` en código de producción.
3. **No asumas I/O global persistente.** `std.io.getStdOut()` / `std.io.getStdErr()`
   existen en 0.14 pero se consideran legado; pásale `stdout`/`stderr` como
   parámetros cuando sea posible para preparar la migración a 0.16+.
4. **Comptime sobre runtime.** Usa bloques `comptime {}` y valores
   comptime-known para invariantes y generación de código.
5. **build.zig.zon requiere `.checksum`.** En 0.14 las dependencias se declaran
   en `build.zig.zon` con `.checksum` (hash del contenido).

## Punto de entrada

```zig
// CORRECT — 0.14.0 style (sin Init, sin io global obligatorio)
pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator{};
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

// Para temporales de vida corta:
var arena = std.heap.ArenaAllocator.init(allocator);
defer arena.deinit();
const tmp = arena.allocator();
```

## Archivos (API global pre-0.16)

```zig
const std = @import("std");

// Abrir para lectura (0.14 API global)
const file = try std.fs.cwd().openFile("datos.txt", .{});
defer file.close();

// Leer todo el contenido
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

## build.zig y build.zig.zon (0.14.0)

**build.zig.zon:**

```zig
.{
    .name = "mi_app",
    .version = "0.1.0",
    .dependencies = &.{},
    .checksum = "...", // hash de contenido requerido en 0.14
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
  firmas + `functions.html` (regenera con `--zig <zvm-root>/0.14.0/zig`).
- `tools/verify.py` — verifica que las firmas generadas existan en el stdlib
  instalado.
- Deep dive: `zig-0.16.0-resource-map/` y `zig-0.17.0-resource-map/` de este
  repo (solo como referencia conceptual; las firmas difieren en 0.14.0).
- Instalación local: `<zvm-root>/0.14.0/lib/std` (fuente del stdlib).

> Tip: antes de inventar una firma, grepea el stdlib local:
> `grep -rn "pub fn readToEndAlloc" <zvm-root>/0.14.0/lib/std`
