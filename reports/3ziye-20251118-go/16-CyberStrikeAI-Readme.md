<div align="center">
  <img src="web/static/logo.png" alt="CyberStrikeAI Logo" width="200">
</div>

# CyberStrikeAI

[中文](README_CN.md) | [English](README.md)

🚀 **AI-Powered Autonomous Penetration Testing Platform** - Built with Golang, featuring hundreds of built-in security tools, flexible custom tool extensions, and intelligent AI decision-making through MCP protocol, making security testing as simple as a conversation.

- Web Mode  
  <img src="./img/效果.png" alt="Preview" width="600">
  
- MCP Stdio Mode   
  <img src="./img/mcp-stdio2.png" alt="Preview" width="600">

- External MCP Server Integration (supports stdio and HTTP transport modes)   
  <img src="./img/外部MCP接入.png" alt="Preview" width="600">

- Attack Chain Visualization   
  <img src="./img/攻击链.jpg" alt="Preview" width="600">

## Changelog
- 2025.11.17 Added attack chain visualization feature: automatically build attack chains from conversations using AI analysis, visualize tool execution flows, vulnerability discovery paths, and relationships between nodes, support interactive graph exploration with risk scoring
- 2025.11.15 Added large result pagination feature: when tool execution results exceed the threshold (default 200KB), automatically save to file and return execution ID, support paginated queries, keyword search, conditional filtering, and regex matching through query_execution_result tool, effectively solving the problem of overly long single responses and improving large file processing capabilities
- 2025.11.15 Added external MCP integration feature: support for integrating external MCP servers to extend tool capabilities, supports both stdio and HTTP transport modes, tool-level enable/disable control, complete configuration guide and management APIs
- 2025.11.14 Performance optimizations: optimized tool lookup from O(n) to O(1) using index map, added automatic cleanup mechanism for execution records to prevent memory leaks, and added pagination support for database queries
- 2025.11.13 Added authentication for the web mode, including automatic password generation and in-app password change
- 2025.11.13 Added `Settings` feature in the frontend
- 2025.11.13 Added MCP Stdio mode support, now seamlessly integrated and usable in code editors, CLI, and automation scripts
- 2025.11.12 Added task stop functionality, optimized frontend

## ✨ Features

### Core Features
- 🤖 **AI Intelligent Agent** - Integrated OpenAI-compatible API (supports GPT, Claude, DeepSeek, etc.), AI autonomously makes decisions and executes security tests
- 🧠 **Intelligent Decision Engine** - AI analyzes targets and automatically selects optimal testing strategies and tool combinations
- ⚡ **Autonomous Execution** - AI agent automatically invokes security tools without human intervention
- 🔄 **Adaptive Adjustment** - AI automatically adjusts testing strategies based on tool execution results and discovered vulnerabilities
- 📝 **Intelligent Summary** - When maximum iterations are reached, AI automatically summarizes test results and provides next-step execution plans
- 💬 **Conversational Interface** - Natural language conversation interface with streaming output (SSE), real-time execution viewing
- 📊 **Conversation History Management** - Complete conversation history records, supports viewing, deletion, and management
- ⚙️ **Visual Configuration Management** - Web interface for system settings, supports real-time loading and saving configurations with required field validation
- 📄 **Large Result Pagination** - When tool execution results exceed the threshold, automatically save to file, support paginated queries, keyword search, conditional filtering, and regex matching, effectively solving the problem of overly long single responses, with examples for various tools (head, tail, grep, sed, etc.) for segmented reading
- 🔗 **Attack Chain Visualization** - Automatically build and visualize attack chains from conversations, showing tool execution flows, vulnerability discovery paths, and relationships between targets, tools, vulnerabilities, and discoveries, with AI-powered analysis and interactive graph exploration

### Tool Integration
- 🔌 **MCP Protocol Support** - Complete MCP protocol implementation, supports tool registration, invocation, and monitoring
- 📡 **Dual Transport Modes** - Supports both HTTP and stdio transport methods, seamlessly usable in web applications and IDEs
- 🛠️ **Flexible Tool Configuration** - Supports loading tool configurations from directories (YAML), easy to extend and maintain
- 📈 **Real-time Monitoring** - Monitors execution status, results, call counts, and statistics of all tools
- 🔍 **Automatic Vulnerability Analysis** - Automatically analyzes tool output, extracts and categorizes discovered vulnerabilities

### Technical Features
- 🚀 **Streaming Output** - Supports Server-Sent Events (SSE) for real-time streaming output, enhancing user experience
- 💾 **Data Persistence** - SQLite database stores conversation history and process d