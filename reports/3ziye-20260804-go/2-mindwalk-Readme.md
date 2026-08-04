# <img src="assets/logo.svg" alt="" width="30" /> mindwalk

A visualization tool that replays coding-agent sessions on a 3D map of your codebase.

https://github.com/user-attachments/assets/5153481b-3805-45e6-a61f-372250a969eb

## The problem

A session log records what an agent did, but not how it understood the task:
which parts of the repo it treated as relevant, where it explored before it
acted, whether its footprint matched the scope you had in mind. Reading the
raw JSONL line by line doesn't answer any of that.

## The idea

Draw the repository as a night map, and play the session back as light moving
through it: where the agent searched, read, and edited, the map glows —
everything else stays dark. The agent's understanding of the task becomes a
shape you can see at a glance. One Go binary reads Claude Code, Codex, and pi
session logs, fully local; viewing sends nothing anywhere. The one exception
is the optional session evaluation: when you explicitly run it, a summary of
that session (task wording, file paths, event digests) is sent to the model
behind your own `claude` or `codex` CLI — see
[Session evaluation](#session-evaluation).

## Quick start

```sh
curl -fsSL https://raw.githubusercontent.com/cosmtrek/mindwalk/master/scripts/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
mindwalk
```

The installer verifies the binary against `checksums.txt` and installs to
`~/.local/bin` (override with `INSTALL_DIR`; pin a release with `VERSION`).
Windows archives are on [GitHub Releases](https://github.com/cosmtrek/mindwalk/releases).
To build from source: `make setup && make build` → `bin/mindwalk`.

With no arguments, mindwalk scans `~/.claude/projects`, `~/.codex/sessions`,
and `~/.pi/agent/sessions`, serves the UI on a random local port, and opens a
browser:

```text
mindwalk serve [--port N] [--no-open] [--claude-dir DIR] [--codex-dir DIR] [--pi-dir DIR]
mindwalk open [--no-open] <session.jsonl>   open one specific session
mindwalk map [--no-open] <repo>             open a repository map, no session needed
mindwalk build <repo> [-o out]              write the repository citymap JSON
mindwalk trace <session> [-o out]           write the normalized trace JSON
mindwalk analyze <session> [--judge claude|codex] [--model name] [--no-rubric]
                                            evaluate one session (see below)
```

## Reading the picture

- **Tree / Terrain views** — the repo as a radial tree or a treemap plain;
  glow ∝ how deeply and how often a file was touched.
- **Touch states** — each file keeps its deepest touch: seen (moss green),
  read (moonlight blue), edited (warm amber), unvisited (dark). Files the
  session touched that are no longer in the repo linger as wireframe ghosts.
  The HUD folds friction signals — error rate, churned files, edits after the
  last verify — into a review strip.
- **Playback deck** — scrub or play the session over a bucketed histogram of
  the run. Bars sit on a cool/warm spectrum: observation stays cool (search,
  read, exec), mutation glows warm (edit, verify), so editing phases jump out
  at a glance. Restart, speed, and video export fold into the deck's `⋯` menu;
  export records the playback to a `.webm` entirely client-side.
- **Timeline marks** — `◇` context compactions, `○` subagent launches,
  `›` user turns; every mark is a click-to-jump target.
- **Agent lenses** — when a session launched subagents, the HUD carries a
  subagent count and an agents panel: pick a lens to replay any subagent's
  trace on the same map, then step back out to the main trace.
- **Inspector** — click a file to pin its visit history; click a visit row to
  jump the playhead to that moment.
- **Evaluate** — ask a local agent CLI to judge the session's trajectory,
  scored against criteria drafted from your own request; session rows carry
  the evaluation state as a quiet badge. See
  [Session evaluation](#session-evaluation).
- **Repo map** — `mindwalk map <repo>` (or the folder icon in the session
  rail) renders any repository's citymap with no session attached; height
  encodes lines of code instead of attention.

![the same session on the terrain view](assets/screenshot-terrain.png)

![agent lenses over the same session](assets/screenshot-agents.png)

Keyboard: `Space` play/pause · `←`/`→` step (`⇧` ×10) · `Home`/`End` ends ·
`S` speed · `V` view · `E` next edit · `X` next error · `M` next mark ·
`⌘B` session rail.

## Session evaluation

The evaluate panel (and `mindwalk analyze`) asks a local agent CLI to judge
how the session went. A report has two layers:

- **Process dimensions** — exploration, scope, wandering, verification: four
  fixed lenses, the same for every session, so reports stay comparable.
- **Task scorecard** — before scoring, the judge drafts criteria from your
  own request wording: what would count as done for *this* task, grouped per
  task when the session carried several. Each criterion is then scored
  against the session, alongside the dimensi