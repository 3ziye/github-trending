# make-pages-interactive

A Claude Code skill that turns any folder of static HTML pages into a **live commenting surface**. Highlight text, click an element, leave a note — the comment lands in a local inbox that Claude reads and responds to by editing the page. The page auto-reloads with a walkthrough of what changed.

Originally built for iterating on research artifacts (long HTML reports with plots, tables, explanations) but works for any folder of HTML: docs, design mocks, generated reports, prototype UIs.

![Screenshot of make-pages-interactive in action](screenshot.png)

---

## How it works

```
                  ┌──────────────────┐
   user highlights│   feedback.js    │   POST /feedback
   / clicks  ───▶ │  (in every page) │ ───────────────┐
                  └──────────────────┘                 ▼
                                              ┌────────────────┐
                  ┌──────────────────┐  poll  │   server.py    │
   page reloads ◀─│   feedback.js    │ ◀───── │  (stdlib HTTP) │
   with walkthru  └──────────────────┘history │                │
                                              └───────┬────────┘
                                                      │ append
                                          ┌───────────▼────────────┐
                                          │  feedback/inbox.jsonl  │
                                          └───────────┬────────────┘
                                                      │ Monitor
                                                      ▼
                                          ┌────────────────────────┐
                                          │  Claude (the agent)    │
                                          │  edits HTML, appends   │
                                          │  feedback/history.json │
                                          └────────────────────────┘
```

The skill is **just three pieces**:

| File | Role |
|------|------|
| `lib/feedback.js` | Client library injected into every page. Handles text selection, element selection, comment editor, page-reload walkthrough. |
| `lib/feedback.css` | Styles for the comment UI. |
| `lib/server.py` | ~250-line stdlib-only HTTP server. Serves the page directory, accepts comment POSTs, serves the lib/ files from `/lib/*`. Auto-shuts-down on parent death or 10 min of idle so it doesn't leak processes. |

Plus glue:

| File | Role |
|------|------|
| `SKILL.md` | What Claude Code reads to know when and how to invoke the skill. |
| `scripts/inject.py` | Idempotently injects (or removes) the two `<link>`/`<script>` tags in every `*.html` in a directory. |
| `scripts/update.py` | `git pull --ff-only` inside the skill directory. |

---

## Install

```bash
git clone https://github.com/paraschopra/make-pages-interactive \
  ~/.claude/skills/make-pages-interactive
```

That's it. Claude Code auto-discovers any folder under `~/.claude/skills/` that contains a `SKILL.md`.

Updates are explicit:

```bash
python ~/.claude/skills/make-pages-interactive/scripts/update.py
```

Or just say "update the make-pages-interactive skill" in Claude Code.

---

## Usage

Inside any Claude Code session, say:

> "Make these pages interactive."

(or any of: "make this page interactive", "let me comment on this page", "add feedback to these pages")

Claude will:

1. Inject the feedback library tags into every `*.html` in the current directory.
2. Create `feedback/inbox.jsonl` and `feedback/history.json`.
3. Pick a free port (5050 by default, falls back if taken).
4. Start the server in the background.
5. Tell you the URL to open.
6. Start monitoring the inbox so any comment you leave gets picked up immediately.

Open the URL. Comment away. Claude edits the page in response.

### Removing the feedback layer

To get a clean static copy back (no `/lib/` dependencies in the HTML):

```bash
python ~/.claude/skills/make-pages-interactive/scripts/inject.py ./your-dir --remove
```

Or say "remove the feedback layer from these pages."

---

## How the server shuts down

The server is designed to never leak — three ways it goes away:

1. **Parent-process death** *(automatic, ~5–10 s)*. The server records its parent PID at startup and polls every 5 s. When the parent dies (e.g., you close the Claude Code window that launched it), the kernel reparents the server to PID 1 — the watchdog notices and calls `os._exit(0)`. Skipped if the server was started detached at launch (parent was already PID 1, e.g. `nohup`).

2. **Idle timeout** *(automatic, default 10 min)*. The page polls `/feedback/history.json` every ~4 s, so any open browser tab keeps the server alive. When no client requests have arrived for `--idle-timeout` seconds (default `600`), the server exits. Pass `--idle-timeout 0` to disable.

3. **Manual stop**. Either:
   - Say "stop the feedback server" in your Claude Code session — Claude runs `lsof -ti:5050 | xargs kill` (adjust the port if you used a non-default one).
   - Or hit `Ctrl-C` in the terminal w