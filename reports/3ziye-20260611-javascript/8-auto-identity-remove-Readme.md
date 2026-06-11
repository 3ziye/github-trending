# auto-identity-remove

![CI](https://github.com/stephenlthorn/auto-identity-remove/actions/workflows/test.yml/badge.svg)

Automated data broker opt-out runner for macOS, Linux, and Windows. Removes your personal information from **500+ people-search sites and data broker databases** on a monthly schedule - with CAPTCHA solving, persistent state tracking (so completed opt-outs aren't resubmitted every run), and an iMessage notification when done. [**Privacy & data flow ->**](docs/PRIVACY.md)

## What it does

Each month, the script:

1. **Searches** each data broker site for your name + state
2. **Finds your specific listing** (for sites that need a profile URL)
3. **Fills and submits** the opt-out form automatically
4. **Solves CAPTCHAs** via [CapSolver](https://capsolver.com) (AI-powered, ~$0.001/solve)
5. **Skips** brokers you were already removed from recently (90-day re-check window)
6. **Sends you an iMessage** with the results summary
7. **Opens** any sites that require manual action in your browser

Beyond the monthly run, it can also:

- **Score your exposure** - a single 0-100 number with a month-over-month trend (`aidr score`), built from verified removals, search-engine visibility, and breach data
- **Close the loop** - re-verify removals (`aidr verify`), watch search engines for new listings (`aidr serp-watch`), and generate a monthly PDF report (`aidr report`)
- **Add teeth** - send CCPA/GDPR right-to-know requests (`aidr know`) and auto-generate regulator complaints when a broker blows the legal deadline (`aidr complaints`)
- **Protect proactively** - check Have I Been Pwned (`aidr breach`) and walk a credit/identity-freeze checklist (`aidr freeze`)
- **Stay private** - submit from a masked relay email (SimpleLogin), encrypt `config.json` at rest (AES-256-GCM, opt-in via `AIDR_PASSPHRASE`), and detect success/confirmation text in 6 languages
- **Run from a browser** - an optional local web dashboard with a first-run config wizard, live run console, and status board (`aidr dashboard`)
- **Keep coverage fresh** - pull the broker list from the official California (SB 362) and Vermont registries (`aidr update-brokers`), and keep brokers you *want* to stay listed on via an allowlist

---

## Requirements

- Node.js 18+
- macOS, Linux, or Windows (scheduling adapts automatically)
- [Playwright](https://playwright.dev) browsers installed

```bash
npx playwright install chromium
```

---

## Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/stephenlthorn/auto-identity-remove.git
cd auto-identity-remove

# 2. One-command install (checks Node, installs deps + the Chromium browser)
bash install.sh

# 3. Run interactive setup (creates config.json and schedules the monthly job)
./node_modules/.bin/aidr setup

# 4. Preview what it will do - submits nothing
./node_modules/.bin/aidr preview

# 5. Run for real anytime
./node_modules/.bin/aidr run
```

> Tip: run `npm link` (or install globally) so you can type `aidr` directly
> instead of `./node_modules/.bin/aidr`.

### The `aidr` command

`aidr` is a friendly wrapper around the underlying scripts. Every subcommand
maps to an existing entrypoint:

| Command | What it does |
|---------|--------------|
| `aidr setup` | Interactive first-run setup (creates `config.json`, schedules the monthly job) |
| `aidr preview` | Dry-run: fills forms but submits nothing |
| `aidr run` | Runs the opt-out pass for real |
| `aidr verify` | Re-searches brokers and reports whether you still appear |
| `aidr score` | Prints your 0-100 exposure score and its month-over-month trend |
| `aidr report` | Generates the monthly PDF + emails the summary |
| `aidr pending` | Lists brokers awaiting an email-confirmation click |
| `aidr serp` | Scans search engines for where your name still ranks |
| `aidr serp-watch` | Scans and alerts only when your name appears on a NEW domain |
| `aidr breach` | Checks Have I Been Pwned and recommends a credit freeze on high-severity breaches |
| `aidr freeze` | Shows the credit/identity-freeze checklist and its status |
| `aidr complaints` | Generates regulator complaints for brokers past the CCPA/GDPR deadline |
| `aidr know` | Sends CCPA/GDPR right-to-know requests |
| `aidr update-brokers` | Refreshes the broker list from the CA + Vermont registries |
| `aidr list` | Lists configured brokers and their last-known status |
| `aidr doctor` | Self-diagnoses your environment and configuration |
| `aidr dashboard` | Starts the local web dashboard and prints its URL + a one-time login |

Pass extra flags straight through, e.g. `aidr run --only Spokeo` or
`aidr preview --skip BeenVerified`. Run `aidr --help` for the full list.
Every subcommand maps to the equivalent `node watcher.js --<flag>` invocation.

> A native desktop wrapper (Electron/Tauri) is a planned follow-up and is **not**
> included here - this release is clean CLI packaging only.

---

## Setup walkthrough

`node setup.js` guides you through:

| Step | What it does |
|---