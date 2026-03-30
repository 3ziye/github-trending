# CoBRA

**Co**efficient-**B**ased **R**econstruction of **A**rithmetic — a Mixed Boolean-Arithmetic expression simplifier.

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![C++23](https://img.shields.io/badge/C%2B%2B-23-blue.svg)](https://en.cppreference.com/w/cpp/23)
[![Tests](https://img.shields.io/badge/tests-1193-brightgreen.svg)](#testing)

CoBRA deobfuscates expressions that interleave arithmetic (`+`, `-`, `*`) with bitwise (`&`, `|`, `^`, `~`) and shift (`<<`, `>>`) operators — a technique commonly used in software obfuscation.

```
$ cobra-cli --mba "(x&y)+(x|y)"
x + y

$ cobra-cli --mba "((a^b)|(a^c)) + 65469 * ~((a&(b&c))) + 65470 * (a&(b&c))" --bitwidth 16
67 + (a | b | c)

$ cobra-cli --mba "((a^b)&c) | ((a&b)^c)"
c ^ a & b

$ cobra-cli --mba "(x&0xFF)+(x&0xFF00)" --bitwidth 16
x

$ cobra-cli --mba "(x ^ 0x10) + 2 * (x & 0x10)"
16 + x

$ cobra-cli --mba "x << 3"
8 * x
```

<details>
<summary>More examples</summary>

```
$ cobra-cli --mba "~x"
~x

$ cobra-cli --mba "(x^y)*(x&y) + 3*(x|y)"
(x ^ y) * (x & y) + 3 * (x | y)

$ cobra-cli --mba '-357*(x&~y)*(x&y)+102*(x&~y)*(x&~y)+374*(x&~y)*~(x^y)
  -306*(x&~y)*~(x|y)-17*(x&~y)*~(x|~y)-105*~(x|~y)*(x&y)+30*~(x|~y)*(x&~y)
  +110*~(x|~y)*~(x^y)-90*~(x|~y)*~(x|y)-5*~(x|~y)*~(x|~y)+34*(x&~y)*~x
  -85*(x&~y)*~y+10*~(x|~y)*~x-25*~(x|~y)*~y'
22 * (x & y) + -17 * x + -5 * y
```

</details>

## How It Works

CoBRA uses a worklist-based orchestrator to simplify expressions. Each input enters the worklist as a work item tagged with a state kind. A scheduler selects the next pass to run based on the item's state, prerequisite dependencies, and an attempt cache that prevents redundant work.

36 discrete passes are organized into families: AST processing, signature-based techniques, semilinear techniques, decomposition, and lifting. Some passes fork local alternatives or child solves that are resolved by competition groups; outside those groups, the worklist returns the first fully verified top-level candidate. All results are verified by spot-checking random inputs (default) or Z3 equivalence proof (`--verify`).

```
Input Expression
       |
  [Worklist Scheduler]
       |
  Work items flow through state kinds:
       |
  kFoldedAst ──> AST processing passes
       |         (classify, lower, rewrite)
       |
       +──> kSignatureState ──> Signature techniques
       |    (pattern match, CoB, ANF, polynomial recovery)
       |
       +──> kSemilinearNormalizedIr ──> Semilinear techniques
       |    (normalize, recover structure, refine, reconstruct)
       |
       +──> kCoreCandidate / kRemainderState ──> Decomposition
       |    (extract core, classify residual, solve)
       |
       +──> kLiftedSkeleton ──> Lifting
       |    (virtual variable substitution, outer solve)
       |
       +──> kCandidateExpr ──> Verification
            (spot-check or Z3 proof)
       |
  Simplified Expression
```

**Signature-based techniques** evaluate the expression on all Boolean inputs to get a signature vector. A CoB butterfly transform recovers AND-product basis coefficients. Pattern matching, ANF, and polynomial recovery handle different complexity levels.

**Semilinear techniques** handle expressions with constant masks (e.g., `x & 0xFF`). The expression is decomposed into weighted bitwise atoms, then structure recovery and term refinement simplify the intermediate representation, and bit-partitioned OR-assembly reconstructs the final result.

**Decomposition** targets mixed expressions with products of bitwise subexpressions. A polynomial core is extracted, then residuals are classified and solved (polynomial, boolean-null/ghost, or template fallback).

**Lifting** replaces complex subexpressions with virtual variables, solves the simplified outer skeleton, then substitutes back.

## Features

- **Linear MBA simplification** — weighted sums of bitwise atoms via signature vector and CoB transform
- **Scaled pattern matching** — `k * f(vars) + c` with Shannon decomposition for 4-5 variable Boolean expressions
- **Semilinear support** — constant-masked atoms with XOR/OR/NOT-AND constant lowering, structure recovery, term refinement, bit-partitioned reconstruction
- **Polynomial recovery** — multilinear terms and singleton powers via coefficient splitting and finite differences
- **Mixed product handling** — decomposition engine with core extraction, residual solving, and ghost residual classification
- **Subexpression lifting** — replace complex subtrees with virtual variables to reduce problem dimension
- **Worklist orchestrator** — DAG-aware pass scheduling with deduplication and bounded search
- **Competition groups** — local alternative branches and child solves use cost-based winner selection with continuations
- **Constant shifts** — `<<` desugars to multiplication, `>>` simplifies via semilinear techniques
- **ANF cleanup** — absorption, common-cube factoring, and OR recognition
- **Configurable bitwidth** — 1-bi