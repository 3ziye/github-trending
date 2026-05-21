# ExecFence

Guard package-manager installs, dependency changes, CI, and agent-run commands before suspicious project code executes.

ExecFence is a local execution and supply-chain guardrail for JavaScript, Python, Rust, Go, JVM, .NET, PHP, Ruby, CI pipelines, package releases, and coding agents. It puts a reviewable fence in front of risky commands such as dependency installs, tests, builds, package scripts, publish steps, and agent-driven tool execution.

## Quick Start

Run a scan without installing globally:

```sh
npx --yes execfence scan
```

Guard a command before it runs:

```sh
npx --yes execfence run -- npm test
```

Enable project-local guardrails:

```sh
npx --yes execfence guard enable
npx --yes execfence guard enable --apply
```

Enable global package-manager interception for terminal and agent-run commands:

```sh
npx --yes execfence guard global-enable
```

## What Version 5 Adds

ExecFence v5 expands supply-chain coverage beyond npm and adds a real sandbox-helper contract in the same major release:

- Windows and Linux helper support through a Go supervisor binary
- `execfence-helper self-test` capability proof before enforce mode is allowed
- `execfence-helper run --policy <policy.json> -- <command>` as the only enforce-mode execution path
- helper manifests pinned by platform, arch, SHA-256, provenance, version, and self-test evidence
- truthful strict-mode blocking when filesystem, network, process-tree, sensitive-read, or new-executable containment is unavailable
- global shims for npm/pnpm/yarn/Bun, Python, Cargo, Go, Maven/Gradle, dotnet/NuGet, Composer, and Bundler package managers
- lifecycle-script suppression for npm-like install commands where package managers expose a reliable suppression flag
- dependency metadata and reputation review for changed packages
- OSV advisory checks without package-manager tokens or user credentials
- tarball integrity/content audit and tarball delta against the previous version
- `supplyChain.mode: "strict"` for CI/release workflows
- runtime dependency behavior audit with helper-backed enforcement when a verified helper proves the required capabilities
- unified coverage evidence across `coverage`, `manifest`, `ci`, and reports: `directGuarded` means the command itself invokes ExecFence; `covered` also counts workflow-level gates, package prehooks, and active global shims
- actionable report summaries that explain why ExecFence blocked, how the code can execute, the affected ecosystem, and the next remediation step
- `execfence config validate` for `.execfence/config/*` schemas, regex signatures, baselines, sandbox policy, and strict-mode coverage checks

Install-like commands such as `npm install`, `pnpm add`, `pip install`, `uv add`, `cargo add`, `go get`, `go install pkg@version`, `composer require`, and `bundle add` run through ExecFence first. When an ecosystem has a reliable lifecycle suppression flag, ExecFence delegates with scripts disabled. Ecosystems such as Go do not have a universal equivalent, so ExecFence uses preflight scan, dependency review, runtime behavior audit, and strict-mode containment checks instead of pretending scripts were disabled.

## Common Commands

| Command | What it does |
| --- | --- |
| `npx --yes execfence --help` | Prints the grouped command reference and examples. Use this to confirm the installed CLI supports the sandbox/helper commands you expect. |
| `npx --yes execfence scan` | Scans the current project before code runs. It blocks high-risk execution surfaces such as suspicious scripts, loaders, workflows, package hooks, and unexpected executable/archive artifacts. |
| `npx --yes execfence run -- npm test` | Runs a command behind ExecFence. It scans first, executes only if clean, records runtime evidence, snapshots file changes, rescans changed files, and writes a report. |
| `npx --yes execfence ci` | Runs the release/CI bundle: scan, manifest diff, dependency diff/review, coverage, config validation, package audit, and trust audit. |
| `npx --yes execfence deps review` | Reviews changed dependencies across npm/Bun/Yarn/pnpm, Python, Cargo, Go, JVM, NuGet, Composer, and Bundler manifests/lockfiles with metadata, reputation, integrity, source, and runtime-surface findings. |
| `npx --yes execfence coverage` | Shows whether sensitive entrypoints are covered by direct `execfence run`, package prehooks, workflow-level gates, or active global shims. |
| `npx --yes execfence config validate` | Validates `.execfence/config/*`, baselines, signatures, sandbox policy, and policy packs. It reports invalid regexes, expired baselines, unsafe allowlists, and strict-mode coverage gaps. |
| `npx --yes execfence pack-audit` | Audits files that would be shipped in the package handoff/release, catching dangerous scripts, unexpected binaries, archives, and suspicious publish inputs. |
| `npx --yes execfence agent-report` | Reviews agent, MCP, tool, and instruction-file surfaces for shell/filesystem/network/browser/creden