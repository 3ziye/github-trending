<p align="center">
  <img src="docs/assets/klaw-logo.png" alt="klaw" width="140" />
</p>

<h1 align="center">klaw</h1>

<p align="center">
  <strong>kubectl for AI Agents</strong>
</p>

<p align="center">
  Enterprise AI agent orchestration. Manage, monitor, and scale your AI workforce.<br/>
  One binary. Deploys in seconds. Scales to hundreds of agents.
</p>

<p align="center">
  <a href="https://klaw.sh/docs">Documentation</a> •
  <a href="#what-is-klaw">What is klaw?</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="#slack-control">Slack Control</a> •
  <a href="#architecture">Architecture</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/license-each::labs-green.svg" alt="License" />
  <img src="https://img.shields.io/badge/go-1.24+-00ADD8.svg" alt="Go Version" />
  <img src="https://img.shields.io/github/stars/klawsh/klaw.sh?style=social" alt="Stars" />
  <a href="https://deepwiki.com/klawsh/klaw.sh"><img src="https://deepwiki.com/badge.svg" alt="Ask DeepWiki"></a>
</p>

---

## What is klaw?

**klaw** is enterprise AI agent orchestration — like kubectl, but for AI agents.

```bash
# See all your agents
$ klaw get agents

NAME              NAMESPACE    STATUS    MODEL              LAST RUN
lead-scorer       sales        running   claude-sonnet-4    2m ago
competitor-watch  research     idle      gpt-4o             1h ago
ticket-handler    support      running   claude-sonnet-4    30s ago
report-gen        analytics    idle      claude-sonnet-4    6h ago

# Check what an agent is doing
$ klaw describe agent lead-scorer

Name:         lead-scorer
Namespace:    sales
Status:       Running
Model:        claude-sonnet-4-20250514
Skills:       crm, web-search
Tools:        hubspot, clearbit, web_fetch
Last Run:     2 minutes ago
Next Run:     in 58 minutes (cron: 0 * * * *)

# View real-time logs
$ klaw logs lead-scorer --follow

[14:32:01] Fetching new leads from HubSpot...
[14:32:03] Found 12 new leads
[14:32:05] Analyzing lead: john@acme.com
[14:32:08] Score: 85/100 (Enterprise, good fit)
[14:32:09] Updated HubSpot lead score
...
```

### Or control everything from Slack

```
You: @klaw status

klaw: 📊 Agent Status
      ├── lead-scorer (sales) — running, 2m ago
      ├── competitor-watch (research) — idle
      ├── ticket-handler (support) — running, 30s ago
      └── report-gen (analytics) — idle

You: @klaw run competitor-watch

klaw: 🚀 Starting competitor-watch...
      Checking competitor.com/pricing...
      Found 2 pricing changes since yesterday.
      Posted summary to #competitive-intel
```

---

## The Problem

You're running AI agents in production:
- **Lead Scorer** — analyzes CRM leads every hour
- **Competitor Watch** — monitors competitor websites daily
- **Ticket Handler** — auto-responds to support tickets
- **Report Generator** — creates weekly analytics reports

But managing them is chaos:

| Challenge | Current State | With klaw |
|-----------|---------------|-----------|
| **Visibility** | "Is the agent running? What's it doing?" | `klaw get agents`, `klaw logs` |
| **Isolation** | Sales agent accessing support secrets | Namespaces with scoped permissions |
| **Scheduling** | Messy cron jobs, Lambda functions | `klaw cron create` — built-in |
| **Scaling** | Manual server provisioning | `klaw node join` — auto-dispatch |
| **Debugging** | grep through CloudWatch | `klaw logs agent --follow` |
| **Deployment** | Complex setup, many dependencies | Single binary, one command |

**OpenClaw works, but deployment is painful and scaling is worse.**

klaw brings Kubernetes-style operations to AI agents. One binary. Deploys in seconds.

---

## Quick Start

### 1. Install

```bash
curl -fsSL https://klaw.sh/install.sh | sh
```

### 2. Configure

```bash
# Pick one provider
export ANTHROPIC_API_KEY=sk-ant-...      # Direct Anthropic
export OPENROUTER_API_KEY=sk-or-...      # OpenRouter (100+ models)
export EACHLABS_API_KEY=...              # each::labs (300+ models)
```

### 3. Run

```bash
# Interactive chat
klaw chat

# Or start the full platform (Slack + scheduler + agents)
export SLACK_BOT_TOKEN=xoxb-...
export SLACK_APP_TOKEN=xapp-...
klaw start
```

---

## Real-World Examples

### Sales: Lead Scoring

```bash
# Create the agent
klaw create agent lead-scorer \
  --namespace sales \
  --model claude-sonnet-4-20250514 \
  --skills crm,web-search

# Schedule hourly runs
klaw cron create score-leads \
  --schedule "0 * * * *" \
  --agent lead-scorer \
  --task "Analyze new leads in HubSpot, score 1-100 based on fit, update Lead Score field"

# Check status anytime
klaw get agents -n sales
klaw logs lead-scorer
```

### Research: Competitor Intelligence

```bash
klaw create agent competitor-watch \
  --namespace research \
  --model gpt-4o \
  --skills web-search,web-fetch,slack

klaw cron create competitor-daily \
  --schedule "0 9 * * *" \
  --agent competitor-watch \
  --task "Check competitor.com/pricing for changes. Post diff to #competitive-intel"
```

### 