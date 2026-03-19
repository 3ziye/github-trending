# Verified Agent Identity

A decentralized identity management toolkit for AI agents using iden3 protocol on Billions Network.

## Overview

This skill enables AI agents to create, manage, link, prove and verify ownership of decentralized identities (DIDs) using cryptographic signatures.

## Installation

### Agent CTA:

1. Ask bot to install the skill:

   ```plaintext
   Install the skill `npx clawhub@latest install verified-agent-identity`
   ```

   Or

   ```plaintext
   Install the `verified-agent-identity` skill from the OpenClaw clawhub.ai.
   ```

2. (Optional) If the verification process did not start automatically after installation, ask your bot to initialize the process by sending a message like:

   ```plaintext
   Please link your agent identity to me.
   ```

### Human CTA:

1. Install the skill:
   ```bash
   npx clawhub@latest install verified-agent-identity
   ```
2. Create a new identity:

   ```bash
   # Generate a new key and create a new identity
   node scripts/createNewEthereumIdentity.js
   ```

   Or

   ```bash
   # Use an existing private key to create an identity
   node scripts/createNewEthereumIdentity.js --key <your-ethereum-private-key>
   ```

3. Generate a verification link to connect your human identity to the agent:

   ```bash
   node scripts/manualLinkHumanToAgent.js --challenge '{"name": "Agent Name", "description": "Short description of the agent"}'
   ```

   This prints the verification URL to the console. Open it in your browser to complete the identity linking process.

## Features

- **Identity Creation**: Generate new DIDs with random or existing Ethereum private keys
- **Identity Management**: List and manage multiple identities with default identity support
- **Human-Agent Linking**: Link a human identity to an agent's DID through signed challenges
- **Proof Generation**: Generate cryptographic proofs to authenticate as a specific identity
- **Proof Verification**: Verify proofs to confirm identity ownership

## Architecture

### Runtime Requirements

- **Node.js `>= v20`** and **npm** are required to run the scripts.

### Dependency Surface

npm dependencies are intentionally minimal and scoped to well-established, audited packages:

| Package                | Purpose                                                      |
| ---------------------- | ------------------------------------------------------------ |
| `@0xpolygonid/js-sdk`  | iden3/Privado ID cryptographic primitives and key management |
| `@iden3/js-iden3-core` | DID and identity core types                                  |
| `@iden3/js-iden3-auth` | JWS/JWA authorization response construction and verification |
| `ethers`               | Ethereum key utilities                                       |
| `uuid`                 | UUID generation for protocol message IDs                     |

Core libraries governing identity management use pinned, well-tested versions to ensure stability and security.

### Key Storage and Isolation

All cryptographic material is persisted to `$HOME/.openclaw/billions/` — a directory that lives **outside the agent's workspace**:

| File               | Contents                                                                           |
| ------------------ | ---------------------------------------------------------------------------------- |
| `kms.json`         | Private keys — per-entry versioned format; keys are plain or AES-256-GCM encrypted |
| `identities.json`  | Identity metadata                                                                  |
| `defaultDid.json`  | Active DID and associated public key                                               |
| `challenges.json`  | Per-DID challenge history                                                          |
| `credentials.json` | Verifiable credentials                                                             |

There are several ways of storing private keys, to enable master key encryption as described in the **KMS Encryption** section below.

### KMS Encryption

Set the environment variable `BILLIONS_NETWORK_MASTER_KMS_KEY` to enable AES-256-GCM at-rest encryption for the private keys inside `kms.json`. When set, every key value is individually encrypted on write; when absent, keys are stored as plain hex strings.

**`kms.json` entry format**

Each entry in the array is versioned. The `alias` is always stored in plaintext — only the `key` value is encrypted:

```json
[
  {
    "version": 1,
    "provider": "plain",
    "data": {
      "alias": "secp256k1:abc123",
      "key": "deadbeef...",
      "createdAt": "2026-03-12T13:46:04.094Z"
    }
  },
  {
    "version": 1,
    "provider": "encrypted",
    "data": {
      "alias": "secp256k1:xyz456",
      "key": "<iv_hex>:<authTag_hex>:<ciphertext_hex>",
      "createdAt": "2026-02-11T13:00:02.032Z"
    }
  }
]
```

**Behavior summary**

| `BILLIONS_NETWORK_MASTER_KMS_KEY` | `provider` on disk | `key` value on disk     |
| --------------------------------- 