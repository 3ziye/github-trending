# MemNixFS

![Language: C++17](https://img.shields.io/badge/C%2B%2B-17-00599C.svg)
![Platform: Windows · Linux](https://img.shields.io/badge/platform-Windows%20%C2%B7%20Linux-lightgrey.svg)

**Mount a Linux memory dump as a filesystem and investigate it with the tools you already use.**

Point MemNixFS at an AVML / LiME / raw / kdump image and the live kernel state at the
moment of capture — processes, open files, sockets, loaded modules, the page cache,
threat-hunt findings, a forensic timeline — shows up as ordinary files and folders. Then
you `cd`, `ls`, `grep`, `cat`, open it in your editor, or feed it to any script. It's the
[MemProcFS](https://github.com/ufrisk/MemProcFS) idea — *memory as a filesystem* — brought
to **Linux** dumps, running natively on **Windows** and **Linux**.

<p align="center">
  <img src="docs/img/mounted-drive.png" width="660"
       alt="A Linux memory dump mounted as a Windows drive (M:) and browsed in File Explorer, showing the proc, sys, fs, forensic, search and mem folders">
</p>
<p align="center"><em>A Linux memory image, mounted as a Windows drive and browsed in Explorer — no exporting, no special viewer.</em></p>

```console
$ memnixfs --dump memory.lime mount M:
$ cat M:/sys/findevil/triage.txt        # one-shot "is this box owned?" verdict
$ cat M:/forensic/timeline.txt          # everything that happened, on one UTC axis
$ rg -i 'password|BEGIN PRIVATE KEY' M:/fs   # your tools, on memory
```

---

## Why a filesystem?

Memory forensics usually means learning a query tool and reading walls of tabular output.
MemNixFS takes a different bet: if the dump *is* a filesystem, then **every tool you already
know becomes a memory-forensics tool.** `grep` searches kernel structures. `find -newer`
filters the page cache by mtime. `diff` compares two captures. Your SIEM's file-ingest
pipeline indexes `/sys` and `/forensic` with zero new integration. Explorer, `less`, HxD,
ripgrep, Python's `os.walk` — they all just work, because the hard part (parsing the dump)
has already been turned into paths.

There's no new query language to learn. If you can navigate a directory tree, you can
navigate a crashed kernel.

## Works even with no symbols

The usual wall in Linux memory forensics is symbols: without the *exact* debug profile
(ISF) for the captured kernel, most tools stall. MemNixFS treats symbols as optional. It
will auto-discover or `--auto-fetch` an ISF if it can — but if it can't, it **generates
what it needs from the dump's own BTF type information**, which modern kernels embed. An
air-gapped analyst with an oddball kernel still gets a browsable `/fs`, recovered file
contents, and process analysis. No internet, no matching profile, still useful.

## What's in the mount

Everything the kernel had at capture time, laid out as folders you can browse,
`grep`, and `cat` however you like:

```
M:\
├── proc\<pid>\      per-process: maps, fds, threads, kstack, environ, strings, ELF core
├── sys\             system-wide: shell history, banner, dmesg, modules, net\, processes\, findevil\, etc
├── fs\              reconstructed root filesystem (recovers cached file contents)
├── forensic\        timeline.{txt,csv} + per-domain splits + JSON/CSV snapshot
├── search\          yara\, iocs, strings, entropy
├── mem\             phys.raw + windowed kernel-VA streams
└── plugins\         third-party file producers
```

See the [CLI reference](docs/cli-reference.md) and the [feature docs](docs/README.md) for
the full path map.

## Supported inputs

| Dump format | Notes |
|---|---|
| **AVML** | Microsoft Azure Memory Loader (framed Snappy) |
| **LiME** | Linux Memory Extractor |
| **raw** | flat physical dumps (`dd`, padded) |
| **kdump / vmcore** | ELF64 with VMCOREINFO |

Targets x86-64 Linux. Symbols are optional — supply an ISF, let it `--auto-fetch`, or rely
on BTF-only mode.

## Quick start

Grab a build (or [build from source](docs/building.md)), then:

```console
$ memnixfs --dump memory.lime list                 # list processes (no symbols needed)
$ memnixfs --dump memory.lime mount M:             # mount the whole tree (Windows: WinFsp)
$ memnixfs --dump memory.lime cat /sys/findevil/findevil.txt   # read one file, no mount
$ memnixfs --dump memory.lime export ./out         # or export everything to a folder
```

> **Windows — the `mount` command requires [WinFsp](https://winfsp.dev/rel/).** It is a
> kernel-mode filesystem driver, so it cannot be bundled in the download; install it once
> (default `.msi` options are fine) and `mount` works. Prefer not to install anything? Use
> `cat` to read a single file or `export` to copy files out to a folder — neither needs WinFsp.

A normal run is quiet — a few status lines (and how long the load took), then your
output. Add `-v` / `--verbose` to see the full diagnostic pipeline (symbol resolution,
page-table and DTB scans, warnings), or `-q` for critical errors only.

No symbol file is needed for a first look: MemNixFS scans the dump to iden