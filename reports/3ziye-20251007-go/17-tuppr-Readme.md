# tuppr - Talos Linux Upgrade Controller

A Kubernetes controller for managing automated upgrades of Talos Linux and Kubernetes.

## ✨ Features

### Core Capabilities

- 🚀 **Automated Talos node upgrades** with intelligent orchestration
- 🎯 **Kubernetes upgrades** - upgrade Kubernetes to newer versions
- 🔒 **Safe upgrade execution** - upgrades always run from healthy nodes (never self-upgrade)
- 📊 **Built-in health checks** - CEL-based expressions for custom cluster validation
- 🔄 **Configurable reboot modes** - default or powercycle options
- 📋 **Comprehensive status tracking** with real-time progress reporting
- ⚡ **Resilient job execution** with automatic retry and pod replacement
- 📈 **Prometheus metrics** - detailed monitoring of upgrade progress and health

## 🚀 Quick Start

### Prerequisites

1. **Talos cluster** with API access configured
2. **Namespace** for the controller (e.g., `system-upgrade`)

### Installation

Allow Talos API access to the desired namespace by applying this config to all of you nodes:

```yaml
machine:
  features:
    kubernetesTalosAPIAccess:
      allowedKubernetesNamespaces:
        - system-upgrade # or the namespace the controller will be installed to
      allowedRoles:
        - os:admin
      enabled: true
```

Install the Helm chart:

```bash
# Install via Helm
helm install tuppr oci://ghcr.io/home-operations/charts/tuppr \
  --version 0.1.0 \
  --namespace system-upgrade
```

### Basic Usage

#### Talos Node Upgrades

Create a `TalosUpgrade` resource:

```yaml
apiVersion: tuppr.home-operations.com/v1alpha1
kind: TalosUpgrade
metadata:
  name: cluster
spec:
  talos:
    # renovate: datasource=docker depName=ghcr.io/siderolabs/installer
    version: v1.11.0  # Required - target Talos version

  policy:
    debug: true          # Optional, verbose logging
    force: false         # Optional, skip etcd health checks
    rebootMode: default  # Optional, default|powercycle
    placement: soft      # Optional, hard|soft

  # Custom health checks (optional)
  healthChecks:
    - apiVersion: v1
      kind: Node
      expr: status.conditions.exists(c, c.type == "Ready" && c.status == "True")

  # Talosctl configuration (optional)
  talosctl:
    image:
      repository: ghcr.io/siderolabs/talosctl  # Optional, default
      tag: v1.11.0                             # Optional, auto-detected
      pullPolicy: IfNotPresent                 # Optional, default
```

#### Kubernetes Upgrades

Create a `KubernetesUpgrade` resource:

```yaml
apiVersion: tuppr.home-operations.com/v1alpha1
kind: KubernetesUpgrade
metadata:
  name: kubernetes
spec:
  kubernetes:
    # renovate: datasource=docker depName=ghcr.io/siderolabs/kubelet
    version: v1.34.0  # Required - target Kubernetes version

  # Custom health checks (optional)
  healthChecks:
    - apiVersion: v1
      kind: Node
      expr: status.conditions.exists(c, c.type == "Ready" && c.status == "True")
      timeout: 10m

  # Talosctl configuration (optional)
  talosctl:
    image:
      repository: ghcr.io/siderolabs/talosctl  # Optional, default
      tag: v1.11.0                             # Optional, auto-detected
      pullPolicy: IfNotPresent                 # Optional, default
```

## 🎯 Advanced Configuration

### Health Checks

Define custom health checks using [CEL expressions](https://cel.dev/). These health checks are evaluated before each upgrade and run concurrently.

```yaml
healthChecks:
  # Check all nodes are ready
  - apiVersion: v1
    kind: Node
    expr: |
      status.conditions.filter(c, c.type == "Ready").all(c, c.status == "True")
    timeout: 10m

  # Check specific deployment replicas
  - apiVersion: apps/v1
    kind: Deployment
    name: critical-app
    namespace: production
    expr: status.readyReplicas == status.replicas

  # Check custom resources
  - apiVersion: ceph.rook.io/v1
    kind: CephCluster
    name: rook-ceph
    namespace: rook-ceph
    expr: status.ceph.health in ["HEALTH_OK"]
```

### Upgrade Policies (TalosUpgrade only)

Fine-tune upgrade behavior:

```yaml
policy:
  # Enable debug logging for troubleshooting
  debug: true

  # Force upgrade even if etcd is unhealthy (dangerous!)
  force: true

  # Controls how strictly upgrade jobs avoid the target node
  placement: hard  # or "soft"

  # Use powercycle reboot for problematic nodes
  rebootMode: powercycle  # or "default"
```

## 📊 Monitoring & Metrics

### Prometheus Metrics

Tuppr exposes comprehensive Prometheus metrics for monitoring upgrade progress, health check performance, and job execution:

#### Talos Upgrade Metrics

```prometheus
# Current phase of Talos upgrades (0=Pending, 1=InProgress, 2=Completed, 3=Failed)
tuppr_talos_upgrade_phase{name="cluster", phase="InProgress"} 1

# Node counts for Talos upgrades
tuppr_talos_upgrade_nodes_total{name="cluster"} 5
tuppr_talos_upgrade_nodes_completed{name="cluster"} 3
tuppr_talos_upgrade_nodes_failed{name="cluster"} 0

# Duration of Talos upgrade phases (histogram)
tuppr_talos_up