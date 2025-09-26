![](./assets/logo.svg)

<h3 align="center">
  A 21 CU Solana Oracle Program
</h3>

## Overview

Doppler is an ultra-optimized oracle program for Solana, achieving unparalleled performance at just **21 Compute Units (CUs)** per update. Built with low-level optimizations and minimal overhead, Doppler sets the standard for high-frequency, low-latency price feeds on Solana.

## Features

- **21 CU Oracle Updates**: The most efficient oracle implementation on Solana
- **Generic Payload Support**: Flexible data structure supporting any payload type
- **Sequence-Based Updates**: Built-in replay protection and ordering guarantees
- **Zero Dependencies**: Pure no_std Rust implementation for minimal overhead
- **Direct Memory Operations**: Optimized assembly-level exits for maximum efficiency

## Installation

Add Doppler SDK and required Solana crates to your `Cargo.toml`:

```toml
[dependencies]
doppler-sdk = "0.1.0"
solana-instruction = "2.3.0"
solana-pubkey = "2.3.0"
solana-compute-budget-interface = "2.2.2"
solana-transaction = "2.3.0"
solana-keypair = "2.3.0"
solana-signer = "2.2.1"
# Add other Solana crates as needed
```

## Program ID

```
fastRQJt3nLdY3QA7n8eZ8ETEVefy56ryfUGVkfZokm
```

## Architecture

Doppler uses a simple yet powerful architecture:

1. **Admin Account**: Controls oracle updates (hardcoded for security)
2. **Oracle Account**: Stores the sequence number and payload data
3. **Sequence Validation**: Ensures updates are monotonically increasing

### Data Structure

```rust
pub struct Oracle<T> {
    pub sequence: u64,  // Timestamp, slot height, or auto-increment
    pub payload: T,     // Your custom data structure
}
```

## Usage Guide

### 1. Setting Up Compute Budget

To achieve the 21 CU performance, configure your transaction with appropriate compute budget:

```rust
use solana_compute_budget_interface::ComputeBudgetInstruction;
use solana_instruction::Instruction;
use solana_transaction::Transaction;

// Request exactly the CUs needed (21 + overhead for other instructions)
let compute_budget_ix = ComputeBudgetInstruction::set_compute_unit_limit(200_000);

// Add to your transaction
let mut instructions = vec![compute_budget_ix];
```

### 2. Setting Priority Fees

For high-frequency oracle updates, use priority fees to ensure timely inclusion:

```rust
// Set priority fee (price per compute unit in micro-lamports)
let priority_fee_ix = ComputeBudgetInstruction::set_compute_unit_price(1000);

instructions.push(priority_fee_ix);
```

### 3. Optimizing Account Data Size

Use `setLoadedAccountsDataSizeLimit` to optimize memory allocation:

```rust
// Set the maximum loaded account data size
// Calculate based on your oracle data structure size
let data_size_limit_ix = ComputeBudgetInstruction::set_loaded_accounts_data_size_limit(
    32_768  // 32KB is usually sufficient for oracle operations
);

instructions.push(data_size_limit_ix);
```

### 4. Creating an Oracle Update

```rust
use doppler_sdk::{Oracle, UpdateInstruction, ID as DOPPLER_ID};
use solana_instruction::Instruction;
use solana_pubkey::Pubkey;

// Define your payload structure
#[derive(Clone, Copy)]
pub struct PriceFeed {
    pub price: u64,
}

// Create oracle update
let oracle_update = Oracle {
    sequence: 1234567890,  // Must be > current sequence
    payload: PriceFeed {
        price: 42_000_000,  // $42.00 with 6 decimals
    },
};

// Create update instruction
let update_ix: Instruction = UpdateInstruction {
    admin: admin_pubkey,
    oracle_pubkey: oracle_pubkey,
    oracle: oracle_update,
}.into();

// Add to instructions
instructions.push(update_ix);
```

### 5. Complete Transaction Example

```rust
use doppler_sdk::{Oracle, UpdateInstruction};
use solana_client::rpc_client::RpcClient;
use solana_compute_budget_interface::ComputeBudgetInstruction;
use solana_instruction::Instruction;
use solana_keypair::Keypair;
use solana_signer::Signer;
use solana_transaction::Transaction;

async fn update_oracle(
    client: &RpcClient,
    admin: &Keypair,
    oracle_pubkey: Pubkey,
    new_price: u64,
    sequence: u64,
) -> Result<(), Box<dyn std::error::Error>> {
    // Build all instructions
    let mut instructions = vec![
        // 1. Set compute budget
        ComputeBudgetInstruction::set_compute_unit_limit(200_000),

        // 2. Set priority fee (1000 micro-lamports per CU)
        ComputeBudgetInstruction::set_compute_unit_price(1_000),

        // 3. Set loaded accounts data size limit
        ComputeBudgetInstruction::set_loaded_accounts_data_size_limit(32_768),
    ];

    // 4. Add oracle update
    let oracle_update = Oracle {
        sequence,
        payload: PriceFeed { price: new_price },
    };

    let update_ix: Instruction = UpdateInstruction {
        admin: admin.pubkey(),
        oracle_pubkey,
        oracle: oracle_update,
    }.into();

    instructions.push(update_ix);

    // Create and send transaction
    let recent_blockhash = client.get_latest_blockhash()?;
    let tx = Transaction::new_sig