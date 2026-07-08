# kkRepo

[![CI](https://github.com/klboke/kkrepo/actions/workflows/ci.yml/badge.svg)](https://github.com/klboke/kkrepo/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/klboke/kkrepo)](https://github.com/klboke/kkrepo/releases)
[![License](https://img.shields.io/github/license/klboke/kkrepo)](LICENSE)
[![Container](https://img.shields.io/badge/ghcr.io-kkrepo-blue)](https://github.com/klboke/kkrepo/pkgs/container/kkrepo)
[![Security Policy](https://img.shields.io/badge/security-policy-green)](SECURITY.md)

**English** | [中文](README.cn.md)

kkRepo is an independent, self-hosted artifact repository for Maven, npm, PyPI, Go, Helm, Cargo/Rust, Docker/OCI, NuGet, RubyGems, Yum, and Raw artifacts.

The project implements client-visible compatibility and migration support for Sonatype Nexus Repository deployments, including the `/repository/<repo>/...` URL layout and compatible permission/authentication behavior where required for migration. kkRepo uses MySQL for metadata and shared runtime state, supports OSS/S3 blob storage, and is designed for multi-replica deployment.

<p align="center">
  <img src="docs/assets/kkrepo-project-map.svg" alt="kkRepo architecture: supported repository formats, protocol entrypoints, service replicas, storage, UI, and Nexus migration" width="100%">
</p>

## Trademark Notice

Sonatype, Nexus, and Nexus Repository are trademarks of Sonatype, Inc. kkRepo is an independent open source project and is not affiliated with, endorsed by, sponsored by, or connected to Sonatype, Inc. References to Sonatype Nexus Repository are used only to describe compatibility, migration, or interoperability.

## Quick Start

Start a local trial environment with the public release image and MySQL:

```bash
curl -fsSL https://raw.githubusercontent.com/klboke/kkrepo/main/scripts/quickstart.sh | bash
```

Open:

- Admin console: `http://127.0.0.1:19090/admin/`
- User browser: `http://127.0.0.1:19090/browse/`
- Health check: `http://127.0.0.1:19091/actuator/health`

On the first visit, create the initial `Local/admin` administrator password in the UI. The quickstart uses File blob storage for local trials; use OSS/S3 and your own encryption secrets for production.

If you prefer to inspect the script before running it, download `scripts/quickstart.sh` first and then run it with `bash`.

## Build And Deployment

Local quick start, Spring Boot executable jar, Docker image, archive package, production deployment architecture, resource sizing, and upgrade flow are documented in the [Build And Deployment Guide](docs/en/build-deployment-guide.md).

If kkRepo is deployed behind Nginx or another HTTPS reverse proxy, follow the [Nginx Reverse Proxy Notes](docs/en/nginx-reverse-proxy.md) so generated repository URLs, such as npm `dist.tarball`, keep the public `https://` scheme and host.

Local hot-reload development and testing are documented in the [Development Guide](docs/en/development-guide.md).

## Supported Capabilities

| Format | Repository types | Client publish/upload | Browse and search | Nexus migration |
| --- | --- | --- | --- | --- |
| Maven | hosted / proxy / group | Maven deploy, PUT upload, and admin UI upload | Supported | Hosted repositories are migrated by default; proxy repositories can be migrated optionally |
| npm | hosted / proxy / group | `npm publish`, dist-tag, and admin UI upload | Supported | Hosted repositories are migrated by default; proxy repositories can be migrated optionally |
| PyPI | hosted / proxy / group | twine upload and admin UI upload | simple index supported | Hosted repositories are migrated by default; proxy repositories can be migrated optionally |
| Go | proxy / group | Go module proxy is mainly read-only proxy; hosted upload is not supported | Supported | Proxy repositories can be migrated optionally |
| Helm | hosted / proxy | chart push, PUT upload, and admin UI upload | index.yaml supported | Hosted repositories are migrated by default; proxy repositories can be migrated optionally |
| Cargo / Rust | hosted / proxy / group | `cargo publish`, yank/unyank, `CargoToken` auth, and UI/API `.crate` upload | Sparse index and `cargo search` supported | Cargo repository migration is supported |
| Docker / OCI | hosted / proxy / group | Registry V2 login, hosted push/pull, proxy pull, group pull, OCI referrers, cleanup, and connector-port access | Manifest/tag/blob metadata supported | Hosted Docker repository data migration is supported through the Nexus Repository Data flow |
| NuGet | hosted / proxy / group | package push and admin UI upload | v3 service index / search supported | Hosted repositories are migrated by default; proxy repositories can be migrated optionally |
| RubyGems | hosted / proxy / group | gem push/yank and admin UI upload | Supported | Hosted repositories are migrated by default; proxy repositories can be migrated optionally |
| Yum | hosted / proxy / group | RPM upload and admin UI upload | repodata supported | Hosted reposi