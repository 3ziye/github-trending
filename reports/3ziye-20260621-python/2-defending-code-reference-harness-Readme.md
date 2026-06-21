# Defending Code Reference Harness

A reference implementation for autonomous vulnerability discovery and
remediation with Claude, based on our learnings from [partnering with security
teams at several organizations](https://www.anthropic.com/glasswing)
since launching Claude Mythos Preview. For a write up of these learnings along with
best practices, see the [accompanying blog post](https://claude.com/blog/using-llms-to-secure-source-code)
(also available in [`blog-post.md`](docs/blog-post.md)). For a lightweight SDK-only 
walkthrough of the same recon → find → triage → report → patch loop, see the 
[companion cookbook](https://platform.claude.com/cookbook/claude-agent-sdk-06-the-vulnerability-detection-agent).

This repo is not maintained and is not accepting contributions.

> 🔒 **Want a managed option?** Anthropic offers
> [Claude Security](https://claude.com/product/claude-security), a hosted product
> that finds and fixes vulnerabilities in your source code across multiple
> projects. Claude Security scans your repository for vulnerabilities,
> applies a multi-stage verification pipeline to reduce false positives, and
> lets you manage findings through their lifecycle: triage, fix validation,
> and rapid fix generation.
>
> This repository is an open-source reference implementation based on general
> best practices for finding vulnerabilities using Claude. You can use it to
> build your own vulnerability finding pipeline, customize the logic, and it
> can be used with whatever access you have to Claude APIs (including
> Bedrock, Vertex, or Azure).

## Contents

- **Claude Code skills**: `/quickstart`, `/threat-model`, `/vuln-scan`,
  `/triage`, `/patch`, `/customize`: interactive scoping, scanning, triage,
  and patching. Open this repo in Claude Code and run `/quickstart` to get
  oriented.
- **`harness/`**: the autonomous reference pipeline (recon → find → verify
  → report → patch), configured for finding C/C++ memory vulnerabilities
  using Docker and ASAN. This harness is a **reference, not a product**. 
  The general shape, prompts, and sandboxing are reusable, but the harness
  will not work on every codebase out of the box. Run `/customize` to port it 
  to your language, detector, or vuln class.

> ⚠️ **Security:** `/quickstart`, `/threat-model`, `/vuln-scan`, and `/triage`
> only read and write files. Running `/patch` on static findings (`TRIAGE.json`
> or `VULN-FINDINGS.json`) is likewise read- and write-only. `/customize` edits
> the harness code and runs validation commands. Any of these skills are safe to
> run unsandboxed, as long as you review and approve each tool use in Claude Code.
> The autonomous reference pipeline (including `/patch` on pipeline results)
> **executes target code**, so it refuses to run outside of a gVisor sandbox
> unless explicitly overridden. To get set up, run `scripts/setup_sandbox.sh` once,
> then invoke the pipeline via `bin/vp-sandboxed`. See [docs/security.md](docs/security.md)
> and [docs/agent-sandbox.md](docs/agent-sandbox.md) for more details.

## Getting Started

```bash
git clone https://github.com/anthropics/defending-code-reference-harness
cd defending-code-reference-harness
claude

# 30-sec intro + guided first run on the canary target
> /quickstart

> /quickstart how do I port the pipeline to Java?
> /quickstart how do I triage all these bugs?
```

## Further Reading

- [**Blog Post**](docs/blog-post.md) · The accompanying blog post with learnings + best practices
- [**Pipeline**](docs/pipeline.md) · How it works: diagram, stages, CLI flags
- [**Security**](docs/security.md) · Sandboxing, what not to mount
- [**Agent sandbox**](docs/agent-sandbox.md) · gVisor isolation + egress allowlist for every agent
- [**Customize**](docs/customizing.md) · Port to my stack; which files change and why
- [**Patching**](docs/patching.md) · Generate and verify fixes for verified crashes
- [**Troubleshooting**](docs/troubleshooting.md) · Duplicates, rate limits, subagent model pinning
- [**Safeguards**](https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude) · Block for dangerous cyber work

---

## Ramp Up

The most successful security teams we've partnered with are those 
that have gotten hands-on the fastest. Though it's tempting to 
spend months designing the perfect pipeline, we recommend starting
small on Day 1 and building from there as learnings come. The
steps below follow that pattern and set an ambitious (but reasonable)
pace based on what we've seen.

|                                                                                     |              |                                                              |
|-------------------------------------------------------------------------------------|--------------|--------------------------------------------------------------|
| [Step 1](#step-1-day-1-build-a-threat-model-and-run-your-first-static-scan--triage) | **Day 1**    | Build a threat model and run your first stati