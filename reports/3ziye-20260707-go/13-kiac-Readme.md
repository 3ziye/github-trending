<p align="center">
  <img src="assets/banner.png" alt="kiac - Kubernetes in Apple Containers" width="100%">
</p>

<p align="center">
  <b>Local Kubernetes clusters where every node is its own lightweight VM.</b><br>
  Native on Apple silicon, powered by <a href="https://github.com/apple/container">apple/container</a>. No Docker Desktop. No Lima. No QEMU.
</p>

<p align="center">
  <a href="https://github.com/saiyam1814/kiac/releases"><img src="https://img.shields.io/github/v/release/saiyam1814/kiac?color=326CE5&label=release" alt="release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-326CE5" alt="MIT"></a>
  <img src="https://img.shields.io/badge/platform-Apple%20silicon-555" alt="Apple silicon">
  <img src="https://img.shields.io/badge/Kubernetes-1.32–1.36-326CE5" alt="Kubernetes 1.32-1.36">
  <a href="https://saiyam1814.github.io/kiac/"><img src="https://img.shields.io/badge/website-kiac-326CE5" alt="website"></a>
</p>

<p align="center">
  <img src="assets/kiac-demo.gif" alt="kiac creating a 3-node cluster" width="80%">
</p>

```bash
brew install saiyam1814/tap/kiac
kiac create cluster --workers 2
```

---

## Why this matters

Running a local Kubernetes cluster on a Mac has always meant a quiet compromise. Your "nodes" were containers sharing one kernel inside one hidden Linux VM, all pretending to be separate machines. It worked until you tried to test a node failure, or `kubectl top`, or a `type: LoadBalancer` service, and the illusion cracked.

A Kubernetes node wants to *be* a machine: its own kernel, its own kubelet, its own cgroups, its own IP that can come and go on its own. **kiac gives every node exactly that** by booting each one as its own lightweight virtual machine on Apple's native runtime. The result is a local cluster that behaves like a real one, created with a single command in a couple of minutes.

## Why Apple containers

When Apple shipped `container` 1.0, most people read it as "Docker, but from Apple." It is something more interesting underneath: **every container is its own lightweight virtual machine.**

<p align="center">
  <img src="assets/apple-container-anatomy.png" alt="How one Apple container works" width="92%">
</p>

The [Containerization](https://github.com/apple/containerization) framework boots a separate, minimal Linux VM for each container on Apple's `Virtualization.framework`:

- **The image becomes a disk.** The OCI image is turned into an EXT4 filesystem and handed to the VM as its root block device. No overlay mount layered on a shared host kernel.
- **A dedicated kernel boots.** Each container gets its own minimal, optimized Linux kernel. It is not shared with the host or any other container.
- **`vminitd` is PID 1.** A tiny Swift init system comes up first, then launches and supervises your process. The host drives it through a gRPC API over `vsock`.
- **virtio devices, direct networking.** No BIOS, no legacy device emulation, so the VM boots in about a second and gets its own IP you can reach from your Mac.

You get the developer experience of containers with the isolation boundary of a virtual machine. That combination is exactly what a Kubernetes node wants.

## Why Kubernetes on Apple containers: real isolation

When local Kubernetes tools run "nodes" as Docker containers, those nodes are processes sharing one Linux kernel, separated only by namespaces. Namespaces are a software boundary *inside* a single shared kernel. With kiac, the boundary between nodes is the **hypervisor** itself.

<p align="center">
  <img src="assets/isolation.png" alt="Where the isolation boundary sits" width="100%">
</p>

That difference is not academic. It changes what the cluster can actually do:

- **Blast radius.** A container escape that reaches the shared kernel reaches every node on it. With a VM per node, an escape is contained to one VM.
- **Failure domains.** A shared kernel is a shared fate: one panic or runaway sysctl takes everything down together. With kiac, a kernel problem stays inside the VM that caused it.
- **Real node failure.** Stop one node VM and it behaves like an actual node going offline: NotReady detection, eviction, rescheduling. You cannot meaningfully test that when "stopping a node" means killing one of several processes that share a kernel.
- **Per-node kernel reality.** Each node has its own `/proc`, `/sys`, modules, and sysctls. Node-level behavior is real, not simulated.

Containers are great for packaging software, and kiac depends on them. The point is narrower: when the workload you are isolating is itself a machine, a machine-grade boundary is the right tool.

## Features

- 🔒 **Hardware-grade isolation** — each node is one lightweight VM with its own kernel and cgroups, not namespaces sharing a daemon.
- 📊 **Metrics out of the box** — `kubectl top nodes` works the moment the cluster is up. metrics-server ships preconfigured.
- 💾 **PVCs that just bind** — a default StorageClass (local-path-provisioner) is instal