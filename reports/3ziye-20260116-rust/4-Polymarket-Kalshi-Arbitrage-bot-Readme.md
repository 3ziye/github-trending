# Polymarket-Kalshi Arbitrage Bot

An arbitrage system for cross-platform prediction market trading between Kalshi and Polymarket.

> 🎯 **Perfect for Beginners!** This bot is designed specifically for **people who don't know how to code**. Even if you've never written a single line of code, you can use this bot with our comprehensive step-by-step guides. No programming experience required!

---

---

<div align="center">

## 📚 **IMPORTANT: Please Refer to the Complete Documentation**

**⚠️ CRITICAL: Before starting, please refer to our comprehensive documentation in the [`doc/`](./doc/) folder for detailed step-by-step guides, troubleshooting, and complete setup instructions.**

![Documentation Guide](./documentation-preview.png)

**[👉 Click here to start with the Getting Started Guide](./doc/01-getting-started.md)** | **[📄 Download Complete PDF Guide](./doc/Polymarket-Kalshi-Arbitrage-Bot-User-Guide.pdf)**

*All guides are designed for beginners with no coding experience - everything is explained step-by-step!*

</div>

---

> 🔍 **What is this?** This bot automatically monitors prices on both platforms and executes trades when it finds opportunities where you can buy both YES and NO for less than $1.00, guaranteeing a profit when the market resolves.

> 🚀 **What's Coming Next:** I'm developing other innovative arbitrage bots with revolutionary strategies. Stay tuned for more advanced trading systems!

---

## Quick Start

### 1. Install Dependencies

```bash
# Rust 1.75+
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Navigate to project directory
cd prediction-market-arbitrage  # or your project directory name

# Build
cargo build --release
```

📖 **Detailed installation guide:** [Installation Guide](./doc/02-installation.md)

### 2. Set Up Credentials

Create a `.env` file:

```bash
# === KALSHI CREDENTIALS ===
KALSHI_API_KEY_ID=your_kalshi_api_key_id
KALSHI_PRIVATE_KEY_PATH=/path/to/kalshi_private_key.pem

# === POLYMARKET CREDENTIALS ===
POLY_PRIVATE_KEY=0xYOUR_WALLET_PRIVATE_KEY
POLY_FUNDER=0xYOUR_WALLET_ADDRESS

# === BOT CONFIGURATION ===
DRY_RUN=1
RUST_LOG=info
```

📖 **Complete credentials setup guide:** [Getting Your Credentials](./doc/03-credentials.md) | [Configuration Setup](./doc/04-configuration.md)

### 3. Run

```bash
# Dry run (paper trading)
dotenvx run -- cargo run --release

# Live execution
DRY_RUN=0 dotenvx run -- cargo run --release
```

📖 **Running the bot guide:** [Running the Bot](./doc/05-running-the-bot.md)

---

## 📚 Documentation

> ⚠️ **CRITICAL: Before Starting - Read the Documentation!**
> 
> **This README provides a quick overview. For complete setup instructions, troubleshooting, and detailed explanations, you MUST refer to the comprehensive documentation in the [`doc/`](./doc/) folder. All guides are designed for beginners with no coding experience.**

**Follow these comprehensive guides in order:**

1. **[📖 Getting Started Guide](./doc/01-getting-started.md)** - Overview and introduction - **START HERE!**
2. **[🔧 Installation Guide](./doc/02-installation.md)** - Install Rust and dependencies (Windows/Mac/Linux)
3. **[🔑 Getting Your Credentials](./doc/03-credentials.md)** - Get API keys from Kalshi and Polymarket
4. **[⚙️ Configuration Setup](./doc/04-configuration.md)** - Complete guide to all configuration options
5. **[▶️ Running the Bot](./doc/05-running-the-bot.md)** - Start and monitor your bot
6. **[🔧 Troubleshooting](./doc/06-troubleshooting.md)** - Common problems and solutions

📄 **PDF Version:** A complete PDF guide combining all documentation: **[📥 Download Polymarket-Kalshi-Arbitrage-Bot-User-Guide.pdf](./doc/Polymarket-Kalshi-Arbitrage-Bot-User-Guide.pdf)**

**Why refer to the documentation?**
- ✅ Step-by-step instructions for every step
- ✅ Screenshots and visual guides
- ✅ Troubleshooting for common issues
- ✅ Configuration explanations
- ✅ Safety warnings and best practices
- ✅ Written specifically for non-technical users

---

## Environment Variables

### Required

| Variable | Description |
|----------|-------------|
| `KALSHI_API_KEY_ID` | Your Kalshi API key ID |
| `KALSHI_PRIVATE_KEY_PATH` | Path to RSA private key (PEM format) for Kalshi API signing |
| `POLY_PRIVATE_KEY` | Ethereum private key (with 0x prefix) for Polymarket wallet |
| `POLY_FUNDER` | Your Polymarket wallet address (with 0x prefix) |

### Bot Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `DRY_RUN` | `1` | `1` = paper trading (no orders), `0` = live execution |
| `RUST_LOG` | `info` | Log level: `error`, `warn`, `info`, `debug`, `trace` |
| `FORCE_DISCOVERY` | `0` | `1` = re-fetch market mappings (ignore cache) |
| `PRICE_LOGGING` | `0` | `1` = verbose price update logging |

### Test Mode

| Variable | Default | Description |
|----------|---------|-------------|
| `TEST_ARB` | `0` | `1` = inject synthetic arb opportunity for testing |
| `TEST_ARB_TYPE` | `poly_yes_kalshi_no` | Arb type: `poly_yes_kalshi_no`, `kalshi_