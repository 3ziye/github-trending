# Agent Skills for production-ready Golang projects

AI agent skills are reusable instruction sets that extend your coding assistant with domain-specific expertise, loaded on demand so they don't bloat your context. This repository covers **Go-specific** skills only (language, testing, security, observability, etc.); for dev workflow skills (git conventions, CI/CD, PR reviews) you'll want to add a separate skills plugin.

For generic skills, please visit [cc-skills](https://github.com/samber/cc-skills).

> [!IMPORTANT]
> Bootstrapped with Claude Code by distilling my Go project commits. **Edited, tested, reviewed and reworked by a human**.
>
> **No AI slop here.** AI-made skills are useless.

<img width="1414" height="491" alt="image" src="https://github.com/user-attachments/assets/620b5835-c1ba-4ea9-bf47-2293b58b879e" />

## 🚀 How to use

**Install with [skills](https://skills.sh/) CLI** (universal, works with any [Agent Skills](https://agentskills.io)-compatible tool):

```bash
npx skills add https://github.com/samber/cc-skills-golang --all
# or a single skill:
npx skills add https://github.com/samber/cc-skills-golang --skill golang-performance
```

<!-- prettier-ignore-start -->

<details>
<summary>Claude Code</summary>

```bash
/plugin marketplace add samber/cc
/plugin install cc-skills-golang@samber
```

</details>

<details>
<summary>Openclaw</summary>

Copy skills into the cross-client discovery directory:

```bash
git clone https://github.com/samber/cc-skills-golang.git ~/.openclaw/skills/cc-skills-golang
# or in workspace:
git clone https://github.com/samber/cc-skills-golang.git ~/.openclaw/workspace/skills/cc-skills-golang
```

</details>

<details>
<summary>Gemini CLI</summary>

```bash
gemini extensions install https://github.com/samber/cc-skills-golang
```

Update with `gemini extensions update cc-skills-golang`.

</details>

<details>
<summary>Cursor</summary>

Copy skills into the cross-client discovery directory:

```bash
git clone https://github.com/samber/cc-skills-golang.git  ~/.cursor/skills/cc-skills-golang
```

Cursor auto-discovers skills from `.agents/skills/` and `.cursor/skills/`.

</details>

<details>
<summary>Copilot</summary>

Copy skills into the cross-client discovery directory:

```bash
/plugin install https://github.com/samber/cc-skills-golang
# or
git clone https://github.com/samber/cc-skills-golang.git ~/.copilot/skills/cc-skills-golang
```

Copilot auto-discovers skills from `.copilot/skills/`.

</details>

<details>
<summary>OpenCode</summary>

Copy skills into the cross-client discovery directory:

```bash
git clone https://github.com/samber/cc-skills-golang.git ~/.agents/skills/cc-skills-golang
```

OpenCode auto-discovers skills from `.agents/skills/`, `.opencode/skills/`, and `.claude/skills/`.

</details>

<details>
<summary>Codex (OpenAI)</summary>

Clone into the cross-client discovery path:

```bash
git clone https://github.com/samber/cc-skills-golang.git ~/.agents/skills/cc-skills-golang
```

Codex auto-discovers skills from `~/.agents/skills/` and `.agents/skills/`. Update with `cd ~/.agents/skills/cc-skills-golang && git pull`.

</details>

<details>
<summary>Antigravity</summary>

Clone and symlink into the cross-client discovery path:

```bash
git clone https://github.com/samber/cc-skills-golang.git ~/.antigravity/skills/cc-skills-golang
```

Update with `cd ~/.antigravity/skills/cc-skills-golang && git pull`.

</details>

<!-- prettier-ignore-end -->

## 🧩 Skills

These skills are designed as **atomic, cross-referencing units**. A skill may reference conventions defined in another (e.g. error-handling rules that affect logging live in `golang-error-handling`, not `golang-observability`). Installing only a subset will give you a partial and potentially inconsistent view of the guidelines. For best results, install all general-purpose skills together.

- ⭐️ Recommended
- ✅ Published
- 👷 Work in progress
- ❌ To-do
- ⚡ Command available
- 🧠 Ultrathink automatically
- ⚙️ Overridable (see doc below)
- **Description (tok)**: weight of the `description` field from YAML frontmatter, always loaded into Claude's context for skill triggering
- **SKILL.md (tok)**: weight of the full `SKILL.md` file loaded when the skill triggers
- **Directory (tok)**: weight of all files in the skill directory (SKILL.md + referenced markdown files)

**General purpose:**

<!-- markdownlint-disable table-column-style -->

|  | Skill | Flags | Error rate gap | Description (tok) | SKILL.md (tok) | Directory (tok) |
| --- | --- | --- | --- | --- | --- | --- |
| ⭐️ | ✅ `golang-code-style` | ⚡ ⚙️ | -40% | 31 | 2,069 | 2,685 |
| ⭐️ | ✅ `golang-data-structures` | ⚡ | -39% | 92 | 2,464 | 6,176 |
| ⭐️ | ✅ `golang-database` | ⚡ ⚙️ | -38% | 112 | 2,725 | 7,248 |
| ⭐️ | ✅ `golang-design-patterns` | ⚡ ⚙️ | -37% | 66 | 2,610 | 9,316 |
| ⭐️ | ✅ `golang-documentation` | ⚡ ⚙️ | -53% | 73 | 2,678 | 10,549 |
| ⭐️ | ✅ `golang-error-handling` | ⚡ ⚙️ | -26% | 90 | 1,520 | 4,394 |
| ⭐️ | 👷 `golang-how-to` |  |