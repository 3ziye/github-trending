```
     ____         ____                       ____  _
    / __ \  ___  / __/___   ___   ___  ___  / ___|| | __ _ __      __
   / / / / / _ \/ /_// _ \ / _ \ / __|/ _ \| |    | |/ _` |\ \ /\ / /
  / /_/ / /  __/ __//  __/| | | |\__ \  __/| |___ | | (_| | \ V  V /
 /_____/  \___/_/   \___/ |_| |_||___/\___| \____||_|\__,_|  \_/\_/

  ╔═══════════════════════════════════════════════════════════════╗
  ║  DefenseClaw — Security Governance for Agentic AI             ║
  ╚═══════════════════════════════════════════════════════════════╝
```

# DefenseClaw

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![Discord](https://img.shields.io/badge/Discord-Join%20Us-7289DA?logo=discord&logoColor=white)](https://discord.com/invite/nKWtDcXxtx)
[![Cisco AI Defense](https://img.shields.io/badge/Cisco-AI%20Defense-049fd9?logo=cisco&logoColor=white)](https://www.cisco.com/site/us/en/products/security/ai-defense/index.html)
[![AI Security and Safety Framework](https://img.shields.io/badge/AI%20Security-Framework-orange)](https://learn-cloudsecurity.cisco.com/ai-security-framework)

**AI agents are powerful. Unchecked, they're dangerous.**

Large language model agents — like those built on [OpenClaw](https://github.com/openclaw/openclaw) — can install skills, call MCP servers, execute code, and reach the network. Every one of those actions is an attack surface. A single malicious skill can exfiltrate data. A compromised MCP server can inject hidden instructions. Generated code can contain hardcoded secrets or command injection.

**DefenseClaw is the enterprise governance layer for OpenClaw.** It sits between your AI agents and the infrastructure they run on, enforcing a simple principle: **nothing runs until it's scanned, and anything dangerous is blocked automatically.**

```
┌─────────────────────────────────────────────────────────┐
│                       DefenseClaw                       │
│                                                         │
│  ┌───────────┐   ┌───────────────────────────────────┐  │
│  │           │   │       DefenseClaw Gateway         │  │
│  │    CLI    │   │                                   │  │
│  │  (Python) │   │  ┌─────────────────────────────┐  │  │
│  │           │   │  │        AI Gateway           │  │  │
│  │           │   │  └─────────────────────────────┘  │  │
│  │           │   │  ┌─────────────────────────────┐  │  │
│  │           │   │  │      Inspect Engine         │  │  │
│  │           │   │  └─────────────────────────────┘  │  │
│  │           │   │                                   │  │
│  └───────────┘   └─────────────────┬─────────────────┘  │
│                                    │                    │
│                           WS (v3) + REST                │
│                                    │                    │
│  ┌─────────────────────────────────┼─────────────────┐  │
│  │         NVIDIA OpenShell        │                 │  │
│  │                                 │                 │  │
│  │  ┌──────────────────────────────┴──────────────┐  │  │
│  │  │                  OpenClaw                   │  │  │
│  │  │                                             │  │  │
│  │  │  ┌───────────────────────────────────────┐  │  │  │
│  │  │  │     DefenseClaw Plugin (TS)           │  │  │  │
│  │  │  └───────────────────────────────────────┘  │  │  │
│  │  │                                             │  │  │
│  │  └─────────────────────────────────────────────┘  │  │
│  │                                                   │  │
│  └───────────────────────────────────────────────────┘  │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## Capabilities

### Skill, MCP, and Plugin Scanning

DefenseClaw scans every skill, MCP server, and plugin **before** it is allowed to run. The CLI wraps [Cisco AI Defense](https://www.cisco.com/site/us/en/products/security/ai-defense/index.html) scanners ([`skill-scanner`](https://github.com/cisco-ai-defense/skill-scanner), [`mcp-scanner`](https://github.com/cisco-ai-defense/mcp-scanner)) and an AI bill-of-materials generator ([`aibom`](https://github.com/cisco-ai-defense/aibom)) to produce a unified `ScanResult` with severity-ranked findings. Scan results feed into the admission gate — HIGH/CRITICAL findings auto-block the component, MEDIUM/LOW findings install with a warning, and clean components pass through. All outcomes are logged to the SQLite audit store and forwarded to SIEM.

```bash
defenseclaw skill scan web-search        # scan a skill by name
defenseclaw mcp scan github-mcp          # scan an MCP server
defenseclaw plugin scan code-review      # scan a plugin
defenseclaw skill scan all               # scan every installed skill
```

### CodeGuard

CodeGuard is a built-in static