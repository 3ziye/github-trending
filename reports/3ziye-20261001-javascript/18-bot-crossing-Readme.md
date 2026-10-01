# Bot Crossing — your agent threads, as a colony

**[botcrossing.com](https://botcrossing.com)**

Every coding-agent thread on this machine is a little bot. They walk out of the ship, claim
a plot for their repo, and build something. When one needs you it stops and holds a `?` over
its head; click it and the thread opens back in whichever harness it came from.

It reads the harness's own files, on your own machine. Nothing is uploaded, there is no
account, and **it never writes to a harness at all** — `data/colony.json`, where the map lives,
is the only file it writes anywhere.

> **Status:** published as-is. I built this for myself and cannot promise to maintain it —
> issues and PRs are welcome but may go unanswered, and forking is an entirely reasonable
> thing to do. [CONTRIBUTING.md](CONTRIBUTING.md) sets out what to expect.

## Run it

```bash
npm install && npm run dev
```

Needs Node 22.13 or newer. `npm test` runs the suite.

`npm run dev` is the whole thing: the API lives inside the Vite dev server, so there is no
second process. For a built version, `npm start` (build + serve) or `npm run serve` if
`dist/` already exists. Binds to `127.0.0.1` by default, and answers only its own page — see
[Keeping it local](#keeping-it-local).

**macOS, Linux and Windows.** Opening a thread, revealing a folder and starting a new session
all go through a `harness://` deep link handed to the OS opener — `open(1)` on macOS,
`xdg-open` on Linux, ShellExecute on Windows. The scanning half was portable already. On Linux,
where a desktop app often is not installed, the scheme is checked first and a terminal running
the harness's own CLI opens instead when nothing answers it.
A setting, *Open threads in*, makes the terminal the first choice rather than the fallback, on all three.

## Which harnesses work

A **harness** is whatever actually runs your threads. Bot Crossing reads each one's local
session files through a small adapter, so support is per-harness and mostly a matter of
somebody writing that adapter.

| Harness | Status |
| --- | --- |
| **[Claude Code](https://claude.com/claude-code)** (Anthropic) | ✅ **Supported** — desktop app and CLI, including worktrees and live-process detection |
| **[Codex](https://developers.openai.com/codex/cli)** (OpenAI) | ✅ **Supported** — desktop, VS Code and CLI sessions, opened through `codex://` |
| **[OpenCode](https://opencode.ai)** | ✅ **Supported** — top-level sessions from its own store; no per-thread link to open |
| **[Antigravity CLI](https://antigravity.google)** (Google) | ✅ **Supported** — transcripts, opened through `antigravity://`. The successor to Gemini CLI, which Google stopped serving individual accounts on 18 June 2026 |
| **[Cursor](https://cursor.com)** (Anysphere) | ✅ **Supported** — agent transcripts; the composer/sidebar threads are not read yet |
| **[Hermes](https://github.com/opsmason/hermes)** | ✅ **Supported** — sessions per pilot profile. Lives in the terminal and chat apps, so there is no link to open |
| **[Kilo Code](https://kilocode.ai)** | ✅ **Supported** — top-level sessions; a thread opens as its repo folder in VS Code |
| [Amp](https://ampcode.com) (Sourcegraph) | ⬜ Not yet |
| [Aider](https://aider.chat) | ⬜ Not yet |
| [Goose](https://block.github.io/goose/) (Block) | ⬜ Not yet |
| [Qwen Code](https://github.com/QwenLM/qwen-code) (Alibaba) | ⬜ Not yet |
| [Amazon Q Developer CLI](https://aws.amazon.com/q/developer/) | ⬜ Not yet |

Every harness that is installed shows up at once — the colony is the union of all of them, and
a bot carries the name of the harness it belongs to.

### Adding one

One new file in `server/harnesses/`, one line in its `index.mjs`, and nothing else. The
interface is small and written down in full, along with the thread shape, the ground rules,
and how to find where a given harness keeps its sessions:

**→ [`server/harnesses/README.md`](server/harnesses/README.md)**

If you add one, a PR is very welcome — see [CONTRIBUTING.md](CONTRIBUTING.md) first, which is
honest about how much support I can offer. If landing it means editing the scanner or anything
under `src/`, please mention that: it means the seam needs widening, and I would rather fix that
than have you work around it.

## What you are looking at

| In the colony | In your threads |
| --- | --- |
| One hex zone | One repo. Bigger repos claim more tiles — one per seven threads, grown as a contiguous blob from the middle outward. A zone stays where it is: see below |
| One bot + one building | One session |
| A bot with no building of its own | An errand that session has out right now — a subagent |
| How finished a building looks | How large its transcript is, on a log scale |
| Scaffolding | Somebody is at that site right now |
| Walking out of the ship | A thread that just appeared |
| Walking back into the ship | You archived it |

### A zone stays where it is

The map is only useful if you can learn it, so the layout is *sticky*. The previous
arrangeme