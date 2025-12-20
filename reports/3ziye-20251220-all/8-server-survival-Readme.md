# Server Survival

![Gameplay Demo](assets/gameplay.gif)

**Server Survival** is an interactive 3D simulation game where you play as a **Cloud Architect**. Your mission is to build and scale a resilient cloud infrastructure to handle increasing traffic loads while fighting off DDoS attacks, managing your budget, and keeping your services healthy.

## How to Play

### Objective

Survive as long as possible! Manage your **Budget ($)**, **Reputation (%)**, and **Service Health**.

- **Earn Money** by successfully processing legitimate traffic requests.
- **Lose Reputation** if requests fail or if malicious traffic slips through.
- **Maintain Health** - Services degrade under load and need repairs.
- **Game Over** if Reputation hits 0% or you go bankrupt ($-1000).

### Traffic Types

| Traffic       | Color  | Destination | Reward | Description                            |
| :------------ | :----- | :---------- | :----- | :------------------------------------- |
| **STATIC**    | Green  | Storage     | $0.50  | Static file requests (images, CSS, JS) |
| **READ**      | Blue   | SQL DB      | $0.80  | Database read operations               |
| **WRITE**     | Orange | SQL DB      | $1.20  | Database write operations              |
| **UPLOAD**    | Yellow | Storage     | $1.50  | File uploads                           |
| **SEARCH**    | Cyan   | SQL DB      | $0.80  | Search queries (CPU intensive)         |
| **MALICIOUS** | Red    | Firewall    | $0.50  | DDoS/Attack traffic - must be blocked! |

### Infrastructure & Services

Build your architecture using the toolbar. Each service has a cost, capacity, and upkeep:

| Service      | Cost | Capacity  | Upkeep    | Function                                                           |
| :----------- | :--- | :-------- | :-------- | :----------------------------------------------------------------- |
| **Firewall** | $40  | 30        | Low       | **Security.** First line of defense. Blocks malicious traffic.     |
| **Queue**    | $40  | Queue:200 | Low       | **Buffer.** Buffers requests during spikes. Prevents drops.        |
| **Load Balancer**| $50  | 20        | Medium    | **Distribution.** Distributes traffic to multiple instances.      |
| **Compute**  | $60  | 4         | High      | **Processing.** Processes requests. **Upgradeable T1→T3.**         |
| **Cache**    | $60  | 30        | Medium    | **Caching.** Caches responses to reduce DB load.                   |
| **SQL DB**   | $150 | 8         | Very High | **Database.** Destination for READ/WRITE/SEARCH. **Upgradeable T1→T3.** |
| **Storage**  | $25  | 25        | Low       | **File System.** Destination for STATIC/UPLOAD traffic.            |

### Scoring & Economy

| Action         | Money  | Score | Reputation |
| :------------- | :----- | :---- | :--------- |
| Static Request | +$0.50 | +3    | +0.1       |
| DB Read        | +$0.80 | +5    | +0.1       |
| DB Write       | +$1.20 | +8    | +0.1       |
| File Upload    | +$1.50 | +10   | +0.1       |
| Search Query   | +$0.80 | +5    | +0.1       |
| Attack Blocked | +$0.50 | +10   | -          |
| Request Failed | -      | -half | -1         |
| Attack Leaked  | -      | -     | -5         |

### Upkeep & Cost Scaling

- **Base Upkeep:** Each service has per-minute upkeep costs
- **Upkeep Scaling:** Costs increase 1x to 2x over 10 minutes
- **Repair Costs:** 15% of service cost to manually repair
- **Auto-Repair:** +10% upkeep overhead when enabled

### Game Modes

#### Survival Mode

The core experience - survive as long as possible against escalating traffic with constant intervention required:

**Dynamic Challenges:**

- **RPS Acceleration** - Traffic multiplies at time milestones (×1.3 at 1min → ×4.0 at 10min)
- **Random Events** - Cost spikes, capacity drops, traffic bursts every 15-45 seconds
- **Traffic Shifts** - Traffic patterns change every 40 seconds
- **DDoS Spikes** - 50% malicious traffic waves every 45 seconds
- **Service Degradation** - Services lose health under load, require repairs

**New UI Features:**

- Health bars on all services
- Active event indicator bar at top
- Detailed finances panel (income/expenses breakdown)
- Service health panel with repair costs
- Auto-repair toggle
- Game over analysis with tips

#### Sandbox Mode

A fully customizable testing environment for experimenting with any architecture:

| Control           | Description                                                       |
| :---------------- | :---------------------------------------------------------------- |
| **Budget**        | Set any starting budget (slider 0-10K, or type any amount)        |
| **RPS**           | Control traffic rate (0 = stopped, or type 100+ for stress tests) |
| **Traffic Mix**   | Adjust all 6 traffic type percentages independently               |
| **Burst**         | Spawn instant bursts of specific traffic types                    |
| **Upkeep Toggle** | Enable/disable service costs                             