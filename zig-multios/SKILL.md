---
name: zig-multios
description: >-
  Zig multiplataforma (Windows/Linux/macOS/Android/WASM) para 0.16.x y 0.17.x.
  Úsalo al escribir o revisar código cross-platform, build.zig para
  cross-compilation, detección de plataforma y gotchas por SO. NO es un skill
  exclusivo de un solo SO.
license: MIT
compatibility:
  - claude-code
  - opencode
  - codex
metadata:
  version: "0.16.x / 0.17.x"
  language: "zig"
  category: "programming-language"
---

# SKILL: Zig Cross-Platform Expert (multi-OS)

## Rol y contexto

Eres un arquitecto de software experto en Zig. Tu especialidad es código nativo,
de alto rendimiento y **estrictamente multiplataforma** (Windows, Linux,
macOS, Android, WASM). Genera código que compile limpiamente en cualquier
target sin hacks de preprocesador, aprovechando el sistema de tipos, el sistema
de build y las abstracciones de la librería estándar.

Versiones verificadas: **0.16.0** y **0.17.0** (instaladas en
`<zvm-root>/`). Para versiones anteriores (0.10–0.14) usa los skills
`zig-0.10` … `zig-0.14` (era pre-`std.Io`).

## 1. Reglas de oro (0.16.x / 0.17.x)

1. **I/O como interfaz.** Toda I/O (archivos, tiempo, aleatorio, sleep, red)
   pasa por un parámetro `io: std.Io`. No existen las APIs globales
   `std.io.getStdOut()`, `std.time.sleep()`, `std.fs.cwd()`.
2. **Punto de entrada "juicy main":** `pub fn main(init: std.process.Init) !void`;
   de ahí obtienes `init.io`, `init.gpa`, `init.arena`, `init.minimal.args`.
3. **Allocators.** Código nuevo: `init.gpa` (Debug con detección de leaks),
   `std.heap.SmpAllocator` (release multihilo) o `std.heap.ArenaAllocator`
   (temporales). `DebugAllocator` es alias deprecated de `SafeAllocator` (0.17).
4. **Errores.** Usa error unions (`!`) y `try`; `errdefer` para limpieza solo
   ante error. `catch unreachable` solo en tests o errores demostrablemente
   imposibles.

### Rutas de archivos

Nunca concatenes separadores a mano. Usa `std.fs.path`:

```zig
const std = @import("std");

// ❌ MAL — falla en Windows y no valida componentes
// const path = "src/" ++ file ++ ".txt";

// ✅ BIEN — separador nativo, allocador explícito
const path = try std.fs.path.join(allocator, &.{ "src", file, "data.txt" });
defer allocator.free(path);
// Complementos: dirname, basename, extension, resolve, relative
```

### Llamadas al sistema (qué usar en cada caso)

| Necesidad | API (0.16 / 0.17) |
|---|---|
| I/O portable (archivos, dirs) | `std.Io` + `std.fs` (`Dir`/`File` con parámetro `io`) |
| POSIX genérico (open/read/mmap/stat…) | `std.posix` |
| Syscalls Linux (epoll, io_uring, inotify) | `std.os.linux` |
| APIs nativas Windows (NtDll, handles) | `std.os.windows` |
| WASI | `std.os.wasi` |
| macOS específica | `std.posix` cubre macOS; bits específicos en `std.c`/`std.posix.darwin` |
  (no existe `std.os.darwin` como módulo independiente) |

`std.os` **no está deprecado**; aloja `std.os.linux`, `std.os.windows`,
`std.os.wasi`, etc.

### Hilos, tiempo y entorno

- **Hilos:** `std.Thread.spawn`, `std.Thread.Mutex`, `std.Thread.Condition`.
  `std.Thread.Pool` fue eliminado; usa `std.Io.Group` + `std.Io.async`
  (`io.concurrent`) para concurrencia estructurada.
- **Tiempo:** nada de `std.time.nanoTimestamp()`. Usa relojes explícitos
  (`std.Io.Clock`: `.real` wall-clock Unix, `.awake`/`.boot` monotónicos,
  `.cpu_process`/`.cpu_thread`):

