

# Windows Copilot API: a free LLM API powered by Microsoft Copilot

![Windows Copilot API — a free, OpenAI-compatible API for your Microsoft Copilot account](assets/windows-copilot-api-banner.png)

**Using your own Microsoft Copilot account.** No API key, no credits, no paid plan: it turns the free chat at [copilot.microsoft.com](https://copilot.microsoft.com) into an API you can call from code.

You can use it in two ways:

- 🐍 **As a Python library:** just call `client.chat("Hi")`. Supports streaming and multi-turn conversations.
- 🔌 **As a local OpenAI-compatible API:** runs a server at `http://localhost:8000/v1` that speaks the OpenAI format, so the official `openai` SDK (and any OpenAI-compatible app) works as a drop-in, with `localhost` in place of OpenAI.

You sign in once in a browser with your Microsoft **or Google** account; your session is saved and refreshed automatically after that.

> **Unofficial project.** Not affiliated with or endorsed by Microsoft. It automates the consumer Copilot web experience for personal use, so use it responsibly and within Microsoft's terms.

---

## Table of contents

- [Why use this?](#why-use-this)
- [Requirements](#requirements)
- [Setup (2 minutes)](#setup-2-minutes)
- [Run with Docker (optional)](#run-with-docker-optional)
- [Usage 1: In Python (no server)](#usage-1-in-python-no-server)
- [Usage 2: As an OpenAI-compatible server](#usage-2-as-an-openai-compatible-server)
- [Command line](#command-line)
- [Concurrency & stress test](#concurrency--stress-test)
- [Rate limiting](#rate-limiting)
- [Project layout](#project-layout)
- [Notes & limitations](#notes--limitations)
- [Troubleshooting](#troubleshooting)
- [Collaboration & support](#collaboration--support)
- [License](#license)
- [Star History](#star-history)

---

## Why use this?

- **Free:** uses your normal signed-in Copilot, no API billing.
- **Drop-in OpenAI replacement:** point any OpenAI client at `localhost` and it just works.
- **Works everywhere you're signed in:** the signed-in path works even in regions where *anonymous* Copilot is blocked (e.g. India).
- **Streaming + conversations:** token-by-token output and multi-turn threads addressed by `conversation_id`.

---

## Requirements

- **Python 3.9+**
- A **Microsoft account** (the free one you use for Copilot is fine)
- Works on Windows, macOS, and Linux

---

## Setup (2 minutes)

```bash
# 1. Clone the project
git clone <your-repo-url>
cd Windows-Copilot-API
```

**2. Create and activate a virtual environment**

On **macOS / Linux**:

```bash
python3 -m venv venv
source venv/bin/activate
```

On **Windows** (PowerShell):

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

> On Windows you may need to allow script execution once: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`. In `cmd.exe` activate with `venv\Scripts\activate.bat` instead.

**3. Install dependencies and sign in**

```bash
# Install dependencies
pip install -r requirements.txt

# Install the browser Playwright needs (one-time)
playwright install chromium

# Sign in once: a browser opens, log into your Microsoft or Google account
python -m copilot login
```

The browser **closes by itself** once sign-in is detected — you don't need to press Enter or close it manually. After sign-in it sends one short warm-up message that mints the chat token **and** passes Cloudflare's "verify you're human" check in the same step (a brief "finishing setup…" appears, and a tiny throwaway chat lands in your history). If a checkbox shows up, click it in that login window. The steps are logged to `session/login.log` if anything goes wrong. That's it: your session is saved under `session/` (git-ignored, never shared) and reused on every run — so your first request works right away.

> 🛠️ **Run into trouble during setup or your first run?** Head to the [Troubleshooting](#troubleshooting) section, the bundled diagnostic both *fixes* common issues (captcha/clearance) and *logs* a shareable report.

---

## Run with Docker (optional)

Prefer a container? You can run the OpenAI-compatible server in Docker once you've signed in.

> **Sign in on the host first.** The login step above opens a *visible* browser, which can't run inside the headless container — so run `python -m copilot login` on your host to populate `session/`. The container mounts that folder and reuses the Cloudflare clearance earned on the host. It refreshes the chat token headlessly, but it can't earn *fresh* clearance without a visible browser, so when clearance expires (~30 min) it returns a `503` — re-run `python -m copilot login` on the host to refresh `session/`.

```bash
docker compose up --build
# -> Copilot OpenAI-compatible API on http://localhost:8000
```

The [docker-compose.yml](docker-compose.yml) maps port `8000` and bind-mounts your `session/` so the login persists across restarts. Tune `RATE_LIMIT_RPM` / `RATE_LIMIT_BURST` there. To run without Compose, build and pass the same bindings by hand:

``