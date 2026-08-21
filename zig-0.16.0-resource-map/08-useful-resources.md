# Zig 0.16.0 — Useful Resources

## Official

| Resource | URL |
|----------|-----|
| Homepage | https://ziglang.org |
| Download | https://ziglang.org/download/ |
| 0.16.0 Release Notes | https://ziglang.org/download/0.16.0/release-notes.html |
| Language Reference | https://ziglang.org/documentation/0.16.0/ |
| Standard Library Docs | https://ziglang.org/documentation/0.16.0/std/ |
| Source Code | https://codeberg.org/ziglang/zig |
| Release Announcement | https://ziglang.org/news/0.16.0-released/ |
| Milestone #30 | https://github.com/ziglang/zig/milestone/30 |
| Zen of Zig | `zig zen` |

## Installation

### Package Managers

```bash
# macOS
brew install zig

# Arch Linux
pacman -S zig

# Windows (winget)
winget install --id zig.zig

# Nix
nix-shell -p zig
```

### Manual Install

```bash
# Download from https://ziglang.org/download/
tar xf zig-linux-x86_64-0.16.0.tar.xz
export PATH="$HOME/zig-linux-x86_64-0.16.0:$PATH"

# Verify
zig version  # should print 0.16.0
```

### Bootstrap for Any Target

```bash
git clone https://codeberg.org/ziglang/zig-bootstrap
# See: https://codeberg.org/ziglang/zig-bootstrap
```

## Documentation Tools

| Tool | URL | Description |
|------|-----|-------------|
| DevDocs | https://devdocs.io/zig/ | Searchable API docs with offline support |
| `zig std` | (built-in) | Opens stdlib docs in browser |
| ZLS | https://github.com/zigtools/zls/ | Zig Language Server (LSP) |

## Editor Support

| Editor | Plugin |
|--------|--------|
| VS Code | `ziglang.vscode-zig` |
| Neovim | `zig.zig` (nvim-lspconfig) |
| Vim/Neovim | `zigtools/zig.vim` |
| Emacs | `zig-mode` |
| Sublime | `Zig` package |

## Migration Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Migration Docs for AI | https://gist.github.com/shreeve/ee32c3e3d7173f2dbf5618faf5e8d60c | Comprehensive 0.15→0.16 migration guide |
| Zig 0.16 Migration Skill | https://github.com/MysticalDevil/zig-0-16-migration | AI skill for migration with verified examples |
| Zig 0.16 SKILL.md | https://github.com/zigcc/skills/blob/main/zig-0.16/SKILL.md | Structured migration guidance |
| translate-c Guide | https://codeberg.org/ziglang/zig/pulls/31451 | @cImport → build system migration |

## Learning Resources

| Resource | URL | Description |
|----------|-----|-------------|
| zig.guide | https://zig.guide | Tutorial-style learning |
| Zen of Zig (book) | https://zenofzig.com | Book for Zig 0.16.0 |
| Zig Exercises | https://codeberg.org/ankits/zig-exercises | Learn by fixing broken programs |
| Learning Zig | https://www.ziglearn.org | Course-style learning |
| Ziglings | https://github.com/ratfactor/ziglings | Fix tiny broken programs |

## Community

| Platform | URL |
|----------|-----|
| Ziggit (forum) | https://ziggit.dev |
| GitHub Discussions | https://github.com/ziglang/zig/discussions |
| IRC | `#zig` on Libera.Chat |
| Discord | https://discord.gg/zig |
| Mastodon | https://hachyderm.io/@ziglang |
| Devlog | https://ziglang.org/devlog/ |

## Third-Party Packages

| Package | URL | Description |
|---------|-----|-------------|
| known-folders | https://github.com/ziglibs/known-folders | Platform-specific folders |
| translate-c | https://codeberg.org/ziglang/translate-c | Official C translation package |
| zig-gamedev | https://github.com/zig-gamedev | Game development libraries |
| zig-network | https://github.com/kubkon/zig-network | Network library |
| zig-clap | https://github.com/Hejsil/zig-clap | Command-line argument parser |
| zig-yaml | https://github.com/kubkon/zig-yaml | YAML parser |
| zig-json | (std) | Built-in JSON support |
| zig-lz4 | https://github.com/kubkon/zig-lz4 | LZ4 compression |
| zig-libgit2 | https://github.com/kubkon/zig-libgit2 | Git bindings |

## Tools

| Tool | URL | Description |
|------|-----|-------------|
| zig-wrapper | https://github.com/kubkon/zig-wrapper | Wrapper for zig commands |
| zon2nix | https://github.com/Anorber/zon2nix | Convert build.zig.zon to Nix |
| zig-out | https://github.com/nicholasgasior/zig-out | Output formatter |

## Blogs & Articles

| Title | URL |
|-------|-----|
| Zig 0.16.0 Release Notes | https://ziglang.org/download/0.16.0/release-notes.html |
| Zig 0.16.0: Juicy Main | https://simonwillison.net/2026/Apr/15/juicy-main/ |
| Zig 0.16.0 Migration Guide | https://byteiota.com/zig-0-16-0-juicy-main-i-o-interfaces-what-breaks/ |
| Zig in 2026: Colorless Async I/O | https://blog.bokvi.com/blog/zig-in-2026/ |
| Zig 0.16.0 — I/O as Interface | https://www.youngju.dev/blog/2026-07-16-zig-016-io-interface.en |
| Zig translate-c Tool | https://www.luisllamas.es/en/zig-translate-c-tool |
| C Interop in Zig 0.16 | https://www.luisllamas.es/en/zig-c-interop/ |

## Key Issue Trackers

| Topic | URL |
|-------|-----|
| @cImport removal | https://github.com/ziglang/zig/issues/20630 |
| Subsystem detection | https://github.com/ziglang/zig/issues/25127 |
| DebugAllocator slowdown | https://github.com/ziglang/zig/issues/30709 |
| translate-c system libs | https://codeberg.org/ziglang/zig/pulls/31451 |
| Fuzzer fix | https://codeberg.org/ziglang/zig/pulls/31863 |

## Quick Commands

```bash
# View stdlib docs in browser
zig std

# Show language reference
zig gen-std

# Check version and paths
zig version
zig env

# List available targets
zig targets

# Show the Zen of Zig
zig zen

# Translate C to Zig
zig translate-c src/c.h > src/c.zig

# Build and run
zig build-exe src/main.zig
zig run src/main.zig

# Run tests
zig test src/main.zig
zig build test

# Format code
zig fmt src/

# Fuzz testing
zig build test --fuzz -Doptimize=ReleaseSafe

# Incremental watch mode
zig build --watch

# Fetch dependencies
zig fetch --save git+https://example.com/package
```
