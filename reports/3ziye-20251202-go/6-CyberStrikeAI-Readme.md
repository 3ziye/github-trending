<div align="center">
  <img src="web/static/logo.png" alt="CyberStrikeAI Logo" width="200">
</div>

# CyberStrikeAI

[中文](README_CN.md) | [English](README.md)

CyberStrikeAI is an **AI-native penetration-testing copilot** built in Go. It combines hundreds of security tools, MCP-native orchestration, and an agent that reasons over findings so that a full engagement can be run from a single conversation.

- Web console  
  <img src="./img/效果.png" alt="Preview" width="560">
- MCP stdio mode  
  <img src="./img/mcp-stdio2.png" alt="Preview" width="560">
- External MCP servers & attack-chain view   
  <img src="./img/外部MCP接入.png" alt="Preview" width="560">   
  <img src="./img/攻击链.jpg" alt="Preview" width="560">

## Highlights

- 🤖 AI decision engine with OpenAI-compatible models (GPT, Claude, DeepSeek, etc.)
- 🔌 Native MCP implementation with HTTP/stdio transports and external MCP federation
- 🧰 100+ prebuilt tool recipes + YAML-based extension system
- 📄 Large-result pagination, compression, and searchable archives
- 🔗 Attack-chain graph, risk scoring, and step-by-step replay
- 🔒 Password-protected web UI, audit logs, and SQLite persistence

## Tool Overview

CyberStrikeAI ships with 100+ curated tools covering the whole kill chain:

- **Network Scanners** – nmap, masscan, rustscan, arp-scan, nbtscan
- **Web & App Scanners** – sqlmap, nikto, dirb, gobuster, feroxbuster, ffuf, httpx
- **Vulnerability Scanners** – nuclei, wpscan, wafw00f, dalfox, xsser
- **Subdomain Enumeration** – subfinder, amass, findomain, dnsenum, fierce
- **API Security** – graphql-scanner, arjun, api-fuzzer, api-schema-analyzer
- **Container Security** – trivy, clair, docker-bench-security, kube-bench, kube-hunter
- **Cloud Security** – prowler, scout-suite, cloudmapper, pacu, terrascan, checkov
- **Binary Analysis** – gdb, radare2, ghidra, objdump, strings, binwalk
- **Exploitation** – metasploit, msfvenom, pwntools, ropper, ropgadget
- **Password Cracking** – hashcat, john, hashpump
- **Forensics** – volatility, volatility3, foremost, steghide, exiftool
- **Post-Exploitation** – linpeas, winpeas, mimikatz, bloodhound, impacket, responder
- **CTF Utilities** – stegsolve, zsteg, hash-identifier, fcrackzip, pdfcrack, cyberchef
- **System Helpers** – exec, create-file, delete-file, list-files, modify-file

## Basic Usage

### Quick Start
1. **Clone & install**
   ```bash
   git clone https://github.com/Ed1s0nZ/CyberStrikeAI.git
   cd CyberStrikeAI-main
   go mod download
   ```
2. **Set up the Python tooling stack (required for the YAML tools directory)**  
   A large portion of `tools/*.yaml` recipes wrap Python utilities (`api-fuzzer`, `http-framework-test`, `install-python-package`, etc.). Create the project-local virtual environment once and install the shared dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
   The helper tools automatically detect this `venv` (or any already active `$VIRTUAL_ENV`), so the default `env_name` works out of the box unless you intentionally supply another target.
3. **Configure OpenAI-compatible access**  
   Either open the in-app `Settings` panel after launch or edit `config.yaml`:
   ```yaml
   openai:
     api_key: "sk-your-key"
     base_url: "https://api.openai.com/v1"
     model: "gpt-4o"
   auth:
     password: ""                  # empty = auto-generate & log once
     session_duration_hours: 12
   security:
     tools_dir: "tools"
   ```
4. **Install the tooling you need (optional)**
   ```bash
   # macOS
   brew install nmap sqlmap nuclei httpx gobuster feroxbuster subfinder amass
   # Ubuntu/Debian
   sudo apt-get install nmap sqlmap nuclei httpx gobuster feroxbuster
   ```
   AI automatically falls back to alternatives when a tool is missing.
5. **Launch**
   ```bash
   chmod +x run.sh && ./run.sh
   # or
   go run cmd/server/main.go
   # or
   go build -o cyberstrike-ai cmd/server/main.go
   ```
6. **Open the console** at http://localhost:8080, log in with the generated password, and start chatting.

### Core Workflows
- **Conversation testing** – Natural-language prompts trigger toolchains with streaming SSE output.
- **Tool monitor** – Inspect running jobs, execution logs, and large-result attachments.
- **History & audit** – Every conversation and tool invocation is stored in SQLite with replay.
- **Settings** – Tweak provider keys, MCP enablement, tool toggles, and agent iteration limits.

### Built-in Safeguards
- Required-field validation prevents accidental blank API credentials.
- Auto-generated strong passwords when `auth.password` is empty.
- Unified auth middleware for every web/API call (Bearer token flow).
- Timeout and sandbox guards per tool, plus structured logging for triage.

## Advanced Usage

### Tool Orchestration & Extensions
- **YAML recipes** in `tools/*.yaml` describe commands, arguments, prompts, and metadata.
- **Directory hot-reload** – pointing `security.tools_dir` to a folder is usually enough; 