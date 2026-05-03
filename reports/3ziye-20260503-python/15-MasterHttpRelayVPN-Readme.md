# MasterHttpRelayVPN

[![GitHub](https://img.shields.io/badge/GitHub-MasterHttpRelayVPN-blue?logo=github)](https://github.com/masterking32/MasterHttpRelayVPN)

**[🇮🇷 راهنمای فارسی (Persian)](README_FA.md)**

A free tool that lets you access the internet freely by hiding your traffic behind trusted websites like Google. No VPS or server needed — just a free Google account.

> **How it works in simple terms:** Your browser talks to this tool on your computer. This tool disguises your traffic to look like normal Google traffic. The firewall/filter sees "google.com" and lets it pass. Behind the scenes, a free Google Apps Script relay fetches the real website for you.

---

## Announcement and Support Channel 📢

For the latest news, releases, and project updates, follow our Telegram channel: [Telegram Channel](https://t.me/masterdnsvpn)

---

### If you like this project, please support it by starring it on GitHub (⭐). It helps the project get discovered.

---

### Optional Financial Support 💸

- TON network:

`masterking32.ton`

- EVM-compatible networks (ETH and compatible chains):

`0x517f07305D6ED781A089322B6cD93d1461bF8652`

- TRC20 network (TRON):

`TLApdY8APWkFHHoxebxGY8JhMeChiETqFH`

Every contribution and every piece of feedback is appreciated. Support directly helps ongoing development and improvement.

---

## Disclaimer

MasterHttpRelayVPN is provided for educational, testing, and research purposes only.

- **Provided without warranty:** This software is provided "AS IS", without express or implied warranty, including merchantability, fitness for a particular purpose, and non-infringement.
- **Limitation of liability:** The developers and contributors are not responsible for any direct, indirect, incidental, consequential, or other damages resulting from the use of this project or the inability to use it.
- **User responsibility:** Running this project outside controlled test environments may affect networks, accounts, proxies, certificates, or connected systems. You are solely responsible for installation, configuration, and use.
- **Legal compliance:** You are responsible for complying with all local, national, and international laws and regulations before using this software.
- **Google services compliance:** If you use Google Apps Script or other Google services with this project, you are responsible for complying with Google's Terms of Service, acceptable use rules, quotas, and platform policies. Misuse may lead to suspension or termination of your Google account or deployments.
- **License terms:** Use, copying, distribution, and modification of this software are governed by the repository license. Any use outside those terms is prohibited.

---

## How It Works

```
Browser -> Local Proxy -> Google/CDN front -> Your relay -> Target website
             |
             +-> shows google.com to the network filter
```

In normal use, the browser sends traffic to the proxy running on your computer.
The proxy sends that traffic through Google-facing infrastructure so the network only sees an allowed domain such as `www.google.com`.
Your deployed relay then fetches the real website and sends the response back through the same path.

This means the filter sees normal-looking Google traffic, while the actual destination stays hidden inside the relay request.

---

## Quick Start (Recommended)

One command sets up a virtualenv, installs dependencies, launches an interactive
config wizard, and starts the proxy.

**Windows:**
```cmd
git clone https://github.com/masterking32/MasterHttpRelayVPN.git
cd MasterHttpRelayVPN
start.bat
```

**Linux / macOS:**
```bash
git clone https://github.com/masterking32/MasterHttpRelayVPN.git
cd MasterHttpRelayVPN
chmod +x start.sh
./start.sh
```

The first time it runs, the wizard asks for your Google Apps Script Deployment ID
and generates a strong random password for you. Follow the Apps Script deployment
instructions in **Step 2** below before running the wizard so you have a
Deployment ID ready.

## Project Structure

- `src/core/` shared modules (config constants, logging, cert install, LAN, scanner)
- `src/proxy/` local proxy runtime (HTTP/SOCKS, MITM, proxy helpers)
- `src/relay/` Apps Script relay runtime (relay engine, parsing, H2, helpers)
- `apps_script/` deployable edge/runtime scripts
- `docs/exit-node/` exit-node deployment guides

After it's running, jump to **Step 5** (browser proxy) and **Step 6** (CA
certificate).

---

## Step-by-Step Setup Guide (Manual)

### Step 1: Download This Project

```bash
git clone https://github.com/masterking32/MasterHttpRelayVPN.git
cd MasterHttpRelayVPN
pip install -r requirements.txt
```

> **Can't reach PyPI directly?** Use this mirror instead:
> ```bash
> pip install -r requirements.txt -i https://mirror-pypi.runflare.com/simple/ --trusted-host mirror-pypi.runflare.com
> ```

Or download the ZIP from [GitHub](https://github.com/masterking32/MasterHttpRelayVPN) and extract it.

### Step 2: Set Up the Google Relay (Code.gs)
