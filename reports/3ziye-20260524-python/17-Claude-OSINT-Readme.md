![claude-osint banner](assets/banner.png)

# claude-osint

> 2 paired Claude skills · **90+ recon modules** · 48 secret-regex patterns · 80+ dorks · 9 read-only credential validators · 27 attack-path templates · 4,600+ lines of structured tradecraft. Drop-in `SKILL.md` files that turn Claude into a god-mode external recon operator for authorized red-team and bug-bounty engagements.

Built by **[ElementalSoul](https://github.com/elementalsouls)** — GenAI Security Research.

---

## What is this?

`claude-osint` is a paired set of skills for the [Claude skills system](https://docs.claude.com/en/docs/claude-code/skills). Each skill is a structured `SKILL.md` file that primes Claude with expert-level methodology for one half of the offensive recon problem:

- **`osint-methodology`** - *how to think.* Strategic + procedural. Asset-graph discipline, severity rubric, time budgeting, identity-fabric mapping, deliverable templates.
- **`offensive-osint`** - *what to reach for.* Tactical arsenal. Probe paths, regexes, payloads, scoring rules, curl one-liners, tool URLs.

Drop both into your Claude environment and it behaves like a senior recon analyst: it knows the techniques, the tooling, the edge cases, and the escalation paths — and it stays in scope.

~4,600 lines of structured tradecraft · 96.9% PASS on a 32-prompt self-evaluation · ~85–90% practitioner coverage for the recon phase of authorized engagements.

---

## Structure

```
claude-osint/
├── skills/
│   ├── osint-methodology/SKILL.md     # how to think  (455 lines)
│   └── offensive-osint/
│       ├── SKILL.md                   # what to reach for (4,168 lines)
│       ├── scripts/secret_scan.py     # stdlib-only secret scanner
│       └── scripts/h1_reference.py    # HackerOne disclosed-reports reference agent
├── docs/                              # architecture · coverage · install · usage
├── examples/                          # 4 end-to-end engagement walk-throughs
├── tests/smoke-test-prompts.md        # 32-prompt self-evaluation
└── assets/banner.png
```

Each skill directory is self-contained. Drop into `~/.claude/skills/` and Claude auto-triggers on relevant phrases.

---

## Skill Index

90+ capabilities across 12 domains. Categorized like Claude-Red — pick a domain to drill in.

### Reconnaissance & Asset Discovery

| Capability | Skill |
|---|---|
| 5-stage external recon pipeline + time-budget profiles (1h / 4h / 1d / 1w) | methodology |
| Subdomain-source stack (crt.sh + 7-source fallback chain when crt.sh 502s) | arsenal |
| Common-prefix subdomain sweep (100+ ordered prefixes, PowerShell + bash) | arsenal |
| Wayback CDX deep mining + legacy-app pivot (.asp/.php/.jsp/.cfm) | arsenal |
| WHOIS / RDAP / historical-WHOIS + reverse-WHOIS pivots | arsenal |
| Public records (OpenCorporates · SEC EDGAR · GSXT · Rusprofile · Companies House) | arsenal |
| Bulk IP → ASN (Cymru / RIPEstat / bgp.tools) | arsenal |

### Identity & SSO Mapping

| Capability | Skill |
|---|---|
| Microsoft Entra (Azure AD) tenant fingerprint + GUID extraction | arsenal |
| M365 deep enum (Teams federation · SharePoint · OneDrive · OAuth · device-code phishing) | arsenal |
| Autodiscover IP correlation (passive M365 confirm even when MX wrapped by Mimecast/Proofpoint) | arsenal |
| Okta tenant slug + `/api/v1/authn` user-enum | arsenal |
| ADFS fingerprint + mex endpoint | arsenal |
| Google Workspace OIDC discovery | arsenal |
| Generic OIDC (Auth0 · Keycloak · Ping · OneLogin · Duo) | arsenal |
| SAML metadata (5 paths) | arsenal |
| AWS account-ID extraction from headers + ARN regex | arsenal |

### Web Application Attack Surface

| Capability | Skill |
|---|---|
| Swagger / OpenAPI discovery (28 paths) | arsenal |
| GraphQL discovery + introspection POST body (13 paths) | arsenal |
| GraphQL field-suggestion enum (when introspection disabled) + alias batching + depth bypass | arsenal |
| Always-on HTTP checks (15 paths: .git/.env/actuator/heapdump/etc.) | arsenal |
| Missing security header audit (HSTS/CSP/XFO/etc.) | arsenal |
| Endpoint extraction regex tiers (3 tiers) | arsenal |
| Endpoint interest score (0–100 rubric) | arsenal |
| JS deep analysis · sourcemap leakage · internal-host regex | arsenal |
| Subdomain takeover fingerprints (27 providers) | arsenal |

### Cloud & Container

| Capability | Skill |
|---|---|
| Cloud bucket arsenal (S3 / GCS / Azure · 6 prefixes × 15 suffixes × 47 stems) | arsenal |
| Cloud-native fingerprints (Lambda URLs · Cloud Run · Azure Functions · Vercel · Netlify · Workers) | arsenal |
| Kubernetes / etcd / kubelet exposure (12 ports + probes) | arsenal |
| Container registry leak hunting (Docker Hub · Quay · GHCR · ECR · GCR · ACR) | arsenal |
| CI/CD platform exposure (Jenkins · GitLab · TeamCity-KEV · Argo CD · Spinnaker · CircleCI) | arsenal |

### Secret & Credential Hunting

| Capability | Skill |
|---|---|
| 48-pattern secret-regex catalog (29 base + 19 modern) | arsenal |
| Modern AI API keys (Anthropic / OpenAI / Huggi