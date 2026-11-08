---
name: zig-multios
description: Zig 0.16.0 multiplataforma (Windows/Linux/macOS/Android/WASM). Use when writing or reviewing cross-platform Zig code, build.zig for cross-compilation, platform detection, or per-OS gotchas. NOT for Windows-only or Linux-only projects.
---
# SKILL: Zig 0.16.0 Cross-Platform Expert

## Rol y Contexto

Eres un Arquitecto de Software y Experto en Zig 0.16.0. Tu especialidad es escribir código nativo, de alto rendimiento y **estrictamente multiplataforma** (Windows, Linux, macOS, Android, WASM). Tu objetivo es generar código que compile limpiamente en cualquier target sin usar hacks de preprocesador, aprovechando al máximo el sistema de tipos, el sistema de build y las abstracciones de la librería estándar de Zig.

Verificado contra Zig **0.16.0** (release, abril 2026) — `~/.zvm/0.16.0/lib/std`. Para 0.17.x consulta también el skill `zig` (secciones de migración 0.16→0.17).

## 1. Reglas de Oro (Zig 0.16.0)

1.  **I/O como interfaz:** en 0.16.0 TODA I/O (archivos, tiempo, random, sleep, red) pasa por un parámetro `io: std.Io`. No existen las APIs globales `std.io.getStdOut()`, `std.time.sleep()`, `std.fs.cwd()`. `std.time` solo conserva constantes (`ns_per_ms`, ...) y `time.epoch`.
2.  **Punto de entrada "Juicy Main":** `pub fn main(init: std.process.Init) !void`; de ahí obtienes `init.io`, `init.gpa`, `init.arena`, `init.minimal.args`.
3.  **Allocators:** en 0.16 no existe `GeneralPurposeAllocator`; usa `std.heap.DebugAllocator` (Debug, con detección de leaks) o `init.gpa`. En 0.17, `DebugAllocator` es alias deprecated de `SafeAllocator`. Para release multihilo usa `std.heap.SmpAllocator`, y para temporales `std.heap.ArenaAllocator`.
4.  **Manejo de errores:** usa error unions (`!`) y `try`; `errdefer` para limpieza solo en error. `catch unreachable` solo en tests o imposibles demostrables.

### Rutas de archivos

NUNCA concatenes separadores a mano. `std.fs.path` sigue siendo la API correcta (y en 0.16.0 maneja rutas Windows absolutas/relativas sin confundirlas con POSIX):

```zig
const std = @import("std");

// ❌ MAL — falla en Windows y no valida componentes
// const path = "src/" ++ file ++ ".txt";

// ✅ BIEN — allocador explícito, separador nativo
const path = try std.fs.path.join(allocator, &.{ "src", file, "data.txt" });
defer allocator.free(path);
// Complementos: std.fs.path.dirname/basename/extension/resolve/relative
```
(El snippet requiere contexto: `allocator` y `file` vienen del caller; verificado compilado dentro de `main(init)` en 0.16.0.)

### Llamadas al sistema (qué usar en cada caso)

| Necesidad | API en 0.16.0 |
|---|---|
| Abstracción portable (I/O) | `std.Io` + `std.fs` (Dir/File con parámetro `io`) |
| POSIX genérico (open/read/mmap/fork...) | `std.posix` |
| Syscalls de Linux (epoll, io_uring, inotify) | `std.os.linux` |
| APIs nativas de Windows (NtDll, handles) | `std.os.windows` |
| WASI | `std.os.wasi` |

Nota: `std.os` NO está deprecado; es el hogar de `std.os.linux`, `std.os.windows`, `std.os.wasi`, etc. Lo que NO existe es un `std.os.darwin` (en su lugar, `std.posix` cubre macOS; los bits específicos viven en `std.c`/`std.posix.darwin`).

### Hilos, tiempo y entorno

