# Home Dashboard

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Node.js](https://img.shields.io/badge/node-%3E%3D16.0.0-brightgreen)](https://nodejs.org/)
[![PM2](https://img.shields.io/badge/PM2-Daemon-blue)](https://pm2.keymetrics.io/)
[![Status](https://img.shields.io/badge/status-production-success)](https://github.com/kyleturman/home-dashboard)

A modular, open-source home dashboard that runs a server on a local network computer (Raspberry Pi, Mac Mini, or any always-on machine) and creates a dashboard of weather forecasts, calendar events, vehicle data, and AI insights to be shown on an e-paper display.

![E-paper Display](screenshots/display.png)

This [tweet](https://x.com/kyleturman/status/1973774056064516346) blew up so I thought I'd share the code and make it a bit easier and more stable to run. The code (and definitely CSS lol) is generally a little messier than I would like, and the quality of the 1-bit image conversion is not perfect with font hinting issues, but done is better than perfect and it's a home project so c'est la vie!

**How it works:** A Node.js server collects data from APIs, renders a dashboard as HTML/CSS, converts it to a 1-bit PNG image, and serves it over your local network available to a microcontroller-powered e-paper display that fetches the image and refreshes every 10 minutes (while sleeping from 12am-5am to save battery).

## Disclaimer

This project is provided **as-is** with no warranty or guarantee of support. It is not actively maintained but serves as a working example of a modular home dashboard system. Feel free to use it as a starting point for your own customizations. For development assistance, consider using [Claude Code](https://www.claude.com/product/claude-code) or other AI coding tools to extend functionality.

## Getting Started

This dashboard is designed to run as a persistent background service on an always-on computer within your local network. It uses **PM2** as a process manager to run the Node.js server as a daemon—automatically restarting on crashes and optionally starting on boot.

### Prerequisites
- **Node.js** (v16 or higher)
- **npm** (comes with Node.js)
- An always-on computer on your local network

### 1. Install Dependencies
```bash
git clone https://github.com/kyleturman/home-dashboard.git
cd home-dashboard
npm install
```

### 2. Configure Environment
```bash
cp .env.example .env
```

Edit `.env` and set at minimum:
```bash
MAIN_LOCATION_ZIP=94607
VISUAL_CROSSING_API_KEY=your_key_here
```

**Required:**
- `MAIN_LOCATION_ZIP` - Your primary 5-digit US ZIP code
- `VISUAL_CROSSING_API_KEY` - Weather forecast API key (see below)

**Optional:**
- `ADDITIONAL_LOCATION_ZIPS` - Up to 3 additional ZIP codes (comma-separated)
- `PORT` - Server port (default: 7272)
- See `.env.example` for all configuration options

### 3. Start the Server
```bash
npm start      # Start as PM2 daemon (auto-restarts on crash)
npm stop       # Stop the service
npm restart    # Restart (reloads .env)
npm run logs   # View live logs
```

The server runs on **port 7272** by default via PM2 process manager.

### 4. Enable Auto-Start on Boot (Optional)

To have the dashboard automatically start when your server reboots:

```bash
# Generate and install startup script
npx pm2 startup

# Follow the command it outputs (may require sudo)
# Then save the current PM2 process list
npx pm2 save
```

This is **highly recommended** to ensure the dashboard restarts after power loss or system updates and your display keeps on kickin'.

### 5. Access the Dashboard

**Core routes:**
- Dashboard: `http://localhost:7272/dashboard`
- E-paper 1-bit PNG image: `http://localhost:7272/dashboard/image`
- Admin panel: `http://localhost:7272/admin`

**API endpoints (used for debugging and custom development):**
- Dashboard data JSON: `http://localhost:7272/api/dashboard`
- Services status: `http://localhost:7272/api/services/status`

## API Keys & Provider Setup

### Visual Crossing Weather (Required)
Multi-location forecasts, hourly data, and astronomy information. Visual Crossing provides a free tier of 1,000 calls per day and seems the most robust and accurate of free weather APIs from my research.

1. Sign up at [visualcrossing.com/weather-api](https://www.visualcrossing.com/weather-api)
2. Free tier: 1,000 calls/day
3. Get your API key from the account dashboard
4. Add to `.env`: `VISUAL_CROSSING_API_KEY=your_key_here`

### Ambient Weather (Optional)
Have a personal weather station from [Ambient Weather](https://ambientweather.com/)? Get real-time data from your home station.

1. Own an Ambient Weather station (The [AMWS1965](https://ambientweather.com/amws1965-wifi-weather-station-with-remote-monitoring) is the most affordable starter option)
2. Create account at [ambientweather.net](https://ambientweather.net/)
3. Navigate to Account → API Keys
4. Generate Application and API keys
5. Add to `.env`:
   ```bash
   AMBIENT_A