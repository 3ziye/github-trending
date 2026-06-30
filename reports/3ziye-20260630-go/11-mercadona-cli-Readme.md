# mercadona

Unofficial, agent-friendly CLI for `tienda.mercadona.es` — search the catalog, read
prices, build a cart, and check out. Single static Go binary, no runtime
deps, structured `--json` output for programmatic/agent use.

> Unofficial. Mercadona has no public API. Bring your own credentials; use at a
> sane request rate. This talks to the same HTTP endpoints the website does.

## Install

**npm** — downloads the prebuilt binary for your platform on install:

```bash
npm install -g @ivorpad/mercadona      # puts `mercadona` on your PATH
npx @ivorpad/mercadona search queso    # …or run without installing
```

**curl** (macOS / Linux):

```bash
curl -fsSL https://raw.githubusercontent.com/ivorpad/mercadona-cli/main/install.sh | sh
```

Override with `MERCADONA_VERSION=v0.1.0` (pin a tag) or `MERCADONA_INSTALL_DIR=/path`
(install location; defaults to `/usr/local/bin`, else `~/.local/bin`).

**Manual** — download a tarball for your OS/arch from the
[releases page](https://github.com/ivorpad/mercadona-cli/releases), extract, and put
`mercadona` on your PATH.

**From source** (Go 1.26+) — clone, then:

```bash
go build -o mercadona ./cmd/mercadona
```

(`go install <module>@latest` isn't wired up yet: the module path is
`github.com/ivorjpc/mercadona`, which doesn't match the repo URL.)

## Commands

### Read core (anonymous — no login)

```bash
mercadona search queso                      # full-text product search
mercadona search --limit 5 --json mayonesa  # structured output for agents
mercadona batch -f lista.txt                 # many terms in ONE request (≈100 items / call)
printf 'queso\ncarne\nmayonesa\n' | mercadona batch -f -
mercadona product 13406                      # detail, price, nutrition (when available)
mercadona categories                         # category tree
mercadona categories --id 112 --json         # one category's products (raw JSON)
```

Common flags: `--wh mad1` (warehouse), `--lang es`, `--json` — and they can go anywhere after the (sub)command, not just up front.
Data goes to **stdout**, logs/errors to **stderr**, exit code `1` on error — friendly to scripts and agents.

### Location (warehouse) — set it from your postal code

```bash
mercadona set-postal 28022   # → resolves to warehouse mad1, saves it as the default
```

Product ids **and prices** are per-warehouse, and online checkout needs the cart's warehouse to
match your delivery address — so pin it to the warehouse that serves your postal code (no login
needed). Precedence: `--wh` flag > `config.toml [defaults]` > built-in `mad1`. `import-har` also
auto-detects and saves the warehouse from your session. (Within a city it varies: `28022 → mad1`,
`28013 → mad3`.)

Example:

```
$ mercadona batch -f lista.txt
• queso            → [51110] Queso rallado mozzarella pizza-Roma Hacendado — 1.60€ (8.000€/kg)
• carne            → [34157] Carne de pimiento choricero Hacendado — 1.55€ (11.072€/kg)
• mayonesa         → [13406] Mayonesa Hacendado — 1.20€ (2.400€/L)
```

### Authenticated: `import-har` (preferred) / `import-curl` / `login`, `whoami`, `cart`, `checkout`

The API authenticates with a **Bearer token** (a SimpleJWT). The first sign-in must happen in a
browser (password login needs a Google reCAPTCHA Enterprise token; Google-account users have no
password at all). After that, the **refresh token renews the session headlessly, forever** —
`POST /api/auth/tokens/ {refresh_token}` needs no captcha and rotates the token. Verified.

**Two login methods, one outcome.** However you sign in, the response carries the same durable
`refresh_token`, so the CLI automates identically:

| Method | Endpoint | Request body | Response |
|---|---|---|---|
| Email + password | `POST /api/auth/tokens/` | `{username, password, recaptcha_token}` | `{access_token, customer_id, refresh_token}` |
| Google sign-in | `POST /api/auth/social/google/` | `{id_token, postal_code}` | `{access_token, customer_uuid, refresh_token}` |

**✅ Preferred login method — `import-har`.** One browser login (email *or* Google), then
headless forever. Export a HAR after signing in and let the CLI pull the refresh token out for you:

```bash
# DevTools → Network → ⤓ "Export HAR…"  (after you've logged in, by either method), then:
mercadona import-har --file tienda.mercadona.es.har
mercadona whoami     # confirms it's authenticated
```

`import-har` seeds `refresh_token` into `~/.mercadona/config.toml` (0600) and caches the current
access token + cookie. From then on every `401 token_not_valid` triggers an automatic refresh +
retry — no browser, no captcha, unattended. (It reads only auth *responses* and Bearer/Cookie
*headers*; the password in the request body is never touched.)

Prefer to do it by hand? Write the token yourself — `mercadona set-refresh <token>` (or edit
`~/.mercadona/config.toml`):

```toml
[auth]
refresh_token = "<your refresh token>"   # the durable, headless-renewable credential
[defaults]
warehouse = "mad1"        # or: `mercadona set-postal 