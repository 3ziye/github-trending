<p align="center">
  <img src="assets/whitedns-logo.png" alt="WhiteDNS logo" width="220">
</p>

# WhiteDNS 3X-UI Wizard
[Telegram: @whitedns](https://t.me/@whitedns)

WhiteDNS is a Cloudflare-first provisioning wizard for setting up a managed 3x-ui/Xray VPN stack on a VPS. It runs locally, connects to the VPS over SSH, manages Cloudflare DNS and certificates, installs or repairs a Docker-based 3x-ui stack, and generates copyable client import strings.

The wizard focuses on a practical default setup:

- Cloudflare-proxied WebSocket TLS profiles.
- DNS-only direct profiles for protocols Cloudflare proxy cannot handle.
- Server-side Tor exit variants users can import separately.
- A managed 3x-ui Docker stack with PostgreSQL.
- Encrypted local project secrets and repeatable reset/repair flows.

## Quick Start

### 1. Build the binary

```bash
go build -o whitedns ./cmd/whitedns
```

### 2. Run the interactive wizard

```bash
./whitedns
```

The root command opens the menu. Select:

```text
0) Init setup
```

The wizard will ask for:

- Cloudflare account ID.
- Cloudflare API token.
- Domain name.
- VPS IPv4 address.
- SSH host, user, key/passphrase, or password.

### 3. Cloudflare token permissions

Create an Account API token in Cloudflare:

1. Go to `Manage Account > Account API Tokens > Create Token`.
2. Choose the `Edit zone DNS` template.

![Choose the Edit zone DNS token template](assets/tutorial/cloudflare-edit-zone-dns-template.png)

3. Scope it to the owning Cloudflare zone when possible. For subdomain projects such as `team.example.com`, this may be the parent zone `example.com`. Use all domains only when needed.
4. Keep `DNS: Read + Edit`.
5. In `DNS & Zones`, add `Zone: Read` and `Zone Settings: Edit`.

![Cloudflare DNS and Zone permissions](assets/tutorial/cloudflare-dns-zone-permissions.png)

6. In `Cache & Performance`, add `Zone SSL & Certificates: Edit`.

![Cloudflare SSL and Certificates permission](assets/tutorial/cloudflare-ssl-certificates-permission.png)

The final required permissions are:

```text
DNS & Zones / DNS: Read + Edit
DNS & Zones / Zone: Read
DNS & Zones / Zone Settings: Edit
Cache & Performance / Zone SSL & Certificates: Edit
```

Cloudflare API docs may call `Edit` permissions `Write`. WhiteDNS uses the account ID you enter for:

```text
GET /client/v4/accounts/<account-id>/tokens/verify
```

Troubleshooting:

| Error area | Usually means |
| --- | --- |
| Token validation | Wrong token, wrong account ID, expired/disabled token, or incompatible token type. |
| Zone lookup | Missing `Zone: Read` or token is not scoped to the selected domain. |
| DNS or ACME DNS-01 | Missing `DNS: Edit`. |
| ACME connectivity | Local network, DNS, proxy/VPN, firewall, or ISP path cannot reach Let's Encrypt. WhiteDNS retries public certificate issuance from the VPS when this happens. |
| Nameserver delegation | The registrar/domain nameserver settings do not point to Cloudflare. This is not fixed by deleting or adding rows in the Cloudflare DNS records table. |
| SSL mode strict | Missing `Zone Settings: Edit`. |
| Origin CA certificate | Missing `Zone SSL & Certificates: Edit`. |

### 4. What the init flow does

The setup flow:

- Validates the Cloudflare token.
- Detects the Cloudflare zone.
- Creates or updates DNS records.
- Sets Cloudflare SSL mode to `strict`.
- Creates a Cloudflare Origin CA certificate for proxied profiles.
- Issues a public ACME wildcard certificate for DNS-only TLS profiles.
- Installs or repairs managed Docker 3x-ui and PostgreSQL.
- Adds a private Tor sidecar for Tor-profile outbound routing.
- Replaces only WhiteDNS-managed inbounds/outbounds after confirmation.
- Prints and saves client import strings.

## DNS Records

WhiteDNS creates these A records for the selected domain. Replace `<domain>` and `<vps-ip>` with your real values.

| Host | Type | Value | Proxy | Purpose |
| --- | --- | --- | --- | --- |
| `vpn.<domain>` | A | `<vps-ip>` | Proxied | VLESS WS TLS through Cloudflare |
| `trojan.<domain>` | A | `<vps-ip>` | Proxied | VLESS WS TLS on 8443 through Cloudflare |
| `panel.<domain>` | A | `<vps-ip>` | DNS-only | 3x-ui dashboard |
| `direct.<domain>` | A | `<vps-ip>` | DNS-only | Direct VLESS TCP TLS |
| `hy2.<domain>` | A | `<vps-ip>` | DNS-only | Hysteria2 UDP |
| `reality.<domain>` | A | `<vps-ip>` | DNS-only | Reality TCP Vision |
| `ss.<domain>` | A | `<vps-ip>` | DNS-only | Shadowsocks 2022 |
| `tor-vless-ws.<domain>` | A | `<vps-ip>` | DNS-only | VLESS WS routed through Tor |
| `tor-vless-ws-8443.<domain>` | A | `<vps-ip>` | DNS-only | VLESS WS 8443 routed through Tor |
| `tor-hy2.<domain>` | A | `<vps-ip>` | DNS-only | Hysteria2 routed through Tor |
| `tor-direct.<domain>` | A | `<vps-ip>` | DNS-only | Direct VLESS routed through Tor |
| `tor-reality.<domain>` | A | `<vps-ip>` | DNS-only | Reality TCP Vision routed through Tor |
| `tor-ss.<domain>` | A | `<vps-ip>` | DNS-only | Shadowsocks routed through Tor |

ACME also creates temporary TXT reco