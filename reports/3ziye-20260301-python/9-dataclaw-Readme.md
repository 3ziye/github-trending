# DataClaw

> **This is a performance art project.** Anthropic built their models on the world's freely shared information, then introduced increasingly [dystopian data policies](https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks) to stop anyone else from doing the same with their data — pulling up the ladder behind them. DataClaw lets you throw the ladder back down. The dataset it produces is yours to share.

Turn your Claude Code, Codex, Gemini CLI, OpenCode, and OpenClaw conversation history into structured data and publish it to Hugging Face with a single command. DataClaw parses session logs, redacts secrets and PII, and uploads the result as a ready-to-use dataset.

![DataClaw](dataclaw.jpeg)

Every export is tagged **`dataclaw`** on Hugging Face. Together, they may someday form a growing [distributed dataset](https://huggingface.co/datasets?other=dataclaw) of real-world human-AI coding collaboration.

## Give this to your agent

Paste this into Claude Code, Codex, Gemini CLI, OpenCode, OpenClaw, or any coding agent:

```
Help me export my Claude Code, Codex, Gemini CLI, OpenCode, and OpenClaw conversation history to Hugging Face using DataClaw.
Install it, set up the skill, then walk me through the process.

STEP 1 — INSTALL
  pip install dataclaw
  If that fails: git clone https://github.com/banodoco/dataclaw.git /tmp/dataclaw && pip install /tmp/dataclaw
  If that also fails, ask the user where the source is.

STEP 2 — INSTALL SKILL
  dataclaw update-skill claude

STEP 3 — START
  dataclaw prep
  Every dataclaw command outputs next_steps in its JSON — follow them through the entire flow.

STEP 3A — CHOOSE SOURCE SCOPE (REQUIRED BEFORE EXPORT)
  Ask the user explicitly: Claude Code, Codex, Gemini CLI, OpenCode, OpenClaw, or all?
  dataclaw config --source "claude|codex|gemini|opencode|openclaw|all"
  Do not export until source scope is explicitly confirmed.

STEP 3B — PRESENT ALL FOLDERS (REQUIRED BEFORE EXPORT)
  dataclaw list --source "claude|codex|gemini|opencode|openclaw|all"
  Send the FULL project/folder list to the user in a message (name, source, sessions, size, excluded).
  Ask which projects to exclude.
  dataclaw config --exclude "project1,project2" OR dataclaw config --confirm-projects
  Do not export until folder selection is explicitly confirmed.

STEP 4 — REVIEW + CONFIRM (REQUIRED BEFORE PUSH)
  dataclaw export --no-push --output /tmp/dataclaw_export.jsonl
  Review PII findings and apply excludes/redactions as needed.
  Full name is requested for an exact-name privacy scan against the export.
  If the user declines sharing full name, use --skip-full-name-scan and attest the skip reason.
  dataclaw confirm --full-name "THEIR FULL NAME" --attest-full-name "..." --attest-sensitive "..." --attest-manual-scan "..."

STEP 5 — PUBLISH (ONLY AFTER EXPLICIT USER APPROVAL)
  dataclaw export --publish-attestation "User explicitly approved publishing to Hugging Face."
  Never publish unless the user explicitly says yes.

IF ANY COMMAND FAILS DUE TO A SKIPPED STEP:
  Restate the 6-step checklist above and resume from the blocked step (do not skip ahead).

IMPORTANT: Never run bare `huggingface-cli login` — always use --token.
IMPORTANT: Always export with --no-push first and review for PII before publishing.
```

<details>
<summary><b>Manual usage (without an agent)</b></summary>

### Quick start

```bash
pip install dataclaw
huggingface-cli login --token YOUR_TOKEN

# See your projects
dataclaw prep
dataclaw config --source all  # REQUIRED: choose claude, codex, gemini, opencode, openclaw, or all
dataclaw list --source all  # Present full list and confirm folder scope before export

# Configure
dataclaw config --repo username/my-personal-codex-data
dataclaw config --exclude "personal-stuff,scratch"
dataclaw config --redact-usernames "my_github_handle,my_discord_name"
dataclaw config --redact "my-domain.com,my-secret-project"

# Export locally first
dataclaw export --no-push

# Review and confirm
dataclaw confirm \
  --full-name "YOUR FULL NAME" \
  --attest-full-name "Asked for full name and scanned export for YOUR FULL NAME." \
  --attest-sensitive "Asked about company/client/internal names and private URLs; none found or redactions updated." \
  --attest-manual-scan "Manually scanned 20 sessions across beginning/middle/end and reviewed findings."

# Optional if user declines sharing full name
dataclaw confirm \
  --skip-full-name-scan \
  --attest-full-name "User declined to share full name; skipped exact-name scan." \
  --attest-sensitive "Asked about company/client/internal names and private URLs; none found or redactions updated." \
  --attest-manual-scan "Manually scanned 20 sessions across beginning/middle/end and reviewed findings."

# Push
dataclaw export --publish-attestation "User explicitly approved publishing to Hugging Face."
```

### Commands

| Command | Description |
|---------|-------------|
| `dataclaw status` | Show current stage and next steps (JSON