```zig
const wall = std.Io.Timestamp.now(io, .real); // ns desde epoch Unix
const mono = std.Io.Clock.Timestamp.now(io, .awake); // monotónico
try std.Io.sleep(io, .{ .nanoseconds = 50 * std.time.ns_per_ms }, .awake);
```

Las duraciones/timestamps son `Io.Duration`/`Io.Timestamp` (`raw.nanoseconds:
i96`) con `durationTo`/`addDuration`/`subDuration` y comparación mediante
`std.math.CompareOperator`.

- **Entorno:** en 0.16+ el entorno no es global; llega por
  `init.minimal.environ` (`std.process.Environ`). `Environ.Map` es
  case-insensitive en Windows y case-sensitive en POSIX. Helpers:
  `environ.createMap(allocator)`, `Environ.getAlloc(environ, gpa, "KEY")`,
  `environ.containsConstant("KEY")`.

## 2. Detección de plataforma en tiempo de compilación

Usa `@import("builtin")`; el compilador elimina el código muerto (DCE).

```zig
const builtin = @import("builtin");

pub fn getPlatformName() []const u8 {
    return switch (builtin.os.tag) {
        .windows => "Windows",
        // Android es linux + abi android (también .androideabi en ARM 32-bit)
        .linux => if (builtin.abi.isAndroid()) "Android" else "Linux",
        .macos, .ios, .tvos, .watchos, .visionos, .maccatalyst => "Apple",
        .freebsd, .netbsd, .openbsd, .dragonfly => "BSD",
        .wasi, .emscripten => "Web",
        else => "Unknown",
    };
}
```

Verificado compilado nativo y cross: `x86_64-windows-gnu`, `aarch64-macos`,
`wasm32-wasi` (0.16.0).

Para lógica que depende del target completo, `builtin.target` (`std.Target`)
expone `cpu.arch`, `os.tag`, `abi` y `os.version_range`. Detecciones útiles:
`builtin.abi.isAndroid()`, `builtin.cpu.arch.isX86()/.isARM()`,
`builtin.link_libc`.

## 3. Patrón de arquitectura multiplataforma (módulo inyectado)

En lugar de llenar el código de `if (is_windows)`, inyecta módulos diferentes
desde el `build.zig`.

**Estructura de archivos:**

```
src/
  main.zig
  platform/
    api.zig        # Interfaz común (decls + docs)
    windows.zig    # Implementación Windows
    posix.zig      # Implementación Linux/macOS/BSD
```

**En `build.zig`:**

```zig
const platform_mod = switch (target.result.os.tag) {
    .windows => b.createModule(.{
        .root_source_file = b.path("src/platform/windows.zig"),
        .target = target,
        .optimize = optimize,
    }),
    else => b.createModule(.{
        .root_source_file = b.path("src/platform/posix.zig"),
        .target = target,
        .optimize = optimize,
    }),
};
exe.root_module.addImport("platform", platform_mod);
```

**En `src/main.zig`:**

```zig
const platform = @import("platform");
// platform.doSomething(io) — misma firma en ambos backends.
```

Consejo: define el "contrato" en `api.zig` y réplicalo en cada implementación.
Si un backend necesita un parámetro extra, usa una función `available()`
comptime en lugar de un `unreachable` silencioso. El `else` cubre WASM/BSD/
móvil: solo úsalo si `posix.zig` realmente compila en esos targets, o lista los
casos POSIX explícitamente.

## 4. El sistema de build (`build.zig`) en 0.16 / 0.17

Usa la API moderna de `std.Build` (todo vía `root_module`). Configura target y
optimización como opciones estándar para permitir cross-compilation desde la
CLI.

```zig
const std = @import("std");

pub fn build(b: *std.Build) void {
    // 1. -Dtarget=x86_64-windows-gnu, -Doptimize=ReleaseFast, etc.
    const target = b.standardTargetOptions(.{});
    const optimize = b.standardOptimizeOption(.{});

    // 2. Ejecutable (root_module obligatorio)
    const exe = b.addExecutable(.{
        .name = "mi_app",
        .root_module = b.createModule(.{
            .root_source_file = b.path("src/main.zig"),
            .target = target,
            .optimize = optimize,
        }),
    });

    // 3. LibC (matizar por OS — ver sección 5)
    const os_tag = target.result.os.tag;
    if (os_tag == .windows or os_tag == .linux or os_tag == .macos) {
        exe.root_module.link_libc = true;
    }
    // Android: NO pongas link_libc ni linkSystemLibrary("log") aquí:
    // Bionic no está vendorizado; falla sin el sysroot del NDK.

    b.installArtifact(exe);
}
```

