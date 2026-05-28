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

# 2. Install dependencies
npm install

# 3. Run interactive setup (creates config.json and schedules the monthly job)
node setup.js

# 4. Run manually anytime
./run.sh
```

---

## Setup walkthrough

`node setup.js` guides you through:

| Step | What it does |
|------|-------------|
| **Personal info** | Name, city, state, ZIP, email, phone |
| **Aliases** | Past names or variations (e.g. "Steve Doe") |
| **CapSolver key** | For CAPTCHA-protected opt-out forms |
| **One-time accounts** | Creates accounts on sites that require login (stored in `config.json`, gitignored) |
| **iMessage** | Phone number to text the results summary to |
| **Monthly schedule** | Registers a monthly job to run on the 1st at 9am (launchd / systemd / crontab / schtasks - detected automatically) |

**Your personal info never leaves your machine.** `config.json` and `state.json` are both gitignored.

---

## CapSolver (optional but recommended)

Some opt-out forms have reCAPTCHA. Without CapSolver, those sites go to your manual list instead of being handled automatically.

1. Sign up at [capsolver.com](https://capsolver.com) - free, pay-as-you-go
2. Add $1-2 of credits (enough for months of use at ~$0.001/solve)
3. Paste your API key when `setup.js` asks, or add it to `config.json`:

```json
"capsolver": {
  "apiKey": "CAP-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}
```

> **CapSolver is optional.** Without it, CAPTCHA-protected sites are flagged as
> manual and opened in your browser for completion. Pass `--no-capsolver` to skip
> them entirely rather than opening the browser.

---

## Running with Docker

The included `Dockerfile` uses the official Playwright image, so Chromium and
all system dependencies are pre-installed. No Mac required.

```bash
# Build the image (once)
docker build -t auto-identity-remove .

# Dry-run (no opt-out forms submitted, no network calls)
docker run --rm \
  -v $(pwd)/config.json:/app/config.json \
  -v $(pwd)/state.json:/app/state.json \
  auto-identity-remove node watcher.js --dry-run

# Full run
docker run --rm \
  -v $(pwd)/config.json:/app/config.json \
  -v $(pwd)/state.json:/app/state.json \
  auto-identity-remove
```

**Persistent state:** mount `state.json` so completed opt-outs are remembered
between container runs. If the file does not exist yet, create an empty one
first: `echo '{}' > state.json`.

### Webhook notifications (any OS)

When running headless or in Docker you won't have iMessage or a desktop - use
a webhook instead. Set `notify.webhook` in `config.json` to any ntfy.sh,
Slack incoming-webhook, or Discord webhook URL:

```json
"notify": {
  "textTo": "",
  "webhook": "https://ntfy.sh/my-private-channel"
}
```

The tool POSTs `{"text": "<summary>"}` after every run. Works on macOS, Linux,
and Windows - the webhook fires in addition to (not instead of) any platform
notification that is available.

---

## Files

```
auto-identity-remove/
├── setup.js            ← Run once: interactive setup + scheduling
├── watcher.js          ← Main runner
├── brokers.js          ← Broker list with opt-out strategies
├── run.sh              ← Manual trigger
├── config.example.json ← Template (copy → config.json)
├── package.json
├── .gitignore
│
├── config.json         ← YOUR personal info (gitignored, created by setup.js)
├── state.json          ← Opt-out history / skip logic (gitignored)
└── logs/               ← Per-run JSON logs (gitignored)
```

---

## State tracking

`state.json` tracks when each broker was last successfully opted out. The default re-check window is **90 days** - brokers typically re-add your data within that window, so the script re-submits