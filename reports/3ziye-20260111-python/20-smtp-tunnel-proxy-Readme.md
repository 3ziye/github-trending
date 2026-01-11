# 📧 SMTP Tunnel Proxy

> **A high-speed covert tunnel that disguises TCP traffic as SMTP email communication to bypass Deep Packet Inspection (DPI) firewalls.**

```
┌─────────────┐      ┌─────────────┐      ┌─────────────┐      ┌──────────────┐
│ Application │─────▶│   Client    │─────▶│   Server    │─────▶│  Internet    │
│  (Browser)  │ TCP  │ SOCKS5:1080 │ SMTP │  Port 587   │ TCP  │              │
│             │◀─────│             │◀─────│             │◀─────│              │
└─────────────┘      └─────────────┘      └─────────────┘      └──────────────┘
                            │                    │
                            │   Looks like       │
                            │   Email Traffic    │
                            ▼                    ▼
                     ┌────────────────────────────────┐
                     │     DPI Firewall               │
                     │  ✅ Sees: Normal SMTP Session  │
                     │  ❌ Cannot see: Tunnel Data    │
                     └────────────────────────────────┘
```

---

## 🎯 Features

| Feature | Description |
|---------|-------------|
| 🔒 **TLS Encryption** | All traffic encrypted with TLS 1.2+ after STARTTLS |
| 🎭 **DPI Evasion** | Initial handshake mimics real SMTP servers (Postfix) |
| ⚡ **High Speed** | Binary streaming protocol after handshake - minimal overhead |
| 👥 **Multi-User** | Per-user secrets, IP whitelists, and logging settings |
| 🔑 **Authentication** | Per-user pre-shared keys with HMAC-SHA256 |
| 🌐 **SOCKS5 Proxy** | Standard proxy interface - works with any application |
| 📡 **Multiplexing** | Multiple connections over single tunnel |
| 🛡️ **IP Whitelist** | Per-user access control by IP address/CIDR |
| 📦 **Easy Install** | One-liner server installation with systemd service |
| 🎁 **Client Packages** | Auto-generated ZIP files for each user |
| 🔄 **Auto-Reconnect** | Client automatically reconnects on connection loss |

> 📚 For in-depth technical details, protocol specifications, and security analysis, see [TECHNICAL.md](TECHNICAL.md).

---

## ⚡ Quick Start

### 📋 Prerequisites

- **Server**: Linux VPS with Python 3.8+, port 587 open
- **Client**: Windows/macOS/Linux with Python 3.8+
- **Domain name**: Required for TLS certificate verification (free options: [DuckDNS](https://www.duckdns.org), [No-IP](https://www.noip.com), [FreeDNS](https://freedns.afraid.org))

---

## 🚀 Server Setup (VPS)

### Step 1️⃣: Get a Domain Name

Get a free domain pointing to your VPS:
- 🦆 **[DuckDNS](https://www.duckdns.org)** - Recommended, simple and free
- 🌐 **[No-IP](https://www.noip.com)** - Free tier available
- 🆓 **[FreeDNS](https://freedns.afraid.org)** - Many domain options

Example: `myserver.duckdns.org` → `203.0.113.50` (your VPS IP)

### Step 2️⃣: Run the Installer

```bash
curl -sSL https://raw.githubusercontent.com/x011/smtp-tunnel-proxy/main/install.sh | sudo bash
```

The installer will:
1. 📥 Download and install everything
2. ❓ Ask for your domain name
3. 🔐 Generate TLS certificates automatically
4. 👤 Offer to create your first user
5. 🔥 Configure firewall
6. 🚀 Start the service

**That's it!** Your server is ready.

### ➕ Add More Users Later

```bash
smtp-tunnel-adduser bob      # Add user + generate client ZIP
smtp-tunnel-listusers        # List all users
smtp-tunnel-deluser bob      # Remove a user
```

### 🔄 Update Server

```bash
smtp-tunnel-update           # Updates code, preserves config/certs/users
```

---

## 💻 Client Setup

### Option A: Easy Way (Recommended)

1. Get your `username.zip` file from the server admin
2. Extract the ZIP file
3. Run the launcher:

| Platform | How to Run |
|----------|------------|
| 🪟 **Windows** | Double-click `start.bat` |
| 🐧 **Linux** | Run `./start.sh` |
| 🍎 **macOS** | Run `./start.sh` |

The launcher will automatically install dependencies and start the client.

✅ You should see:
```
SMTP Tunnel Proxy Client
User: alice

[INFO] Starting SMTP Tunnel...
[INFO] SOCKS5 proxy will be available at 127.0.0.1:1080

Connecting to myserver.duckdns.org:587
Connected - binary mode active
SOCKS5 proxy on 127.0.0.1:1080
```

### Option B: Manual Way

```bash
cd alice
pip install -r requirements.txt
python client.py
```

### Option C: Custom Configuration

```bash
# Download files
scp root@myserver.duckdns.org:/etc/smtp-tunnel/ca.crt .

# Create config.yaml:
cat > config.yaml << EOF
client:
  server_host: "myserver.duckdns.org"
  server_port: 587
  socks_port: 1080
  username: "alice"
  secret: "your-secret-from-admin"
  ca_cert: "ca.crt"
EOF

# Run client
python client.py -c config.yaml
```

---

## 📖 Usage

### 🌐 Configure Your Applications

Set SOCKS5 proxy to: `127.0.0.1:1080`

#### 🦊 Firefox
1. Settings → Network Settings → Settings
2. Manual proxy configuration
3. SOCKS Host: `127.0.0.1`, Port: `1080`
4. Select SOCKS v5
5. ✅ Check "Proxy DNS when using SOCKS v5"

#### 🌐 Chrome
1. Install "Proxy SwitchyOmega" extension
2. Create profile with SOCKS5: `127.0.0.1:1080`

#### 🪟 Wind