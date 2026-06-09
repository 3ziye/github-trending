# agentcookie

Your agent runs on a Mac that isn't your daily driver. It needs to act as you on every site you're already logged into and against every API you've already authenticated. agentcookie keeps your second Mac's session state (Chrome cookies, per-CLI bearer tokens, API keys, and the auth blobs your tools persist next to them) in sync with your first Mac's, continuously, encrypted over your Tailscale tailnet, with zero per-site auth ceremony.

OpenClaw, Hermes, or any other agent runtime you point at the second Mac wakes up authenticated, on the web and in the terminal.

## What it looks like

You browse normally on your first Mac. agentcookie watches Chrome's Cookies file (and a parallel per-CLI secrets bus) and ships the diff to your second Mac the moment anything changes. On the second Mac, an agent does its work:

```
$ ssh second-mac 'instacart-pp-cli carts'
  Costco                 slug=costco   cart=757109404 items=5
  Safeway                slug=safeway  cart=3190      items=1

$ ssh second-mac 'ebay-pp-cli auctions "watch" --has-bids --ending-within 1h'
12 active auctions:
  $352   23 bids   1m   Apple Watch Ultra 2 49mm Titanium ...
  $115   26 bids   1m   Gucci 5500M Steel Quartz ...
  ...

$ ssh second-mac 'table-reservation-goat-pp-cli goat "omakase" --location seattle'
{ "results": [ { "name": "Omakase Dinner Series", "network": "tock", ... } ] }
```

No `auth login`. No Keychain prompt. No paste-the-cookie ritual. No re-entering API keys you already configured on your laptop. The agent's sessions were already there when the request hit.

The same is true for browser-driving agents and for any unmodified cookie tool. On a universal sink (the default), agentcookie writes your real Default Chrome profile and opens its Safe Storage key with a single login-password entry at install, so a tool that has never heard of agentcookie, yt-dlp, gallery-dl, a Polymarket CLI, a browser-driving agent, reads your synced, logged-in session with no per-tool setup. Prefer not to touch Chrome at all? Read the plaintext cookies sidecar at `~/.agentcookie/cookies-plain.db`, and the per-CLI secrets under `~/.agentcookie/secrets/<cli>/secrets.env`.

## What this fixes

Logging in twice. Once on your laptop, once again on the Mac your agent lives on. Per site, per CLI, per API key. Forever.

Tools that ship cookies between machines today assume a human is going to click "merge" or unlock a vault or open the destination browser. They were built for switching accounts between two laptops the same person uses. They weren't built for "the agent on the headless Mac mini needs my session in 30 seconds and there's nobody home."

agentcookie is the second pattern. One-way, continuous, unattended replication from the machine you live in to the machine your agents act from. Pairing-derived per-peer keys, blocklist filters on both sides, AES-256-GCM over the Tailscale tailnet's WireGuard channel. The hard parts (macOS Keychain protections, Chrome's App-Bound Encryption, per-CLI auth conventions) are handled.

## How it works

```
laptop                                              second Mac
======                                              ==========

Chrome cookies change      secrets bus change
(fsnotify on Cookies)      (fsnotify on ~/.agentcookie/
  |                         secrets/<cli>/secrets.env,
  |                         or autodiscovered via
  |                         agentcookie.toml manifests)
  |                                |
  +--------------+-----------------+
                 |
                 v
agentcookie source --watch  (decrypt Chrome with Keychain key,
                             filter against blocklist, fold in
                             secrets bus payload)
                 |
                 v
+----- HTTPS over Tailscale (AES-256-GCM, replay-defended) -----+
                                                                |
                                                                v
                                              agentcookie sink (LaunchAgent)
                                                |
                                                | cookie delivery surfaces:
                                                v
                                              1. Chrome's Cookies SQLite (re-encrypted for sink Keychain)
                                              2. Plaintext sidecar at ~/.agentcookie/cookies-plain.db
                                                 (env var: AGENTCOOKIE_PLAIN_COOKIES)
                                              3. Per-CLI adapter fan-out:
                                                   instacart  -> session.json
                                                   airbnb     -> config.toml + cookies.json
                                                   ebay       -> config.toml + cookies.json
                                                   pagliacci  -> config.toml + cookies.json
                                      