<div align="center">

<a href="https://www.testsprite.com">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/testsprite-logo-dark.png">
    <source media="(prefers-color-scheme: light)" srcset="assets/testsprite-logo-light.png">
    <img src="assets/testsprite-logo-light.png" alt="TestSprite" width="420">
  </picture>
</a>

### The verification layer for the agentic coding era.

AI ships code in minutes — verifying it hasn't. `testsprite` opens your live app, uses it like a real user, and shows your coding agent exactly what broke — so it fixes its own work before a bug ever reaches you.

<sub><b>Proof, in public: verification beats model size.</b> With this CLI in the loop, the cheapest model in the field shipped the most correct app on an open leaderboard — <b>89%</b>, at half the cost of the priciest one. <a href="https://codercup.ai">See the leaderboard →</a></sub>

<p>
  <a href="https://www.npmjs.com/package/@testsprite/testsprite-cli"><img src="https://img.shields.io/npm/v/@testsprite/testsprite-cli?color=19C379&label=npm" alt="npm version"></a>
  <a href="https://www.npmjs.com/package/@testsprite/testsprite-cli"><img src="https://img.shields.io/npm/dm/@testsprite/testsprite-cli?color=19C379&label=downloads" alt="npm downloads"></a>
  <a href="#quickstart"><img src="https://img.shields.io/badge/node-20.19%2B%20%7C%2022.13%2B%20%7C%2024%2B-19C379" alt="Node 20.19+, 22.13+, or 24+"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/license-Apache%202.0-0A0A0A" alt="License Apache 2.0"></a>
  <a href="https://github.com/TestSprite/testsprite-cli/actions/workflows/ci.yml"><img src="https://github.com/TestSprite/testsprite-cli/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
</p>

<p>
  <a href="https://www.testsprite.com"><img src="https://img.shields.io/badge/testsprite.com-19C379?style=for-the-badge&logoColor=white" alt="Website"></a>
  <a href="https://www.testsprite.com/docs"><img src="https://img.shields.io/badge/Docs-0A0A0A?style=for-the-badge" alt="Docs"></a>
  <a href="https://x.com/Test_Sprite"><img src="https://img.shields.io/badge/Follow%20on%20X-000000?style=for-the-badge&logo=x&logoColor=white" alt="Follow on X"></a>
  <a href="https://www.linkedin.com/company/testsprite"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="https://discord.gg/W4JDrZfdB"><img src="https://img.shields.io/badge/Join%20our%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Join our Discord"></a>
</p>

⭐ _Help us reach more developers and grow the TestSprite community. Star this repo!_

</div>

<video src="https://github.com/user-attachments/assets/eca90a91-93ef-49f6-8d13-86b4eb25f4cf" controls muted></video>

<p align="center"><sub><b><a href="https://github.com/user-attachments/assets/eca90a91-93ef-49f6-8d13-86b4eb25f4cf">▶ Watch the launch video</a></b> — the three hard limits every coding agent hits, and the loop that breaks them (4 min).</sub></p>

---

## What is it?

[TestSprite](https://www.testsprite.com) is the AI testing platform 100,000+ teams use to test their software, frontend and backend — in the cloud, against the live product, not mocks. This repo is its official CLI.

It puts that platform in your coding agent's hands: the agent verifies every behavior it ships, and what broke comes back as **one self-consistent bundle** it can act on — no dashboard scraping. Humans drive the same surface from a terminal or CI.

## ⭐️ Star the Repository

<img width="900" height="506" alt="testsprite-repo-star-fast" src="https://github.com/user-attachments/assets/8c3975df-8d47-4d6c-a485-135b80f779a5" />

If you find `testsprite` useful, a GitHub Star ⭐️ would be greatly appreciated — it helps other builders (and their agents) find the project, and stars notify you about new releases.

## Quickstart

Requires **Node.js 20.19+**, **22.13+**, or **24+**. (No global install? `npx @testsprite/testsprite-cli` works too.)

```bash
npm install -g @testsprite/testsprite-cli
testsprite setup
```

`testsprite setup` prompts for your [API key](https://www.testsprite.com), verifies it, and installs the verification-loop skill for your coding agent (`claude`, `cursor`, `cline`, `windsurf`, `antigravity`, `codex`, etc.) — one command, so your agent is wired to verify its own work. Non-interactive (CI / onboarding scripts):

```bash
TESTSPRITE_API_KEY=sk-... testsprite setup --from-env --yes --agent claude
```

> **Pointing a coding agent (Claude Code, Cursor, Codex, Cline, …) at TestSprite?** Have it run `testsprite setup` first — that installs the verification skill, so the agent knows how to create, run, and triage tests on its own (instead of guessing from this README). New here? Start with the **[getting-started overview](https://docs.testsprite.com/cli/getting-started/overview)**.

> **Privacy note:** interactive runs check the npm registry at most once per 24 h to offer a "n