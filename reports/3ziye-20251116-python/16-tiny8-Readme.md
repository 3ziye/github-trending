# Tiny8

[![PyPI version](https://img.shields.io/pypi/v/tiny8)](https://pypi.org/project/tiny8/)
[![License](https://img.shields.io/github/license/sql-hkr/tiny8)](LICENSE)
[![Python versions](https://img.shields.io/pypi/pyversions/tiny8)](https://pypi.org/project/tiny8/)
[![CI](https://github.com/sql-hkr/tiny8/actions/workflows/ci.yml/badge.svg)](https://github.com/sql-hkr/tiny8/actions/workflows/ci.yml)
[![codecov](https://codecov.io/github/sql-hkr/tiny8/graph/badge.svg?token=OBM58R8MCL)](https://codecov.io/github/sql-hkr/tiny8)

> **An educational 8-bit CPU simulator with interactive visualization**

Tiny8 is a lightweight and educational toolkit for exploring the fundamentals of computer architecture through hands-on assembly programming and real-time visualization. Designed for learning and experimentation, it features an AVR-inspired 8-bit CPU with 32 registers, a rich instruction set, and powerful debugging tools — all with zero heavy dependencies.


<div align="center">
  <img src="https://github.com/user-attachments/assets/ffbcb2c4-2c3a-469f-b7b7-e6e86eb374da" alt="Animated bubble sort visualization" width="600">
  <p><em>Real-time visualization of a bubble sort algorithm executing on Tiny8</em></p>
</div>

## ✨ Features

### 🎯 **Interactive Terminal Debugger**
<img width="600" src="https://github.com/user-attachments/assets/0bbd4382-806e-4b5a-af0b-54d83417fcfb" alt="CLI visualizer screenshot">

- **Vim-style navigation**: Step through execution with intuitive keyboard controls
- **Change highlighting**: See exactly what changed at each step (registers, flags, memory)
- **Advanced search**: Find instructions, track register/memory changes, locate PC addresses
- **Marks and bookmarks**: Set and jump to important execution points
- **Vertical scrolling**: Handle programs with large memory footprints

### 🎬 **Graphical Animation**
- Generate high-quality GIF/MP4 videos of program execution
- Visualize register evolution, memory access patterns, and flag changes
- Perfect for presentations, documentation, and learning materials

### 🏗️ **Complete 8-bit Architecture**
- **32 general-purpose registers** (R0-R31)
- **8-bit ALU** with arithmetic, logical, and bit manipulation operations
- **Status register (SREG)** with 8 condition flags
- **2KB address space** for unified memory and I/O
- **Stack operations** with dedicated stack pointer
- **AVR-inspired instruction set** with 60+ instructions

### 📚 **Educational Focus**
- Clean, readable Python implementation
- Comprehensive examples (Fibonacci, bubble sort, factorial, and more)
- Step-by-step execution traces for debugging
- Full API documentation and instruction set reference

## 🚀 Quick Start

### Installation

```bash
pip install tiny8
```

### Your First Program

Create `fibonacci.asm`:
```asm
; Fibonacci Sequence Calculator
; Calculates the 10th Fibonacci number (F(10) = 55)
; F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)
;
; Results stored in registers:
; R16 and R17 hold the two most recent Fibonacci numbers

    ldi r16, 0          ; F(0) = 0
    ldi r17, 1          ; F(1) = 1
    ldi r18, 9          ; Counter: 9 more iterations to reach F(10)

loop:
    add r16, r17        ; F(n) = F(n-1) + F(n-2)
    mov r19, r16        ; Save result temporarily
    mov r16, r17        ; Shift: previous = current
    mov r17, r19        ; Shift: current = new result
    dec r18             ; Decrement counter
    brne loop           ; Continue if counter != 0

done:
    jmp done            ; Infinite loop at end
```

Run it:
```bash
tiny8 fibonacci.asm # Interactive debugger
tiny8 fibonacci.asm -m ani -o fibonacci.gif # Generate animation
```

### Python API

```python
from tiny8 import CPU, assemble_file

asm = assemble_file("fibonacci.asm")
cpu = CPU()
cpu.load_program(asm)
cpu.run(max_steps=1000)

print(f"Result: R17 = {cpu.read_reg(17)}")  # Final Fibonacci number
```

## 💡 Why Tiny8?

**For Students** — Write assembly, see immediate results with visual feedback. Understand how each instruction affects CPU state without abstractions.

**For Educators** — Interactive demonstrations, easy assignment creation, and generate animations for lectures.

**For Hobbyists** — Rapid algorithm prototyping at the hardware level with minimal overhead and an extensible, readable codebase.

## 📖 Documentation

- [**Full Documentation**](https://sql-hkr.github.io/tiny8/) — Complete API reference and guides
- [**Instruction Set Reference**](#instruction-set-reference) — All 60+ instructions
- [**CLI Guide**](#interactive-cli-controls) — Terminal debugger keyboard shortcuts
- [**Examples**](#examples) — Sample programs with explanations
- [**Contributing**](CONTRIBUTING.md) — Guidelines for contributors

## 🎮 Interactive CLI Controls

The terminal-based debugger provides powerful navigation and inspection capabilities.

### Navigation & Playback

- `l` / `h` or `→` / `←` — Step forward/backward
- `w` / `b` — Jump ±10 steps
- `0` / `$` — Jump to first/last step
- `Space` — Play/p