# BOF_RunPE

BOF RunPE is a Beacon Object File for Cobalt Strike that executes PE files entirely in-memory within the beacon process. Unlike traditional fork&run, **no child process is spawned, no console is created, and no pipe is used** - all output is captured via IAT hooking and redirected to the beacon console.

**Architecture:** x64 only

## Overview

```
┌──────────────────────────────────────────────────────────────┐
│                   Cobalt Strike Beacon                       │
│                    (Current Process)                         │
└────────────────────────┬─────────────────────────────────────┘
                         │
                         │  beacon_inline_execute()
                         │
                         ▼
┌──────────────────────────────────────────────────────────────┐
│                    BOF RunPE                                 │
│  ┌────────────────────────────────────────────────────────┐  │
│  │  VxTable + Draugr Initialization                       │  │
│  │  (Syscall Resolution + Stack Spoofing)                 │  │
│  └──────────────────────┬─────────────────────────────────┘  │
│                         │                                    │
│  ┌──────────────────────▼─────────────────────────────────┐  │
│  │  PE Mapping                                            │  │
│  │  - Section Copy    - IAT Patching (with hooks)         │  │
│  │  - Relocations     - Memory Protection                 │  │
│  └──────────────────────┬─────────────────────────────────┘  │
│                         │                                    │
│  ┌──────────────────────▼─────────────────────────────────┐  │
│  │  Thread Execution                                      │  │
│  │  - Spoofed Start Address                               │  │
│  │  - RIP Hijacking to Entry Point                        │  │
│  │  - Output Redirection via Hooks                        │  │
│  └────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
```

## Key Features

- **No Process Creation**: PE runs inside the beacon process
- **No Console/Pipe**: Output captured via `printf`/`WriteConsole` hooks
- **Multiple Allocation Methods**: Heap, VirtualAlloc, Module Stomping
- **Proxy Loading**: Timer Queue, RegisterWait, or direct calls
- **Ntdll Unhooking**: Optional fresh copy from disk
- **RWX** : Optional allocate memory in RWX
- **Thread Start Spoofing**: Legitimate start address with RIP hijacking

## Configuration Options

The behaviorus of BOF can be edited in `Additionals postex` -> `RunPe Config`

![Custom BOF](/img/custom_bof.png)

### Proxy Methods

| Method |  Description |
|--------|--------------|
| `None`      | Direct API calls |
| `Draugr`    | Stack spoofed API calls |
| `Regwait`   | RegisterWaitForSingleObject callback |
| `Timer`     | Timer Queue callback |

### Allocation Methods

| Method | Description  | 
|--------|--------------|
| `Heap`                | Private heap via RtlCreateHeap with Draugr | 
| `VirtualAlloc`        | NtAllocateVirtualMemory with Draugr | 
| `Module stomping`     | Overwrites legitimate DLL .text section | 

### General Options

| Option |  Description |
|--------|-------------------|
| `AllocRWX`    |  Allocate as RWX (vs RW→RX transition) |
| `UnhookNtdll` |  Replace ntdll.dll .text with fresh copy from disk |
| `Timeout`     |  Execution timeout in milliseconds (0 = infinite) |
| `StompModule` |  DLL path for module stomping (e.g., `chakra.dll`) |

### Thread Spoofing

| Option | Description |
|--------|-------------|
| `ModuleName`      | Legitimate module for start address (e.g., `Kernel32.dll`) |
| `ProcedureName`   | Function name within module (e.g., `BaseThreadInitThunk`) |
| `Offset`          | Offset from function start |

## Output Capture

All PE output is redirected to the beacon console via IAT hooks. **No console window or named pipe is created.**

| Hooked Function | Target |
|-----------------|--------|
| `GetCommandLineA/W`                   | Returns spoofed arguments |
| `__getmainargs` / `__wgetmainargs`    | CRT argument initialization |
| `printf` / `wprintf`                  | BeaconPrintf redirection |
| `WriteConsoleA/W`                     | BeaconPrintf redirection |
| `__stdio_common_vfprintf`             | UCRT print functions |
| `ExitProcess` / `exit`                | Converted to ExitThread |

## Evasion Techniques

| Technique | Bypasses |
|-----------|----------|
| Indirect Syscalls         | Userland API hooks (EDR/AV) |
| Draugr Stack Spoofing     | Call stack inspection |
| Thread Start Spoofing     | Thread start address analysis |
| Module Stomping           | Unbacked memory detection |
| Private Heap Allocation   | VirtualAlloc monitoring |
| Ntdll Unhooking           | Overwrite in memory ntdll with Ntdll on a disk |
| IAT Hooking (n