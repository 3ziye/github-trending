# DPAPI RPC Internals and Custom Decryption

Calling the undocumented DPAPI RPC interface directly

## tl;dr

CryptUnprotectData is just a wrapper around an RPC call to lsass. we can skip the API and call NdrClientCall3 directly with the right parameters. disassembled dpapi.dll to figure out the exact calling convention.

## why did i reverse this

good question. it started with "i wonder how DPAPI actually works under the hood" and ended with me at 3am staring at RPC stubs in IDA wondering what i'm doing with my life.

also CryptUnprotectData is boring and i wanted to see if i could do it the cool way. turns out Microsoft's "security through obscurity" approach to internal APIs isn't that secure when you have IDA Pro and too much free time.

spoiler: it wasn't worth it, the high level API works fine, but now i know way too much about MIDL_STUBLESS_PROXY_INFO structures and i need to tell someone about it. so here we are.

## Background

DPAPI uses a local RPC server (protected_storage endpoint) running in lsass.exe for all crypto operations. the high level API (CryptProtectData/CryptUnprotectData) is basically just doing parameter marshalling and calling into this RPC interface.

interesting parts:
- RPC endpoint runs in lsass context so it has access to user's master keys
- communication happens over ncalrpc (local RPC, no network)
- actual decryption happens in two stages: RPC call returns encrypted memory, then SystemFunction041 decrypts it ( RtlEncryptMemory / RtlDecryptMemory )

## Reverse Engineering CryptUnprotectDataNoUI

started with dpapi.dll from Windows 10 22H2 (probably works on other versions too but offsets might differ)

### Initial RPC Setup

```asm
.text:00000001800012A0 CryptUnprotectDataNoUI proc near
.text:00000001800012B6                 and     [rsp+78h+Binding], 0
.text:00000001800012BB                 and     [rsp+78h+String], 0
.text:00000001800012C0                 mov     rsi, r9
.text:00000001800012C3                 test    r9, r9
.text:00000001800012C6                 jz      short error_invalid_param
.text:00000001800012C8                 test    rcx, rcx
.text:00000001800012CB                 jz      short error_invalid_param
.text:00000001800012CD                 cmp     qword ptr [rcx+8], 0
.text:00000001800012D2                 jz      short error_invalid_param
```

basic parameter validation, nothing special

### Binding String Composition

```asm
.text:0000000180001320                 lea     r9, [rsp+78h+String]
.text:0000000180001325                 xor     r8d, r8d
.text:0000000180001328                 lea     rdx, ProtectedStorage
.text:000000018000132F                 xor     ecx, ecx
.text:0000000180001331                 mov     qword ptr [rsp+78h+var_58], r9
.text:0000000180001336                 lea     r9, Ncalrpc
.text:000000018000133D                 call    cs:RpcStringBindingComposeW
.text:0000000180001343                 mov     ebx, eax
.text:0000000180001345                 test    eax, eax
.text:0000000180001347                 jnz     cleanup_and_exit
.text:000000018000134D                 mov     rcx, [rsp+78h+String]
.text:0000000180001352                 lea     rdx, [rsp+78h+Binding]
.text:0000000180001357                 call    cs:RpcBindingFromStringBindingW
```

the important strings here:

```asm
.rdata:0000000180003000 Ncalrpc         dq offset aNcalrpc        ; "ncalrpc"
.rdata:0000000180003008 ProtectedStorage dq offset aProtectedStor ; "protected_storage"
```

so it's composing a binding string for local RPC (ncalrpc) to the "protected_storage" endpoint. this endpoint is hosted by lsass.exe

### The Actual RPC Call

this is where it gets interesting

```asm
.text:00000001800013A0                 lea     rcx, pProxyInfo
.text:00000001800013A7                 mov     edx, 1
.text:00000001800013AC                 xor     r8d, r8d
.text:00000001800013AF                 mov     r9, [rsp+78h+Binding]
.text:00000001800013B4                 mov     [rsp+78h+var_58], r12
.text:00000001800013B9                 mov     [rsp+78h+var_50], rsi
.text:00000001800013BE                 mov     rax, [r15+8]
.text:00000001800013C2                 mov     [rsp+78h+var_48], rax
.text:00000001800013C7                 mov     ecx, [r15]
.text:00000001800013CA                 mov     [rsp+78h+var_40], rcx
.text:00000001800013CF                 lea     rax, [rsp+78h+hMem]
.text:00000001800013D4                 mov     [rsp+78h+var_38], rax
.text:00000001800013D9                 mov     rax, [r14+8]
.text:00000001800013DD                 mov     [rsp+78h+var_30], rax
.text:00000001800013E2                 mov     ecx, [r14]
.text:00000001800013E5                 mov     [rsp+78h+var_28], rcx
.text:00000001800013EA                 lea     rax, [rsp+78h+var_60]
.text:00000001800013EF                 mov     [rsp+78h+var_20], rax
.text:00000001800013F4                 mov     [rsp+78h+var_18], r13d
.text:00000001800013F9                 mov     [rsp+78h+var_10], r8
