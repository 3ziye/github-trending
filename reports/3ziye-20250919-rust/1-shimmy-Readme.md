<div align="center">
  <img src="assets/shimmy-logo.png" alt="Shimmy Logo" width="300" height="auto" />
  
  # The Privacy-First Alternative to Ollama
  
  ### 🔒 Local AI Without the Lock-in 🚀

  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  [![Security](https://img.shields.io/badge/Security-Audited-green)](https://github.com/Michael-A-Kuykendall/shimmy/security)
  [![Crates.io](https://img.shields.io/crates/v/shimmy.svg)](https://crates.io/crates/shimmy)
  [![Downloads](https://img.shields.io/crates/d/shimmy.svg)](https://crates.io/crates/shimmy)
  [![Rust](https://img.shields.io/badge/rust-stable-brightgreen.svg)](https://rustup.rs/)
  [![GitHub Stars](https://img.shields.io/github/stars/Michael-A-Kuykendall/shimmy?style=social)](https://github.com/Michael-A-Kuykendall/shimmy/stargazers)
  
  [![💝 Sponsor this project](https://img.shields.io/badge/💝_Sponsor_this_project-ea4aaa?style=for-the-badge&logo=github&logoColor=white)](https://github.com/sponsors/Michael-A-Kuykendall)
</div>

**Shimmy will be free forever.** No asterisks. No "free for now." No pivot to paid.

### 💝 Support Shimmy's Growth

🚀 **If Shimmy helps you, consider [sponsoring](https://github.com/sponsors/Michael-A-Kuykendall) — 100% of support goes to keeping it free forever.**

- **$5/month**: Coffee tier ☕ - Eternal gratitude + sponsor badge  
- **$25/month**: Bug prioritizer 🐛 - Priority support + name in [SPONSORS.md](SPONSORS.md)
- **$100/month**: Corporate backer 🏢 - Logo placement + monthly office hours  
- **$500/month**: Infrastructure partner 🚀 - Direct support + roadmap input

[**🎯 Become a Sponsor**](https://github.com/sponsors/Michael-A-Kuykendall) | See our amazing [sponsors](SPONSORS.md) 🙏

---

## Drop-in OpenAI API Replacement for Local LLMs

Shimmy is a **5.1MB single-binary** that provides **100% OpenAI-compatible endpoints** for GGUF models. Point your existing AI tools to Shimmy and they just work — locally, privately, and free.

## 🤔 What are you building with Shimmy?

**New developer tools and specifications included!** Whether you're forking Shimmy for your application or integrating it as a service, we now provide:

- **🔧 Integration Templates**: Copy-paste guidance for embedding Shimmy in your projects
- **📋 Development Specifications**: GitHub Spec-Kit methodology for planning Shimmy-based features
- **🛡️ Architectural Guarantees**: Constitutional principles ensuring Shimmy stays reliable and lightweight
- **📖 Complete Documentation**: Everything you need to build on Shimmy's foundation

**Building something cool with Shimmy?** These tools help you do it systematically and reliably.

### 🚀 **GitHub Spec-Kit Integration**
Shimmy now includes [GitHub's brand-new Spec-Kit methodology](https://github.com/github/spec-kit) – specification-driven development that just launched in September 2025! Get professional-grade development workflows:

- **🏗️ Systematic Development**: `/specify` → `/plan` → `/tasks` → implement
- **🤖 AI-Native Workflow**: Works with Claude Code, GitHub Copilot, and other AI assistants  
- **📋 Professional Templates**: Complete specification and planning frameworks
- **🛡️ Constitutional Protection**: Built-in governance and architectural validation

[**📖 Complete Developer Guide →**](DEVELOPERS.md) • [**🛠️ Learn GitHub Spec-Kit →**](https://github.com/github/spec-kit)

### Try it in 30 seconds

```bash
# 1) Install + run
cargo install shimmy --features huggingface
shimmy serve &

# 2) See models and pick one
shimmy list

# 3) Smoke test the OpenAI API
curl -s http://127.0.0.1:11435/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{
        "model":"REPLACE_WITH_MODEL_FROM_list",
        "messages":[{"role":"user","content":"Say hi in 5 words."}],
        "max_tokens":32
      }' | jq -r '.choices[0].message.content'
```

## 🚀 Works with Your Existing Tools

**No code changes needed** - just change the API endpoint:

- **VSCode Extensions**: Point to `http://localhost:11435`
- **Cursor Editor**: Built-in OpenAI compatibility  
- **Continue.dev**: Drop-in model provider
- **Any OpenAI client**: Python, Node.js, curl, etc.

### Use with OpenAI SDKs

- Node.js (openai v4)

```ts
import OpenAI from "openai";

const openai = new OpenAI({
  baseURL: "http://127.0.0.1:11435/v1",
  apiKey: "sk-local", // placeholder, Shimmy ignores it
});

const resp = await openai.chat.completions.create({
  model: "REPLACE_WITH_MODEL",
  messages: [{ role: "user", content: "Say hi in 5 words." }],
  max_tokens: 32,
});

console.log(resp.choices[0].message?.content);
```

- Python (openai>=1.0.0)

```python
from openai import OpenAI

client = OpenAI(base_url="http://127.0.0.1:11435/v1", api_key="sk-local")

resp = client.chat.completions.create(
    model="REPLACE_WITH_MODEL",
    messages=[{"role": "user", "content": "Say hi i