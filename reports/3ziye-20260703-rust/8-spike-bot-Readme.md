# Polymarket Spike Bot

> ## ⚠️ Public demo version — not the production bot
>
> **This repository is the version shared for selling / demonstration.** It does **not** include the real production settings used on the live account, including:
>
> - **Strike time**
> - **Entry point**
> - **Momentum variables**
>
> The constants in this repo are illustrative. Results on [@antsaslyku](https://polymarket.com/@antsaslyku) come from the **full, tuned configuration** — not from this public copy alone.
>
> **Want the complete bot or to collaborate?** Contact on Telegram:
>
> ### [**t.me/antsaslyku**](https://t.me/antsaslyku)

**Repository:** [github.com/ale2348/spike-bot](https://github.com/ale2348/spike-bot) · **Author:** [@ale2348](https://github.com/ale2348)

A **Rust** bot for **Polymarket 5-minute crypto Up/Down** markets — **BTC, ETH, SOL, and XRP**. It watches **Binance** spot prices for momentum, then places a **limit buy** on the matching Polymarket Up or Down token at the **current ask**, holds through resolution, and tracks P/L.

**Live profile using this strategy family:** [**@antsaslyku on Polymarket**](https://polymarket.com/@antsaslyku)

The bot connects to Polymarket Gamma + CLOB APIs, streams live order-book prices, and can run in **simulation mode** (no real orders) or **live mode** with your wallet. Press **Ctrl+C** to stop.

---

## Live proof — buy → redeem cycles

These are real on-chain transactions from [@antsaslyku](https://polymarket.com/@antsaslyku) on Polygon. Each pair shows the same pattern the bot follows: **buy the favorite late in the window → redeem at $1.00 after resolution**.

### Trade 1 — Jun 11, 2026 · ~$0.99 entry

| Step | Time (UTC) | Details | Polygonscan |
|------|------------|---------|-------------|
| **Buy** | 09:30:01 | ~**$67.32** USDC → **68 shares** @ **~$0.99** (late-window favorite) | [View buy tx](https://polygonscan.com/tx/0x6874a18bcd84c18a6e9d5cffd0a94eb0bdc148089a364370eb9120384bc4e21c) |
| **Redeem** | 09:31:03 | Market resolves → shares redeemed for **~$1.00** each | [View redeem tx](https://polygonscan.com/tx/0x17e8fbc7ed8d995c44127da034e487733a43f18c6638cdcba9088a519b11ad63) |

**Approx. gross profit:** ~**$0.68** on ~$67 stake (~**1%**) before fees, in **~62 seconds**.

### Trade 2 — Jun 11, 2026 · ~$0.99 entry

| Step | Time (UTC) | Details | Polygonscan |
|------|------------|---------|-------------|
| **Buy** | 08:55:01 | Buy favorite @ **~$0.98–$0.99** near window end | [View buy tx](https://polygonscan.com/tx/0x7fa58be45dc24afbc8bd135fc6a7147fb548e2c00ad2f5b6100fa7510dd58b45) |
| **Redeem** | 08:55:30 | Resolution redeem **~29s** after buy | [View redeem tx](https://polygonscan.com/tx/0x4edaaa3a6a6d854fe6ec938280ab3cfd34d07f34fcc75c7f4757feccfc9d30dc) |

> **How to read these txs:** The **buy** tx interacts with `Polymarket: CTF Exchange V2` — USDC out, outcome shares in. The **redeem** tx settles winning shares back to USDC at **$1.00** per share when the 5m window resolves. Repeat this across many windows and P/L compounds — see the full history on [polymarket.com/@antsaslyku](https://polymarket.com/@antsaslyku).

### Profile screenshots ([@antsaslyku](https://polymarket.com/@antsaslyku))

Live Polymarket dashboard — portfolio growth and buy/redeem activity on **BTC** and **XRP** 5m markets at **96–99¢**:

![Polymarket profile — past day profit/loss and recent trades](doc/daily_pnl.png)

- Past year P/L: **+$82,537.48**
- Past day P/L: **+$208.04**
- 24h Return: **+3.51%**
- Portfolio Value: **~$3,467**

Trade history includes repeated entries in late-stage crypto prediction markets followed by successful redemptions at settlement.

---

## How it works

Each **5-minute Up/Down** market (BTC, ETH, SOL, XRP) runs for **300 seconds**. The bot streams **Binance** mid-prices and **Polymarket** best asks in real time.

```
Binance price move (lookback window)
        │
        ▼
  Up or Down signal?
        │
        ▼
Limit buy @ current Polymarket ask  ──►  cancel if unfilled after N seconds
        │
        ▼
Hold to resolution  ──►  redeem winning shares @ $1.00
```

1. **Subscribe** to Binance book-ticker feeds for configured symbols
2. **Detect momentum** — price moved up or down by a USD threshold within `lookback_secs`
3. **Buy Up** on upward momentum, **buy Down** on downward momentum
4. **Place a limit order** at the current Polymarket ask (skipped if ask > `max_ask_price`)
5. **Cancel** unfilled orders after `cancel_after_secs`
6. **Track fills and resolution** — wins pay ~$1/share; losses cost the entry notional

| | Typical win | Risk |
|---|-------------|------|
| **Math** | Buy @ ~$0.50–$0.98 → redeem @ **$1.00** if correct side wins | Wrong side → stake lost |
| **Edge** | Momentum + early entry before the crowd | Reversal or no fill → missed or losing trade |

---

## Configuration

Copy [`config.json.example`](config.json.example) to `config.json` and fill in your wallet details. **Never commit `config.json`** — it is gitignored and