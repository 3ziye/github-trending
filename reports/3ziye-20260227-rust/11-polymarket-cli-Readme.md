# Polymarket CLI

Rust CLI for Polymarket. Browse markets, place orders, manage positions, and interact with onchain contracts — from a terminal or as a JSON API for scripts and agents.

> **Warning:** This is early, experimental software. Use at your own risk and do not use with large amounts of funds. APIs, commands, and behavior may change without notice. Always verify transactions before confirming.

## Install

### Homebrew (macOS / Linux)

```bash
brew tap Polymarket/polymarket-cli https://github.com/Polymarket/polymarket-cli
brew install polymarket
```

### Shell script

```bash
curl -sSL https://raw.githubusercontent.com/Polymarket/polymarket-cli/main/install.sh | sh
```

### Build from source

```bash
git clone https://github.com/Polymarket/polymarket-cli
cd polymarket-cli
cargo install --path .
```

## Quick Start

```bash
# No wallet needed — browse markets immediately
polymarket markets list --limit 5
polymarket markets search "election"
polymarket events list --tag politics

# Check a specific market
polymarket markets get will-trump-win-the-2024-election

# JSON output for scripts
polymarket -o json markets list --limit 3
```

To trade, set up a wallet:

```bash
polymarket setup
# Or manually:
polymarket wallet create
polymarket approve set
```

## Configuration

### Wallet Setup

The CLI needs a private key to sign orders and on-chain transactions. Three ways to provide it (checked in this order):

1. **CLI flag**: `--private-key 0xabc...`
2. **Environment variable**: `POLYMARKET_PRIVATE_KEY=0xabc...`
3. **Config file**: `~/.config/polymarket/config.json`

```bash
# Create a new wallet (generates random key, saves to config)
polymarket wallet create

# Import an existing key
polymarket wallet import 0xabc123...

# Check what's configured
polymarket wallet show
```

The config file (`~/.config/polymarket/config.json`):

```json
{
  "private_key": "0x...",
  "chain_id": 137,
  "signature_type": "proxy"
}
```

### Signature Types

- `proxy` (default) — uses Polymarket's proxy wallet system
- `eoa` — signs directly with your key
- `gnosis-safe` — for multisig wallets

Override per-command with `--signature-type eoa` or via `POLYMARKET_SIGNATURE_TYPE`.

### What Needs a Wallet

Most commands work without a wallet — browsing markets, viewing order books, checking prices. You only need a wallet for:

- Placing and canceling orders (`clob create-order`, `clob market-order`, `clob cancel-*`)
- Checking your balances and trades (`clob balance`, `clob trades`, `clob orders`)
- On-chain operations (`approve set`, `ctf split/merge/redeem`)
- Reward and API key management (`clob rewards`, `clob create-api-key`)

## Output Formats

Every command supports `--output table` (default) and `--output json`.

```bash
# Human-readable table (default)
polymarket markets list --limit 2
```

```
 Question                            Price (Yes)  Volume   Liquidity  Status
 Will Trump win the 2024 election?   52.00¢       $145.2M  $1.2M      Active
 Will BTC hit $100k by Dec 2024?     67.30¢       $89.4M   $430.5K    Active
```

```bash
# Machine-readable JSON
polymarket -o json markets list --limit 2
```

```json
[
  { "id": "12345", "question": "Will Trump win the 2024 election?", "outcomePrices": ["0.52", "0.48"], ... },
  { "id": "67890", "question": "Will BTC hit $100k by Dec 2024?", ... }
]
```

Short form: `-o json` or `-o table`.

Errors follow the same pattern — table mode prints `Error: ...` to stderr, JSON mode prints `{"error": "..."}` to stdout. Non-zero exit code either way.

## Commands

### Markets

```bash
# List markets with filters
polymarket markets list --limit 10
polymarket markets list --active true --order volume_num
polymarket markets list --closed false --limit 50 --offset 25

# Get a single market by ID or slug
polymarket markets get 12345
polymarket markets get will-trump-win

# Search
polymarket markets search "bitcoin" --limit 5

# Get tags for a market
polymarket markets tags 12345
```

**Flags for `markets list`**: `--limit`, `--offset`, `--order`, `--ascending`, `--active`, `--closed`

### Events

Events group related markets (e.g. "2024 Election" contains multiple yes/no markets).

```bash
polymarket events list --limit 10
polymarket events list --tag politics --active true
polymarket events get 500
polymarket events tags 500
```

**Flags for `events list`**: `--limit`, `--offset`, `--order`, `--ascending`, `--active`, `--closed`, `--tag`

### Tags, Series, Comments, Profiles, Sports

```bash
# Tags
polymarket tags list
polymarket tags get politics
polymarket tags related politics
polymarket tags related-tags politics

# Series (recurring events)
polymarket series list --limit 10
polymarket series get 42

# Comments on an entity
polymarket comments list --entity-type event --entity-id 500
polymarket comments get abc123
polymarket comments by-user 0xf5E6...

# Public profiles
polymarket profiles get 0xf5E6...

# Sports metadata
polymarket sports list
polymarket sports market-types
polyma