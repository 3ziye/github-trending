# Crypto Tax Calc 
[![Twitter Follow](https://img.shields.io/twitter/url/https/twitter.com/cloudposse.svg?style=social&label=Follow%20@bartoMer177)](https://x.com/bartoMerl77)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Donate](https://img.shields.io/badge/Donate-PayPal-black.svg)](https://www.paypal.com/donate?business=)

# Introduction
Crypto Tax Calculator is an open-source model with UIE (Unified Import Engine) support for crypto and personal income tax calculation. It is designed for individuals, accountants, and organizations that require transparency, precision, and compliance across multiple tax jurisdictions. CryptoTaxCalc helps users consolidate all crypto activity — trades, transfers, staking, airdrops, mining rewards, NFT sales, and more — into a clear, tax-compliant report.

# Getting Started
**To use Crypto-Tax-Calc, your machine must meet the following requirements:**
1. Windows/MacOS
2. Git
3. At least 4GB of RAM
4. Python 3.10+ (all versions above are supported)
   
**To install the program on your machine, follow these instructions:**
1. Install the program on your machine.
```bash
git clone https://github.com/Uak0/crypto-tax-calculator
```
2. Setup the program.
```bash
cd crypto-tax-calculator
python setup.py
```
This will install all the required packages and prepare the program to work out of the box.

# Configuration
Edit the crypto_tax_calculator.conf file to configure the program. All the parameters used in the configuration are listed below.

| Parameter | Default Value | Description |
|------------|----------------|--------------|
| **base_currency** | `'USD'` | Main fiat currency used for all calculations and final reports. You can change it to `'EUR'`, `'GBP'`, etc. |
| **timezone** | `'Europe/London'` | Local timezone applied to all transaction timestamps. Must be a valid [IANA timezone string](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). |
| **date_is_day_first** | `True` | Defines date format: `True` → DD/MM/YYYY, `False` → MM/DD/YYYY. |
| **fiat_currencies** | `[USD, EUR, GBP, JPY, AUD]` | List of fiat currencies used in your transaction records. Add or remove as needed based on your data. |
| **crypto_currencies** | `[BTC, ETH, USDT, BNB, SOL, XRP, DOGE]` | List of supported cryptoassets. Most major cryptocurrencies are supported — you can freely extend this list. |
| **price_data_sources.fiat** | `[ExchangeRateAPI, ECB]` | APIs used to fetch historical fiat currency exchange rates for conversion. |
| **price_data_sources.crypto** | `[CoinGecko, CryptoCompare]` | APIs used to retrieve historical cryptocurrency prices. Multiple sources improve accuracy and redundancy. |
| **trade_value_method** | `2` | Determines how the trade value is calculated:<br>• `0` – use buy-side value<br>• `1` – use sell-side value<br>• `2` – use priority value *(recommended)* |
| **fee_handling_mode** | `2` | Defines how transaction fees are treated:<br>• `0` – ignore fees<br>• `1` – treat as expense<br>• `2` – include in cost basis *(recommended)* |
| **transfer_fees_taxable** | `True` | If `True`, transfer fees (e.g. blockchain fees) are treated as taxable disposals. |
| **include_transfers** | `False` | Whether to include wallet-to-wallet transfers in tax calculations. Usually disabled to avoid double counting. |
| **lost_tokens_as_loss** | `True` | If enabled, tokens marked as *lost* or *burned* are considered realized capital losses. |
| **show_empty_wallets** | `False` | Whether to display wallets with zero balance in generated reports. |
| **hide_zero_balances** | `True` | Hides assets with a zero total value from the reports for better readability. |
| **optimize_large_data** | `False` | Enables optimization for large transaction datasets. Increases speed at the cost of higher memory usage. |
| **debug_mode** | `False` | Enables verbose logging for debugging and troubleshooting. Recommended only during testing. |

# Usage
You can run Crypto Tax Calc from the command line or use it interactively.
The program automatically detects the exchange source, converts data, fetches historical prices, and calculates taxes.

**Option 1 — Direct File Processing (Recommended)**

If you have an exchange export (e.g. Binance, Kraken, Coinbase), simply run:

```bash
cryptotaxcalc ./data/binance_2024.csv
```

The program will automatically:

- Detect the source exchange
- Convert the file to a unified internal format
- Fetch historical prices
- Calculate capital gains and personal income taxes
- Generate a PDF/CSV report

Output example:
```bash
Report successfully generated: ./reports/tax_report_2024.pdf
```
**Option 2 — Interactive Mode**

You can also start an interactive session without arguments:
```bash
cryptotaxcalc
```
This will open the CLI interface.


# Supported crypto exchanges and wallets:
- [X] [Binance](https://www.binance.com/)
- [X] [Bitmart](https://bitmart.com/)
- [X] [MEXC](https://mexc.com/)
- [X