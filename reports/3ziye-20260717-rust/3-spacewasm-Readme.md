<h1 align="center">SpaceWasm</h2>
<p align="center">
  <a href="https://github.com/nasa/spacewasm/actions/workflows/ci.yml"><img src="https://github.com/nasa/spacewasm/actions/workflows/ci.yml/badge.svg" /></a>
  <a href="https://codecov.io/gh/nasa/spacewasm"><img src="https://codecov.io/gh/nasa/spacewasm/branch/main/graph/badge.svg" /></a>
  <a href="#license"><img src="https://img.shields.io/badge/license-Apache%202.0-blue" alt="license" /></a>
</p>

SpaceWasm is an implementation of the [Wasm 1.0](https://webassembly.github.io/spec/versions/core/WebAssembly-1.0.pdf)
specification meant to interpret Wasm binary on-board spacecraft. It is developed at [NASA JPL](https://www.jpl.nasa.gov).

## Rationale

1. **Sequencing**: High-level spacecraft activities are typically encoded outside of the embedded flight-software in a command sequence.
These activities can include anything from driving the Mars rover and operating its arm, to checking temperature ranges are nominal.
Historically, the form and capability of sequences has varied from mission to mission, resulting in assorted/fragmented implementations.
SpaceWasm implements an industry standard, providing consolidation.

2. **Sandboxing**: The cost and time of flight-software development is high due to its constrained requirements and scope. Validating a new flight-software capability
often involves validating interactions with the entire system. This extends the V&V timeline and increases competition for testbed resources, which makes it hard to
get new autonomy software into flight. WebAssembly gives the opportunity for untrusted or low-trust executables to make their way on-board in a
way that flight-software can restrict access and compute time as well as monitor health and safety.

3. **Portability**: WebAssembly provides well-defined interfaces and sandboxing that make transferring to another platform trivial.

4. **Tooling**: Standardizing to WebAssembly opens doors into a wide community of rich tooling and research!

## Overview

This software comes with two major components:

1. Decoder/Validator:

   Reads the Wasm binary in [chunks](#streaming) and decodes it to an executable form. The decoder will use a fixed
   amount of memory and can be measured per-Wasm binary using the `spacewasm-check` executable on the ground.

   WebAssembly is validated during the decoding process and does not require another pass of the bytecode.

2. Interpreter:

   A Wasm interpreter that can operate on linear memory and interface with
   hooks from the [embedding](#embedding).

SpaceWasm does not execute direct WebAssembly bytecode. Wasm bytecode is meant to be small and structured in a way to
validate easily. These properties however make it slow to execute in-place. During the decoding process of Wasm
instructions, SpaceWasm converts bytecode into another intermediate representation (IR) which includes properties better
suited for interpretation. Read more about the IR in the [specification](src/SPEC.md).

## Requirements

The requirements of SpaceWasm are levied from similar work produced by [DLR](https://github.com/DLR-FT/wasm-interpreter).

See [requirements](./REQUIREMENTS.md).

## Embedding

Embedding the interpreter refers to instantiating it and providing implementations for the functions that are imported
into the module. Typically, the set of functions imported by the module are fixed and should be specified at compile
time both for the Wasm module and the embedder.

## Dynamic Allocation

SpaceWasm has a unique dynamic memory allocation model. All of its design choices stem from requirements levied by common
flight-software standards. Dynamic allocation follows the following rules:

1. All allocations occur over a discrete number of fixed size blocks called _pages_. These pages are distinct from Wasm's linear memory pages.
2. Deallocation cannot precede allocation.
3. Sub-regions inside pages cannot grow or shrink, sizes should be fixed ahead of time.
4. Memory usage must be deterministic.
5. Any allocation failures must _not_ result in panic.

The standard Rust [allocation](https://doc.rust-lang.org/alloc/) does not meet these constraints even with custom
allocators. To that end, SpaceWasm provides its own data structures that guarantee these properties. You will find these
data-structures contain the only usage of `unsafe` Rust semantics.

> [!NOTE]
> These limitations are only enforced on the implementation of the interpreter and _not_ on the Wasm bytecode it is made to interpret.

Wasm linear memory pages are allocated outside of dynamic memory pages.

## Streaming

_Peak_ memory usage is often an important constraint on small systems found on spacecraft. Many Wasm interpreters
require the Wasm binary to be given in one linear blob to the interpreter. This is typically fine for systems where the
same regions of memory may be reused for different purposes. Flight software on spacecraft generally assign fixed
portions of memory for certain purposes. Th