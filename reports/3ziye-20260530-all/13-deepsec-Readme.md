# deepsec

`deepsec` an agent-powered vulnerability scanner that you can run in your own infrastructure, optimized to perform on-demand review of all code in existing 
large-scale repos.

`deepsec` is designed to surface hard-to-find issues that have been lurking in applications for a long time. It is configured to use the best models at maximum thinking levels, meaning scans can cost thousands or even tens-of-thousands of dollars for large codebases. Our customers have found the cost worth it for how quickly they were able to patch vulnerabilities that would have otherwise gone unfixed.

For large codebases, work fans out across worker machines in parallel.
If a run is interrupted or errors out partway through, just re-run the same
command — deepsec picks up where it left off, skipping files it already
analyzed and only investigating the rest.

## Get started

Navigate to the root of the repository that you want to scan, then:

```bash
npx deepsec init       # creates .deepsec/ with this repo as the first project
cd .deepsec
pnpm install           # installs deepsec from npm

# Proceed as instructed by `init` output
```

Now have your coding agent bootstrap your installation. Open the agent of choice
and prompt:

> Read `.deepsec/node_modules/deepsec/SKILL.md` to understand the
> tool. Then read `.deepsec/data/<id>/SETUP.md` and follow it:
> skim this repo's README, any AGENTS.md/CLAUDE.md, and a handful
> of representative code files, then replace each section of
> `.deepsec/data/<id>/INFO.md`.
>
> Keep it SHORT — target 50–100 lines total. Pick 3–5 examples per
> section, not exhaustive enumeration. Name primitives (auth helpers,
> middleware) but no line numbers. Skip generic CWE categories —
> built-in matchers cover those. Cover only what's project-specific.
> INFO.md is injected into every scan batch; verbose context dilutes
> signal.

Then scan from inside `.deepsec/`:

```bash
pnpm deepsec scan
pnpm deepsec process    
pnpm deepsec revalidate # optional, cuts FP rate
pnpm deepsec export --format md-dir --out ./findings
```

If you feel like the `deepsec` should look at more parts of the code, give it [the writing matchers](docs/writing-matchers.md) doc to find more valuable starting points in your code base.

## Docs

- [docs/getting-started.md](docs/getting-started.md) — first-scan walkthrough
- [docs/reviewing-changes.md](docs/reviewing-changes.md) — `process --diff` for PR review and CI gating
- [docs/supported-tech.md](docs/supported-tech.md) — frameworks and ecosystems deepsec recognizes out of the box
- [docs/writing-matchers.md](docs/writing-matchers.md) — **prompt your coding agent to grow your matcher set**
- [docs/configuration.md](docs/configuration.md) — `deepsec.config.ts` reference
- [docs/plugins.md](docs/plugins.md) — plugin authoring
- [docs/models.md](docs/models.md) — model selection, defaults, refusals, future models
- [docs/vercel-setup.md](docs/vercel-setup.md) — AI Gateway + Vercel Sandbox keys / tokens
- [docs/architecture.md](docs/architecture.md) — pipeline internals
- [docs/data-layout.md](docs/data-layout.md) — `data/` schemas (FileRecord, RunMeta, …)
- [docs/faq.md](docs/faq.md) — cost, model choice, sandbox mode, FP rate
- [samples/](samples/) — copy-paste starting points (currently: `webapp/`)
- [CONTRIBUTING.md](CONTRIBUTING.md) — repo layout, dev workflow

## AI provider

When running locally, `deepsec` falls back to your existing `claude` /
`codex` subscription if you've logged in on this machine. Subscriptions
(Claude Pro/Max, ChatGPT Plus) are useful for evaluating deepsec but
generally don't have enough headroom for full repo scans.

For real scans, use Vercel AI Gateway. One key covers both Claude and
Codex, and the gateway's default quotas are sized for highly concurrent
research.

```
AI_GATEWAY_API_KEY=vck_...
```

See [docs/vercel-setup.md](docs/vercel-setup.md) for getting a key and
for the Vercel Sandbox setup. To bypass the gateway, set
`ANTHROPIC_AUTH_TOKEN` + `ANTHROPIC_BASE_URL` (or the OpenAI pair)
explicitly. Explicit values always win over the `AI_GATEWAY_API_KEY`
expansion.

If a `process` or `revalidate` run halts because the upstream credential
ran out of quota or credits, deepsec stops gracefully and tells you
where to top up. Re-run the same command afterward and it picks up
where it left off.

## Distributed execution (optional)

Large monorepos can fan work across [Vercel Sandbox](https://vercel.com/docs/vercel-sandbox) microVMs:

```bash
pnpm deepsec sandbox process --project-id my-app --sandboxes 10 --concurrency 4
```

Needs a Vercel account. The local working tree is tarballed and
uploaded; `.git` is excluded. Both OIDC tokens (local) and access
tokens (CI) are supported — see
[docs/vercel-setup.md](docs/vercel-setup.md).

## Security model of deepsec itself

Treat `deepsec` like a coding agent with full shell access on the enviroment that it is
running on. It is designed to run on trusted inputs (your source code) but you may still
be c