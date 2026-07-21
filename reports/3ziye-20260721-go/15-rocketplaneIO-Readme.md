<div align="center">

<h2>Full-stack Kubernetes observability —<br>that can safely fix things, too.</h2>

<p><b>Self-hosted · eBPF traces, logs & metrics, zero instrumentation · a safe MCP interface for AI agents · Apache-2.0 · air-gapped capable</b></p>

![Status](https://img.shields.io/badge/status-alpha-e5484d)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue)](LICENSE)
![Go](https://img.shields.io/badge/go-1.25+-00ADD8)

[**Quick start**](#quick-start) · [**Is it safe?**](#is-it-safe) · [**Under the hood**](#under-the-hood)

</div>

<br>

<a href=".github/assets/demo.mp4">
  <img alt="rocketplaneIO walkthrough: connect a cluster and the live service map draws itself in, then an external AI agent opens a transaction over MCP, acts on the cluster, a human approves the hard part — and one click rolls everything back" src=".github/assets/demo.gif" width="100%">
</a>

<br>

> **Alpha.** The full loop works end-to-end today, developed against minikube. APIs and schemas
> still change without notice — don't point it at production yet.

## Three things you don't get anywhere else

### 1 · Traces for services you never instrumented

One outbound-only agent plus an eBPF DaemonSet
([OTel eBPF Instrumentation](https://github.com/grafana/beyla), née Grafana Beyla). HTTP/gRPC
spans **with cross-service context propagation — including compiled Go binaries** — plus SQL,
Redis and Kafka client spans. No SDKs, no sidecars, no code changes.

<img alt="A real 500 investigated: the failure cascades across three services, correlated error logs on the right" src=".github/assets/shot-trace.png" width="100%">
<div align="center"><sub>A real 500 on <code>GET /checkout</code>: the failure cascades frontdoor → checkout → catalog,
the exact ERROR log lines are correlated on the right. <b>No SDK in any of these services.</b></sub></div>

### 2 · Logs, traces, metrics and topology — one dataset, not four tools

It's not four products bolted together. A log line is two clicks from its distributed trace. The
service map is drawn from **real eBPF traffic**, not a static config — tech logos matched from
container images, health live from RED metrics. PromQL runs on the actual Prometheus evaluation
engine, embedded, over ClickHouse. And the complete Kubernetes inventory — Services, Ingress,
ConfigMaps, policies, volumes — is synced and searchable right beside it. Everything self-hosted;
your telemetry never leaves your infrastructure.

<img alt="Live service map with automatic technology detection, drawn from real eBPF traffic" src=".github/assets/shot-servicemap.png" width="100%">
<div align="center"><sub><b>Service map</b> — topology from real traffic flows, not config. Healthy is calm
grey; only anomalies light up. The whole UI follows one instrument-panel design system (RETICLE).</sub></div>

### 3 · And it can fix what it finds — safely

Observability that stops at *"here's the problem"* leaves the hard part to you. rocketplaneIO
doesn't ship its own AI — it's the **MCP interface** your existing agent (Claude Code, Cursor,
anything that speaks MCP) connects to. The agent reads everything above, and acts through
kubectl-shaped primitives (`k8s_get` / `k8s_patch` / `k8s_apply` / `k8s_delete` / `k8s_exec` /
Starlark workflows) on **any resource, CRDs included**.

The guardrail is a transaction. **Nothing mutates outside one** — every change is snapshotted
durably *before* it commits, so cancel, timeout or a later **Revert** restores every before-state
in reverse (LIFO). Each operation is risk-classified by rocketplaneIO, not by the model:

| Level | Examples | Default policy |
|---|---|---|
| ◎ read | `k8s_get`, `k8s_list`, logs, traces, PromQL | runs immediately, no transaction |
| ↺ reversible | `k8s_patch`, `k8s_apply` (snapshot-backed) | runs inside the transaction |
| ◇ disruptive | `k8s_delete` on Pods/Jobs | **a human approves in the UI** |
| △ destructive | any other delete, `k8s_exec`, workflows, **scale-to-0** | **a human approves in the UI** |

Classification is parameter-aware (`replicas: 3` is reversible; `: 0` is destructive) and
fail-closed. Disruptive and destructive operations park until a human approves them — and an API
token can never approve its own proposals.

<img alt="A transaction timeline: every tool call, the parked approval, the human decision, and the rollback — one auditable spine" src=".github/assets/shot-transactions.png" width="100%">
<div align="center"><sub><b>Transactions</b> — the audit trail. What the agent read, what it
changed, who approved what, and <b>↺ revert</b> at run- or transaction-level. Cancel always
terminates — a reaper finalizes anything a dead agent leaves behind and drives the rollback to
its end.</sub></div>

## Quick start

You need Docker and a Kubernetes cluster to point it at (minikube is fine).

**1 — run the platform** (one command)

```bash
curl -fsSL https://rocketplane.io/install.sh | sh
```

That's the whole install: it downloads the compose bundle, genera