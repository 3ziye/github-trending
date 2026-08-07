# Kakehashi

Userspace **macOS ARM64 → Linux aarch64** translation layer (CLI-first, no JIT).

Load Darwin Mach-O on Linux aarch64, map a freestanding `libSystem`, translate
BSD syscalls, and run real guests (clang probes, **7-Zip `7zz`**, **curl**,
**Apple `git`**, threads).

|                    |                                                   |
| ------------------ | ------------------------------------------------- |
| Live execution     | **Linux aarch64** (bare metal, VM, Colima/Docker) |
| Dry-load / inspect | Any host (including macOS)                        |
| Design reference   | [`docs/`](docs/README.md)                         |

## What works

Verified on **Docker/Colima** and **UTM** (Linux aarch64). Install once:

```bash
cargo install kakehashi
# or from a checkout:
cargo install --path crates/kh-cli --force

kh bottle ensure
kh install 7zip         # Darwin 7zz → guest /usr/local/bin/7zz
kh install curl         # Darwin curl → guest /usr/local/bin/curl
kh install xcode-tools  # Apple CLT git (public swscan; no Apple ID)
```

Relative `-o` / archive paths resolve against the **host CWD** of the `kh`
process (create parent dirs yourself, or rely on auto-mkdir for `O_CREAT`).
Through the bottle, `/Volumes/linux/…` bridges to the host root (`/` → host `/`).

### 7-Zip (`7zz`)

```bash
# Version / help
kh run 7zz --
kh run 7zz -- --help

# Create archive (cwd-relative)
kh run 7zz -- a demo.7z README.md
kh run 7zz -- t demo.7z
kh run 7zz -- l demo.7z
kh run 7zz -- x -o./out demo.7z

# Multi-thread compress (correctness gate)
kh run 7zz -- a -t7z -m0=lzma2 -mx=5 -mmt=4 mt.7z README.md
kh run 7zz -- t mt.7z
# expect: Everything is Ok, exit 0
```

**Docker helpers** (artifacts under host `.tmp/kh-out/`):

```bash
./scripts/docker-7zz.sh --help
./scripts/docker-7zz.sh a /Volumes/linux/out/demo.7z /Volumes/linux/src/README.md
ls -lh .tmp/kh-out/demo.7z

./scripts/docker-7zz.sh a -t7z -m0=lzma2 -mx=5 -mmt=4 \
  /Volumes/linux/out/mt.7z /Volumes/linux/src/README.md
./scripts/docker-7zz.sh t /Volumes/linux/out/mt.7z
```

### curl

```bash
# Banner (G1)
kh run curl -- --version

# HTTP GET → file (G3 / G5). Parents for -o are created when missing.
kh run curl -- -sS -o .tmp/kh-out/body http://example.com/
# expect: exit 0, ~559 bytes, HTML contains "Example Domain"
wc -c .tmp/kh-out/body
head -c 80 .tmp/kh-out/body; echo

# HTTP to stdout
kh run curl -- -sS http://example.com/ | head -c 80; echo

# HTTPS GET (G4) — OpenSSL + bottle CA (from host or curl.se download)
kh run curl -- -sS -o .tmp/kh-out/https-body https://example.com/
wc -c .tmp/kh-out/https-body

# Negative: bad / self-signed cert must fail (rc ≠ 0)
kh run curl -- -sS -o /dev/null https://self-signed.badssl.com/; echo exit:$?
```

**Docker helpers:**

```bash
./scripts/docker-curl.sh --version
./scripts/docker-curl.sh -sS -o /Volumes/linux/out/body http://example.com/
./scripts/docker-curl.sh -sS -o /Volumes/linux/out/https-body https://example.com/
ls -lh .tmp/kh-out/body .tmp/kh-out/https-body

# Trace-first probe logs → .tmp/kh-curl-probe/
./scripts/docker-curl-probe.sh --version

# Option matrix (large tiers) → .tmp/kh-curl-options/
./scripts/docker-curl-options.sh tier1
./scripts/docker-curl-options.sh tier9-10
./scripts/docker-curl-options.sh all          # tier1..10
```

Harmless noise on many runs:

- `kh: open fail ENOENT(openat) path=/etc/ssl/openssl.cnf` — OpenSSL optional config; HTTP/HTTPS still work via the seeded CA bundle.
- `WARN … skip dylib … Security/CoreFoundation` — Apple frameworks not in the bottle; soft stubs cover the load path.
- `unresolved strong symbol; bound to named missing trampoline` — symbols not hit on the happy path.

Details and gates: [`docs/curl.md`](docs/curl.md).

### Also green

| Surface                           | Notes                                                    |
| --------------------------------- | -------------------------------------------------------- |
| Clang / fixture probes            | `tests/clang-probe/`, `tests/fixtures/`                  |
| Multi-thread `7zz -mmt=4`         | Docker + UTM                                             |
| Bottle + freestanding `libSystem` | `kh bottle ensure` embeds dylib                          |
| Unit tests + clippy               | `cargo test` / `clippy` workspace (excl. `kh-libsystem`) |

### Apple `git` (CLT)

**Milestone met** (G0–G8). Day-to-day remotes work: local commits, HTTPS/SSH
clone and push, plain `http://`, private GitHub. Large clones verified below.

```bash
kh install xcode-tools   # public swscan; no Apple ID
# Default is protocol v2 (also set by scripts/docker-git.sh):
git config --global protocol.version 2

kh run git -- --version
kh run git -- ls-remote https://github.com/octocat/Hello-World.git
kh run git -- clone --depth 1 https://github.com/octocat/Hello-World.git hw
# full / large clones stream over TLS guest FDs (path B; no 64 MiB body cap)
# kh run git -- clone https://github.com/octocat/Hello-World.git hw-fu