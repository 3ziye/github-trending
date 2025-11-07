# Percolator

A formally-verified perpetual futures exchange protocol for Solana with three-tier bad debt defense, constant product AMM, and rigorous security guarantees.

> **⚠️ EDUCATIONAL USE ONLY**
>
> This code is provided for educational and research purposes only. It has not been independently audited for production use and should not be deployed to handle real funds. Use at your own risk.

## Overview

Percolator is a high-assurance decentralized exchange (DEX) protocol built on Solana that combines:

- **Formal Verification**: 70+ Kani proofs covering safety-critical invariants
- **Three-Tier Bad Debt Defense**: Insurance fund → Warmup burn → Equity haircut
- **O(1) Crisis Resolution**: Constant-time loss socialization via global scale factors
- **Insurance Fund**: Separate vault with configurable authority, fee accrual, and payout caps
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

### 1. Three-Tier Bad Debt Defense (O(1))

When liquidations create bad debt, the protocol uses a three-tier defense mechanism to socialize losses across winners without iterating over users.

**Loss Waterfall**:
1. **Insurance Fund** (first line of defense)
   - Separate vault PDA controlled by insurance authority
   - Accrues fees from trades
   - Pays out during liquidations with bad debt
   - Configurable authority for topup/withdrawal
   - Hard caps: per-event payout (0.5% of OI) and daily limit (3% of vault)

2. **Warming PnL** (second line of defense)
   - Burns unvested profits from users
   - Only after insurance exhausted

3. **Equity Haircut** (final resort)
   - Global scale factor applied to all users
   - Only after insurance AND warmup exhausted
   - Haircut = (deficit - insurance - warmup) / total_equity

```rust
use model_safety::crisis::*;

// Example: 150 SOL bad debt, 50 SOL insurance, 800 SOL equity
let mut accums = Accums::new();
accums.sigma_principal = 800_000_000_000;        // 800 SOL
accums.sigma_collateral = 650_000_000_000;      // 650 SOL (150 SOL deficit)
accums.sigma_insurance = 50_000_000_000;        // 50 SOL

let outcome = crisis_apply_haircuts(&mut accums);

// Result:
// - Insurance drawn: 50 SOL (exhausted completely)
// - Remaining deficit: 100 SOL
// - Haircut ratio: 100 / 800 = 12.5%
// - User with 300 SOL → keeps 262.5 SOL (loses 37.5