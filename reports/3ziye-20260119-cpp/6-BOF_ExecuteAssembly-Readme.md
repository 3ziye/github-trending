# BOF Execute-Assembly

Beacon Object File for Cobalt Strike that executes .NET assemblies in beacon with evasion techniques. 

## Overview

## Core Architecture
```
┌──────────────────────────────────────────────────────────────────────────────┐
│                         Cobalt Strike Beacon                                 │
│                         (Parent Process)                                     │
└──────────────────────────────────┬───────────────────────────────────────────┘
                                   │
                                   │ beacon_inline_execute()
                                   │ - Parse packed arguments
                                   │ - Call go()
                                   ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│                      BOF Execute-Assembly Entry (go)                         │
│  ┌────────────────────────────────────────────────────────────────────────┐  │
│  │ Configuration Parsing                                                  │  │
│  │  • ProxyMethod (None/Draugr/Timer/RegWait)                             │  │
│  │  • AmsiEvasion (None/Patch/HWBP)                                       │  │
│  │  • EtwEvasion (None/Patch)                                             │  │
│  │  • PipeName, AppDomainName, Assembly bytes, Arguments                  │  │
│  └────────────────────────────────┬───────────────────────────────────────┘  │
│                                   │                                          │
│  ┌────────────────────────────────▼───────────────────────────────────────┐  │
│  │ Framework Initialization                                               │  │
│  │  • InitVxTable() - Resolve syscall numbers                             │  │
│  │    └─> NtProtectVirtualMemory, NtContinue, NtCreateEvent,              │  │
│  │        NtSetEvent, NtWaitForSingleObject, NtClose                      │  │
│  │  • DraugrInit() - Setup synthetic stack frames                         │  │
│  │    └─> Locate RtlUserThreadStart, BaseThreadInitThunk                  │  │
│  └────────────────────────────────┬───────────────────────────────────────┘  │
│                                   │                                          │
│  ┌────────────────────────────────▼───────────────────────────────────────┐  │
│  │ DLL Loading (ProxyLoadLibraryA)                                        │  │
│  │  • amsi.dll, OleAut32.dll, mscoree.dll, User32.dll                     │  │
│  │                                                                        │  │
│  │  PROXY_NONE:     LoadLibraryA() directly                               │  │
│  │  PROXY_DRAUGR:   DRAUGR_API(LoadLibraryA) - spoofed stack              │  │
│  │  PROXY_TIMER:    CreateTimerQueue → Timer callback                     │  │
│  │  PROXY_REGWAIT:  RegisterWaitForSingleObject → Event callback          │  │
│  └────────────────────────────────┬───────────────────────────────────────┘  │
│                                   │                                          │
│  ┌────────────────────────────────▼───────────────────────────────────────┐  │
│  │ AMSI Evasion Setup                                                     │  │
│  │                                                                        │  │
│  │  AMSI_PATCH:                         AMSI_HWBP:                        │  │
│  │  ┌─────────────────────────┐         ┌──────────────────────────────┐  │  │
│  │  │ 1. Backup 4 bytes       │         │ 1. Add VEH Handler           │  │  │
│  │  │ 2. NtProtectVirtualMem  │         │ 2. RtlCaptureContext         │  │  │
│  │  │    (RW)                 │         │ 3. Set DR0 = AmsiScanBuffer  │  │  │
│  │  │ 3. Write:               │         │ 4. Enable DR7 breakpoint     │  │  │
│  │  │    48 31 C0  xor rax,rax│         │ 5. NtContinue (apply ctx)    │  │  │
│  │  │    C3        ret        │         │                              │  │  │
│  │  │ 4. NtProtectVirtualMem  │         │ On AmsiScanBuffer call:      │  │  │
│  │  │    (restore)            │         │   → #BP Exception            │  │  │
│  │  └─────────────────────────┘         │   → VEH redirects to RET     │  │  │
│  │                                      │   → RAX = 0                  │  │  │
│  │                                      └──────────────────────────────┘  │  │
│  └────────────────────────────────┬───────────────────────────────────────┘  │
│                                   │                                          │
│  ┌────────────────────────────────▼───────────────────────────────────────┐  │
│  │ ETW Evasion (if enabled)                                               │  │
│  │  • NtProtectVirtualMemory(NtTraceEvent, RW)                            │  │
│  │  • Backup 4 bytes                                                      │  │
│  │  • Write: 48 31 C0 C3 (xor rax,rax; ret)                               │  │
│  │  • NtProtectVirtualMemory(restore protection)  