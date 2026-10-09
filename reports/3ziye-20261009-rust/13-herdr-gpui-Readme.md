<p align="center">
  <img src="assets/icons/herdr-ui-icon-badge.png" alt="Herdr ram on a simple ivory tile with a red notification badge showing 1" width="176" height="176">
</p>

<h1 align="center">Herdr GPUI</h1>

<p align="center">
  <a href="https://github.com/penso/herdr-gpui/actions/workflows/ci.yml"><img src="https://github.com/penso/herdr-gpui/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
</p>

<p align="center">
  <a href="https://github.com/penso/herdr-gpui/releases">Releases</a> ·
  <a href="docs/updating.md">App updates</a> ·
  <a href="crates/herdr-gpui/README.md">GUI scope &amp; configuration</a> ·
  <a href="crates/herdr-gpui/PERFORMANCE.md">Performance report</a> ·
  <a href="AGENTS.md">Contributing</a> ·
  <a href="#star-history">Star history</a>
</p>

A native Rust/GPUI client for macOS, Linux, and Windows, for a
[Herdr](https://herdr.dev/) daemon you installed yourself. It paints the daemon's terminal cells, split panes included, without
running another terminal emulator or wrapping the TUI.

> **Unaffiliated project.** Not affiliated with, endorsed by, or supported by
> Herdr or [herdr.dev](https://herdr.dev/).

## Gallery

<p align="center">
  <img src="docs/screenshots/workspaces.png" alt="Herdr GPUI window: a sidebar with the local host's CPU and memory, a repository with two linked worktrees, and every agent with its status dot; tabs in the title bar; three split panes running Neovim, git log, and cargo test" width="900">
  <br>
  <sub><b>Workspaces, worktrees, and agents in one sidebar.</b> Each agent carries the daemon's status dot (idle, working, or waiting on you), and tabs and splits are painted natively from the daemon's cells.</sub>
</p>

<table>
  <tr>
    <td width="50%" valign="top">
      <img src="docs/screenshots/worktree-popover.png" alt="Right-click popover on a worktree with tiles for New worktree, Fan out, Rename, Teleport, Teleport back, and Close, plus Checkpoints and a red Delete worktree checkout row">
      <br>
      <sub><b>Worktree popover.</b> Right-click a workspace or worktree for a new worktree, fan out, rename, Teleport, checkpoints, close, or delete the checkout.</sub>
    </td>
    <td width="50%" valign="top">
      <img src="docs/screenshots/teleport.png" alt="Teleport dialog listing two saved SSH hosts as destinations for the feat-multi-currency worktree">
      <br>
      <sub><b><a href="crates/herdr-gpui/README.md#teleport">Teleport</a>.</b> Move a worktree to another host with its commits, uncommitted changes, tabs, splits, running programs, and agent sessions.</sub>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <img src="docs/screenshots/review.png" alt="Review tab showing a unified diff of uncommitted changes with syntax colouring, a changed-files list, and two numbered review notes ready to send to Claude">
      <br>
      <sub><b><a href="crates/herdr-gpui/README.md#reviewing-an-agents-changes">Review an agent's changes</a>.</b> Open <b>Review Changes</b> from a tab strip's <b>+</b> menu, click any line to leave a note like a pull request comment, then <b>Send to agent</b>.</sub>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <img src="docs/screenshots/review-split-collapsed.png" alt="The same review side by side with the sidebar collapsed to a narrow rail of workspace and agent icons">
      <br>
      <sub><b>Side-by-side diffs and a collapsed sidebar.</b> Switch the review to side by side, and fold the sidebar to a rail that keeps every workspace and agent one click away.</sub>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <img src="docs/screenshots/browser-annotate.png" alt="Browser tab showing a local page with two numbered annotations, a hovered element outline, and a notes panel with element screenshots and Send to agent">
      <br>
      <sub><b><a href="crates/herdr-gpui/README.md#annotating-a-page">Browser tabs with annotations</a>.</b> An agent opens its page with <code>herdr-gpui browser open</code>; you pick elements or regions, write notes, and send them back to that agent. Listening ports such as <code>:4173</code> appear under their workspace.</sub>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <img src="docs/screenshots/layouts.png" alt="The same sidebar in five layouts side by side: comfortable-rounded, compact, superset, orca, and minimal">
      <br>
      <sub><b>Sidebar layouts.</b> Pick a density or a design of its own from <b>View &gt; Layout</b> or Settings; the choice applies live.</sub>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <img src="docs/screenshots/usage.png" alt="Codex usage panel opened from the status bar, showing the weekly limit left, reserve, reset credits, and balance">
      <br>
      <sub><b><a href="docs/usage-providers.md">Plan usage</a>.</b> The status bar shows the signed-in AI services closest to their limits; click one for the details.</sub>
    </td>
    <td width="50%" valign="top">
      <img src="docs/screenshots/system-load.png" alt="A s