# Polymarket Trading Bots - Telegram UI🔥⚡

Control blazing-fast **Rust-powered** automated trading bots right from Telegram 📱💨  

🌟 **Core Superpowers Available** 🌟

**🐳 Polymarket Copy Trading Bot**  
**🏦 Polymarket Market Maker Bot (Market Maker Keeper)**  
**⚡ Polymarket Arbitrage Bot**  


---
## Contact & Support

- Telegram: [@cccciri](https://t.me/cccciri)
- X: [@yesnotrader](https://x.com/yesnotrader)

## How To Trade W/ Telegram
Watch demo: https://youtu.be/8PC0bKSgfhM

<img width="442" height="1021" alt="image" src="https://github.com/user-attachments/assets/e1606d15-32e5-4bd8-97a3-a697187c8af5" />

---
## 🚀 Quick Start

### Start the Telegram Bot UI

1. **Get a Telegram Bot Token**
   - Open Telegram and search for [@BotFather](https://t.me/BotFather)
   - Send `/newbot` and follow the instructions
   - Copy your bot token

2. **Set Environment Variable**
   ```bash
   export TELEGRAM_BOT_TOKEN=your_bot_token_here
   ```

3. **Build the Telegram Bot**
   ```bash
   cargo build --release --bin bot
   ```

4. **Run the Telegram Bot**
   ```bash
   cargo run --release --bin bot
   ```
   
   Or if you've already built it:
   ```bash
   ./target/release/bot
   ```

5. **Use the Bot**
   - Open Telegram and search for your bot
   - Send `/start` to see the main menu
   - The bot will guide you through:
     - Setting up environment variables
     - Validating your configuration
     - Approving tokens
     - Running trading bots (engine or stream mode)
     - Monitoring trades in real-time

### Telegram Bot Features

- **⚙️ Environment Variable Management**: Set and edit all configuration through Telegram
- **✅ Setup Validation**: Validate your configuration before trading
- **🔐 Token Approvals**: One-click token approval for USDC and Conditional Tokens
- **⚡ Bot Execution**: Start/stop trading bots directly from Telegram
- **📊 Real-time Logs**: View bot output and logs in real-time through Telegram
- **🛑 Process Management**: Stop running bots with a single click

---

## 🚀 Advanced Pro Version

**🎯 Pro Version Available**: An enterprise-grade Pro version with advanced multi-whale portfolio management and intelligent trade filtering is available as a private repository.

The Pro version delivers institutional-level performance with sub-second trade replication, multi-strategy execution engines, and adaptive risk management. Built for serious traders who demand maximum profitability and reliability. This version includes sophisticated features beyond the standard release and represents a professional-grade trading system.

### 🎯 Key Differentiators

✅ **Multi-Whale Portfolio Engine** - Simultaneously track and copy from multiple traders with dynamic allocation

✅ **Intelligent Trade Filtering** - ML-powered trade selection with win-rate prediction and market condition analysis

✅ **Adaptive Position Sizing** - Dynamic position scaling based on market volatility, trader performance, and portfolio exposure

✅ **Advanced Order Routing** - Multi-venue execution with smart order splitting and optimal fill strategies

✅ **Portfolio Risk Engine** - Real-time correlation analysis, exposure limits, and automated position rebalancing

✅ **Performance Analytics Dashboard** - Comprehensive P&L tracking, trader attribution, and strategy backtesting

✅ **Market Regime Detection** - Automatic adaptation to different market conditions (trending, ranging, volatile)

✅ **Custom Strategy Builder** - Create and deploy custom trading rules with visual workflow editor

For access to the Pro version and enterprise features, contact [@cccciri](https://t.me/cccciri) on Telegram.

---

## ✨ Features

### Core Functionality
- **Real-time Trade Monitoring**: WebSocket-based monitoring of blockchain events (`OrdersFilled`)
- **Automatic Trade Execution**: Copies whale trades with configurable position scaling
- **Dual Trading Modes**:
  - **Engine Mode**: More reliable, waits for block confirmation
  - **Stream Mode**: Faster execution, monitors pending transactions
- **Smart Order Execution**: Tiered execution strategies based on trade size
- **Order Resubmission**: Automatic retry with price escalation for failed orders

### Risk Management
- **Circuit Breaker System**: Multi-layer protection against dangerous market conditions
- **Liquidity Checks**: Validates order book depth before executing trades
- **Consecutive Trade Detection**: Monitors for rapid trade sequences
- **Configurable Safety Thresholds**: Customizable risk parameters via environment variables

### Market Intelligence
- **Market Data Caching**: Efficient caching of market information (neg-risk status, slugs, sport tokens)
- **Sport-Specific Handling**: Special price buffers for tennis (ATP) and soccer (Ligue 1) markets
- **Live Market Detection**: Identifies and handles live markets differently

### Trading Configuration
- **Position Scaling**: Configurable position size as percentage of whale trades
- **Price Buffers**: Adjustable price buffers for different 