Comandos de cross-compilation (funcionan sin instalar toolchains):

```bash
zig build -Dtarget=x86_64-windows-gnu          # Windows x64 (MinGW vendorizado)
zig build -Dtarget=aarch64-windows-gnu         # Windows ARM64
zig build -Dtarget=x86_64-linux-musl           # Linux estático (musl)
zig build -Dtarget=aarch64-linux-gnu           # Linux ARM64 (glibc)
zig build -Dtarget=aarch64-macos               # macOS ARM64
zig build -Dtarget=x86_64-macos                # macOS Intel
zig build -Dtarget=wasm32-wasi                 # WASI
zig build -Dtarget=x86_64-linux-android        # Android (ver sección 5)
```

En 0.16.0, para librerías compartidas usa
`b.addLibrary(.{ .linkage = .dynamic, ... })` — **`b.addSharedLibrary()` ya no
existe**.

## 5. Trucos y "gotchas" por sistema operativo

### 🪟 Windows

- **Consola y UTF-8:** La consola de Windows usa por defecto una codepage
  legacy (no UTF-8). Con `std.Io.File.stdout()` esto importa poco (escribe vía
  `NtWriteFile` sin pasar por la codepage), pero para entrada de consola y
  programas C externos conviene `SetConsoleOutputCP(65001)` (vía `@cImport`/
  translate-c del SDK de Windows). Guarda siempre el fuente en UTF-8.
- **Salida estándar correcta en 0.16:**

```zig
std.debug.print("hola\n", .{});
// std.Io.File.stdout() también existe para escritura vía Io cuando se necesita.
```

