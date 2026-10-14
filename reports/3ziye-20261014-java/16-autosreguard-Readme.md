# AutoSREGuard

[![ci](https://github.com/sauravgoel/autosreguard/actions/workflows/ci.yml/badge.svg)](https://github.com/sauravgoel/autosreguard/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**SRE tooling for reliable, cost-efficient AI inference.**

AutoSREGuard is a control-plane library and service for teams running LLM inference fleets. It
watches what users actually experience, per segment and per tenant, forecasts demand before it
arrives, diagnoses incidents against recent changes, and remediates them with graduated
autonomy: it acts alone only when it is confident, asks first when it is not, and keeps a
reversible audit trail either way.

It is written in Java 21 with **zero runtime dependencies**.

---

## Why

At very large scale, averages lie. A fleet can be at "five nines" while an important customer
is having a terrible day, because their failures are a rounding error in the global number.
Meanwhile, GPU inference adds failure modes classic tooling doesn't see: slow thermal decline,
KV-cache memory pressure, quality regressions that don't show up as errors, and replicas that
take minutes to warm up.

AutoSREGuard turns five reliability lessons into code:

| Lesson | Where it lives |
|---|---|
| Reliability is contextual: segment, don't average | `slo` — per-segment and per-tenant SLOs, burn-rate alerts, `MASKED-BY-AGGREGATE` flag |
| Predict demand; autoscaling is table stakes | `forecast`, `capacity` — Holt-Winters + event signals, warm-up-aware planner, GPU bin packing |
| Automate the repetitive; humans for the novel | `detection`, `diagnosis`, `remediation` — detect → diagnose → remediate with confidence tiers |
| Every automated action is logged, explainable, reversible | `remediation.AuditLog`, `RemediationAction.inverse()`, `OscillationGuard` |
| GenAI infrastructure needs its own playbook | `inference`, `gpu`, `canary`, `shadow` — degradation ladder, cache-aware routing, GPU health, quality canaries |

## Quickstart

Requirements: JDK 21, Maven 3.9+.

```bash
git clone https://github.com/sauravgoel/autosreguard.git
cd autosreguard
mvn -B verify                                        # build + 133 tests
java -jar target/autosreguard-0.1.0-SNAPSHOT.jar --scenario=all
```

Run a single scenario:

```bash
java -jar target/autosreguard-0.1.0-SNAPSHOT.jar --scenario=bad-deploy
```

Run the long-lived service (control loop + admin API) against simulated traffic:

```bash
java -jar target/autosreguard-0.1.0-SNAPSHOT.jar --serve --config=config/autosreguard.properties
curl localhost:9464/v1/slo
curl localhost:9464/metrics
```

Or with Docker:

```bash
docker build -t autosreguard .
docker run --rm -p 9464:9464 autosreguard
```

## The scenarios

Each scenario is deterministic (manual clock, seeded randomness), prints a narrated timeline,
and is asserted in `ScenarioSmokeTest`, so the demo cannot silently drift from the code.

| Scenario | What you will see |
|---|---|
| `hidden-tenant` | 100 enterprise tenants; one fails 4% of requests. The segment SLO is green; that tenant pages, flagged `MASKED-BY-AGGREGATE`. |
| `bad-deploy` | A deploy breaks a model pool. Diagnosis blames it with 0.91 confidence and AutoSREGuard rolls it back in about a minute with no human. A second bad config change minutes later is held by the cooldown guardrail and a human is paged; it is proposed and executed only after the cooldown. |
| `gpu-degradation` | One GPU node slowly overheats: AutoSREGuard proposes a drain and executes it when the veto window lapses. Another node throws an uncorrectable ECC error: drained immediately. Workloads are re-packed onto healthy nodes. |
| `predictive-scaling` | A product launch doubles demand. Reactive scaling is short for two intervals while replicas warm up; the event-aware forecaster has capacity ready in advance. |
| `graceful-degradation` | Pressure ramps on the flagship model. Consumer traffic moves to a quantized variant first; enterprise keeps the flagship until its latency budget is truly at risk. A tripped breaker degrades rather than errors. Includes shedding and prefix-cache routing comparisons. |
| `canary` | A new model is faster and equally reliable but worse. Error/latency checks would promote it; the quality gate rolls it back. |
| `shadow` | A proposed, more aggressive autonomy policy runs in shadow. It disagrees with the incumbent 20% of the time and stays in shadow; a minor retune agrees 99% of the time and becomes eligible for review. |

## Architecture

```
            telemetry (outcomes, signals, GPU stats)          change events (CI/CD, config)
                         |                                              |
     +-------------------v-------------------+                          |
     |  SegmentedSloTracker   Detectors      |                          |
     |  GpuHealthScorer                      |                          |
     +-------------------+-------------------+                   