<h1 align="center">
  <img src="./img/prompt-icon.svg" alt="prompt-icon" width="40">
  ClawSec: Security Skill Suite for AI Agents
  <img src="./img/prompt-icon.svg" alt="prompt-icon" width="40">
</h1>

<div align="center">

## Secure Your OpenClaw Bots with a Complete Security Skill Suite

<h4>Brought to you by <a href="https://prompt.security">Prompt Security</a>, the Platform for AI Security</h4>

</div>

<div align="center">

![Prompt Security Logo](./img/Black+Color.png)
<img src="./public/img/mascot.png" alt="clawsec mascot" width="200" />

</div>
<div align="center">

🌐 **Live at: [https://clawsec.prompt.security](https://clawsec.prompt.security) [https://prompt.security/clawsec](https://prompt.security/clawsec)**

[![CI](https://github.com/prompt-security/clawsec/actions/workflows/ci.yml/badge.svg)](https://github.com/prompt-security/clawsec/actions/workflows/ci.yml)
[![Deploy Pages](https://github.com/prompt-security/clawsec/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/prompt-security/clawsec/actions/workflows/deploy-pages.yml)
[![Poll NVD CVEs](https://github.com/prompt-security/clawsec/actions/workflows/poll-nvd-cves.yml/badge.svg)](https://github.com/prompt-security/clawsec/actions/workflows/poll-nvd-cves.yml)


</div>

---

## 🦞 What is ClawSec?

ClawSec is a **complete security skill suite for the OpenClaw family of agents (Moltbot, Clawdbot, some clones)**. It provides a unified installer that deploys, verifies, and maintains security skills-protecting your agent's cognitive architecture against prompt injection, drift, and malicious instructions.

### Core Capabilities

- **📦 Suite Installer** - One-command installation of all security skills with integrity verification
- **🛡️ File Integrity Protection** - Drift detection and auto-restore for critical agent files (SOUL.md, IDENTITY.md, etc.)
- **📡 Live Security Advisories** - Automated NVD CVE polling and community threat intelligence
- **🔍 Security Audits** - Self-check scripts to detect prompt injection markers and vulnerabilities
- **🔐 Checksum Verification** - SHA256 checksums for all skill artifacts
- **Health Checks** - Automated updates and integrity verification for all installed skills

---

## 🚀 Quick Start

### For AI Agents

```bash
# Fetch and install the ClawSec security suite
curl -sL https://clawsec.prompt.security/releases/latest/download/SKILL.md
```

The skill file contains deployment instructions. Your agent will:
1. Detect its agent family (OpenClaw/MoltBot/ClawdBot or other)
2. Install appropriate skills from the catalog
3. Verify integrity using checksums
4. Set up cron update checks

### For Humans

Copy this instruction to your AI agent:

> Read https://clawsec.prompt.security/releases/latest/download/SKILL.md and follow the instructions to install the protection skill suite.

---

## 📦 ClawSec Suite

The **clawsec-suite** is a skill-of-skills manager that installs, verifies, and maintains security skills from the ClawSec catalog.

### Skills in the Suite

| Skill | Description | Installation | Compatibility |
|-------|-------------|--------------|---------------|
| 📡 **clawsec-feed** | Security advisory feed monitoring with live CVE updates | ✅ Included by default | All agents |
| 🔭 **openclaw-audit-watchdog** | Automated daily audits with email reporting | ⚙️ Optional (install separately) | OpenClaw/MoltBot/ClawdBot |
| 👻 **soul-guardian** | Drift detection and file integrity guard with auto-restore | ⚙️ Optional | All agents |
| 🤝 **clawtributor** | Community incident reporting | ❌ Optional (Explicit request) | All agents |

> ⚠️ **clawtributor** is not installed by default as it may share anonymized incident data. Install only on explicit user request.

> ⚠️ **openclaw-audit-watchdog** is tailored for the OpenClaw/MoltBot/ClawdBot agent family. Other agents receive the universal skill set.

### Suite Features

- **Integrity Verification** - Every skill package includes `checksums.json` with SHA256 hashes
- **Updates** - Automatic checks for new skill versions 
- **Self-Healing** - Failed integrity checks trigger automatic re-download from trusted releases
- **Advisory Cross-Reference** - Installed skills are checked against the security advisory feed

---

## 📡 Security Advisory Feed

ClawSec maintains a continuously updated security advisory feed, automatically populated from NIST's National Vulnerability Database (NVD).

### Feed URL

```bash
# Fetch latest advisories
curl -s https://clawsec.prompt.security/advisories/feed.json | jq '.advisories[] | select(.severity == "critical" or .severity == "high")'
```

### Monitored Keywords

The feed polls CVEs related to:
- `OpenClaw`
- `clawdbot`  
- `Moltbot`
- Prompt injection patterns
- Agent security vulnerabilities

### Advisory Schema

**NVD CVE Advisory:**
```json
{
  "id": "CVE-2026-XXXXX",
  "severity": "critical|high|medium|low",
  "type": "vulnerable_skill",
  "title": "Short description",
  "description": "Full CVE description from NVD