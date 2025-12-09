<p align="center">
  <a href="https://github.com/Vyntral/god-eye/releases"><img src="https://img.shields.io/badge/version-0.1-blue.svg?style=for-the-badge" alt="Version"></a>
  <a href="https://golang.org/"><img src="https://img.shields.io/badge/language-Go-00ADD8.svg?style=for-the-badge&logo=go" alt="Go"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green.svg?style=for-the-badge" alt="License"></a>
  <a href="#installation"><img src="https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey.svg?style=for-the-badge" alt="Platform"></a>
  <br>
  <a href="#ai-integration"><img src="https://img.shields.io/badge/AI-Ollama%20Powered-blueviolet.svg?style=for-the-badge&logo=ollama" alt="AI Powered"></a>
  <a href="AI_SETUP.md"><img src="https://img.shields.io/badge/privacy-100%25%20Local-success.svg?style=for-the-badge&logo=shield" alt="Privacy"></a>
  <a href="#features"><img src="https://img.shields.io/badge/CVE-Real--time%20Detection-critical.svg?style=for-the-badge&logo=cve" alt="CVE Detection"></a>
  <a href="https://github.com/Vyntral/god-eye/stargazers"><img src="https://img.shields.io/github/stars/Vyntral/god-eye?style=for-the-badge&color=yellow" alt="GitHub stars"></a>
</p>

<h1 align="center">
  <br>
  <img src="https://raw.githubusercontent.com/Vyntral/god-eye/main/assets/logo.png" alt="God's Eye" width="200">
  <br>
  God's Eye
  <br>
</h1>

<h4 align="center">Ultra-fast subdomain enumeration & reconnaissance tool with AI-powered analysis</h4>

<p align="center">
  <a href="#-why-gods-eye">Why?</a> •
  <a href="#features">Features</a> •
  <a href="#ai-integration">🧠 AI</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#-performance-benchmarks">Benchmarks</a> •
  <a href="#credits">Credits</a>
</p>

---

## 🎯 Why God's Eye?

<table>
<tr>
<td width="33%" align="center">

### ⚡ All-in-One
**20 passive sources** + DNS brute-forcing + HTTP probing + security checks in **one tool**. No need to chain 5+ tools together.

</td>
<td width="33%" align="center">

### 🧠 AI-Powered
**Zero-cost local AI** with Ollama for intelligent vulnerability analysis, CVE detection, and executive reports. **100% private**.

</td>
<td width="33%" align="center">

### 🚀 Production-Ready
Battle-tested on **real bug bounties**. Fast, reliable, and packed with features that actually matter.

</td>
</tr>
</table>

---

## ⚠️ Legal Notice

**IMPORTANT: This tool is for AUTHORIZED security testing only.**

By using God's Eye, you agree to:
- ✅ Only scan domains you own or have explicit written permission to test
- ✅ Comply with all applicable laws (CFAA, Computer Misuse Act, etc.)
- ✅ Use responsibly for legitimate security research and bug bounties
- ❌ Never use for unauthorized access or malicious activities

**The authors accept NO liability for misuse. You are solely responsible for your actions.**

Read the full [Legal Disclaimer](#️-legal-disclaimer--terms-of-use) before use.

---

## 📖 Overview

**God's Eye** is a powerful, ultra-fast subdomain enumeration and reconnaissance tool written in Go. It combines multiple passive sources with active DNS brute-forcing and comprehensive security checks to provide a complete picture of a target's attack surface.

Unlike other tools that only find subdomains, God's Eye performs **deep reconnaissance** including:
- ✅ HTTP probing with technology detection
- ✅ Security vulnerability scanning
- ✅ Cloud provider identification
- ✅ JavaScript secret extraction
- ✅ Subdomain takeover detection
- ✅ **AI-Powered Analysis** with local LLM (Ollama)
- ✅ Real-time CVE detection via function calling

### ⚡ Quick Start

```bash
# Clone and build
git clone https://github.com/Vyntral/god-eye.git && cd god-eye
go build -o god-eye ./cmd/god-eye

# Basic scan
./god-eye -d target.com

# With AI-powered analysis
./god-eye -d target.com --enable-ai
```

<p align="center">
  <a href="https://twitter.com/intent/tweet?text=God's%20Eye%20-%20AI-powered%20subdomain%20enumeration%20tool&url=https://github.com/Vyntral/god-eye&hashtags=bugbounty,infosec,pentesting"><img src="https://img.shields.io/badge/Share%20on-Twitter-1DA1F2?style=for-the-badge&logo=twitter" alt="Share on Twitter"></a>
  <a href="https://www.linkedin.com/sharing/share-offsite/?url=https://github.com/Vyntral/god-eye"><img src="https://img.shields.io/badge/Share%20on-LinkedIn-0077B5?style=for-the-badge&logo=linkedin" alt="Share on LinkedIn"></a>
</p>

### 🌟 **NEW: AI Integration**

God's Eye now features **AI-powered security analysis** using local LLM models via Ollama:
- ✅ **100% Local & Private** - No data leaves your machine
- ✅ **Free Forever** - No API costs
- ✅ **Intelligent Analysis** - JavaScript code review, CVE detection, anomaly identification
- ✅ **Smart Cascade** - Fast triage + deep analysis for optimal performance

<table>
<tr>
<td width="50%" align="center">

**Basic Scan**
<img src="assets/demo.gif" alt="God's Eye Basic Demo" width="100