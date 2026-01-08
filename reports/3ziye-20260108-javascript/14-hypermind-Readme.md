<div align="center">
<img src="hypermind2.svg" width="150" alt="Hypermind Logo" />
<h1>Hypermind</h1>
</div>

### The High-Availability Solution to a Problem That Doesn't Exist.

**Hypermind** is a completely decentralized, Peer-to-Peer deployment counter.

It solves the critical infrastructure challenge of knowing exactly how many other people are currently wasting 50MB of RAM running this specific container.

---

## » What is this?

You have a server rack in your basement. You have 128GB of RAM. You have deployed the Arr stack, Home Assistant, Pi-hole, and a dashboard to monitor them all. **But you crave more.**

You need a service that:

1. Does absolutely nothing useful.
2. Uses "Decentralized" and "P2P" in the description.
3. Makes a number go up on a screen.

**Enter Hypermind.**

There is no central server. There is no database. There is only **The Swarm**.

## » How it works

We utilize the **Hyperswarm** DHT (Distributed Hash Table) to achieve a singular, trivial goal of **Counting.**

1. **Discovery:** Your node screams into the digital void (`hypermind-lklynet-v1`) to find friends.
2. **Gossip:** Nodes connect and whisper "I exist" to each other.
3. **Consensus:** Each node maintains a list of peers seen in the last 2.5 seconds.

If you turn your container off, you vanish from the count. If everyone turns it off, the network ceases to exist. If you turn it back on, you are the Creator of the Universe (Population: 1).

## » Deployment

### Docker (The Fast Way)

Since you're probably pasting this into Portainer anyway:

```bash
docker run -d \
  --name hypermind \
  --network host \
  --restart unless-stopped \
  -e PORT=3000 \
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

```

### Kubernetes (The Enterprise Way)

For when you need your useless counter to be orchestrated by a control plane.

```bash
kubectl create deployment hypermind --image=ghcr.io/lklynet/hypermind:latest --port=3000
kubectl set env deployment/hypermind PORT=3000
kubectl expose deployment hypermind --type=LoadBalancer --port=3000 --target-port=3000

```

## » Configuration

You can customize Hypermind's behavior using environment variables.

### Extras
These features are disabled by default. Set them to `true` to enable.

| Variable | Default | Description |
|----------|---------|-------------|
| `ENABLE_CHAT` | `false` | Enables the decentralized chat system. |
| `ENABLE_MAP` | `false` | Enables map visualization features. |
| `ENABLE_THEMES` | `true` | Controls the theme switcher function ([THEMES.md](THEMES.md))

### Refinement
Tune the network parameters to fit your system resources. The defaults are safe for most users. Don't change unless you know what you're doing.

| Variable | Default | Description |
|----------|---------|-------------|
| `MAX_PEERS` | `50000` | Maximum number of peers to track in memory. |
| `MAX_MESSAGE_SIZE` | `2048` | Maximum size of a single message in bytes. |
| `MAX_RELAY_HOPS` | `5` | Maximum number of times a message is relayed. |
| `MAX_CONNECTIONS` | `15` | Maximum number of active P2P connections. |
| `HEARTBEAT_INTERVAL` | `30000` | How often (ms) to send heartbeat messages. |
| `CONNECTION_ROTATION_INTERVAL` | `300000` | How often (ms) to rotate connections. |
| `PEER_TIMEOUT` | `45000` | Time (ms) before a silent peer is considered offline. |
| `CHAT_RATE_LIMIT` | `5000` | Time window (ms) for chat rate limiting. |
| `VISUAL_LIMIT` | `500` | Max number of particles to render on the dashboard. |

## » Ecosystem & Integrations

The community has bravely stepped up to integrate Hypermind into critical monitoring infrastructure.

### Home Assistant

Do you want your living room lights to turn red when the swarm grows? Of course you do.

The [Hypermind HA Integration](https://github.com/synssins/hypermind-ha) (installable via HACS) provides:

* **RGB Control:** 0 nodes = Green. 10,000 nodes = Red.
* **Sensors:** Swarm health checks and statistics logging.
* **WLED Support:** Visualize the swarm size on a literal LED strip.

### Homepage Dashboard

If it's not on your dashboard, does it even exist? You can query the `/api/stats` endpoint to add a widget to [gethomepage/homepage](https://gethomepage.dev/).

Add this to your `services.yaml`:

```yaml
- Hypermind:
    icon: /icons/hypermind2.png
    href: http://<YOUR_IP>:3000
    widget:
      type: customapi
      url: http://<YOUR_IP>:3000/api/stats
      method: GET
      mappings:
        - field: count
          label: 