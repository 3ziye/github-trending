# JVM Custom Memory Arena

This project is a from-scratch, educational implementation of a manual memory arena in Java, built to understand how low-level memory, pointers, and data structures actually work beneath high-level language abstractions.

 

## Motivation

After ~4 years of programming in Java, a persistent and sizable chunk of its functionality as a language still feels opaque and abstract because of how it manages things under the hood:

- Objects appear without visible allocation
- Memory is automatically managed
- References feel disconnected from actual memory

This project aims to remove that abstraction.

Everything here is built on top of a single `byte[]`, and all structures, safety measures, and meaning are implemented manually.

The design emphasizes explicit control and fail-fast behavior so that incorrect assumptions about memory usage surface immediately.

 

## Project Overview

At its core, this project implements a **manual memory arena**:

- Memory is allocated explicitly
- All reads and writes are bounds-checked
- Data structures are constructed by defining layouts over raw bytes
- Pointers are represented as integer offsets
- Invalid memory access fails immediately

The project incrementally builds higher-level behavior on top of this foundation in a controlled and well-defined manner.

 

## Core Concepts Implemented

### 1. Memory Arena

A contiguous `byte[]` with a single allocation pointer (`offset`).

```
Memory Arena (128 bytes capacity)
┌─────────────────────────────────────────────────────────┐
│ 0x00 │ 0x01 │ 0x02 │ ... │ 0x0B │ 0x0C │ ... │ 0x7F     │
├──────┴──────┴──────┴─────┴──────┴──────┴─────┴──────────┤
│ ←─── Allocated (12 bytes) ───→ │ ←─── Free ────────────→│
│                                ↑                        │
│                            offset = 12                  │
└─────────────────────────────────────────────────────────┘

Rules: Allocate before use | Bounds-checked access | Reset clears all
```

 

### 2. Strict Allocation Model

All access validated against allocation boundary. Invalid access → immediate exception.

```
Valid Access:          Invalid Access:
┌─────────────┐        ┌─────────────┐
│ Allocated   │        │ Allocated   │
│   [data]    │        │   [data]    │
│             │        │             │
│ ←─✓─→       │        │ ←─✓─→  ✗──→ │
└─────────────┘        └─────────────┘
   offset=12              offset=12
                          (tries to read at 20)
```

 

### 3. Primitive Storage (Big Endian)

All primitives stored with explicit byte-level encoding.

```
Type Sizes:           Big-Endian Encoding Example (int 0x12345678):
┌─────────┬──────┐   ┌─────────────────────────────────────────┐
│ byte    │  1B  │   │ Value: 0x12345678                       │
│ boolean │  1B  │   │                                         │
│ short   │  2B  │   │ Memory Layout:                          │
│ char    │  2B  │   │ ┌──────┬──────┬──────┬──────┐           │
│ int     │  4B  │   │ │ 0x12 │ 0x34 │ 0x56 │ 0x78 │           │
│ long    │  8B  │   │ └──────┴──────┴──────┴──────┘           │
└─────────┴──────┘   │   MSB ────────────────→ LSB             │
                     │   (Most Significant Byte First)         │
                     └─────────────────────────────────────────┘


Example: storing an `int`:

Storage (big-endian approach):   
(x >>> 24) & 0xFF  →  byte[0]
(x >>> 16) & 0xFF  →  byte[1]
(x >>>  8) & 0xFF  →  byte[2]
(x >>>  0) & 0xFF  →  byte[3]

- An `int` occupies 4 bytes
- Values are stored in big-endian order: `[byte0][byte1][byte2][byte3]`
- Bit shifting: `(x >>> 24) & 0xFF` for most significant byte
- Reconstruction: `(byte0 << 24) | (byte1 << 16) | (byte2 << 8) | byte3`

This makes primitive representation and endianness explicit instead of implicit.
```
 

### 4. Struct-like Layouts (Nodes)

On top of raw memory, the project defines structured layouts through the `NodeStore` class.

A Node is defined as:

```
Node (8 bytes total):
+------------------+
| value (int)      |  offset + 0
+------------------+
| next (int)       |  offset + 4
+------------------+
```


 

### 5. Pointers and Sentinel Values

Pointers = integer offsets. `-1` = null sentinel.

```
Pointer States:
┌─────────────┬──────────────────────────────────────┐
│ Valid       │ Points to allocated memory           │
│   ptr = 8   │ ┌────┐                               │
│             │ │ 8  │→ [Node at address 8]          │
├─────────────┼──────────────────────────────────────┤
│ Null        │ Sentinel value                       │
│   ptr = -1  │ ┌────┐                               │
│             │ │ -1 │→ (end of list)                │
├─────────────┼──────────────────────────────────────┤
│ Invalid     │ Throws InvalidPointerException       │
│   ptr = 999 │ ┌────┐                               │
│             │ │999 │→ ✗ Out of bounds              │
└─────────────┴──────────────────────────────────────┘
```

 

### 6. Data Structures Built from Raw 