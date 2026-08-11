<p align="center">
  <img src="docs/assets/machine-genome-mark.svg" width="88" height="88" alt="Machine Genome mark">
</p>

# Machine Genome

[![Conformance](https://github.com/paxlabs-inc/machine-genome/actions/workflows/ci.yml/badge.svg)](https://github.com/paxlabs-inc/machine-genome/actions/workflows/ci.yml)
[![CodeQL](https://github.com/paxlabs-inc/machine-genome/actions/workflows/codeql.yml/badge.svg)](https://github.com/paxlabs-inc/machine-genome/actions/workflows/codeql.yml)
[![Go Reference](https://pkg.go.dev/badge/github.com/paxlabs-inc/machine-genome.svg)](https://pkg.go.dev/github.com/paxlabs-inc/machine-genome)
[![License: Apache-2.0](https://img.shields.io/badge/code-Apache--2.0-blue.svg)](LICENSE)
[![Protocol: experimental](https://img.shields.io/badge/protocol-experimental-8b5cf6.svg)](docs/versioning.md)

**Other languages:** [Русский](README.ru.md) · [Português](README.pt.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [हिन्दी](README.hi.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md)

---

Machine Genome is an open identity and provenance protocol for models, agents,
harnesses, datasets, and the artifacts that connect them. Every immutable,
signed genesis record receives a content-addressed **Gene**. Genes form a
verifiable lineage graph; later amendments and third-party attestations add
evidence without rewriting history.

**Live registry:** [machinegenome.org](https://machinegenome.org) ·
**Protocol:** [MGS 0.2.0 implementation profile](spec/MGS-0.2.0-implementation-profile.md) ·
**API:** [OpenAPI 3.1](api/openapi.json)

> [!IMPORTANT]
> MGS is an experimental interoperability profile and this repository is one
> reference implementation. A record proves who signed a claim and what bytes
> were committed; it does not prove inherited capability, consciousness,
> ownership, vendor endorsement, or legal status.

## Why this exists

Modern agents are assembled from model weights, prompts, scaffolds, tools,
datasets, and runtime policy. Names alone cannot answer which exact components
were used, who asserted the relationship, or whether the evidence changed.
Machine Genome provides:

- **stable identity** — a Gene is a SHA-256 multihash of a secured canonical
  genesis record;
- **agent identity** — every agent receives a full Gene-backed Agent ID plus a
  claimed given name and genome-derived unique family name;
- **agent discovery** — signed capability and training-data declarations let
  agents advertise strengths while preserving evidence and trust boundaries;
- **explicit lineage** — typed parent edges distinguish authorized,
  operator-observed, and unresolved relationships;
- **cryptographic accountability** — W3C `eddsa-jcs-2022` proofs bind records
  to controller DIDs;
- **append-only evolution** — ordered amendments and independent attestations
  add history without mutating genesis;
- **public transparency** — registries provide canonical bytes, inclusion and
  consistency proofs, signed checkpoints, conflict evidence, and tombstones.

The implementation has no dependency on a blockchain, a specific model vendor,
Prometheus, Matrix, or a proprietary DID resolver. The current profile resolves
Ed25519 `did:key` identities offline.

## What is included

| Area | Deliverable |
| --- | --- |
| Protocol | Byte-exact MGS `0.2.0` profile with `0.1.1` verification compatibility |
| Go library | Strict JCS, multihash Genes, Data Integrity, lineage, amendments, attestations |
| Registry | ACID storage, verified admission, DNS namespace control, Merkle log, audit chain |
| Explorer | Responsive, plain-language identity, lineage, artifact, and proof views |
| CLI | Key generation, authoring, signing, verification, digest, backup, and integrity tools |
| Contracts | JSON Schemas, OpenAPI 3.1 document, and machine-readable conformance vectors |
| Operations | Hardened systemd, nginx/Cloudflare, container, backup, restore, and monitoring assets |

See [project status](docs/status.md) for the precise implemented, validated, and
deferred boundaries.

## Quick start

Requirements: Go 1.24 or newer, GNU Make, and `jq`.

```sh
git clone https://github.com/paxlabs-inc/machine-genome.git
cd machine-genome
make check build

bin/mgs keygen --out controller.key.json
bin/mgs init-genesis \
  --key controller.key.json \
  --name cody \
  --namespace example.org \
  --subject-type agent \
  --given-name Cody \
  --version 1.0.0 \
  --out genesis.unsigned.json
bin/mgs sign \
  --in genesis.unsigned.json \
  --key controller.key.json \
  --out genesis.json
bin/mgs verify --in genesis.json
bin/mgs gene --in genesis.json
```

Private key files are created with mode `0600`. Never commit keys, registry
tokens, or private evidence.

### Run a local registry

```sh
bin/mgs keygen --out registry-checkpoint.key.json
umask 077
openssl rand -hex 32 > admin.token

bin/mgs registry-serve \
  --data-dir ./registry-data \
  --checkpoint-key registry-checkpoint.key.json \
  --admin-tok