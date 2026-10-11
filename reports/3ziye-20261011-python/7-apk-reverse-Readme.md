<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
    <img src="assets/banner-light.svg" alt="apk-reverse" width="100%">
  </picture>
</p>

<p align="center">
  <b>English</b> · <a href="README.zh-CN.md">简体中文</a>
</p>

<p align="center">
  <a href="https://github.com/newliver666/apk-reverse/stargazers"><img src="https://img.shields.io/github/stars/newliver666/apk-reverse?style=flat-square&label=stars&color=49454F" alt="stars"></a>
  <a href="https://github.com/newliver666/apk-reverse/network/members"><img src="https://img.shields.io/github/forks/newliver666/apk-reverse?style=flat-square&label=forks&color=49454F" alt="forks"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/newliver666/apk-reverse?style=flat-square&color=49454F" alt="license"></a>
  <img src="https://img.shields.io/badge/python-3.9%2B-49454F?style=flat-square&logo=python&logoColor=white" alt="python">
  <img src="https://img.shields.io/badge/platform-android-49454F?style=flat-square&logo=android&logoColor=white" alt="android">
  <a href="https://github.com/newliver666/apk-reverse/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/newliver666/apk-reverse/ci.yml?style=flat-square&label=ci&color=49454F" alt="ci"></a>
</p>

<p align="center">
  <a href="#what-it-is-good-at">Capabilities</a> · <a href="#structure">Structure</a> · <a href="#install">Install</a> · <a href="#requirements">Requirements</a> · <a href="#read-this-first">Failure catalogue</a> · <a href="#scope">Scope</a> · <a href="#repository-maintenance">Maintenance</a> · <a href="#disclaimer">Disclaimer</a>
</p>

# apk-reverse

An Agent Skill for Android APK reverse engineering, debloating, ad removal, surgical
dex patching, repacking, and runtime/server analysis.

It is a **skill**, not a tutorial: it is written to be loaded by an agent (Claude Code,
Codex, or any harness that supports the Agent Skills format) while it works, so it is
organized for progressive disclosure — a short decision-oriented `SKILL.md`, detailed
references loaded only when a step needs them, and parameterized scripts you can run
directly.

## How an agent is expected to consume this

`SKILL.md` is deliberately written as a **procedure with gates** rather than as advice, because the
observed failure mode is not ignorance — it is a model reading the whole thing, agreeing with it, and
then reasoning from first principles anyway.

So there are four things in the body that are meant to be *acted on*, not read:

- **Four override rules (R1–R4).** Where they conflict with the current plan, they win until evidence
  overrides them.
- **A symptom index.** Each row is a failure that has already been paid for. **A matching row is a
  stop signal**: load that file before running another command, rather than after a few more attempts.
  Reasoning past a known symptom is how the same hours get spent twice.
- **Four gates (G1–G4),** each an action with a pass criterion. "I understand the idea" does not clear
  a gate. They exist so that classification, environment truth and a control build happen *before*
  the first patch, not after the third failure.
- **A two-strike rule and stop conditions.** Two failures of the same shape mean the model is wrong,
  not the parameters. The third variant of a hypothesis that already failed twice is where rounds go
  to die.

And one thing at the end that is meant to be *withheld*: **"done"** has a definition (six items). A
clean log is not one of them. Anything short of all six is a checkpoint, and should be reported as a
checkpoint with what remains.

If you are an agent reading this: the cheapest possible first command is
`python skills/apk-reverse/scripts/doctor.py`. It tells you which of these tools exist here, which
scripts can actually run, and whether something in the environment is already poisoning your
measurements.

## What it is good at

- Deciding **fast** whether a request is even achievable client-side, instead of
  burning hours on a paywall that is enforced by a server.
- Deciding **what form the deliverable must take** before any work starts — an
  unrooted, self-contained artifact is a different problem from "make it work on this
  machine", and confusing the two is the most expensive drift in this domain.
- Choosing the **safest patch layer** for a given change, and avoiding the layers that
  break the app.
- Catching the repack failure that looks like success: an app that installs, launches and
  renders perfectly while **every signed request is rejected**, because the client derives its
  request-signing key from its own signing certificate.
- Separating **your own mistakes from the app's or the server's problems** — a
  feature-scoped failure (login, registration, payment) is often a TLS/certificate issue on
  one code path, not a consequence of the patch you just built. Device state, a dead device
  server and clock drift masquerade the same