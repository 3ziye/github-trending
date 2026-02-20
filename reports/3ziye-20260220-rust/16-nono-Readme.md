<div align="center">

<img src="assets/nono-logo.png" alt="nono logo" width="600"/>

**AI agent security that makes the dangerous bits structurally impossible.**

<p>
  From the creator of
  <a href="https://sigstore.dev"><strong>Sigstore</strong></a>
  <br/>
  <sub>The standard for secure software attestation, used by PyPI, npm, brew, and Maven Central</sub>
</p>
<p>
  <a href="https://opensource.org/licenses/Apache-2.0"><img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="License"/></a>
  <a href="https://github.com/always-further/nono/actions/workflows/ci.yml"><img src="https://github.com/always-further/nono/actions/workflows/ci.yml/badge.svg" alt="CI Status"/></a>
  <a href="https://docs.nono.sh"><img src="https://img.shields.io/badge/Docs-docs.nono.sh-green.svg" alt="Documentation"/></a>
</p>
<p>
  <a href="https://discord.gg/pPcjYzGvbS">
    <img src="https://img.shields.io/badge/Chat-Join%20Discord-7289da?style=for-the-badge&logo=discord&logoColor=white" alt="Join Discord"/>
  </a>
</p>

</div>

> [!WARNING]
> This is an early alpha release that has not undergone comprehensive security audits. While we have taken care to implement robust security measures, there may still be undiscovered issues. We do not recommend using this in production until we release a stable version of 1.0.

> [!NOTE]
> We are just wrapping up the separation of the CLI and core library. The last stable CLI release is still available on homebrew tap (version v0.5.0) and is fine to use. We will update this README with installation instructions when all library clients are ready. We plan to submit to homebrew-core, but the repo is not yet 30 days old.

AI agents get filesystem access, run shell commands, and are inherently open to prompt injection. The standard response is guardrails and policies. The problem is that policies can be bypassed and guardrails linguistically overcome.

Kernel-enforced sandboxing (Landlock/Seatbelt) blocks unauthorized access at the syscall level. Every filesystem change gets a rollback snapshot with integrity protection. Destructive commands are denied before they run. Secrets are injected without touching disk. When the agent needs access outside its permissions, a kernel-mediated supervisor intercepts the syscall via seccomp BPF, opens the file after user approval, and injects only the file descriptor — the agent never executes its own `open()`. No root or `CAP_SYS_ADMIN` required. Runs on any Linux kernel 5.13+ — bare metal, containers(Docker,Podman,K8s), Firecracker, Kata.

> *"nono, so secure, Chuck Norris tried to break out, but gave up and went home."* — Chuck Norris (allegedly)

> 
## CLI

The CLI builds on the library to provide a ready-to-use sandboxing tool, popular with coding-agents, with built-in profiles, policy groups, and interactive UX.

```bash
# Claude Code with inbuilt profile
nono run --profile claude-code -- claude
# OpenCode with custom permissions
nono run --profile opencode --allow-cwd/src --allow-cwd/output -- opencode
# OpenClaw with custom permissions
nono run --profile openclaw --allow-cwd -- openclaw gateway
# Any command with custom permissions
nono run --read ./src --write ./output -- cargo build
```

## Library (Coming very Soon!)

The core is a Rust library that can be embedded into any application via native bindings. The library is a policy-free sandbox primitive -- it applies only what clients explicitly request.

#### <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/rust/rust-original.svg" width="18" height="18" alt="Rust"/> Rust — [crates.io](https://crates.io/crates/nono)

```rust
use nono::{CapabilitySet, Sandbox};

let mut caps = CapabilitySet::new();
caps.allow_read("/data/models")?;
caps.allow_write("/tmp/workspace")?;

Sandbox::apply(&caps)?;  // Irreversible — kernel-enforced from here on
```

#### <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" height="18" alt="Python"/> Python — [nono-py](https://github.com/always-further/nono-py)

```python
from nono_py import CapabilitySet, AccessMode, apply

caps = CapabilitySet()
caps.allow_path("/data/models", AccessMode.READ)
caps.allow_path("/tmp/workspace", AccessMode.READ_WRITE)

apply(caps)  # Apply CapabilitySet
```

#### <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" height="18" alt="TypeScript"/> TypeScript — [nono-ts](https://github.com/always-further/nono-ts)

```typescript
import { CapabilitySet, AccessMode, apply } from "nono-ts";

const caps = new CapabilitySet();
caps.allowPath("/data/models", AccessMode.Read);
caps.allowPath("/tmp/workspace", AccessMode.ReadWrite);

apply(caps);  // Irreversible — kernel-enforced from here on
```

## Features

### Kernel-Enforced Sandbox

nono applies OS-level restrictions that cannot be bypassed or escalated from within the sandboxed process. Permissions are defined as capabilities granted before execution -- once the sa