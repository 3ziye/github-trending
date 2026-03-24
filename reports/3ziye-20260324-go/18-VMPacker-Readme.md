<p align="center">
  <h1 align="center">🛡️ VMPacker</h1>
  <p align="center">
    <strong>ARM64 ELF Virtual Machine Protection System</strong>
  </p>
  <p align="center">
    Translate ARM64 native instructions into custom VM bytecode for function-level code protection
  </p>
  <p align="center">
    <a href="README_CN.md">🇨🇳 中文文档</a> •
    <a href="#features">Features</a> •
    <a href="#architecture">Architecture</a> •
    <a href="#quick-start">Quick Start</a> •
    <a href="#usage">Usage</a> •
    <a href="#license">License</a>
  </p>
</p>

---

## Overview

VMPacker is a **Virtual Machine Protection (VMP)** system for **ARM64 (AArch64) Linux ELF** binaries. It decodes target function's native ARM64 instructions into an intermediate representation, translates them into custom VM bytecode, and injects an embedded VM interpreter into the ELF file. At runtime, protected functions are executed by the VM interpreter instead of natively.

### Core Concept

```
ARM64 Native Code  →  Decode  →  Translate  →  Custom VM Bytecode
                                                      ↓
                    Original ELF  ←  Inject  ←  VM Interpreter Stub
```

## Features

### 🔄 Instruction Translation Engine
- **63 VM instructions** — covering ALU, memory, branch, syscall, and more
- **Table-driven decoder** — pattern matching based on the ARM Architecture Reference Manual
- **121 ARM64 instructions** supported (base A64 100% coverage), including:
  - Arithmetic/Logic (ADD, SUB, MUL, AND, ORR, EOR, LSL, LSR, ASR, MVN, BIC, ORN, EON...)
  - Multiply-Extend (MADD, MSUB, SMADDL, SMSUBL, UMADDL, UMSUBL, SMULH, UMULH, UDIV, SDIV)
  - Data Movement (MOV, MOVZ, MOVK, MOVN)
  - Memory Access (LDR, STR, LDP, STP, LDPSW, LDADD, CAS, LDAR, STLR, LDAXR, STLXR — various widths and addressing modes)
  - Branch Control (B, BL, BR, BLR, RET, B.cond, CBZ/CBNZ, TBZ/TBNZ)
  - Conditional Select (CSEL, CSINC, CSINV, CSNEG, CCMP, CCMN)
  - Bitfield (UBFM, SBFM, BFM, EXTR)
  - Bit Manipulation (CLZ, CLS, RBIT, REV, REV16, REV32)
  - Carry Arithmetic (ADC, ADCS, SBC, SBCS)
  - SIMD Load/Store (LD1, ST1)
  - System/Barriers (SVC, MRS, MSR, ADRP/ADR, DMB, DSB, ISB, HLT, BRK, PRFM)

### 🔐 Multi-Layer Protection
| Layer | Technique | Description |
|-------|-----------|-------------|
| **VM Protection** | Custom ISA | Randomly mapped opcodes — reverse engineers cannot directly identify instruction semantics |
| **OpcodeCryptor** | Per-instruction opcode encryption | `enc[pc] = op[pc] ^ (key ^ (pc * 0x9E3779B9))` |
| **Bytecode Reversal** | Execution order reversal | Instructions stored in reverse order; interpreter traverses backwards |
| **Token Entry** | 3-instruction trampoline | Original function replaced with tokenized entry, hiding actual bytecode location |
| **Indirect Dispatch** | Function pointer jump table | Filled at runtime on the stack, breaking IDA cross-references |

### 🖥️ GUI
- Cross-platform desktop app built with **Wails v2** (Go + Vue 3)
- Element Plus UI components
- Symbol function selection + manual function input (protect by address range)
- One-click protection with real-time log output

<table>
  <tr>
    <td><img src="docs/1.png" width="450" alt="Main Interface"></td>
    <td><img src="docs/2.png" width="450" alt="Function Analysis"></td>
    <td><img src="docs/3.png" width="450" alt="Protection Options"></td>
  </tr>
  <tr>
    <td align="center"><sub>Function List</sub></td>
    <td align="center"><sub>Analysis & Selection</sub></td>
    <td align="center"><sub>Protection Options</sub></td>
  </tr>
  <tr>
    <td><img src="docs/4.png" width="450" alt="Protection Execution"></td>
    <td><img src="docs/5.png" width="450" alt="Protection Complete"></td>
    <td></td>
  </tr>
  <tr>
    <td align="center"><sub>Real-time Logs</sub></td>
    <td align="center"><sub>Protection Complete</sub></td>
    <td></td>
  </tr>
</table>

## Architecture

```
vmp/
├── cmd/vmpacker/          # CLI entry point
│   ├── main.go            # CLI argument parsing + orchestration
│   └── vm_interp.bin      # Compiled VM interpreter (GCC, go:embed)
│
├── pkg/                   # Go core library
│   ├── arch/arm64/        # ARM64 architecture support
│   │   ├── decoder.go     # Table-driven instruction decoder (implements vm.Decoder)
│   │   ├── decode_*.go    # Decode pattern tables (DP-IMM/DP-REG/Branch/LdSt)
│   │   ├── translator.go  # ARM64 → VM bytecode translator
│   │   ├── tr_alu.go      # ALU instruction translation
│   │   ├── tr_branch.go   # Branch instruction translation
│   │   ├── tr_loadstore.go # Memory instruction translation
│   │   ├── tr_bitfield.go # Bitfield instruction translation
│   │   └── tr_special.go  # Special instructions (ADRP/ADR)
│   ├── vm/                # VM ISA definitions
│   │   ├── types.go       # Shared types + interfaces (Decoder/Translator/Packer)
│   │   ├── opcodes.go     # 58+ VM opcode definitions (randomly mapped values)
│   │   └── disasm.go      # VM bytecode disassembler
│   └── binary