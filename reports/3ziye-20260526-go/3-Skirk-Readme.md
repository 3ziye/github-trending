# Skirk

[فارسی](README.fa.md)

<p align="center">
  <img src="assets/logo.png" alt="Skirk logo" width="160">
</p>

## Donate

If Skirk is useful to you, donations help fund testing infrastructure and
maintenance:

- USDT: `0x5d0b46d821910a5a5503de78e230f9a5e9c52c2f`
- BTC: `bc1q8qsxlp7pzgdqkhu2aj5ss3krnkrecyrh6hedpj`
- ETH: `0x5d0b46d821910a5a5503de78e230f9a5e9c52c2f`
- TON: `UQAO9dEwEVIrrTwoWzCd3Rksb6r3qFSs80Xa7yp3nkO4CPyp`

Skirk is a Go-first transport for restricted-network testing. It exposes a local
SOCKS5 proxy, optional HTTP proxy, or Android VPN frontend, then moves encrypted
TCP stream frames through a Google Drive mailbox folder to an exit
machine with normal internet egress.

Skirk is for lawful, authorized, owned-account and owned-network use only. It is
not affiliated with or endorsed by Google, Google Cloud, Google Drive,
Cloudflare, GitHub, Microsoft, Android, or any other provider. Read
[DISCLAIMER.md](DISCLAIMER.md) before using or redistributing it.

## What You Need

- One exit machine with working internet egress. A VPS is best for uptime, but a
  laptop or home server works while it stays online.
- One Google account for the Drive mailbox.
- One generated `skirk:...` client profile to share with client devices.

Clients do not need Google login, `gcloud`, or a Google Cloud project. The exit
setup creates the Google-backed kit once and prints a one-line client profile.
The same profile can be imported on multiple devices. Each client app creates a
local profile identity, and each connection run gets a fresh run identity, so
Drive replies are routed back to the correct device.

## Quick Start

Install Skirk on the exit machine:

```bash
curl -fsSL https://raw.githubusercontent.com/ShahabSL/Skirk/main/install.sh | sh
skirk version
```

Create a kit and start the exit service:

```bash
skirk setup init --out skirk-kit --reset-google-login
```

Interactive setup first lets you choose easy Skirk OAuth or a personal Google
OAuth project. Easy mode prints a Google device URL plus a short code; open the
URL, enter the code in the browser, approve Drive access, and the terminal
continues.
On Linux, setup also installs/enables `skirk-exit.service` and starts the exit
immediately. Use `--start-exit=false` if you only want the config files.

By default this uses Skirk's built-in OAuth client for the easiest install.
Heavy users can instead use their own Google Cloud OAuth client so Drive API
traffic is charged to their own project quota:

```bash
skirk setup init --out skirk-kit --reset-google-login --oauth-mode personal
```

For personal OAuth, create a Google OAuth client with application type
`Desktop app`, paste its client ID and client secret, approve the printed Google
URL, then paste the redirected localhost URL back into the VPS terminal if the
browser cannot reach it locally.

This is the same operational model used by tools such as rclone: shared OAuth
is convenient, personal OAuth isolates quota.

Check the exit service:

```bash
skirk service status
```

Or run the operator menu and choose setup, service, cleanup, or revoke actions
from one place:

```bash
skirk
```

Uninstall from Linux:

```bash
skirk uninstall --dry-run
skirk uninstall --yes
# or:
curl -fsSL https://raw.githubusercontent.com/ShahabSL/Skirk/main/install.sh | sh -s -- uninstall
```

If you generated a kit with `--start-exit=false`, start the exit manually or
install the service later:

```bash
skirk service install --config skirk-kit/exit.json
skirk service status
```

Copy the one-line text from `skirk-kit/client.skirk` and use it on a client.
From a Linux client:

```bash
curl -fsSL https://raw.githubusercontent.com/ShahabSL/Skirk/main/install.sh | sh

read -r SKIRK_CLIENT_CONFIG
# paste the skirk:... profile, press Enter, then run:
skirk serve-client --config "$SKIRK_CLIENT_CONFIG" --listen 127.0.0.1:18080
```

Test the local SOCKS proxy:

```bash
curl --socks5-hostname 127.0.0.1:18080 http://example.com/
```

Use `socks5h` behavior in apps that support it so DNS resolution happens through
the Skirk exit path.

## Client Options

Linux users can use either the portable desktop app from
`Skirk_linux_x64_portable.zip` or the Go CLI. The Linux desktop app imports the
same one-line `skirk:` profile and supports Proxy mode with SOCKS5 and HTTP
listeners, including trusted-LAN sharing when enabled. Linux VPN mode is also
available when the app is run with root or `CAP_NET_ADMIN` privileges.

Headless servers use the Go CLI:

```bash
skirk serve-client --config client.skirk --listen 127.0.0.1:18080
```

For a long-lived Linux install, set a stable local client ID once. This is not a
secret; it only separates this device from other devices using the same copied
profile:

```bash
skirk serve-client --config client.skirk --listen 127.0.0.1:18080 --client-id my-laptop
```

Windows, Linux, and macOS users should use the portable desktop app from the
release assets. It imports the same one-line `skirk:` profile and starts the
S