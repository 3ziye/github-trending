<div align="center">
<img src="public/hypernode.svg" width="150" alt="Hypermind Logo" />
<h1>Hypermind</h1>
</div>

[![VirusTotal](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/lklynet/hypermind/main/.github/badges/virustotal.json)](https://github.com/lklynet/hypermind/actions/workflows/virustotal.yml)

### The High-Availability Solution to a Problem That Doesn't Exist.

**Hypermind** is a completely decentralized, Peer-to-Peer deployment counter and ephemeral chat platform.

It solves the critical infrastructure challenge of knowing exactly how many other people are currently wasting ~~50MB of~~ RAM running this specific container, while providing a secure, serverless way to say "hello" to them.

---

## What is this?

You need a service that:

1.  **Does absolutely nothing useful.**
2.  **Uses "Decentralized" and "P2P" in the description.**
3.  **Makes a number go up on a screen.**

**Enter Hypermind.**

There is no central server. There is no database. There is only **The Swarm**.

## How it works

We utilize the **Hyperswarm** DHT (Distributed Hash Table) to create a mesh network of useless nodes.

1.  **Discovery:** Your node screams into the digital void to find friends.
2.  **Gossip:** Nodes connect and whisper "I exist" to each other.
3.  **State:**
    *   **Active Count:** Maintained via a distributed LRU cache of peers seen in the last 45 seconds.
    *   **Total History:** Uses a **HyperLogLog** probabilistic data structure to estimate total unique peers with >98% accuracy.
4.  **Chaos:** Connections are rotated every 5 minutes to ensure a dynamic, unblockable topology.

## Features

### 1. The Counter
It counts. That's the main thing.
*   **Active Nodes:** Real-time count of currently online peers.
*   **Total Unique:** A probabilistic estimate of every unique node ever encountered.

### 2. Ephemeral Chat
A completely decentralized chat system built directly on top of the swarm topology.
*   **Modes:** Local (direct neighbors) and Global (gossip relay).
*   **Ephemeral:** No database. No history.
*   **Markdown:** Full support for rich text.

### 3. Visualizations
*   **Particle Map:** Visualizes approximate peer locations (if enabled).
*   **Themes:** Built-in theme switcher (Hypermind, Hypermind Classic, Nord, Solarized, Tokyo Night, etc).<br>
    <img src="assets/images/hypermind-theme.png" width="100" alt="Hypermind" /> <img src="assets/images/hypermind-classic-theme.png" width="100" alt="Hypermind Classic" /> <img src="assets/images/nord-dark-theme.png" width="100" alt="Nord" /> <img src="assets/images/solarized-light-theme.png" width="100" alt="Solarized" /> <img src="assets/images/tokyo-night-theme.png" width="100" alt="Tokyo Night" /> <img src="assets/images/volcano-theme.png" width="100" alt="Volcano" />

---

## Usage

### Dashboard
Open `http://localhost:3000`. The dashboard updates in **Realtime** via Server-Sent Events.

### Chat Commands
*   `/help` - Show all commands.
*   `/local <msg>` - Send message only to direct connections.
*   `/whisper <user> <msg>` - Send a private message.
*   `/block <user>` - Block a user.
*   `/timestamp` - Toggle message timestamps.
*   `/sound` - Toggle sound effects for sent/received messages.
*   **Easter Eggs:** `/shrug`, `/tableflip`, `/heart`, and more.

---

<details>
<summary><strong>Deployment</strong></summary>

### Docker


```bash
docker run -d \
  --name hypermind \
  --network host \
  --restart unless-stopped \
  -e PORT=3000 \
  -e ENABLE_CHAT=true \
  -e ENABLE_MAP=true \
  ghcr.io/lklynet/hypermind:latest
```

> **⚠️ CRITICAL NETWORK NOTE:**
> Use `--network host`. This is a P2P application that needs to punch through NATs. If you bridge it, the DHT usually fails, and you will be the loneliest node in the multiverse.

### Docker Compose (The Classy Way)

Add this to your `docker-compose.yml` to permanently reserve system resources for no reason:

```yaml
services:
  hypermind:
    image: ghcr.io/lklynet/hypermind:latest
    container_name: hypermind
    network_mode: host
    restart: unless-stopped
    environment:
      - PORT=3000
      - ENABLE_CHAT=true
      - ENABLE_MAP=true
```

### Kubernetes (The Enterprise Way)

For when you need your useless counter to be orchestrated by a control plane.

```bash
kubectl create deployment hypermind --image=ghcr.io/lklynet/hypermind:latest --port=3000
kubectl set env deployment/hypermind PORT=3000 ENABLE_CHAT=true
kubectl expose deployment hypermind --type=LoadBalancer --port=3000 --target-port=3000
```

</details>

<details>
<summary><strong>Environment Variables</strong></summary>

Hypermind is highly configurable. Use these variables to tune your experience.

### Feature Flags

| Variable | Default | Description |
|----------|---------|-------------|
| `ENABLE_CHAT` | `false` | Set to `true` to enable the P2P chat system. |
| `ENABLE_MAP` | `false` | Set to `true` to enable the map visualization. |
| `ENABLE_THEMES` | `true` | Set to `false` to disable the them