<p align="center">
  <img src="./images/mkpivm.png" width="30%" height="30%">
  <br>
  <a href="./research/mkpivm-research.pdf">Read</a> the research paper (written for 1.0.0).
</p>

**mkPIVM** is a polymorphic position-independent shellcode virtualizer for Windows x86 and x64 (Linux soon).

Feed it raw shellcode. It emits another raw blob: a small virtual machine that interprets a lifted, encrypted-at-rest version of your original instructions. The output is itself position-independent code and runs anywhere the original shellcode would, from a remote-thread loader to a code cave detour. Every per-seed knob varies independently: cipher family, register slot layout, opcode-to-handler permutation, dispatcher topology, junk-gadget pattern, IR obfuscation insertion points. Two builds from the same input share fewer than a hundred coincidental bytes out of tens of kilobytes.

Why: native shellcode is signature-trivial. Wrapping it in a per-instance VM with a per-instance cipher leaves nothing useful at rest, and lifting the instructions to bytecode puts another wall between disk bytes and any disassembler that knows what x86 looks like. As far as I can tell from a literature sweep, no public tool ships exactly this pipeline: raw PIC in, raw polymorphic VM PIC out. So, I mentioned that in the research paper it demanded. To be honest, if I am right about no one having done this (publicly) before, and I am pretty confident, I am surprised. _Nonetheless, enjoy._

## Related Work & Plans
* Linux support will be added soon.

## Quick start

```
mkpivm.exe shellcode.bin --arch x64 -o out.bin
```

Your PIVM is hot and ready. That's the simplest path. Several other modes vary how aggressively the original instructions get virtualized, whether the output is a standalone blob or a patched PE, and whether the lift runs at all.

# Showcase

I got the receipts. You can see a video of mkPIVM in action below, fully virtualizing a Meterpreter stager (vanilla btw), injecting into explorer.exe, and us capturing a callback. Of course this is just an example, and mkPIVM can be applied to much more, assuming the instructions in the shellcode are supported. If they aren't, make an Issue, send me the shellcode, I got you.

See it [here](https://github.com/D7EAD/mkPIVM/raw/refs/heads/main/media/mkpivm-showcase.mp4). Hosted in ./media, can't embed sadly.

Here is the VirusTotal report for that exact virtualized sample (as of 06/04/2026).

<img src="./images/vt.png">

...and the packed version, not even virtualized, notably higher entropy.

<img src="./images/packed.png">

There was careful attention paid to the entropy telemetry of the output of this tool, which results in shellcode of entropy less than typical Windows WinAPI DLLs (outside of packing mode), such as ntdll.dll or kernel32.dll. The entropy comparison is about...

| File | Bytes | Entropy |
|------|-------|---------|
| `p_m64.bin` | 3,969 | **7.1181** |
| `msvcrt.dll` | 699,888 | 6.5319 |
| `wininet.dll` | 2,724,528 | 6.4934 |
| `shell32.dll` | 7,839,992 | 6.3639 |
| `kernel32.dll` | 836,232 | 6.3597 |
| `crypt32.dll` | 1,538,632 | 6.3010 |
| `rpcrt4.dll` | 1,162,672 | 6.2405 |
| `ntdll.dll` | 2,522,104 | 6.1934 |
| `v.bin` | 29,229 | **6.0442** |

## Modes at a glance

| Mode | Flags | What changes |
|------|-------|--------------|
| Default | none | Lift the whole input. Everything virtualized. |
| Packer | `--pack` | Don't lift. Wrap input as encrypted data, decrypt at runtime, jump in. |
| Hybrid | `--ranges A:B,...` | Lift only the chosen byte ranges. Rest stays native. |
| Stacked | `--pack --ranges A:B` | Build the hybrid blob, then pack-wrap it. |
| Detour | `--embed-into PE --at RVA` | Take a pre-built blob, embed into a PE, patch a jmp at the chosen RVA. |
| Scan | `--scan` | Print eligible `--ranges` candidates from the input's CFG, then exit. |
| RX | `--rx` | PAGE_EXECUTE_READ blob. Data island stays encrypted at rest; in-blob PEB walker resolves VirtualProtect, decrypts in-place at state_init. |
| RX w/ Loader | `--rx --rx-loader-vp` | Like `--rx` but your loader passes VirtualProtect in as the blob's first arg. No PEB walker. |

Every mode honors `--seed`, `--arch`, `--input-format`, and `--format`. See the per-mode sections below for the build pipeline and the runtime flow.

## Default virtualization

The lifter walks the whole CFG and lowers every instruction to a custom IR. The IR goes through two obfuscation passes, then through codecs that encode each insn into the per-seed bytecode shape. The block table, handler table, and data island are encrypted with the same per-byte stream cipher as the bytecode. At runtime the prologue decrypts those three regions in place and the dispatcher loop fetches bytecode bytes one at a time, decrypting and dispatching to a handler that does the work.

### Build pipeline

Steps the build performs to turn raw shellcode into the emitted virtualized blob, end to end. _All graphs below apply to the 1.0.0 release, these have c