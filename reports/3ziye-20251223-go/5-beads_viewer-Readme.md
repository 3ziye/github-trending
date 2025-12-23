# Beads Viewer (bv)

![Release](https://img.shields.io/github/v/release/Dicklesworthstone/beads_viewer?style=for-the-badge&color=bd93f9)
![Go Version](https://img.shields.io/github/go-mod/go-version/Dicklesworthstone/beads_viewer?style=for-the-badge&color=6272a4)
![License](https://img.shields.io/badge/License-MIT-50fa7b?style=for-the-badge)
![Build Status](https://img.shields.io/github/actions/workflow/status/Dicklesworthstone/beads_viewer/ci.yml?style=for-the-badge&logo=github)
[![Coverage](https://codecov.io/gh/Dicklesworthstone/beads_viewer/branch/main/graph/badge.svg)](https://codecov.io/gh/Dicklesworthstone/beads_viewer)

> **The elegant, keyboard-driven terminal interface for the [Beads](https://github.com/steveyegge/beads) issue tracker.**

<div align="center" style="margin: 1.2em 0;">
  <table>
    <tr>
      <td align="center" style="padding: 8px;">
        <img src="screenshots/screenshot_01__main_screen.webp" alt="Main split view" width="420" />
        <div><sub>Main split view: fast list + rich details</sub></div>
      </td>
      <td align="center" style="padding: 8px;">
        <img src="screenshots/screenshot_03__kanban_view.webp" alt="Kanban board" width="420" />
        <div><sub>Kanban board (`b`) for flow at a glance</sub></div>
      </td>
    </tr>
    <tr>
      <td align="center" style="padding: 8px;">
        <img src="screenshots/screenshot_02__insights_view.webp" alt="Insights view" width="420" />
        <div><sub>Insights panel: PageRank, critical path, cycles</sub></div>
      </td>
      <td align="center" style="padding: 8px;">
        <img src="screenshots/screenshot_04__graph_view.webp" alt="Graph view" width="420" />
        <div><sub>Graph view (`g`): navigate the dependency DAG</sub></div>
      </td>
    </tr>
  </table>
</div>

### ⚡ Quick Install

```bash
curl -fsSL "https://raw.githubusercontent.com/Dicklesworthstone/beads_viewer/main/install.sh?$(date +%s)" | bash
```

---

## 💡 TL;DR

`bv` is a high-performance **Terminal User Interface (TUI)** for browsing and managing tasks in projects that use the **Beads** issue tracking system. 

**Why you'd care:**
*   **Speed:** Browse thousands of issues instantly with zero network latency.
*   **Focus:** Stay in your terminal and use Vim-style keys (`j`/`k`) to navigate.
*   **Intelligence:** It visualizes your project as a **dependency graph**, automatically highlighting bottlenecks, cycles, and critical paths that traditional list-based trackers miss.
*   **AI-Ready:** It provides structured, pre-computed insights for AI coding agents, acting as a "brain" for your project's task management.

---

## 📖 The Core Experience

At its heart, `bv` is about **viewing your work nicely**.

### ⚡ Fast, Fluid Browsing
No web page loads, no heavy clients. `bv` starts instantly and lets you fly through your issue backlog using standard Vim keys (`j`/`k`).
*   **Split-View Dashboard:** On wider screens, see your list on the left and full details on the right.
*   **Markdown Rendering:** Issue descriptions, comments, and notes are beautifully rendered with syntax highlighting, headers, and lists.
*   **Instant Filtering:** Zero-latency filtering. Press `o` for Open, `c` for Closed, or `r` for Ready (unblocked) tasks.
*   **Live Reload:** Watches `.beads/beads.jsonl` and refreshes lists, details, and insights automatically when the file changes—no restart needed.

### 🔎 Rich Context
Don't just read the title. `bv` gives you the full picture:
*   **Comments & History:** Scroll through the full conversation history of any task.
*   **Metadata:** Instantly see Assignees, Labels, Priority badges, and creation dates.
*   **Search:** Powerful fuzzy search (`/`) finds issues by ID, title, or content instantly.

### 🎯 Focused Workflows
*   **Kanban Board:** Press `b` to switch to a columnar view (Open, In Progress, Blocked, Closed) to visualize flow.
*   **Visual Graph:** Press `g` to explore the dependency tree visually.
*   **Insights:** Press `i` to see graph metrics and bottlenecks.
*   **History View:** Press `h` to see the timeline of changes, correlating git commits with bead modifications. On wider terminals, enjoy a responsive three-pane layout showing commits, affected beads, and details.
*   **Ultra-Wide Mode:** On large monitors, the list expands to show extra columns like sparklines and label tags.

### 🛠️ Quick Actions
*   **Export:** Press `E` to export all issues to a timestamped Markdown file with Mermaid diagrams.
*   **Graph Export (CLI):** `bv --robot-graph` outputs the dependency graph as JSON, DOT (Graphviz), or Mermaid format. Use `--graph-format=dot` for rendering with Graphviz, or `--graph-root=ID --graph-depth=3` to extract focused subgraphs.
*   **Copy:** Press `C` to copy the selected issue as formatted Markdown to your clipboard.
*   **Edit:** Press `O` to open the `.beads/beads.jsonl` file in your preferred GUI editor.
*   **Time-Travel:** Press `t` to compare against any git revision, or `T` for quick HEAD~5 comp