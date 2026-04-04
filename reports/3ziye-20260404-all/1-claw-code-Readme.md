# Rewriting Project Claw Code

<p align="center">
  <strong>⭐ The fastest repo in history to surpass 50K stars, reaching the milestone in just 2 hours after publication ⭐</strong>
</p>

<p align="center">
  <a href="https://star-history.com/#instructkr/claw-code&Date">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=instructkr/claw-code&type=Date&theme=dark" />
      <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=instructkr/claw-code&type=Date" />
      <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=instructkr/claw-code&type=Date" width="600" />
    </picture>
  </a>
</p>

<p align="center">
  <img src="assets/clawd-hero.jpeg" alt="Claw" width="300" />
</p>

<p align="center">
  <strong>Better Harness Tools, not merely storing the archive of leaked Claw Code</strong>
</p>

<p align="center">
  <a href="https://github.com/sponsors/instructkr"><img src="https://img.shields.io/badge/Sponsor-%E2%9D%A4-pink?logo=github&style=for-the-badge" alt="Sponsor on GitHub" /></a>
</p>

> [!IMPORTANT]
> **Rust port is now in progress** on the [`dev/rust`](https://github.com/instructkr/claw-code/tree/dev/rust) branch and is expected to be merged into main today. The Rust implementation aims to deliver a faster, memory-safe harness runtime. Stay tuned — this will be the definitive version of the project.

> If you find this work useful, consider [sponsoring @instructkr on GitHub](https://github.com/sponsors/instructkr) to support continued open-source harness engineering research.

---

## Rust Port

The Rust workspace under `rust/` is the current systems-language port of the project.

It currently includes:

- `crates/api-client` — API client with provider abstraction, OAuth, and streaming support
- `crates/runtime` — session state, compaction, MCP orchestration, prompt construction
- `crates/tools` — tool manifest definitions and execution framework
- `crates/commands` — slash commands, skills discovery, and config inspection
- `crates/plugins` — plugin model, hook pipeline, and bundled plugins
- `crates/compat-harness` — compatibility layer for upstream editor integration
- `crates/claw-cli` — interactive REPL, markdown rendering, and project bootstrap/init flows

Run the Rust build:

```bash
cd rust
cargo build --release
```

## Backstory

At 4 AM on March 31, 2026, I woke up to my phone blowing up with notifications. The Claw Code source had been exposed, and the entire dev community was in a frenzy. My girlfriend in Korea was genuinely worried I might face legal action from the original authors just for having the code on my machine — so I did what any engineer would do under pressure: I sat down, ported the core features to Python from scratch, and pushed it before the sun came up.

The whole thing was orchestrated end-to-end using [oh-my-codex (OmX)](https://github.com/Yeachan-Heo/oh-my-codex) by [@bellman_ych](https://x.com/bellman_ych) — a workflow layer built on top of OpenAI's Codex ([@OpenAIDevs](https://x.com/OpenAIDevs)). I used `$team` mode for parallel code review and `$ralph` mode for persistent execution loops with architect-level verification. The entire porting session — from reading the original harness structure to producing a working Python tree with tests — was driven through OmX orchestration.

The result is a clean-room Python rewrite that captures the architectural patterns of Claw Code's agent harness without copying any proprietary source. I'm now actively collaborating with [@bellman_ych](https://x.com/bellman_ych) — the creator of OmX himself — to push this further. The basic Python foundation is already in place and functional, but we're just getting started. **Stay tuned — a much more capable version is on the way.**

The Rust port was developed with both [oh-my-codex (OmX)](https://github.com/Yeachan-Heo/oh-my-codex) and [oh-my-opencode (OmO)](https://github.com/code-yeongyu/oh-my-openagent): OmX drove scaffolding, orchestration, and architecture direction, while OmO was used for later implementation acceleration and verification support.

https://github.com/instructkr/claw-code

![Tweet screenshot](assets/tweet-screenshot.png)

## The Creators Featured in Wall Street Journal For Avid Claw Code Fans

I've been deeply interested in **harness engineering** — studying how agent systems wire tools, orchestrate tasks, and manage runtime context. This isn't a sudden thing. The Wall Street Journal featured my work earlier this month, documenting how I've been one of the most active power users exploring these systems:

> AI startup worker Sigrid Jin, who attended the Seoul dinner, single-handedly used 25 billion of Claw Code tokens last year. At the time, usage limits were looser, allowing early enthusiasts to reach tens of billions of tokens at a very low cost.
>
> Despite his countless hours with Claw Code, Jin isn't faithful to any one AI lab. The tools availa