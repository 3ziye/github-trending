# Claude for Legal

Reference agents, skills, and data connectors for the legal workflows we see most — in-house commercial, privacy, product, corporate, employment, litigation, regulatory, AI governance, IP, and the learning side of the practice (law school clinics and students).

> **New here?** Start with [QUICKSTART.md](QUICKSTART.md) — install in 60 seconds. This README is the full reference.

Everything here is available **two ways from one source**: install it as a [Claude Cowork](https://claude.com/product/cowork) or [Claude Code](https://claude.com/product/claude-code) plugin, or deploy it through the [Claude Managed Agents API](https://docs.claude.com/en/api/managed-agents) behind your own workflow engine. Same system prompt, same skills — you choose where it runs.

## Getting started in Cowork
- [Install Claude Desktop](https://claude.com/download)
- Get access to Claude Cowork
- Follow the instructions in the video below:

https://github.com/user-attachments/assets/51394f0a-5277-4fe2-b81c-5c5e9ac876b5

> [!IMPORTANT]
> **Every output from these plugins is a draft for attorney review — not legal advice, not a legal conclusion, not a substitute for a lawyer.** They are built with guardrails that reflect that: source attribution on every citation, conservative defaults on privilege and subjective legal calls, jurisdiction assumptions surfaced, and explicit gates before anything is filed, sent, or relied on. A lawyer reviews, verifies, and takes professional responsibility for anything that leaves the building. These plugins make that review faster; they do not replace it.
>
> **These plugins do not represent Anthropic's legal positions.** They are tools that help lawyers analyze issues. Where a skill includes a checklist item, a suggested framework, a risk flag, or a characterization of case law or regulatory guidance, that is an aid to the reviewing attorney's own analysis, not a statement of Anthropic's view of the law. The law in many of these areas is unsettled and evolving. The attorney using the plugin — not the plugin, and not Anthropic — is responsible for the legal positions taken in their work product.

What's in the repo:

- **Practice-area plugins** covering in-house, firm, and academic legal work — each one built around a cold-start interview that learns your playbook and a `CLAUDE.md` practice profile that every skill reads from.
- **Managed-agent cookbooks** for the scheduled, eyes-on-the-feed workflows (renewal watcher, docket watcher, regulatory feed monitor, diligence grid, launch radar).
- **MCP connectors** across general productivity (Slack, Google Drive, Box) and legal-specific systems (Ironclad, DocuSign, iManage, Everlaw, CourtListener, and more).
- **[Named agents](#agents)** — end-to-end workflow agents (Vendor Agreement Reviewer, DSAR Responder, Termination Reviewer, Claim Chart Builder, …) with job-style names and a single command to run each one.

## Agents

Each agent is named for the workflow it runs. They're the most common surface — start with the ones that match your work, then tune the underlying skill, the practice profile, and the connectors to how your team does it.

| Agent | What it does | Plugin | Command |
|---|---|---|---|
| **Vendor Agreement Reviewer** | Reviews a vendor MSA against your playbook and produces a redline memo | `commercial-legal` | `/commercial-legal:review` |
| **NDA Triager** | GREEN/YELLOW/RED triage of inbound NDAs so only the hard ones hit a lawyer's desk | `commercial-legal` | `/commercial-legal:review` |
| **Amendment Tracer** | Traces how a contract has changed across its base agreement and every amendment | `commercial-legal` | `/commercial-legal:amendment-history` |
| **Renewal Watcher** | Scans the contract register for cancel-by and renewal deadlines | `commercial-legal` | scheduled agent |
| **Deal Debrief** | Weekly sweep of signed agreements with playbook deviations — prompts the attorney to log context while memory is fresh | `commercial-legal` | scheduled agent |
| **Playbook Monitor** | Watches the deviation log and proposes playbook updates when a clause has drifted | `commercial-legal` | scheduled agent |
| **Escalation Router** | Routes contract issues to the right approver and drafts the ask | `commercial-legal` | `/commercial-legal:escalation-flagger` |
| **Tabular Diligence Review** | Tabular review over a data room with one row per document and every cell cited | `corporate-legal` | `/corporate-legal:tabular-review` |
| **Issue Extractor** | Reads VDR documents and extracts issues per house categories and materiality thresholds | `corporate-legal` | `/corporate-legal:diligence-issue-extraction` |
| **Board Consent Drafter** | Drafts unanimous written consents in house format with precedent search | `corporate-legal` | `/corporate-legal:written-consent` |
| **Material Contracts Schedule Builder** | Builds the disclosure schedule from diligence findings against the purchase-agreement threshold | `corporate-legal` | `