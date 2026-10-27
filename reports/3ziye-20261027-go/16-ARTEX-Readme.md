<div align="center">

# ARTEX

AI autonomous penetration testing system (Go backend + Next.js frontend)


 Fork of [ARTEX by Autumn-27](https://github.com/Autumn-27) · English translation of the Chinese source · maintained publicly under AGPL-3.0

</div>

---

## Screenshots


| Dashboard (overview / token usage / activity stream) | Task list |
| :---: | :---: |
| ![Dashboard](screenshots/dashboard.png) | ![Tasks](screenshots/tasks.png) |

| Task · execution (sessions / tool calls) | Exploration graph |
| :---: | :---: |
| ![Execution](screenshots/sessions.png) | ![Exploration graph](screenshots/graph.png) |

| Findings | Assets |
| :---: | :---: |
| ![Findings](screenshots/findings.png) | ![Assets](screenshots/assets.png) |

| Asset coverage graph (force-directed layout · tested highlights · node collapse/expand) |
| :---: |
| ![Asset coverage graph](screenshots/assets_test.png) |

| Traffic recording | Human-in-the-loop chat |
| :---: | :---: |
| ![Traffic](screenshots/traffic.png) | ![Chat](screenshots/chat.png) |

| Agent management | LLM configuration |
| :---: | :---: |
| ![Agent](screenshots/agents.png) | ![LLM](screenshots/llm.png) |

| Interception approvals | Backend logs |
| :---: | :---: |
| ![Interception](screenshots/intercept.png) | ![Logs](screenshots/logs.png) |


---

## Approval record details

The global "Approval Records", the in-task "Interception Approvals", and the approval cards in conversations all support expanding to view details. The display structure references the
[AegisHook approval details component](https://github.com/RuoJi6/AegisHook/blob/main/web/src/components/CallDetail.vue), reusing ARTEX's components and theme:


## Traffic capture browser extension

The bundled browser extension (`extension/`) turns your own browsing into agent-visible evidence: log into an authenticated target once (captchas, email OTP and 2FA included), and the captured requests/responses land in ARTEX's traffic store like proxy-recorded traffic, ready to search and bind to findings:

- Load the unpacked extension from `extension/` (Chrome/Edge, Developer Mode → Load unpacked);
- In the popup, set your ARTEX URL and token, then press **Start capture** on the tab you are browsing;
- Use the site normally; text requests/responses are batched to `POST /api/traffic/ingest` (authenticated). Binary bodies (images, fonts) are skipped, bodies are truncated at 256 KiB, batches are capped at 50 entries;
- Press **Stop** when done. Everything stays in your local traffic store.

## Asset sync (ScopeSentry)

Sync asset data directly from [ScopeSentry](https://github.com/Autumn-27/ScopeSentry), avoiding duplicate collection:

- On the "**Asset Sync**" page, enter the ScopeSentry address and API Key to connect the data source;
- Choose the targets and asset types to sync by **project** or **task** (domains / subdomains / IPs / ports / sites / endpoints…);
- One-click import, merged by company asset scope, straight into ARTEX's asset graph for agents to explore.

---

## Installation

> Requires a **PostgreSQL** database; exploration requires an **LLM** (`ANTHROPIC_API_KEY` or `OPENAI_API_KEY`, which can also be configured in the UI).

### Option 1: one-click install script (recommended)

```bash
git clone https://github.com/BaaRai/ARTEX.git
cd ARTEX
./install.sh
```

The script will: detect / auto-install Docker → then let you choose **① all-Docker** or **② local build and run**:

- **① All-Docker**: enter a Postgres password (press Enter for a random one) → auto-writes `.env` → `docker compose up -d`.
- **② Local run**: choose a database (connect to an existing one / start one with Docker) → generates `config.json` → `go` builds the embedded single binary → starts.

Once installed, open **http://localhost:8787** (on first entry, `/setup` sets the admin password).

### Option 2: Docker Compose (manual)

```bash
git clone https://github.com/BaaRai/ARTEX.git
cd ARTEX
cp .env.example .env          # set POSTGRES_PASSWORD, optionally ANTHROPIC_API_KEY
docker compose up -d          # pulls the autumn27/artex image + postgres
# → http://localhost:8787
```

The image already includes common tools (ripgrep/curl/vim/npm/nmap…); `./skills` and `./data` are persisted via bind mounts.

For remote MCP, you can choose `http` (Streamable HTTP) or `sse` (legacy SSE) in system settings.
Legacy SSE servers usually establish the event stream with `GET /sse`, then receive JSON-RPC requests via the
`/message?sessionId=...` returned by the server; when configuring, set the URL to `/sse` and the request header as
`Authorization=Bearer <token>`.

### Option 3: download prebuilt binaries (Releases)

Download the zip for your platform from [Releases](https://github.com/BaaRai/ARTEX/releases); after extracting you get `artex` + `start.sh` (`start.bat` on Windows) + `skills/` + `config.example.json`:

```bash
cp config.example.json config.json   # fill in the database connection
./start.sh                           # → http://localhost:8787