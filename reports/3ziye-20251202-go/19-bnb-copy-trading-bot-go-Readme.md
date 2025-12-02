# BSC Copy Trading Bot (Go)

A Binance Smart Chain (BSC) copy trading bot built in Go that monitors swap transactions from a master wallet on PancakeSwap and automatically replicates them on your follower wallet.

## Features

- ✅ Real-time monitoring of BSC transactions
- ✅ Automatic detection of PancakeSwap swaps from master wallet
- ✅ Configurable copy percentage (e.g., copy 50% or 100% of trade size)
- ✅ Support for multiple token pairs
- ✅ Testnet support for safe testing
- ✅ Graceful shutdown handling
- ✅ Comprehensive logging

## Prerequisites

- Go 1.21 or higher
- BSC wallet with BNB for gas fees
- Access to BSC node (public RPC or your own node)
- Basic understanding of DeFi and smart contracts

## Contact Me

If you have any question or something, feel free to reach out me anytime.
<br>
#### 🌹 You're always welcome 🌹

Telegram: [@crypmancer](https://t.me/cryp_mancer) <br>

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/crypmancer/bnb-copy-trading-bot-go
   cd bnb-copy-trading-bot-go
   ```

2. **Install dependencies**
   ```bash
   go mod download
   ```

3. **Configure environment variables**
   
   Copy the example environment file:
   ```bash
   cp env.example .env
   ```
   
   Edit `.env` and configure:
   ```
   BSC_NODE_URL=https://bsc-dataseed1.binance.org
   MASTER_WALLET_ADDRESS=0x...
   FOLLOWER_PRIVATE_KEY=0x...
   COPY_PERCENTAGE=100
   TESTNET=false
   ```

4. **Get BSC Node Access**
   
   You have several options:
   - **Public RPC**: Use free public endpoints (may have rate limits)
     - Mainnet: `https://bsc-dataseed1.binance.org`
     - Testnet: `https://data-seed-prebsc-1-s1.binance.org:8545`
   - **Infura/Alchemy**: Get a dedicated endpoint for better reliability
   - **Your own node**: Run a BSC node for maximum control

5. **Prepare Your Wallet**
   
   - Export your private key from MetaMask or your wallet
   - Ensure your follower wallet has BNB for gas fees
   - **NEVER share your private key** - keep it secure!

## Usage

### Running the Bot

```bash
go run main.go
```

Or build and run:

```bash
go build -o bsc-copy-trading-bot
./bsc-copy-trading-bot
```

### Configuration Options

- `BSC_NODE_URL`: BSC mainnet node URL
- `BSC_TESTNET_URL`: BSC testnet node URL (if using testnet)
- `TESTNET`: Set to `true` to use testnet
- `MASTER_WALLET_ADDRESS`: Address of the wallet you want to copy trades from
- `FOLLOWER_PRIVATE_KEY`: Your wallet's private key (starts with 0x)
- `COPY_PERCENTAGE`: Percentage of trade size to copy (100 = copy full size)
- `TOKEN_ADDRESSES`: Optional comma-separated list of token addresses to monitor
- `ROUTER_ADDRESS`: PancakeSwap router address
- `WBNB_ADDRESS`: Wrapped BNB token address
- `GAS_PRICE_GWEI`: Gas price in Gwei (default: 5)
- `GAS_LIMIT`: Gas limit for transactions (default: 300000)

## How It Works

1. **Connection**: The bot connects to a BSC node via JSON-RPC

2. **Block Scanning**: Every 3 seconds, the bot scans new blocks for transactions

3. **Transaction Detection**: When a transaction from the master wallet to PancakeSwap router is detected:
   - The bot analyzes the transaction
   - Extracts swap parameters (amounts, tokens, paths)
   - Calculates the copy amount based on percentage

4. **Trade Replication**: The bot executes the same swap on your follower wallet with the adjusted amount

5. **Logging**: All transactions and errors are logged for monitoring

## Security Considerations

⚠️ **CRITICAL SECURITY WARNINGS**:

- **Never share your private key** or commit it to version control
- **Use a dedicated wallet** for copy trading (not your main wallet)
- Start with **small amounts** and test thoroughly
- Use **testnet** mode first to verify everything works
- Ensure your wallet has **sufficient BNB** for gas fees
- Monitor the bot regularly, especially in the beginning
- Be aware of **slippage** and **front-running** risks
- The bot currently monitors public transactions - advanced traders may use private transactions

## Limitations

- Currently scans blocks sequentially (may miss fast transactions)
- Requires manual token approval before first swap of each token
- No slippage protection built-in
- No automatic token approval (needs to be done manually or added)
- Monitoring public transactions only (private transactions won't be detected)

## Future Enhancements

- WebSocket subscriptions for real-time event monitoring
- Automatic token approval before swaps
- Slippage protection and price impact checks
- Multiple master wallet support
- Database logging of all trades
- Web dashboard for monitoring
- Support for limit orders
- MEV protection

## Troubleshooting

### "Failed to connect to BSC node"
- Check your `BSC_NODE_URL` is correct
- Verify you have internet connection
- Try a different public RPC endpoint
- Consider using Infura/Alchemy for more reliable connection

### "Invalid private key"
- Ensure your private key starts with `0x`
- Verify the key is correct (no extra spaces)
- 