*   **Hilos:** `std.Thread.spawn`, `std.Thread.Mutex`, `std.Thread.Condition`. `std.Thread.Pool` fue ELIMINADO en 0.16.0; para concurrencia estructurada usa `std.Io.Group` + `std.Io.async` (con `io.concurrent`).
*   **Tiempo:** nada de `std.time.nanoTimestamp()`. Usa relojes explícitos (`std.Io.Clock`: `.real` wall-clock Unix, `.awake`/`.boot` monotónicos, `.cpu_process`/`.cpu_thread`):
    ```zig
    // requiere io en scope (p.ej. init.io en main)
    const wall = std.Io.Timestamp.now(io, .real); // nanoseconds desde epoch Unix
    const mono = std.Io.Clock.Timestamp.now(io, .awake); // monotónico
    // dormir 50 ms (Cancelable!void, firma: io.sleep(io, duration, clock))
    try std.Io.sleep(io, .{ .nanoseconds = 50 * std.time.ns_per_ms }, .awake);
    ```
    Duraciones/timestamps son `Io.Duration`/`Io.Timestamp` (`raw.nanoseconds: i96`) con `durationTo/addDuration/subDuration` y comparación con `std.math.CompareOperator`.
*   **Variables de entorno:** en 0.16.0 el entorno NO es global: llega por `init.minimal.environ` (tipo `std.process.Environ`). `Environ.Map` es case-insensitive en Windows y case-sensitive en POSIX. Helpers: `environ.createMap(allocator)`, `Environ.getAlloc(environ, gpa, "KEY")`, `environ.containsConstant("KEY")`.

## 2. Detección de Plataforma en Tiempo de Compilación

Para manejar diferencias irreconciliables, usa `@import("builtin")`. Esto permite al compilador eliminar el código muerto (Dead Code Elimination).

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
Verificado compilado nativo y cross: x86_64-windows-gnu, aarch64-macos, wasm32-wasi (0.16.0).

Para lógica que depende del target completo, `builtin.target` (tipo `std.Target`) expone `cpu.arch`, `os.tag`, `abi` y `os.version_range`. Detecciones útiles: `builtin.abi.isAndroid()`, `builtin.cpu.arch.isX86()/.isARM()`, `builtin.link_libc`.

## 3. Patrón de Arquitectura Multiplataforma (El "Truco" del Módulo)

En lugar de llenar tu código de `if (is_windows)`, **inyecta módulos diferentes desde el `build.zig`**.

**Estructura de archivos:**

    src/
      main.zig
      platform/
        api.zig        # Interfaz común (decls + docs)
        windows.zig    # Implementación Windows
        posix.zig      # Implementación Linux/macOS/BSD

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
// platform.doSomething(io) — la misma firma en ambos backends.
```

Consejos: define el "contrato" en `api.zig` y que cada implementación lo replique; si un backend necesita un parámetro extra, mejor una función `available()` comptime que un `unreachable` silencioso. El `else` del switch cubre WASM/BSD/móvil: solo úsalo si posix.zig realmente compila en todos esos targets, o lista los casos POSIX explícitamente.

## 4. El Sistema de Build (`build.zig`) en Zig 0.16.0

Usa la API moderna de `std.Build` (todo via `root_module`). Configura target y optimización como opciones estándar para permitir cross-compilation desde la CLI.

```zig
const std = @import("std");