- **Extensiones:** `zig build` añade `.exe` automáticamente en Windows.
- **Rutas largas:** límite clásico de 260 chars (`MAX_PATH`) salvo manifiesto
  `longPathAware` + registro, o prefijo `\\?\`. Zig maneja rutas UTF-8→UTF-16
  internamente; controla el manifiesto con `exe.win32_manifest` en build.zig.
- **Subsistemas:** apps GUI sin consola, `exe.subsystem = .windows`; consola
  explícita, `.console` (en 0.16.0 los valores de `std.zig.Subsystem` son
  minúsculas; `.Console`/`.Windows` son aliases deprecated).

### 🐧 Linux

- **glibc vs musl:** Para máxima portabilidad binaria,
  `-Dtarget=x86_64-linux-musl` produce estáticos que corren en cualquier
  distro (sin `libc.so.6 not found`). glibc cross (`x86_64-linux-gnu`) también
  es vendorizada y válida cuando quieres linking dinámico (plugins, OpenSSL del
  sistema).
- **Permisos:** `chmod` POSIX ya no está en `std.posix` en 0.16; la API
  portable es la de `std.Io`:

```zig
const f = try std.Io.Dir.createFile(std.Io.Dir.cwd(), io, "script.sh", .{});
defer std.Io.File.close(f, io);
try std.Io.File.setPermissions(f, io, @enumFromInt(0o755));
```

### 🍎 macOS

- **SDK:** para apps de terminal puras (Zig sin frameworks de Apple) no
  necesitas SDK: Zig vendoriza `libSystem.tbd` y enlaza bien desde Linux/
  Windows. Necesitas el SDK de Apple (o `apple-sdks`) si enlazas frameworks
  GUI (Cocoa, Metal, CoreFoundation) — pásalo con `--sysroot`/`-isysroot` o
  usa `xcrun` en una Mac.
- **Firma (code signing):** el linker de Zig emite firma ad-hoc en los Mach-O
  (incluidos los cross-compilados desde Linux), suficiente para ejecutar
  localmente. Para distribución (notarización, Gatekeeper) sí necesitas firmar
  con identidad real (`codesign` + `notarytool`) desde macOS.

### 🤖 Android

- **Qué sale de la caja (0.16.0):**
  - `zig build -Dtarget=x86_64-linux-android` (o `aarch64-...`) compila ELF
    **sin `link_libc`** (std usa syscalls directas).
  - `zig build-lib -target=aarch64-linux-android -dynamic` produce una `.so`
    válida (la vía correcta para apps).
  - Enlazar libc **falla sin el NDK**: Bionic no está vendorizado. Con el
    sysroot del NDK (`--sysroot` + `-target ...-android<API>` vía `zig cc`)
    sí se puede.
- **El flujo real:** compila la lógica pesada (motor, parser, IA) como
  **librería compartida** con `b.addLibrary(.{ .linkage = .dynamic, ... })` y
  cárgala desde Kotlin/JNI (NDK) o empaquétala en un `.apk`. Un ejecutable suelto
  solo corre en `/data/local/tmp` (con `run-as`/adb, apps debug) o con root;
  no es distribuible.
- **Logging:** no uses stdout en Android. Con el NDK enlaza `liblog`
  (`linkSystemLibrary("log", .{})` solo contra el sysroot del NDK) y llama
  `__android_log_print` vía translate-c.

### 🌐 WASM / WASI

- `zig build -Dtarget=wasm32-wasi` compila sin toolchain adicional.
- No hay filesystem real por defecto; usa `std.Io` sobre las capacidades WASI
  que el host conceda.
- Para ejecutar fuera del navegador usa un runtime WASI (wasmtime, wasmer, etc.).

## 6. Manejo de memoria en entornos cruzados

- **Tamaño de página:** nunca asumas 4096. En 0.16.0 `std.mem.page_size` ya no
  existe. Consulta en runtime `std.heap.pageSize()` o usa
  `std.heap.page_size_min` / `page_size_max` (mínimos/máximos garantizados) en
  comptime.
- **Layout de structs:** el compilador de Zig **nunca reordena campos**, pero el
  layout por defecto no es estable entre versiones/arquitecturas. Para ABI C o
  wire-format usa `extern struct` (layout C, mantiene padding del ABI) y
  aporta `@bitSizeOf`/`@offsetOf` en asserts. `packed struct` elimina padding
  in-registry pero **no** soluciona endianidad en red: serializa campos
  explícitamente.
- **Allocators:** `std.heap.page_allocator` solo para memoria cruda del SO.
  Para la app: `init.gpa` (Debug trae detección de leaks),
  `std.heap.DebugAllocator(.{})` explícito, `std.heap.SmpAllocator` para
  release multihilo, `std.heap.ArenaAllocator` (thread-safe y lock-free desde
  0.16.0) para grupos de objetos de vida corta.

## 7. Instrucciones de comportamiento para la IA

Cuando generes código Zig en este contexto:

1. **Valida el target:** si el usuario pide una función específica de un SO,
   pregúntate: "¿Cómo hago esto en los otros SOs?". Si no puedes, aísla el
   código en un módulo condicional (sección 3).
2. **Manejo de errores:** usa SIEMPRE error unions (`!`) y `try`. No uses
   `catch unreachable` salvo en tests o errores matemáticamente imposibles.
3. **C-Interop:** en 0.16+ `@cImport` está **deprecado**; prefiere
   `b.addTranslateC` en build.zig e `@import("c")` del módulo resultante.
   Asegúrate de que las cabeceras existan en el target (p.ej. no uses headers
   de Linux al compilar para Windows).
4. **Sistema de build:** si el usuario pide compilar para X plataforma, da el
   comando exacto `zig build -Dtarget=...` y verifica que las libc/side-effects
   (manifest, subsystem) estén en build.zig.
5. **Comprobación de API:** ante la duda, grepea la stdlib local antes de
   inventar firmas:
   `grep -rn "pub fn join" $(zig env | jq -r .std_dir)`.
6. **Comandos de verificación sugeridos:**

```bash
zig build && zig build test
zig build -Dtarget=x86_64-windows-gnu
zig build -Dtarget=aarch64-macos
zig build -Dtarget=wasm32-wasi
zig fmt src/
```

## Referencias

- `zig/` (skill principal) — patrones, lenguaje, std.Io, process, allocators,
  collections, encoding, crypto, build system, errores comunes, idioms,
  migración 0.16→0.17.
- `zig-0.16.0-resource-map/` y `zig-0.17.0-resource-map/` — deep dive por
  versión.
- `tools/gen.py` / `tools/verify.py` / `tools/check-skill-examples.py` —
  generación y verificación de tablas de firmas y ejemplos.
