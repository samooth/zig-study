# Zig 0.16.0 — Standard Library Modules

**Source:** `<zig-install-dir>/lib/std/`

## Module Map

### Core

| Module | File | Purpose |
|--------|------|---------|
| `std` | `std.zig` | Root namespace, re-exports all sub-modules |
| `std.Io` | `Io.zig` | Central I/O abstraction (vtable-based) |
| `std.process` | `process.zig` | Process management, `Init` (Juicy Main) |
| `std.mem` | `mem.zig` | `Allocator` interface, byte utilities |
| `std.heap` | `heap.zig` | Allocator implementations |
| `std.meta` | `meta.zig` | Compile-time type reflection |
| `std.builtin` | `builtin.zig` | Compile-time build configuration |
| `std.posix` | `posix.zig` | Cross-platform POSIX abstraction |
| `std.os` | `os.zig` | OS-specific low-level APIs |

### Data Structures

| Module | File | Purpose |
|--------|------|---------|
| `std.array_list` | `array_list.zig` | `ArrayList` — growable array |
| `std.multi_array_list` | `multi_array_list.zig` | `MultiArrayList` — SoA layout |
| `std.hash_map` | `hash_map.zig` | Hash map implementation |
| `std.array_hash_map` | `array_hash_map.zig` | Ordered hash map |
| `std.DoublyLinkedList` | `DoublyLinkedList.zig` | Doubly linked list |
| `std.SinglyLinkedList` | `SinglyLinkedList.zig` | Singly linked list |
| `std.Deque` | `deque.zig` | Double-ended queue |
| `std.PriorityQueue` | `priority_queue.zig` | Priority queue |
| `std.PriorityDequeue` | `priority_dequeue.zig` | Priority deque |
| `std.Treap` | `treap.zig` | Treap data structure |
| `std.bit_set` | `bit_set.zig` | Static/dynamic bit sets |
| `std.BitStack` | `BitStack.zig` | Nested boolean state stack |
| `std.StaticStringMap` | `static_string_map.zig` | Comptime string maps |
| `std.Enums` | `enums.zig` | `EnumArray`, `EnumMap`, `EnumSet` |

### Serialization & Encoding

| Module | File | Purpose |
|--------|------|---------|
| `std.json` | `json.zig` | JSON parser/serializer |
| `std.zon` | `zon.zig` | ZON (Zig Object Notation) |
| `std.fmt` | `fmt.zig` | String formatting |
| `std.base64` | `base64.zig` | Base64 encoding/decoding |
| `std.leb128` | `leb128.zig` | LEB128 encoding |
| `std.compress` | `compress.zig` | flate/lzma/xz/zstd |
| `std.tar` | `tar.zig` | Tar archive handling |
| `std.zip` | `zip.zig` | ZIP archive handling |
| `std.Uri` | `Uri.zig` | URI parsing |
| `std.unicode` | `unicode.zig` | Unicode utilities |

### Networking & HTTP

| Module | File | Purpose |
|--------|------|---------|
| `std.http` | `http.zig` | HTTP client/server |
| `std.http.Client` | `http/Client.zig` | HTTP client with TLS |
| `std.http.Server` | `http/Server.zig` | HTTP server |
| `std.Io.net` | `Io/net.zig` | TCP/UDP/Unix sockets |

### Cryptography

| Module | File | Purpose |
|--------|------|---------|
| `std.crypto` | `crypto.zig` | All crypto primitives |
| `std.crypto.tls` | `crypto/tls.zig` | TLS implementation |
| `std.crypto.aes` | `crypto/aes.zig` | AES |
| `std.crypto.aes_gcm` | `crypto/aes_gcm.zig` | AES-GCM |
| `std.crypto.chacha20` | `crypto/chacha20.zig` | ChaCha20-Poly1305 |
| `std.crypto.sha2` | `crypto/sha2.zig` | SHA-2 family |
| `std.crypto.sha3` | `crypto/sha3.zig` | SHA-3 family |
| `std.crypto.blake2` | `crypto/blake2.zig` | BLAKE2 |
| `std.crypto.blake3` | `crypto/blake3.zig` | BLAKE3 |
| `std.crypto.argon2` | `crypto/argon2.zig` | Argon2 password hashing |
| `std.crypto.scrypt` | `crypto/scrypt.zig` | scrypt |
| `std.crypto.ml_dsa` | `crypto/ml_dsa.zig` | ML-DSA (post-quantum) |
| `std.crypto.ml_kem` | `crypto/ml_kem.zig` | ML-KEM (post-quantum) |
| `std.crypto.ascon` | `crypto/ascon.zig` | Ascon (NIST lightweight) |

### Math

| Module | File | Purpose |
|--------|------|---------|
| `std.math` | `math.zig` | Math utilities |
| `std.math.big` | `math/big.zig` | Arbitrary precision integers |
| `std.math.complex` | `math/complex.zig` | Complex numbers |
| `std.math.float` | `math/float.zig` | Float utilities |

### Hashing