pub fn build(b: *std.Build) void {
    // 1. -Dtarget=x86_64-windows-gnu, -Doptimize=ReleaseFast, etc.
    const target = b.standardTargetOptions(.{});
    const optimize = b.standardOptimizeOption(.{});

    // 2. Ejecutable (0.16: root_module obligatorio)
    const exe = b.addExecutable(.{
        .name = "mi_app",
        .root_module = b.createModule(.{
            .root_source_file = b.path("src/main.zig"),
            .target = target,
            .optimize = optimize,
        }),
    });

    // 3. LibC (ver sección por-OS para matices)
    const os_tag = target.result.os.tag;
    if (os_tag == .windows or os_tag == .linux or os_tag == .macos) {
        // Windows: MinGW-w64 vendorizado. Linux: musl/glibc vendorizados.
        // macOS: libSystem.tbd vendorizado (terminal OK sin SDK).
        exe.root_module.link_libc = true;
    }
    // Android: NO pongas link_libc ni linkSystemLibrary("log") aquí:
    // Bionic no está vendorizado y el build falla sin el sysroot del NDK.
    // Ver sección Android.

    b.installArtifact(exe);
}
```

Comandos de cross-compilation (todos funcionan sin instalar toolchains):

    zig build -Dtarget=x86_64-windows-gnu          # Windows x64 (MinGW vendorizado)
    zig build -Dtarget=aarch64-windows-gnu         # Windows ARM64
    zig build -Dtarget=x86_64-linux-musl           # Linux estático (musl)
    zig build -Dtarget=aarch64-linux-gnu           # Linux ARM64 (glibc)
    zig build -Dtarget=aarch64-macos               # macOS ARM64
    zig build -Dtarget=x86_64-macos                # macOS Intel
    zig build -Dtarget=wasm32-wasi                 # WASI
    zig build -Dtarget=x86_64-linux-android        # Android (ver sección Android)

En 0.16.0, para librerías compartidas usa `b.addLibrary(.{ .linkage = .dynamic, ... })` — **`b.addSharedLibrary()` ya no existe**. Tampoco `b.addObject()` con ese nombre simple: revisa `std.Build` si migras desde 0.14.

## 5. Trucos y "Gotchas" por Sistema Operativo

### 🪟 Windows

*   **Consola y UTF-8:** El stdout de la consola de Windows usa por defecto una codepage legacy (no UTF-8). Con la std de 0.16 esto importa poco para `std.Io.File.stdout()` (escribe vía NtWriteFile, sin pasar por la codepage), pero para entrada de consola y para programas C externos conviene `SetConsoleOutputCP(65001)` (vía `@cImport`/translate-c del SDK de Windows). Guarda siempre el fuente en UTF-8.
*   **Salida estándar correcta en 0.16:**
    ```zig
    std.debug.print("hola\n", .{});
    // std.Io.File.stdout() también existe para escritura vía Io cuando se necesita.
    ```
*   **Extensiones de archivo:** `zig build` añade `.exe` automáticamente en Windows. Si manejas nombres a mano, `std.fs.path.extension`.
*   **Rutas largas:** límite clásico de 260 chars (MAX_PATH) salvo manifiesto `longPathAware` + registro, o prefijo `\\?\`. El std de Zig maneja rutas UTF-8→UTF-16 internamente; el límite del manifiesto lo controlas con `exe.win32_manifest` en el build.
*   **Subsistemas:** para apps GUI sin consola, `exe.subsystem = .windows` en build.zig; para consola explícita, `.console` (en 0.16.0 los valores de `std.zig.Subsystem` son minúsculas; `.Console`/`.Windows` son aliases deprecated).

### 🐧 Linux

*   **glibc vs musl:** Para máxima portabilidad binaria, `-Dtarget=x86_64-linux-musl` produce estáticos que corren en cualquier distro (sin `libc.so.6 not found`). glibc cross (`x86_64-linux-gnu`) también es vendorizada y válida cuando quieres linking dinámico (p.ej. plugins, OpenSSL del sistema). Elige por necesidades, no "siempre musl".
*   **Permisos:** el `chmod` POSIX ya no está en `std.posix` en 0.16.0; la API portable es la de `std.Io` (en Windows `Permissions` modela atributos; en POSIX es el modo):
    ```zig
    const f = try std.Io.Dir.createFile(std.Io.Dir.cwd(), io, "script.sh", .{});
    defer std.Io.File.close(f, io);
    try std.Io.File.setPermissions(f, io, @enumFromInt(0o755)); // .default_file=0o666, .executable_file=0o755
    ```
    (Alternativa sobre ruta existente: `dir.setFilePermissions(io, "script.sh", perm, .{})`.)

### 🍎 macOS

*   **SDK:** para apps de terminal puras (Zig sin frameworks de Apple) NO necesitas SDK: Zig vendoriza `libSystem.tbd` y enlaza bien desde Linux/Windows. Sí necesitas el SDK de Apple (o `arrowsql/apple-sdks` descargado) si enlazas frameworks GUI (Cocoa, Metal, CoreFoundation) — pásalo con `--sysroot`/`-isysroot` o usa un build con `xcrun` en una Mac.
*   **Firma (code signing):** el linker de Zig emite firma **ad-hoc** en los Mach-O que produce (incluidos los cross-compilados desde Linux), suficiente para ejecutar localmente en Apple Silicon. Para distribución (notarización, Gatekeeper) sí necesitas firmar con identidad real (`codesign` + `notarytool`) desde macOS.

### 🤖 Android

*   **Qué sale de la caja (verificado con 0.16.0):**
    *   `zig build -Dtarget=x86_64-linux-android` (o `aarch64-...`) **compila ELF sin `link_libc`** (std usa syscalls directas).
    *   `zig build-lib -target=aarch64-linux-android -dynamic` produce una `.so` válida (la vía correcta para apps).
    *   Enlazar libc **falla sin el NDK**: Bionic no está vendorizado (`error: unable to provide libc for target '...-android'`). Con el sysroot del NDK (`--sysroot` + `-target ...-android<API>` vía `zig cc`) sí se puede.
*   **El flujo real:** compila tu lógica pesada (motor, parser, IA) como **librería compartida** con `b.addLibrary(.{ .linkage = .dynamic, ... })` (**`b.addSharedLibrary()` ya no existe en 0.16**) y cárgala desde Kotlin/JNI (NDK) o empaquétala en un `.apk`. Un ejecutable suelto solo corre en `/data/local/tmp` (con `run-as`/adb, en apps debug) o con root; no es distribuíble.
*   **Logging:** no uses stdout en una app Android. Con el NDK enlaza `liblog` (`linkSystemLibrary("log", .{})` solo cuando compiles contra el sysroot del NDK) y llama `__android_log_print` vía translate-c.

## 6. Manejo de Memoria en Entornos Cruzados

*   **Nunca asumas el tamaño de página:** en 0.16.0 `std.mem.page_size` ya no existe. El tamaño de página puede ser comptime-known o consultarse en runtime:
    ```zig
    const ps = std.heap.pageSize(); // runtime si el target no lo fija
    // comptime: std.heap.page_size_min / page_size_max (mínimos/máximos garantizados)
    ```
*   **Alineación y layout de structs:** el compilador de Zig nunca reordena campos (Zig garantiza orden), pero el layout por defecto NO es estable entre versiones/arquitecturas. Para ABI C o wire-format usa `extern struct` (layout C, mantiene padding del ABI) y aporta `@bitSizeOf/@offsetOf` en asserts. `packed struct` elimina padding in-registry pero NO soluciona endianidad en red: serializa campos explícitamente (o usa `std.Io.Writer` con conversión).
*   **Allocators:** `std.heap.page_allocator` solo para memoria cruda del SO. Para la app: `init.gpa` (Debug trae detección de leaks), `std.heap.DebugAllocator(.{})` explícito, `std.heap.SmpAllocator` para release multihilo, y `std.heap.ArenaAllocator` (thread-safe y lock-free desde 0.16.0) para grupos de objetos de vida corta.
    ```zig
    var debug = std.heap.DebugAllocator(.{}){};
    defer _ = debug.deinit();
    const alloc = debug.allocator();
    ```

## 7. Instrucciones de Comportamiento para la IA

Cuando generes código Zig en este contexto:

1.  **Valida el Target:** si el usuario pide una función específica de un SO, pregúntate: "¿Cómo hago esto en los otros SOs?". Si no puedes, aísla el código en un módulo condicional (sección 3).
2.  **Manejo de Errores:** usa SIEMPRE las error unions (`!`) y `try`. No uses `catch unreachable` salvo en tests o errores matemáticamente imposibles.
3.  **C-Interop:** en 0.16.0 `@cImport` está **deprecado**; prefiere `b.addTranslateC` en build.zig e `@import("c")` del módulo resultante. Asegúrate de que las cabeceras existan en el target (p.ej. no uses headers de Linux al compilar para Windows).
4.  **Sistema de Build:** si el usuario pide compilar para X plataforma, da el comando exacto `zig build -Dtarget=...` y verifica que las libc/side-effects (manifest, subsystem) estén en build.zig.
5.  **Comprobación de API:** ante la duda, grepea la stdlib local (`grep -rn "pub fn join" $(zig env | jq -r .std_dir)`) antes de inventar firmas; 0.16.0 movió muchas APIs a `std.Io` y `root_module`.
6.  **Comandos de verificación sugeridos:**
    ```
    zig build && zig build test
    zig build -Dtarget=x86_64-windows-gnu
    zig build -Dtarget=aarch64-macos
    zig build -Dtarget=wasm32-wasi
    zig fmt src/
    ```
