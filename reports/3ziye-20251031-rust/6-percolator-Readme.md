# Percolator

A formally-verified perpetual futures exchange protocol for Solana with O(1) crisis loss socialization, constant product AMM, and rigorous security guarantees.

> **⚠️ EDUCATIONAL USE ONLY**
>
> This code is provided for educational and research purposes only. It has not been independently audited for production use and should not be deployed to handle real funds. Use at your own risk.

## Overview

Percolator is a high-assurance decentralized exchange (DEX) protocol built on Solana that combines:

- **Formal Verification**: 70+ Kani proofs covering safety-critical invariants
- **O(1) Crisis Resolution**: Constant-time loss socialization via global scale factors
- **Constant Product AMM**: Verified x·y=k invariant with fee accrual
- **Cross-Margin Portfolio**: Net exposure calculation for capital efficiency
- **Adaptive PnL Vesting**: Taylor series approximation for withdrawal throttling
- **Zero Allocations**: Pure `no_std` Rust optimized for Solana BPF

**Verification Coverage**: 85% of production operations use formally verified functions

## Quick Start

```bash
# Build all programs and CLI
cargo build-sbf
cargo build --release --bin percolator

# Run unit tests (257 passing)
cargo test --lib

# Run formal verification proofs
cargo kani -p proofs-kani --harness i2_conservation_2users_3steps
cargo kani -p model_safety --harness proof_c3_no_overburn

# Deploy to localnet
solana-test-validator &
./target/release/percolator -n localnet deploy --all

# Initialize exchange and run integration tests
./target/release/percolator -n localnet test --all
```

## Architecture

### Two-Program Design

#### Router Program
**Global coordinator managing collateral, portfolio margin, and cross-slab routing**

Responsibilities:
- Maintain user portfolios with equity and net exposure tracking
- Manage central collateral vaults (SPL tokens, currently SOL only)
- Registry of whitelisted matcher programs
- Execute trades via CPI to matchers
- Handle liquidations when equity < maintenance margin
- Apply adaptive PnL vesting (warmup period throttling)

#### Slab (Matcher) Program
**LP-owned order book maintaining its own state and matching logic**

Responsibilities:
- Maintain local order book with price-time priority
- Update quote cache for router exposure calculations
- Verify router authority and sequence numbers (TOCTOU protection)
- Execute fills at captured maker prices
- Never holds or moves funds (router-only)

### Safety Architecture

```
┌──────────────────┐
│  User Wallets    │
└────────┬─────────┘
         │ SOL deposits/withdrawals
         ▼
┌──────────────────┐     CPI      ┌──────────────────┐
│  Router Program  │─────────────▶│  Slab Programs   │
│  (Authority)     │◀─────────────│  (Matchers)      │
│                  │   read-only  │                  │
│ • Collateral     │              │ • Order books    │
│ • Portfolios     │              │ • Quote cache    │
│ • Liquidations   │              │ • Matching       │
│ • Vesting        │              │                  │
└──────────────────┘              └──────────────────┘
         │
         ▼
  Formally Verified
  Model Safety Layer
```

**Security Rules**:
- All funds stay in router vaults
- Router → Matcher is one-way CPI (no callbacks)
- Whitelist controls which matchers can be invoked
- Sequence numbers prevent TOCTOU attacks
- Atomicity: any CPI failure aborts entire transaction

## Core Features

### 1. Crisis Loss Socialization (O(1))

When the system becomes insolvent (liquidations fail to cover losses), the crisis module socializes losses across winners without iterating over users.

**Loss Waterfall**:
1. Warming PnL (unvested profits)
2. Insurance fund
3. Equity (principal + realized PnL)

```rust
use model_safety::crisis::*;

// Crisis occurs - 200K deficit
let mut accums = Accums::new();
accums.sigma_principal = 1_000_000;
accums.sigma_collateral = 800_000;

let outcome = crisis_apply_haircuts(&mut accums);

// Later, user materializes on next action
materialize_user(&mut user, &mut accums, MaterializeParams::default());
```

**Verified Invariants** (C1-C9):
- C1: Post-crisis solvency (or best effort)
- C2: Scales monotone (never increase)
- C3: No over-burn (bounded haircuts)
- C4: Materialization idempotent
- C5: Vesting conservation
- C8: Loss waterfall ordering
- C9: Vesting progress guarantee

### 2. Constant Product AMM (x·y=k)

Embedded AMM for immediate liquidity with formally verified invariants.

```rust
use amm_model::*;

// Buy 1 BTC at current reserves
let result = quote_buy(
    x_reserve,  // 1000 BTC (scaled)
    y_reserve,  // 60M USD (scaled)
    fee_bps,    // 5 bps
    1 * SCALE,  // 1 BTC desired
    min_liq,    // Liquidity floor
)?;

// Result includes VWAP, new reserves, quote amount
```

**Verified Properties** (A1-A8):
- A1: Invariant non-decreasing (fees increase k)
- A2: Reserves non-negative
- A3: No arithmetic overflow
- A4: Deterministic execution
- A5: Fee routing correctness
- A6: Price impact scal