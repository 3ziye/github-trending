# BOF Spawn - Process Injection 

## Update

### 11/23/25

- Update `Makefile` and add `.gitkeep` in `Bin/` and `Bin/temp`, thanks @0xTriboulet for issues
- Update `BOF_spawn.cna` to fix initialization, thanks @D1sAbl4 for issues

## Overview

**BOF Spawn** is a Beacon Object File for Cobalt Strike that implements process spawning and shellcode injection Draugr stack spoofing with indirect syscalls. This tool combines multiple evasion techniques to bypass userland hooks, call stack analysis, and memory scanners.

**Architecture**: x64 only

### Core Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                    Cobalt Strike Beacon                      │
│                    (Parent Process)                          │
└────────────────────────┬─────────────────────────────────────┘
                         │
                         │ beacon_inline_execute()
                         │
                         ▼
          ┌──────────────────────────────┐
          │      BOF Spawn (Bof.c)       │
          │  ┌────────────────────────┐  │
          │  │  VxTable Initialization │ │
          │  │  (Syscall Resolution)   │ │
          │  └──────────┬─────────────┘  │
          │             │                │
          │  ┌──────────▼─────────────┐  │
          │  │  Draugr Framework      │  │
          │  │  - Stack Spoofing      │  │
          │  │  - Indirect Syscalls   │  │
          │  └──────────┬─────────────┘  │
          │             │                │
          │  ┌──────────▼─────────────┐  │
          │  │  SpawnAndRun()         │  │
          │  │  - Process Creation    │  │
          │  │  - Memory Allocation   │  │
          │  │  - Shellcode Injection │  │
          │  │  - Execution           │  │
          │  └────────────────────────┘  │
          └──────────────┬───────────────┘
                         │
                         ▼
          ┌──────────────────────────────┐
          │     Target Process           │
          │  (Suspended → Executing)     │
          │                              │
          │  ┌────────────────────────┐  │
          │  │  Injected Shellcode    │  │
          │  └────────────────────────┘  │
          └──────────────────────────────┘
```

## Configuration Options

The BOF provides extensive customization through the CNA script configuration dialog:

| Option | Description | Format/Notes |
|--------|-------------|--------------|
| **Process Name** | Executable path to spawn | NT path format: `\??\C:\Windows\System32\rundll32.exe` |
| **Working Directory** | Current directory for spawned process | Standard path: `C:\Windows\System32` |
| **PPID Spoof Process** | Parent process name for PPID spoofing | Process name only (e.g., `explorer.exe`) |
| **Command Line** | Arguments for spawned process | Full command line string |
| **Block DLL Policy** | Restrict to Microsoft-signed DLLs only | Boolean |
| **Disable CFG** | Disable Control Flow Guard | Boolean - Required for callback execution method |
| **Use RWX** | Allocate memory as RWX vs RW→RX | Boolean - RW→RX recommended for stealth |
| **Execution Method** | Shellcode execution technique | See section below |

**Note on Process Path Format**: The BOF uses NT path format (`\??\C:\...`) for the process name. This is the native format used by `NtCreateUserProcess` and bypasses some Win32 path parsing mechanisms.

## Shellcode Execution Methods

### 1. Direct RIP Hijacking
```
Original State:          Modified State:
┌──────────────┐        ┌──────────────┐
│ RIP: ntdll   │   →    │ RIP: 0x7FFE  │ (shellcode)
│ RAX: ...     │        │ RAX: ...     │
└──────────────┘        └──────────────┘
```
**Advantage**: Simple and reliable.  
**Detection Risk**: High - RIP directly pointing to non-module memory is easily detected by EDR thread scanning.

### 2. JMP RAX Gadget
```
Step 1: Find Gadget               Step 2: Set Context
┌──────────────────┐             ┌──────────────────┐
│ Scan ntdll.dll   │             │ RIP: ntdll!gadget│ (0xFF 0xE0)
│ for 0xFF 0xE0    │    →        │ RAX: shellcode   │
└──────────────────┘             └──────────────────┘
```
**Advantage**: RIP points to legitimate ntdll.dll, more stealthy than direct hijacking.  
**Detection Risk**: Medium - Suspicious RAX value and unusual gadget execution may trigger heuristics.

### 3. JMP RBX Gadget
```
Step 1: Find Gadget               Step 2: Set Context
┌──────────────────┐             ┌──────────────────┐
│ Scan ntdll.dll   │             │ RIP: ntdll!gadget│ (0xFF 0xE3)
│ for 0xFF 0xE3    │    →        │ RBX: shellcode   │
└──────────────────┘             └──────────────────┘
```
**Advantage**: Similar to JMP RAX, RIP remains in legitimate module space.  
**Detection Risk**: Medium - Same as JMP RAX, slightly different register makes detection signatures less common.

### 4. Callback Function Hijacking
```
EnumResourceTypesW(hModule, lpEnumFunc, lParam)
                              ↓
                   