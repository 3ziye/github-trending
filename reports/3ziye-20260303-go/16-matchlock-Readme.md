# Matchlock

> **Experimental:** This project is still in active development and subject to breaking changes.

Matchlock is a CLI tool for running AI agents in ephemeral microVMs - with network allowlisting, secret injection via MITM proxy, and VM-level isolation. Your secrets never enter the VM.

## Why Matchlock?

AI agents need to run code, but giving them unrestricted access to your machine is a risk. Matchlock lets you hand an agent a full Linux environment that boots in under a second - isolated and disposable.

When you pass `--allow-host` or `--secret`, Matchlock seals the network - only traffic to explicitly allowed hosts gets through, and everything else is blocked. When your agent calls an API the real credentials are injected in-flight by the host. The sandbox only ever sees a placeholder. Even if the agent is tricked into running something malicious your keys don't leak and there's nowhere for data to go. Inside the agent gets a full Linux environment to do whatever it needs. It can install packages and write files and make a mess. Outside your machine doesn't feel a thing. Volume overlay mounts are isolated snapshots that vanish when you're done. Same CLI and same behaviour whether you're on a Linux server or a MacBook.

## Quick Start

### System Requirements

- **Linux** with KVM support
- **macOS** on Apple Silicon

### Install

```bash
brew tap jingkaihe/essentials
brew install matchlock
```

### Usage

```bash
# Basic
matchlock run --image alpine:latest cat /etc/os-release
matchlock run --image alpine:latest -it sh
matchlock run --image alpine:latest --no-network -- sh -lc 'echo offline'

# Network allowlist
matchlock run --image python:3.12-alpine \
  --allow-host "api.openai.com" python agent.py

# Keep interception enabled even with an empty allowlist,
# so hosts can be added/removed at runtime.
matchlock run --image alpine:latest --rm=false --network-intercept
matchlock allow-list add <vm-id> api.openai.com,api.anthropic.com
matchlock allow-list delete <vm-id> api.openai.com

# Secret injection (never enters the VM)
export ANTHROPIC_API_KEY=sk-xxx
matchlock run --image python:3.12-alpine \
  --secret ANTHROPIC_API_KEY@api.anthropic.com python call_api.py

# Long-lived sandboxes
matchlock run --image alpine:latest --rm=false   # prints VM ID
matchlock run --image nginx:latest -d             # same as above, detached
matchlock exec vm-abc12345 -it sh                # attach to it
matchlock port-forward vm-abc12345 8080:8080     # forward host:8080 -> guest:8080

# Publish ports at startup
matchlock run --image alpine:latest --rm=false -p 8080:8080

# Lifecycle
matchlock list | kill | rm | prune

# Build from Dockerfile (uses BuildKit-in-VM)
matchlock build -f Dockerfile -t myapp:latest .

# Pre-build rootfs from registry image (caches for faster startup)
matchlock build alpine:latest

# Image management
matchlock image ls                                           # List all images
matchlock image rm myapp:latest                              # Remove a local image
docker save myapp:latest | matchlock image import myapp:latest  # Import from tarball
```

## SDK

Matchlock ships Go, Python, and TypeScript SDKs for embedding sandboxes directly in your application. You can launch VMs, execute commands, stream output, and manage files programmatically.

**Go**

```go
package main

import (
	"context"
	"fmt"
	"os"

	"github.com/jingkaihe/matchlock/pkg/sdk"
)

func main() {
	ctx := context.Background()

	client, err := sdk.NewClient(sdk.DefaultConfig())
	if err != nil {
		panic(err)
	}
	defer client.Close(0)
	defer client.Remove()

	sandbox := sdk.New("alpine:latest").
		AllowHost("dl-cdn.alpinelinux.org", "api.anthropic.com").
		AddSecret("ANTHROPIC_API_KEY", os.Getenv("ANTHROPIC_API_KEY"), "api.anthropic.com")
	if _, err := client.Launch(sandbox); err != nil {
		panic(err)
	}
	if _, err := client.Exec(ctx, "apk add --no-cache curl"); err != nil {
		panic(err)
	}
	// The VM only ever sees a placeholder - the real key never enters the sandbox
	result, err := client.Exec(ctx, "echo $ANTHROPIC_API_KEY")
	if err != nil {
		panic(err)
	}
	fmt.Print(result.Stdout) // prints "SANDBOX_SECRET_a1b2c3d4..."

	curlCmd := `curl -s --no-buffer https://api.anthropic.com/v1/messages \
  -H "content-type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{"model":"claude-haiku-4-5-20251001","max_tokens":1024,"stream":true,
       "messages":[{"role":"user","content":"Explain TCP to me"}]}'`
	if _, err := client.ExecStream(ctx, curlCmd, os.Stdout, os.Stderr); err != nil {
		panic(err)
	}
}
```

Go SDK private-IP behavior (`10/8`, `172.16/12`, `192.168/16`):

- Default (unset): private IPs are blocked whenever a network config is sent.
- Explicit block: call `.WithBlockPrivateIPs(true)` (or `.BlockPrivateIPs()`).
- Explicit allow: call `.AllowPrivateIPs()` or `.WithBlockPrivateIPs(false)`.

```go
sandbox := sdk.New("alpine:latest").
	AllowHost("api.openai.com