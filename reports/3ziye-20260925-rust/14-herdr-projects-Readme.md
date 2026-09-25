<p align="center"><img src="https://img.shields.io/badge/Herdr%20Projects-Projects%20for%20Herdr-2ea44f?style=flat-square&labelColor=24292f" alt="Herdr Projects | Projects for Herdr" /></p>

<h3 align="center">Run a whole project across your coding agents without handing each one its task or keeping track of who is doing what</h3>

<p align="center">Herdr Projects lets you run a larger piece of work in <a href="https://herdr.dev">Herdr</a> when one agent isn't enough and managing five by hand is a job in itself. You talk to one coordinator agent. It starts a separate agent for each task on its own branch, gives every one of them the same goal, instructions and memory, and Herdr's own sidebar shows you which threads need you, which are ready for review and which are still working.</p>

<p align="center"><a href="https://github.com/eliasstravik/herdr-projects/blob/main/assets/herdr-projects-launch.mp4"><img src="assets/herdr-projects-launch.webp" width="88%" alt="Animation: you tell a coordinator what you want, it starts three threads that each work on their own branch, and an overview groups them as ready for review, waiting on you, and working" /></a></p>

<p align="center"><a href="https://github.com/eliasstravik/herdr-projects/blob/main/docs/getting-started.md"><img src="assets/buttons/open-your-first-project.svg" alt="Open your first project" /></a></p>

<p align="center"><sub>✓&nbsp;Free,&nbsp;MIT&nbsp;licensed &nbsp; ✓&nbsp;Runs&nbsp;on&nbsp;your&nbsp;machines,&nbsp;no&nbsp;hosted&nbsp;service &nbsp; ✓&nbsp;macOS&nbsp;and&nbsp;Linux,&nbsp;Herdr&nbsp;0.9.1+</sub></p>

<br />

## Keep one conversation going while the work happens in parallel

The coordinator never does the work itself, so it's always free to answer you. Each task runs in its own thread: a separate agent in its own git worktree and branch, or in its own folder when there's no repository. You read reports and answer the threads that need you instead of briefing every agent yourself.

## Choose between briefing each agent by hand, one long agent session, a cloud projects product, or a coordinator in Herdr

| | **Herdr Projects** | Briefing agents by hand | One long agent session | Cloud projects products |
|---|:---:|:---:|:---:|:---:|
| **No extra software fee** | ✅ | ✅ | ✅ | ❌ |
| **Parallel tasks on separate branches** | ✅ | ✅ | ❌ | ✅ |
| **Same instructions and memory for every task** | ✅ | ❌ | ✅ | ✅ |
| **One conversation that stays free to answer** | ✅ | ❌ | ❌ | ✅ |
| **Threads grouped by what needs you** | ✅ | ❌ | ❌ | ✅ |
| **Runs on your own machines** | ✅ | ✅ | ✅ | ❌ |
| **Adopts an agent pane you already started** | ✅ | ✅ | ❌ | ❌ |
| **Works with the agent CLI you already use** | ✅ | ✅ | ✅ | ❌ |
| **Runs with no machine of yours switched on** | ❌ | ❌ | ❌ | ✅ |

Keep your attention on decisions. Herdr Projects starts and tracks the threads, your agents do the work, and you choose what to review, answer, or merge.

## Tell the coordinator what you want. See which thread needs you in the sidebar.

### 📈 See every thread at a glance

Each thread's sidebar row shows its id and title, a state line (`needs you · ~55%` in red, `review · PR #4` in yellow, `working · ~40%`) and the agent's own activity. Each project's row says `2 need you · 3 working`, the tab bar says `projects: 2 need you`, and the agent list is sorted with what needs you first. `prefix+a` opens one popup with threads, tasks, inbox, routines and settings, where every thread's own list of next steps is a number key away.

### ⚡ Stop briefing every agent yourself

Say what you want once. The coordinator proposes threads and waits for your go-ahead, then each thread starts from a brief with the project's goal, your standing instructions, the project's memory and its task, on the agent you pick (Claude Code, Codex, OpenCode or any other kind Herdr runs). Lessons a thread reports under `## Remember` flow back into memory for the next one.

### 💬 Know when a thread needs an answer

Agents report their own progress, so a thread that asked you something shows `needs you` even when it looks idle, and you get a notification that names the project and the thread. A background ticker follows pull requests: failing checks and review comments go back to the thread to fix, and a merged pull request resolves the thread and removes its worktree and branch once its agent has finished (it may still be tagging or deploying).

## Open your first project in three steps

<table>
<tr>
<td align="center" valign="top" width="33%"><h3>1️⃣</h3><b>Install and configure</b><br /><sub>Run <code>herdr plugin install eliasstravik/herdr-projects</code>, then <code>herdr-projects configure</code> once for the sidebar rows, the popup key, the progress hooks and the <code>/autoproject</code> skill.</sub></td>
<td align="center" valign="top" width="33%"><h3>2️⃣</h3><b>Create and open a project</b><br /><sub>Run <code>herdr plugin action invoke new --plugin herdr-projects</code>, or <code>herdr-projects new "B