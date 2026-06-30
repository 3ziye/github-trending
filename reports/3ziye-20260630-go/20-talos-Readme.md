<!-- Follow-up: upload talos.svg to ory/meta:static/banners/talos.svg. -->
<h1 align="center">
  <img src="https://raw.githubusercontent.com/ory/meta/master/static/banners/talos.svg" alt="Ory Talos - API credential management for high-throughput systems">
</h1>

<h4 align="center">
  <a href="https://www.ory.com/chat">Chat</a> ·
  <a href="https://github.com/ory/talos/discussions">Discussions</a> ·
  <a href="https://www.ory.com/l/sign-up-newsletter">Newsletter</a> ·
  <a href="https://www.ory.com/docs/">Docs</a> ·
  <a href="https://console.ory.sh/">Try Ory Network</a> ·
  <a href="https://www.ory.com/jobs/">Jobs</a>
</h4>

Ory Talos is a scalable and secure API key server optimized for low-latency verification, horizontal
scaling, and predictable operations. It follows established security best-practices for API keys and
issues, verifies, revokes, and derives API keys and short-lived tokens for high-throughput systems.

---

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [What is Ory Talos?](#what-is-ory-talos)
  - [Why Ory Talos](#why-ory-talos)
- [Deployment options](#deployment-options)
  - [Use Ory Talos on the Ory Network](#use-ory-talos-on-the-ory-network)
  - [Self-host Ory Talos](#self-host-ory-talos)
- [Quickstart](#quickstart)
- [Who is using Ory Talos](#who-is-using-ory-talos)
- [Ecosystem](#ecosystem)
  - [Ory Kratos: Identity and User Infrastructure and Management](#ory-kratos-identity-and-user-infrastructure-and-management)
  - [Ory Hydra: OAuth2 & OpenID Connect Server](#ory-hydra-oauth2--openid-connect-server)
  - [Ory Oathkeeper: Identity & Access Proxy](#ory-oathkeeper-identity--access-proxy)
  - [Ory Keto: Access Control Policies as a Server](#ory-keto-access-control-policies-as-a-server)
- [Documentation](#documentation)
- [Developing Ory Talos](#developing-ory-talos)
- [Security](#security)
  - [Disclosing vulnerabilities](#disclosing-vulnerabilities)
- [Telemetry](#telemetry)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## What is Ory Talos?

Ory Talos is a server for issuing, verifying, and managing API keys. It follows
[cloud architecture best practices](https://www.ory.com/docs/ecosystem/software-architecture-philosophy)
and focuses on:

- Issuing, verifying, and revoking API keys at scale
- Importing externally-issued API keys for unified verification
- Deriving short-lived JWT and macaroon tokens from long-lived keys
- Side-car deployment for fast API key verification
- Low-latency verification with caching and eventual revocation
- Predictable operations through structured logging, metrics, and tracing

We recommend starting with the [Ory Talos documentation](https://www.ory.com/docs/talos) to learn
more about its architecture, feature set, and how it compares to other systems.

### Why Ory Talos

Ory Talos is designed to:

- Run as a single binary with three deployment modes: admin, self-service, or all-in-one
- Verify API keys against the database with caching for low latency, while derived JWT and macaroon
  tokens verify offline without a database lookup
- Separate admin and self-service surfaces so key creation, revocation, derivation, and verification
  scale and are secured independently from proof-of-possession self-revocation
- Scale horizontally with external databases (Postgres, MySQL, CockroachDB) and optional distributed
  caching
- Fit modern cloud-native environments such as Kubernetes and managed platforms
- Mint reduced-scope, short-lived tokens offline so agents, CI/CD jobs, and services don't call the
  server on every request
- Keep credential routing, hashing, and verification centralized and constant-time

## Deployment options

You can run Ory Talos in two main ways:

- As a managed service on the Ory Network
- As a self-hosted service under your own control, with or without the Ory Enterprise License

### Use Ory Talos on the Ory Network

The [Ory Network](https://www.ory.com/network) is the fastest way to use Ory Talos in production.

The Ory Network provides:

- API key issuance, verification, and derivation with low-latency global edge
- OAuth2 and OpenID Connect for single sign on, API access, and machine to machine authorization
- Identity and credential management that scales to billions of users and devices
- Registration, login, and account management flows for passkeys, biometrics, social login, SSO, and
  multi factor authentication
- Prebuilt login, registration, and account management pages and components
- Low latency permission checks based on the Zanzibar model with the Ory Permission Language
- GDPR friendly storage with data locality and compliance in mind
- Web based Ory Console and Ory CLI for administration and operations
- Cloud native APIs compatible with the open source servers
- Fair, usage based [pricing](https://www.ory.com/pricing)

Sign up for a
[free developer account](https://console.or