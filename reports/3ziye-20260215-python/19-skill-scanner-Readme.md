# Skill Scanner

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![PyPI version](https://img.shields.io/pypi/v/cisco-ai-skill-scanner.svg)](https://pypi.org/project/cisco-ai-skill-scanner/)
[![CI](https://github.com/cisco-ai-defense/skill-scanner/actions/workflows/python-tests.yml/badge.svg)](https://github.com/cisco-ai-defense/skill-scanner/actions/workflows/python-tests.yml)
[![Discord](https://img.shields.io/badge/Discord-Join%20Us-7289da?logo=discord&logoColor=white)](https://discord.com/invite/nKWtDcXxtx)
[![Cisco AI Defense](https://img.shields.io/badge/Cisco-AI%20Defense-049fd9?logo=cisco&logoColor=white)](https://www.cisco.com/site/us/en/products/security/ai-defense/index.html)
[![AI Security Framework](https://img.shields.io/badge/AI%20Security-Framework-orange)](https://learn-cloudsecurity.cisco.com/ai-security-framework)

A security scanner for AI Agent Skills that detects prompt injection, data exfiltration, and malicious code patterns. Combines **pattern-based detection** (YAML + YARA), **LLM-as-a-judge**, and **behavioral dataflow analysis** for comprehensive threat detection.

Supports [OpenAI Codex Skills](https://openai.github.io/codex/) and [Cursor Agent Skills](https://docs.cursor.com/context/rules) formats following the [Agent Skills specification](https://agentskills.io).

---

## Highlights

- **Multi-Engine Detection** - Static analysis, behavioral dataflow, LLM semantic analysis, and cloud-based scanning
- **False Positive Filtering** - Meta-analyzer significantly reduces noise while preserving detection capability
- **CI/CD Ready** - SARIF output for GitHub Code Scanning, exit codes for build failures
- **Extensible** - Plugin architecture for custom analyzers

**[Join the Cisco AI Discord](https://discord.com/invite/nKWtDcXxtx)** to discuss, share feedback, or connect with the team.

---

## Documentation

| Guide | Description |
|-------|-------------|
| [Quick Start](docs/quickstart.md) | Get started in 5 minutes |
| [Architecture](docs/architecture.md) | System design and components |
| [Threat Taxonomy](docs/threat-taxonomy.md) | Complete AITech threat taxonomy with examples |
| [LLM Analyzer](docs/llm-analyzer.md) | LLM configuration and usage |
| [Meta-Analyzer](docs/meta-analyzer.md) | False positive filtering and prioritization |
| [Behavioral Analyzer](docs/behavioral-analyzer.md) | Dataflow analysis details |
| [API Reference](docs/api-server.md) | REST API documentation |
| [Development Guide](docs/developing.md) | Contributing and development setup |

---

## Installation

**Prerequisites:** Python 3.10+ and [uv](https://docs.astral.sh/uv/) (recommended) or pip

```bash
# Using uv (recommended)
uv pip install cisco-ai-skill-scanner

# Using pip
pip install cisco-ai-skill-scanner
```

<details>
<summary><strong>Cloud Provider Extras</strong></summary>

```bash
# AWS Bedrock support
pip install cisco-ai-skill-scanner[bedrock]

# Google Vertex AI support
pip install cisco-ai-skill-scanner[vertex]

# Azure OpenAI support
pip install cisco-ai-skill-scanner[azure]

# All cloud providers
pip install cisco-ai-skill-scanner[all]
```

</details>

---

## Quick Start

### Environment Setup (Optional)

```bash
# For LLM analyzer and Meta-analyzer
export SKILL_SCANNER_LLM_API_KEY="your_api_key"
export SKILL_SCANNER_LLM_MODEL="claude-3-5-sonnet-20241022"

# For VirusTotal binary scanning
export VIRUSTOTAL_API_KEY="your_virustotal_api_key"

# For Cisco AI Defense
export AI_DEFENSE_API_KEY="your_aidefense_api_key"
```

### CLI Usage

```bash
# Scan a single skill (static analyzer only)
skill-scanner scan /path/to/skill

# Scan with behavioral analyzer (dataflow analysis)
skill-scanner scan /path/to/skill --use-behavioral

# Scan with all engines
skill-scanner scan /path/to/skill --use-behavioral --use-llm --use-aidefense

# Scan with meta-analyzer for false positive filtering
skill-scanner scan /path/to/skill --use-llm --enable-meta

# Scan multiple skills recursively
skill-scanner scan-all /path/to/skills --recursive --use-behavioral

# CI/CD: Fail build if threats found
skill-scanner scan-all ./skills --fail-on-findings --format sarif --output results.sarif

# Use custom YARA rules
skill-scanner scan /path/to/skill --custom-rules /path/to/my-rules/

# Disable specific noisy rules
skill-scanner scan /path/to/skill --disable-rule YARA_script_injection --disable-rule MANIFEST_MISSING_LICENSE

# Strict mode (more findings, higher FP rate)
skill-scanner scan /path/to/skill --yara-mode strict

# Permissive mode (fewer findings, may miss some threats)
skill-scanner scan /path/to/skill --yara-mode permissive
```

### Python SDK

```python
from skill_scanner import SkillScanner
from skill_scanner.core.analyzers import StaticAnalyzer, BehavioralAnalyzer

# Create scanner with analyzers
scanner = SkillScanner(analyzers=[
 