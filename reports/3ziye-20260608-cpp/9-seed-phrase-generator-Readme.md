# Seed Phrase Generator (WalletGen) – Crypto Wallet Generator & Balance Finder for Lost Bitcoin (BTC), Ethereum (ETH), BNB, Polygon (MATIC) and EVM Chains & Bitcoin Wallet Recover

**WalletGen** is an open-source, ultra-fast **crypto wallet generator** and **seed phrase brute force tool**. It helps you find and recovery lost or inactive **Bitcoin (BTC)**, **Ethereum (ETH)**, **BNB**, **Polygon (MATIC)**, and other **EVM-compatible wallets** with real-time balance checking and high-performance C++ engine.

<!--
Meta description:
WalletGen is a high-speed, open-source crypto wallet generator and balance finder for Bitcoin, Ethereum, and other EVM-compatible blockchains. It allows brute-force seed phrase testing, wallet generation, and recovery of lost crypto wallets using databases or real-time balance checks.
-->

## Quick Navigation
- [Download WalletGen](#how-to-start)
- [Database Download](#download-and-use-database-for-more-speed)
- [How It Works](#how-it-works)
- [Why WalletGen](#why-walletgen)
- [Features](#features)
- [The Program Found a Wallet - What Next?](#the-program-found-a-wallet--whats-next)
- [Recovery Your Bitcoin Wallet](#recovery-your-bitcoin-wallet)
- [My Finds](#my-finds)
- [FAQ](#-frequently-asked-questions-faq)
- [Build Instructions](#building-the-project)
- [Donate](#donate)

[![platform](https://img.shields.io/badge/platform-Windows%20%7C%20MacOS%20%7C%20Linux%20%7C%20Android-blue)](https://github.com/tony-dev1/wallets-finder/releases/tag/walletgen)
![build](https://img.shields.io/badge/build-passing-brightgreen)
[![x](https://img.shields.io/badge/@tonydevbtc-black.svg?logo=x)](https://x.com/tonydevbtc)

<p align="center">
    <img width="1000" alt="WalletGen wallet generator demo" title="WalletGen wallet generator" height="460" src="/assets/walletgen.webp" />
</p>

<p align="center">
    <img width="1000" alt="WalletGen MacOS wallet generator demo" title="WalletGen wallet generator" height="460" src="/assets/walletgen_macos1.webp" />
</p>

⚠️ **Disclaimer**: WalletGen is a research and educational tool. It is not intended for unauthorized access or malicious activity. Use it responsibly and only with wallets you own or have permission to access.

## How It Works

WalletGen generates wallets using [BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki), [BIP44](https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki), and [Bech32](https://en.bitcoin.it/wiki/Bech32) for Bitcoin, and [Keccak256](https://emn178.github.io/online-tools/keccak_256.html) hashing for EVM-based chains like Ethereum.

The software compares generated addresses against known address databases or checks balances in real-time via public blockchain explorers. 

Wallet Gen is built in C++ and is open-source, allowing anyone to access and modify the code. Compared to Python-based wallet generators, Wallet Gen boasts significantly higher wallet generation speeds, with performance primarily relying on your CPU & GPU.

##  Why WalletGen?

Unlike Python-based brute force tools, **WalletGen** is written in C++ and optimized for multi-threaded CPU and GPU usage, delivering up to **10x faster** performance. Whether you’re exploring lost wallets, verifying private key space, or recovering your own wallet, WalletGen gives you the power to do it efficiently and securely.

## Features

- **Generation of cryptocurrency wallets**: Wallet Gen supports creating single wallets for Bitcoin, Ethereum, BNB, MATIC and other cryptocurrencies.
- **Search for wallets with balance**: Using bruteforce techniques, Wallet Gen allows you to search for existing wallets with balances in both the Bitcoin network and EVMs.
- **Support for various algorithms**: Keccak256 algorithm for EVM wallets and BIP39, BIP44, Bech32 algorithm for Bitcoin are used for wallet generation.
- **Using a database to speed up searches**: Download and use databases to search for balance wallets, speeding up the process tenfold.
- **High speed of operation**: Wallet Gen utilizes the power of the CPU and GPU to achieve the best performance.
- **Recovery your Bitcoin wallet**: WalletGen allows you to recover your bitcoin wallet by seed phrase (mnemonic phrase).

## Supported Blockchains

- Bitcoin (BTC)
- Ethereum (ETH)
- Binance Smart Chain (BNB)
- Any EVM-compatible chain

# Demo

<p align="center">
    <img width="1000" height="460" alt="WalletGen search lost bitcoin wallets on Windows Demo" title="WalletGen search lost bitcoin wallets on Windows" src="/assets/walletgen-demo.gif" />
</p>

<p align="center">
    <img width="1000" height="460" alt="WalletGen search lost bitcoin wallets on MacOS Demo" title="WalletGen search lost bitcoin wallets on MacOS" src="/assets/walletgen_macos2.gif" />
</p>

<p align="center">
    <img width="1000" alt="WalletGen MacOS wallet generator demo" title="WalletGen wallet generator" height="460" src="/assets/walletgen_macos2.webp" />
</p>

