# Quip Network Experimental Node

> **WARNING: This is experimental demonstration software provided without warranty of any kind. It is not intended for production use. Use at your own risk.**

This project implements a quantum blockchain using quantum annealing for proof-of-work consensus. It features competitive mining between quantum computers (QPU) and classical simulated annealing (SA) with a dynamic difficulty adjustment mechanism.

## Overview

The blockchain demonstrates:

- **Quantum Annealing PoW**: Using Ising model optimization as the mining puzzle
- **Competitive Mining**: Multiple miners (QPU and SA) compete to mine blocks
- **Multi-Miner Support**: Configure any number of QPU and SA miners
- **Dynamic Difficulty**: Inverted difficulty mechanism that prevents miner monopolization
- **Streak Rewards**: Consecutive wins increase block rewards
- **Solution Diversity**: Requires multiple diverse solutions to prevent trivial mining
- **Individual Miner Tracking**: Each miner has unique ID and performance stats

## Current Scope

The current implementation:
- **Quantum PoW only** - No transactions, accounts, or other typical blockchain features
- **Demonstration signatures** - The signature system is not yet production-secure; it demonstrates the hybrid ECDSA + WOTS+ approach but requires proper integration

## Roadmap

We plan to build a complete blockchain by forking an existing battle tested codebase to maximize development velocity.

### Phase 1: Core Integration
- Fork a battle-tested blockchain codebase
- Integrate our quantum proof-of-work mechanism (Ising model optimization, difficulty adjustment, block time targets already defined)
- Target: Testnet deployment

### Phase 2: Signature System
- Integrate our hybrid signature system: classical ECDSA combined with post-quantum WOTS+ signatures
- Implement stateful signature management
- Wire signatures into transaction processing and consensus

### Phase 3: Subnet Architecture
- Implement a subnet system with **objective, measurable metrics** for validation
- Subnets will solve computational problems (scientific computing, cryptographic proofs, etc.) with verifiable results
- Define subnet registration, validation mechanisms, and reward distribution

### Phase 4: Smart Contracts
- Add smart contract support via EVM compatibility (Solidity/Vyper) and/or Rust-based WebAssembly runtime
- Later: Enable contracts to interact with subnet computational results

### Open Technical Decisions
1. Which blockchain codebase to fork?
2. How to structure subnets for different computational problem types?
3. How to validate objective metrics across the decentralized network?
4. Performance targets (TPS, finality time, subnet throughput)?

## Getting Started

You can run your own node using the "latest" release, see the README in the `docker` directory for instructions on how to run the node in a container.

## Setup

1. Create and activate a virtual environment (Python 3.10+):

   ```bash
   python3 -m venv .quip
   source .quip/bin/activate  # Windows: .venv\Scripts\activate
   ```

2. Install the package in editable mode:

   ```bash
   pip install -U pip setuptools wheel
   pip install -e .
   ```

   This will install all dependencies from pyproject.toml and register console scripts.

3. Set up D-Wave API credentials (optional, for QPU access):
   ```bash
   echo "DWAVE_API_KEY=your_api_key_here" > .env
   ```

## Project Structure

```
quip-protocol/
├── quip_cli.py                # Main CLI entry point
├── blockchain_base.py         # Base classes for miners
├── shared/                    # Core modules
│   ├── network_node.py       # P2P networking (QUIC protocol)
│   ├── node.py               # Node state management
│   ├── block.py              # Block and header dataclasses
│   ├── block_signer.py       # ECDSA + WOTS+ signatures
│   ├── quantum_proof_of_work.py  # Ising model PoW
│   ├── base_miner.py         # Abstract miner interface
│   └── ...                   # Additional utilities
├── CPU/                       # CPU-based miners
│   ├── sa_miner.py           # Simulated annealing miner
│   └── sa_sampler.py         # SA sampler implementation
├── GPU/                       # GPU-accelerated miners
│   ├── cuda_miner.py         # CUDA GPU miner
│   ├── metal_miner.py        # Apple Metal/MPS miner
│   └── modal_miner.py        # Modal Labs cloud GPU
├── QPU/                       # Quantum processor miners
│   ├── dwave_miner.py        # D-Wave QPU miner
│   └── dwave_sampler.py      # D-Wave sampler wrapper
├── docker/                    # Docker deployment files
├── tests/                     # Test suite
├── reference/                 # Reference implementation
└── benchmarks/                # Performance benchmarks
```

## quip-network-node

Run a single P2P node of a specific type. Subcommands: cpu, gpu, qpu.

- Always enables competitive mode
- Implies a single miner of that type (num-sa/num-gpu/num-qpu = 1)
- Supports a top-level --con