<p align="center">
  <img src="artifact-fs.png" alt="ArtifactFS" width="720">
</p>

# ArtifactFS

[![Build & Test](https://github.com/cloudflare/artifact-fs/actions/workflows/build-test.yml/badge.svg)](https://github.com/cloudflare/artifact-fs/actions/workflows/build-test.yml)

> This is a beta release of ArtifactFS. Your mileage may vary.

ArtifactFS is a Git-backed filesystem daemon (FUSE driver) in Go that mounts repositories as normal working trees while avoiding eager blob downloads.

It exposes the tree quickly, then hydrates file contents on demand. That makes it useful for sandboxes, agents, and other short-lived environments where waiting for a full clone is too expensive.

In practice:

* The operating system sees the full tree almost immediately, while the FUSE driver fetches file contents in the background. It prioritizes package manifests, dependency manifests, and source files ahead of large blobs.
* ArtifactFS is part of [Cloudflare Artifacts](http://workers.cloudflare.com/product/artifacts), a versioned filesystem that speaks git, but it also works with any git repo.
* ArtifactFS is optional. You can clone an Artifact repo directly, but larger repos still take time to clone. ArtifactFS lets you mount the repo and fetch blob contents as they are needed.

## What are Cloudflare Artifacts?

[Cloudflare Artifacts](https://workers.cloudflare.com/product/artifacts) is a versioned filesystem that speaks git. It is built for agent toolchains, sandboxes, and CI/CD systems that need fast access to code repositories.

ArtifactFS is the optional FUSE driver -- it lets you mount an Artifact (or any git repo) as a local filesystem without waiting for a full clone.

## Build and Install

Requires Go 1.24+ and a FUSE implementation:

- **macOS** -- [macFUSE](https://osxfuse.github.io/)
- **Linux** -- `fuse3` (`apt install fuse3` on Debian/Ubuntu, `dnf install fuse3` on Fedora)

Install the CLI from the module:

```bash
go install github.com/cloudflare/artifact-fs/cmd/artifact-fs@latest
```

Or build it directly from the module path:

```bash
go build -o artifact-fs github.com/cloudflare/artifact-fs/cmd/artifact-fs
```

Quick start against a public repo:

```bash
export ARTIFACT_FS_ROOT=/tmp/artifact-fs-test

# Register and clone (returns immediately)
./artifact-fs add-repo \
  --name workers-sdk \
  --remote https://github.com/cloudflare/workers-sdk.git \
  --branch main \
  --mount-root /tmp

# Start the daemon (mounts via FUSE, blocks until killed)
./artifact-fs daemon --root /tmp &
DAEMON_PID=$!

# Use the repo
ls /tmp/workers-sdk/
cat /tmp/workers-sdk/README.md
git -C /tmp/workers-sdk log --oneline -5

# Cleanup
kill $DAEMON_PID
```

## Monitoring hydration and repo status

Check the state of a mounted repo with `status`:

```bash
./artifact-fs status --name workers-sdk
# repo=workers-sdk state=mounted head=d4c61587... ref=main ahead=0 behind=0 diverged=false last_fetch=2026-03-27T12:00:00Z result=ok overlay_dirty=false
```

| Field | Meaning |
|-------|---------|
| `state` | `mounted` or `unmounted` |
| `head` | Current HEAD commit OID |
| `ref` | Tracked branch |
| `ahead` / `behind` | Commits ahead/behind the remote tracking branch |
| `overlay_dirty` | `true` if there are local writes (created, modified, or deleted files) |
| `last_fetch` / `result` | Timestamp and outcome of the last background fetch |

Hydration (blob downloading) is transparent: the file tree is visible immediately after mount, and reads block only until the requested blob is fetched. The daemon prioritizes code and manifests (`package.json`, `go.mod`, `README.md`) over binary files.

To monitor hydration activity, watch the daemon's JSON log output:

```bash
./artifact-fs daemon --root /tmp 2>/tmp/daemon.log &
# In another terminal:
tail -f /tmp/daemon.log | grep -i hydrat
```

Use `--hydration-concurrency` to control the number of parallel blob-fetch workers (default 4). Each worker maintains a persistent `git cat-file --batch` process, so higher values trade memory for faster bulk hydration:

```bash
./artifact-fs daemon --root /tmp --hydration-concurrency 8
```

## Sandboxes and Containers

[`examples/Dockerfile`](examples/Dockerfile) builds artifact-fs and starts a FUSE-mounted repo inside a container. The container requires `--cap-add SYS_ADMIN --device /dev/fuse` for FUSE access.

```bash
# Build the image
docker build -t artifact-fs-example -f examples/Dockerfile .

# Run with the default repo (cloudflare/workers-sdk)
docker run --rm --cap-add SYS_ADMIN --device /dev/fuse artifact-fs-example

# Run with a private repo
docker run --rm --cap-add SYS_ADMIN --device /dev/fuse \
  -e REPO_REMOTE_URL=https://<token>@github.com/org/private-repo.git \
  artifact-fs-example

# Run a command inside the mounted repo
docker run --rm --cap-add SYS_ADMIN --device /dev/fuse \
  artifact-fs-example git log --oneline -5
```

The entrypoint registers the repo, starts the daemon, waits for the mount, then either runs the provided command or