| Module | File | Purpose |
|--------|------|---------|
| `std.hash` | `hash.zig` | Hash functions |
| `std.hash.wyhash` | `hash/wyhash.zig` | Wyhash |
| `std.hash.fnv` | `hash/fnv.zig` | FNV |
| `std.hash.crc` | `hash/crc.zig` | CRC |
| `std.hash.xxhash` | `hash/xxhash.zig` | xxHash |

### Heap Allocators

| Module | File | Purpose |
|--------|------|---------|
| `std.heap.ArenaAllocator` | `heap/arena_allocator.zig` | Bump allocator |
| `std.heap.DebugAllocator` | `heap/debug_allocator.zig` | Debug allocator (was GPA) |
| `std.heap.FixedBufferAllocator` | `heap/FixedBufferAllocator.zig` | Stack/buffer allocator |
| `std.heap.PageAllocator` | `heap/PageAllocator.zig` | OS page allocator |
| `std.heap.SmpAllocator` | `heap/SmpAllocator.zig` | SMP-optimized (new) |
| `std.heap.MemoryPool` | `heap/memory_pool.zig` | Single-type pool |

### Debugging & Diagnostics

| Module | File | Purpose |
|--------|------|---------|
| `std.debug` | `debug.zig` | Stack traces, debug info |
| `std.Progress` | `Progress.zig` | Progress bar/reporting |
| `std.log` | `log.zig` | Logging infrastructure |
| `std.testing` | `testing.zig` | Test utilities |

### I/O Subsystem

| Module | File | Purpose |
|--------|------|---------|
| `std.Io.Dir` | `Io/Dir.zig` | Directory operations |
| `std.Io.File` | `Io/File.zig` | File handle |
| `std.Io.Reader` | `Io/Reader.zig` | Generic reader |
| `std.Io.Writer` | `Io/Writer.zig` | Generic writer |
| `std.Io.Terminal` | `Io/Terminal.zig` | Terminal/ANSI handling |
| `std.Io.RwLock` | `Io/RwLock.zig` | Reader-writer lock |
| `std.Io.Semaphore` | `Io/Semaphore.zig` | Semaphore |
| `std.Io.Uring` | `Io/Uring.zig` | Linux io_uring backend |
| `std.Io.Kqueue` | `Io/Kqueue.zig` | BSD/macOS kqueue backend |
| `std.Io.Threaded` | `Io/Threaded.zig` | Thread-pool backend |

### Process

| Module | File | Purpose |
|--------|------|---------|
| `std.process.Init` | `process.zig` | Juicy Main entry point |
| `std.process.Child` | `process/Child.zig` | Child process handle |
| `std.process.Args` | `process/Args.zig` | CLI argument parsing |
| `std.process.Environ` | `process/Environ.zig` | Environment variables |
| `std.process.Preopens` | `process/Preopens.zig` | WASI preopened dirs |

### Build System

| Module | File | Purpose |
|--------|------|---------|
| `std.Build` | `Build.zig` | Build system API |
| `std.Build.Step` | `Build/Step.zig` | Build step base |
| `std.Build.Step.Compile` | `Build/Step/Compile.zig` | Compilation step |
| `std.Build.Step.Run` | `Build/Step/Run.zig` | Run step |
| `std.Build.Step.WriteFile` | `Build/Step/WriteFile.zig` | File generation |
| `std.Build.Module` | `Build/Module.zig` | Module definition |
| `std.Build.Cache` | `Build/Cache.zig` | Content-addressable cache |
| `std.Build.Watch` | `Build/Watch.zig` | File watching |
| `std.Build.Fuzz` | `Build/Fuzz.zig` | Fuzzing support |

### Platform-Specific

| Module | File | Purpose |
|--------|------|---------|
| `std.os.linux` | `os/linux.zig` | Linux syscalls |
| `std.os.windows` | `os/windows.zig` | Windows API |
| `std.os.wasi` | `os/wasi.zig` | WASI interface |
| `std.os.uefi` | `os/uefi.zig` | UEFI firmware API |

### Miscellaneous

| Module | File | Purpose |
|--------|------|---------|
| `std.Thread` | `Thread.zig` | OS thread abstraction |
| `std.Random` | `Random.zig` | Random number generation |
| `std.Target` | `Target.zig` | Target triple resolution |
| `std.atomic` | `atomic.zig` | Atomic operations |
| `std.sort` | `sort.zig` | Sorting algorithms |
| `std.simd` | `simd.zig` | SIMD utilities |
| `std.SemanticVersion` | `SemanticVersion.zig` | Semver parsing |
| `std.time` | `time.zig` | Time constants (ops moved to Io) |
| `std.time.epoch` | `time/epoch.zig` | Unix epoch calculations |
| `std.tz` | `tz.zig` | Timezone data |
| `std.dynamic_library` | `dynamic_library.zig` | dlopen/LoadLibrary |
| `std.coff` | `coff.zig` | COFF format |
| `std.elf` | `elf.zig` | ELF format |
| `std.macho` | `macho.zig` | Mach-O format |
| `std.pdb` | `pdb.zig` | PDB format |
| `std.dwarf` | `dwarf.zig` | DWARF debug info |
| `std.valgrind` | `valgrind.zig` | Valgrind integration |
| `std.wasm` | `wasm.zig` | WebAssembly support |
| `std.gpu` | `gpu.zig` | GPU interface |
