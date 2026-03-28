<p align="center">
  <h1 align="center">🛰️ S H A D O W B R O K E R</h1>
  <p align="center"><strong>Global Threat Intercept — Real-Time Geospatial Intelligence Platform</strong></p>
  <p align="center">

  </p>
</p>

---




https://github.com/user-attachments/assets/248208ec-62f7-49d1-831d-4bd0a1fa6852





**ShadowBroker** is a real-time, multi-domain OSINT dashboard that fuses 60+ live intelligence feeds into a single dark-ops map interface. Aircraft, ships, satellites, conflict zones, CCTV networks, GPS jamming, internet-connected devices, police scanners, mesh radio nodes, and breaking geopolitical events — all updating in real time on one screen.

Built with **Next.js**, **MapLibre GL**, **FastAPI**, and **Python**. 35+ toggleable data layers. TMany visual modes (DEFAULT / SATELLITE / NIGHTLIGHT ETC>). Right-click any point on Earth for a country dossier, head-of-state lookup, and the latest Sentinel-2 satellite photo. No user data is collected or transmitted — the dashboard runs entirely in your browser against a self-hosted backend.

Designed for analysts, researchers, radio operators, and anyone who wants to see what the world looks like when every public signal is on the same map.


## Why This Exists

A surprising amount of global telemetry is already public — aircraft ADS-B broadcasts, maritime AIS signals, satellite orbital data, earthquake sensors, mesh radio networks, police scanner feeds, environmental monitoring stations, internet infrastructure telemetry, and more. This data is scattered across dozens of tools and APIs. ShadowBroker combines all of it into a single interface.

The project does not introduce new surveillance capabilities — it aggregates and visualizes existing public datasets. It is fully open-source so anyone can audit exactly what data is accessed and how. No user data is collected or transmitted — everything runs locally against a self-hosted backend. No telemetry, no analytics, no accounts.

### Shodan Connector

ShadowBroker includes an optional Shodan connector for operator-supplied API access. Shodan results are fetched with your own `SHODAN_API_KEY`, rendered as a local investigative overlay (not merged into core feeds), and remain subject to Shodan’s terms of service.

---

## Interesting Use Cases

* **Transmit on the InfoNet testnet** — the first decentralized intelligence mesh built into an OSINT tool. Obfuscated messaging with gate personas, Dead Drop peer-to-peer exchange, and a built-in terminal CLI. No accounts, no signup. Privacy is not guaranteed yet — this is an experimental testnet — but the protocol is live and being hardened.
* **Track Air Force One**, the private jets of billionaires and dictators, and every military tanker, ISR, and fighter broadcasting ADS-B — with automatic holding pattern detection when aircraft start circling
* **Estimate where US aircraft carriers are** using automated GDELT news scraping — no other open tool does this
* **Search internet-connected devices worldwide** via Shodan — cameras, SCADA systems, databases — plotted as a live overlay on the map
* **Right-click anywhere on Earth** for a country dossier (head of state, population, languages), Wikipedia summary, and the latest Sentinel-2 satellite photo at 10m resolution
* **Click a KiwiSDR node** and tune into live shortwave radio directly in the dashboard. Click a police scanner feed and eavesdrop in one click.
* **Watch 11,000+ CCTV cameras** across 6 countries — London, NYC, California, Spain, Singapore, and more — streaming live on the map
* **See GPS jamming zones** in real time — derived from NAC-P degradation analysis of aircraft transponder data
* **Monitor satellites overhead** color-coded by mission type — military recon, SIGINT, SAR, early warning, space stations — with SatNOGS and TinyGS ground station networks
* **Track naval traffic** including 25,000+ AIS vessels, fishing activity via Global Fishing Watch, and billionaire superyachts
* **Follow earthquakes, volcanic eruptions, active wildfires** (NASA FIRMS), severe weather alerts, and air quality readings worldwide
* **Map military bases, 35,000+ power plants**, 2,000+ data centers, and internet outage regions — cross-referenced automatically
* **Connect to Meshtastic mesh radio nodes** and APRS amateur radio networks — visible on the map and integrated into Mesh Chat
* **Switch visual modes** — DEFAULT, SATELLITE, FLIR (thermal), NVG (night vision), CRT (retro terminal) — via the STYLE button
* **Track trains** across the US (Amtrak) and Europe (DigiTraffic) in real time

---

## ⚡ Quick Start (Docker)

```bash
git clone https://github.com/BigBodyCobain/Shadowbroker.git
cd Shadowbroker
docker compose pull
docker compose up -d
```

Open `http://localhost:3000` to view the dashboard! *(Requires [Docker Desktop](https://www.docker.com/products/docker-desktop/) or Docker Engine)*

> **Podman users:** Replace `docker compose` with `podman compose`, or use the `compose.sh` wrapper which auto-detects your engine.