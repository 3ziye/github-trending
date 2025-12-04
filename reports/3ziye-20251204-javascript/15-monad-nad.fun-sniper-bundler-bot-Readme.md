
# 🚀 NAD.FUN TRADING BOT V2

<div align="center">

```text
███╗   ██╗ █████╗ ██████╗     ███████╗██╗   ██╗███╗   ██╗
████╗  ██║██╔══██╗██╔══██╗    ██╔════╝██║   ██║████╗  ██║
██╔██╗ ██║███████║██║  ██║    █████╗  ██║   ██║██╔██╗ ██║
██║╚██╗██║██╔══██║██║  ██║    ██╔══╝  ██║   ██║██║╚██╗██║
██║ ╚████║██║  ██║██████╔╝    ██║     ╚██████╔╝██║ ╚████║
╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝     ╚═╝      ╚═════╝ ╚═╝  ╚═══╝
                                                         
████████╗██████╗  █████╗ ██████╗ ██╗███╗   ██╗ ██████╗   
╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝   
   ██║   ██████╔╝███████║██║  ██║██║██╔██╗ ██║██║  ███╗  
   ██║   ██████╔╝██╔══██║██║  ██║██║██║╚██╗██║██║   ██║  
   ██║   ██║  ██╗██║  ██║██████╔╝██║██║ ╚████║╚██████╔╝  
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝   
```

**The Ultimate Modular Trading Bot for Nad.fun**

[![License: ISC](https://img.shields.io/badge/License-ISC-blue.svg)](https://opensource.org/licenses/ISC)
[![Node.js](https://img.shields.io/badge/Node.js-v16+-green.svg)](https://nodejs.org/)
[![Ethers.js](https://img.shields.io/badge/Ethers.js-v6-darkblue.svg)](https://docs.ethers.org/)

</div>

---

## ⚡ Overview

**NAD.FUN TRADING BOT V2** is a high-performance, modular trading bot designed for the Nad.fun platform. Whether you're looking to snipe new token launches, manage multiple wallets with a bundler, or execute precision manual trades, this bot has you covered. Built with **Node.js** and **Ethers.js**, it offers speed, reliability, and ease of use through a sleek interactive CLI.

## 🔥 Key Features

### 🎯 **Sniper Mode**
- **Auto Buy New Tokens:** Automatically detect and buy new tokens the moment they hit the chain. Be the first in line!

### 💼 **Bundler Mode**
- **Multi-Wallet Management:** Generate and manage multiple wallets effortlessly.
- **Batch Operations:** Execute buy and sell orders across all your generated wallets simultaneously.
- **Interactive Control:** Full control over bundler actions via the CLI.

### 🛠️ **Manual Trading**
- **Precision Buy/Sell:** Manually execute trades for specific tokens with custom amounts and slippage settings.
- **Sell All Strategy:** Quickly liquidate positions across tokens or wallets with a single command.

### ⚙️ **Advanced Core**
- **Modular Design:** Easily extensible codebase.
- **Robust Error Handling:** Built-in retry mechanisms and error management.
- **Secure Configuration:** Sensitive data managed via `.env`.

---

## 🚀 Getting Started

### Prerequisites
- **Node.js** (v16 or higher)
- **npm** or **yarn**

### Installation

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/Angel7Dev/monad-nad.fun-sniper-bundler-bot.git
    ```

2.  **Install Dependencies**
    ```bash
    npm install
    ```

3.  **Configure Environment**
    Rename `example.env` to `.env` and add your configuration
    

4.  **Run the Bot**
    ```bash
    npm start
    ```

---

## 🎮 Usage Guide

Upon starting the bot, you will be presented with the **Main Menu**:

```text
=================================================
          NAD.FUN TRADING BOT V2                 
=================================================

Select an operation:
1. Manual Buy
2. Manual Sell
3. Sell All (API)
4. Auto Buy New Tokens (Sniper)
5. Bundler Mode (Interactive)
6. Exit
```

### 1. Manual Buy/Sell
Select option `1` or `2` to trade a specific token. You will be prompted to enter the **Token Address**. The bot will use the settings from your `.env` file for amounts and slippage.

### 2. Sniper Mode (Auto Buy)
Select option `4` to start the sniper. The bot will monitor the chain for new token pairs or liquidity events and attempt to buy immediately.

### 3. Bundler Mode
Select option `5` to enter the **Bundler Sub-menu**:
- **Generate Wallets:** Create fresh wallets for bundling.
- **Bundler Buy/Sell:** Execute trades across all loaded wallets.
- **Export:** Save generated wallets to `generated_wallets.txt`.

---

## ⚠️ Disclaimer

**USE AT YOUR OWN RISK.**

Trading cryptocurrencies and using automated bots involves significant risk. This software is provided "as is", without warranty of any kind, express or implied. The authors and contributors are not responsible for any financial losses, damages, or legal consequences resulting from the use of this bot.

- Always test with small amounts first.
- Keep your private keys secure.
- Do not share your `.env` file.

---

<div align="center">

**Happy Trading! 💸**

</div>
