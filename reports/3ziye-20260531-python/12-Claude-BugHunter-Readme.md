![claude-bughunter banner](assets/banner.svg)

# claude-bughunter

> A self-contained Claude skill bundle for bug hunting and external red-team work · **51 skills** · 15 slash commands · **681 disclosed-report patterns** across 24 vulnerability classes · enterprise identity + infrastructure attack matrices · engagement-folder scaffolding · Burp MCP integration · battle-tested across authorized red-team and bug-hunting engagements, plus public training platforms (DVWA, OWASP Juice Shop, Hacker101, testphp.vulnweb.com).

Built by **[Sachin Sharma](https://www.linkedin.com/in/sachinsharma8080/)** — Bug Hunting & GenAI Security Research.

---

## What is this?

`claude-bughunter` is a drop-in skill bundle for the [Claude Code skills system](https://docs.claude.com/en/docs/claude-code/skills). Install once and Claude Code stops being a chatbot and starts behaving like a senior bug-hunting researcher or red-team operator: it knows the techniques, the chain templates, the VRT mappings, the platform CVE chains, and the hygiene — and it stays in scope.

Four layers stack:

- **`bug-bounty` + `bb-methodology` + `redteam-mindset`** — *how to think.* 5-phase non-linear hunting workflow, critical-thinking framework, developer-psychology heuristics, anomaly detection patterns, and the red-team operator-discipline corrections (when scope is "external red team" not "bug hunting / WAPT").
- **24 `hunt-*` skills + `security-arsenal`** — *what to look for in webapps.* Per-class detection patterns, payloads, bypass tables, and chain templates curated from 681 disclosed HackerOne reports.
- **Enterprise platform attack chains** — *what to look for on the perimeter.* `m365-entra-attack`, `okta-attack`, `cloud-iam-deep`, `vmware-vcenter-attack`, `enterprise-vpn-attack`, `hunt-sharepoint`, `hunt-aspnet`, `hunt-ntlm-info`, `apk-redteam-pipeline`, `supply-chain-attack-recon` — current 2024-2026 CVE chains, AADSTS error references, version-fingerprint matrices, and post-credential escalation paths.
- **`triage-validation` + `bugcrowd-reporting` + `evidence-hygiene` + `redteam-report-template` + `mid-engagement-ir-detection`** — *how to ship it.* 7-Question Gate, VRT category fallback, severity-request paragraphs, OOS rebuttals, cookie/PII redaction, client-facing red-team deliverable format, and SOC-patch / mid-engagement-attacker detection methodology.

All triggered automatically by topic — describe what you're testing in plain English and the relevant skill loads. No invocation by name.

> **51 skills · 15 commands · 681 disclosed reports curated · 6-phase workflow · exercised against public training platforms (DVWA, OWASP Juice Shop, Hacker101, testphp.vulnweb.com) and calibrated through authorized real-world engagements.**

---

## Scope — what this bundle is for, and what it isn't

This bundle covers the **external attack surface** — anything reachable from the internet without first compromising an internal endpoint.

### In scope

- **Bug bounty hunting** — web apps, APIs, SaaS, GraphQL, OAuth, JWT, file upload, IDOR, SSRF, RCE chains
- **Web application pentesting** — full hunt-* coverage of OWASP-mapped bug classes + discipline rules
- **External red-team engagements** — initial-access against internet-facing enterprise estate: M365 / Entra ID, Okta-as-IdP, SharePoint on-prem (ToolShell + legacy SOAP), VMware vCenter / Workspace ONE, SSL VPN appliances (Cisco / Fortinet / Citrix / Palo Alto / Pulse / SonicWall / F5), Android APK red-team, supply-chain recon
- **Cloud misconfig + post-credential escalation** — public S3, IMDS chains, STS AssumeRole, cross-account confused-deputy
- **Recon + OSINT** — subdomain enum, identity-fabric mapping, certificate transparency, JS analysis, secret scanning
- **Reporting** — H1, Bugcrowd (VRT-aware), Intigriti, Immunefi, plus client-facing red-team deliverable format

### Out of scope (deliberate — not gaps, design decisions)

- **Internal Active Directory attacks** — BloodHound, Kerberoasting, ASREProast, DCSync, Pass-the-Hash, AD CS abuse, ntlmrelayx, Responder, PetitPotam, etc. Different operational risk profile; needs different tooling and judgment. **Future bundle, not this one.**
- **C2 frameworks** — Cobalt Strike, Sliver, Mythic, Havoc, BRC4 tradecraft. Out of scope for external-only engagement model.
- **Post-exploit / persistence / lateral** — Mimikatz/comsvcs LSASS dumping, golden/silver tickets, named-pipe impersonation, persistence (registry, scheduled tasks, WMI events, COM hijacking), token theft. These start after the perimeter has already broken — different bundle territory.
- **Evasion** — AMSI bypass, ETW patching, AV/EDR bypass. Tied to C2 tradecraft above.
- **iOS pentesting / hardware / RF / ICS** — out of scope by design.
- **Binary exploitation / kernel pwn / browser internals** — different skill universe.

If you're running an internal red team that includes domain-takeover chains via Kerberos or lateral movement, **this bundle won't help you in those phases** — 