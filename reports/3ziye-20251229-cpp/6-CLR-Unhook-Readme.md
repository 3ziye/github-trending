# CLR Unhooking Tool
- Note: For this to have the effect of a clean CLR, you’d need to manually map the DLL from disk into memory. You cannot use LoadLibraryA/W, because antivirus solutions will detect the DLL load event and may hook it immediately. If you want this behavior, you can look up existing manual mappers on GitHub and integrate one into your codebase. I’m not including one here, as AV vendors generally don’t appreciate that

A native C++ utility that bypasses EDR/AV hooks in the .NET Common Language Runtime by restoring the original `nLoadImage` function implementation.

## Quick Description

This tool removes security product hooks from the CLR's `nLoadImage` function - the critical native entry point that handles all in-memory .NET assembly loading. By reading the clean `clr.dll` from disk and overwriting the hooked function bytes in memory, it restores the original CLR behavior, allowing `Assembly.Load(byte[])` to execute without EDR inspection or scanning.

## What Does This Do?

Modern security products (BitDefender, CrowdStrike, SentinelOne, etc.) hook the `nLoadImage` function inside `clr.dll` to intercept and scan in-memory .NET assembly loads. This tool unhooks that function by:

1. Reading the clean `clr.dll` from disk
2. Finding the original `nLoadImage` bytes
3. Overwriting the hooked version in memory

After unhooking, `Assembly.Load(byte[])` executes without EDR inspection.

### Understanding nLoadImage

`nLoadImage` is the critical native function that handles **all** in-memory assembly loading in the .NET runtime. It's declared as an `InternalCall` in managed code, meaning it has no C# implementation - instead, it's a direct bridge to native CLR code.

**The Call Chain:**
```
Managed Code (C#)
    ↓
Assembly.Load(byte[])
    ↓
RuntimeAssembly.nLoadImage(...) [InternalCall - no managed body]
    ↓
clr.dll!AssemblyNative::LoadImage (Native C++ implementation)
    ↓
Assembly loaded into AppDomain
```

**Why It's Critical:**

Nearly every in-memory assembly load goes through `nLoadImage`. The `Assembly.Load(byte[])` method and its overloads (including loading with symbol bytes) all invoke `nLoadImage` under the hood. When you call `Assembly.Load(byte[])`, the managed code in `mscorlib.dll` passes your byte array through `RuntimeAssembly.nLoadImage()`, which is marked with `[MethodImpl(MethodImplOptions.InternalCall)]` - meaning its body is empty in C# and execution immediately jumps to native CLR code.

Even dynamic code generation scenarios - serialization frameworks that emit assemblies at runtime, XML serializer generation, and red team tools like Cobalt Strike's `execute-assembly` - all funnel through this single function.

**Native Implementation:**

The `nLoadImage` InternalCall stub in `mscorlib.dll` points to the native C++ function `AssemblyNative::LoadImage` inside `clr.dll`. This function:
- Parses the PE headers from the byte array
- Validates metadata and IL code
- Allocates memory for the assembly
- Registers the assembly in the AppDomain
- Triggers post-load events (ETW, AMSI scanning in .NET 4.8+)
- Handles mixed-mode assemblies (native + managed)
- Enforces strong-name verification

In .NET Framework 4.8+, every `nLoadImage` call automatically passes the assembly bytes to Windows Defender's AMSI (`AmsiScanBuffer`) for scanning before execution, making it a critical chokepoint for security products.

**Function Signature (.NET Framework 4.7+):**
```csharp
[MethodImpl(MethodImplOptions.InternalCall)]
static internal extern Assembly nLoadImage(
    byte[] rawAssembly,              // PE bytes
    byte[] rawSymbolStore,           // Optional PDB bytes
    Evidence evidence,               // CAS evidence (obsolete)
    ref StackCrawlMark stackMark,    // Security stack marker
    bool fIntrospection,             // Reflection-only flag
    bool fSkipIntegrityCheck,        // Skip integrity validation
    SecurityContextSource securityContextSource  // Security context
);
```

When you call `Assembly.Load(byte[])`, it invokes `nLoadImage` with these typical parameters:
```csharp
StackCrawlMark stackMark = StackCrawlMark.LookForMyCaller;
return RuntimeAssembly.nLoadImage(
    rawAssembly,                            // Your byte array
    null,                                   // rawSymbolStore
    null,                                   // evidence
    ref stackMark,                          // LookForMyCaller
    false,                                  // fIntrospection
    SecurityContextSource.CurrentAssembly   // securityContextSource
);
```

The `fIntrospection` parameter controls whether the assembly is loaded for execution (`false`) or reflection-only inspection (`true`). The `Assembly.ReflectionOnlyLoad(byte[])` method calls `nLoadImage` with `fIntrospection=true`, allowing metadata examination without code execution.

**Why EDR Hooks It:**

Since `nLoadImage` is the **single entry point** for all in-memory assembly loads, EDR products hook it at the native level in