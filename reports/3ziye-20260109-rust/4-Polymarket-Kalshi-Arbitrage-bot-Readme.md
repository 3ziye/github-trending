# Kalshi-Poly / Poly-Poly / Kalshi-Kalshi Arbitrage Bot

**Kalshi-Poly arbitrage bot**, **Poly-Poly arbitrage bot**, and **Kalshi-Kalshi arbitrage bot** for automated cross-platform trading. A high-performance, production-ready arbitrage trading system that monitors price discrepancies between Kalshi and Polymarket, executing risk-free arbitrage opportunities in real-time with sub-millisecond latency.

> 🔍 **Search Keywords**: polymarket arbitrage bot, polymarket-kalshi arbitrage bot, kalshi-poly arbitrage, poly-poly arbitrage, kalshi-kalshi arbitrage, kalshi arbitrage, prediction market arbitrage, cross-platform trading bot

## Overview

This **Kalshi-Poly / Poly-Poly / Kalshi-Kalshi arbitrage bot** identifies and executes arbitrage opportunities across:

- **Kalshi-Poly markets** (cross-platform arbitrage between Kalshi and Polymarket)
- **Poly-Poly markets** (same-platform arbitrage on Polymarket)
- **Kalshi-Kalshi markets** (same-platform arbitrage on Kalshi)

The bot takes both sides of a market when YES and NO prices add up to less than $1.00, guaranteeing a risk-free profit at market expiry.

### How It Works

**Example Opportunity:**
- YES = $0.40, NO = $0.58
- Total cost = $0.98
- At expiry: YES = $1.00 and NO = $0.00 (or vice versa)
- **Result: 2.04% risk-free return**

### Market Insights

When observing large traders like PN1 finding significant size in these opportunities, the initial assumption was that opportunities would be extremely fleeting with intense competition. However, the reality is quite different:

- **Opportunities are persistent**: While concurrent dislocations aren't frequent, when they do occur, they persist long enough to execute manually
- **Large traders use limit orders**: Whales typically fill positions via limit orders over extended periods, as odds don't fluctuate significantly before game time
- **Manual execution is viable**: Opportunities remain available long enough for manual intervention if needed

### System Workflow

The repository implements the following workflow:

1. **Market Scanning**: Scans sports markets that expire within the next couple of days
2. **Market Matching**: Matches Kalshi-Polymarket markets using:
   - Cached mapping of team names between platforms
   - Kalshi-Polymarket event slug building conventions
3. **Real-time Monitoring**: Subscribes to orderbook delta WebSockets to detect instances where YES + NO can be purchased for less than $1.00
4. **Order Execution**: Executes trades concurrently on both platforms
5. **Risk Management**: Includes position management and circuit breakers (note: not extensively battle-tested in production)

### Useful Components

Beyond the complete arbitrage system, you may find these components particularly useful:

- **Cross-platform market mapping**: The team code mapping system for matching markets across Kalshi and Polymarket
- **Rust CLOB client**: A Rust rewrite of Polymarket's Python `py-clob-client` (focused on order submission only)

## Quick Start

### 1. Install Dependencies

```bash
# Rust 1.75+
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Build
cargo build --release
```

### 2. Set Up Credentials

Create a `.env` file:

```bash
# === KALSHI CREDENTIALS ===
KALSHI_API_KEY_ID=your_kalshi_api_key_id
KALSHI_PRIVATE_KEY_PATH=/path/to/kalshi_private_key.pem

# === POLYMARKET CREDENTIALS ===
POLY_PRIVATE_KEY=0xYOUR_WALLET_PRIVATE_KEY
POLY_FUNDER=0xYOUR_WALLET_ADDRESS

# === SYSTEM CONFIGURATION ===
DRY_RUN=1
RUST_LOG=info
```

### 3. Run

```bash
# Dry run (paper trading)
dotenvx run -- cargo run --release

# Live execution
DRY_RUN=0 dotenvx run -- cargo run --release
```

---

## Environment Variables

### Required

| Variable                  | Description                                                 |
| ------------------------- | ----------------------------------------------------------- |
| `KALSHI_API_KEY_ID`       | Your Kalshi API key ID                                      |
| `KALSHI_PRIVATE_KEY_PATH` | Path to RSA private key (PEM format) for Kalshi API signing |
| `POLY_PRIVATE_KEY`        | Ethereum private key (with 0x prefix) for Polymarket wallet |
| `POLY_FUNDER`             | Your Polymarket wallet address (with 0x prefix)             |

### System Configuration

| Variable          | Default | Description                                           |
| ----------------- | ------- | ----------------------------------------------------- |
| `DRY_RUN`         | `1`     | `1` = paper trading (no orders), `0` = live execution |
| `RUST_LOG`        | `info`  | Log level: `error`, `warn`, `info`, `debug`, `trace`  |
| `FORCE_DISCOVERY` | `0`     | `1` = re-fetch market mappings (ignore cache)         |
| `PRICE_LOGGING`   | `0`     | `1` = verbose price update logging                    |

### Test Mode

| Variable        | Default              | Description                                                                                    |
| --------------- | ----------