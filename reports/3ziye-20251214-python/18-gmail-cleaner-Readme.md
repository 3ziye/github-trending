# Gmail Bulk Unsubscribe & Cleanup Tool

A **free**, privacy-focused tool to bulk unsubscribe from emails, delete emails by sender, and mark emails as read. No subscriptions, no data collection - runs 100% on your machine.

[![GitHub Sponsors](https://img.shields.io/badge/Sponsor-%E2%9D%A4-pink?style=flat-square&logo=github-sponsors)](https://github.com/sponsors/Gururagavendra)
[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-FFDD00?style=flat-square&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/gururagavendra)

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=flat-square&logo=docker)
![Gmail API](https://img.shields.io/badge/Gmail-API-EA4335?style=flat-square&logo=gmail)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![GitHub stars](https://img.shields.io/github/stars/Gururagavendra/gmail-cleaner?style=flat-square&logo=github)

> **No Subscription Required - Free Forever**

## Features

| Feature | Description |
|---------|-------------|
| **Bulk Unsubscribe** | Find newsletters and unsubscribe with one click |
| **Delete by Sender** | See who sends you the most emails, delete in bulk |
| **Mark as Read** | Bulk mark thousands of unread emails as read |
| **Smart Filters** | Filter by days, size of email, and category (Promotions, Social, Updates) |
| **Privacy First** | Runs locally - your data never leaves your machine |
| **Super Fast** | Gmail API with batch requests (100 emails per API call) |
| **Gmail-style UI** | Clean, familiar interface |

## Platform Support

Works on **all major platforms** - both Docker and local installation:

| Platform | Docker | Local (Python) |
|----------|--------|----------------|
| Linux (x86_64) | Native | Native |
| Windows (x86_64) | Native | Native |
| macOS Intel | Native | Native |
| macOS Apple Silicon (M1/M2/M3/M4) | Native | Native |

## Demo

![Gmail Cleaner Demo](demo.gif)

**[Watch Setup Video on YouTube](https://youtu.be/CmOWn8Tm5ZE)** - Step-by-step video on how to setup the repo and run the project locally.

## Feature Requests

Lets make this tool a better one by improving as much as possible, All features are welcome, To request a feature, [open a GitHub issue](https://github.com/Gururagavendra/gmail-cleaner/issues/new).

## Prerequisites

- **Docker**: [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- **Local (Python)**: [Python 3.9+](https://www.python.org/downloads/) and [uv](https://docs.astral.sh/uv/getting-started/installation/)

## Setup

**Important**: You must create your **OWN** Google Cloud credentials. This app doesn't include pre-configured OAuth - that's what makes it privacy-focused! Each user runs their own instance with their own credentials.

### 1. Get Google OAuth Credentials

**Video Tutorial**: [Watch on YouTube](https://youtu.be/CmOWn8Tm5ZE) for a visual walkthrough

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (or select existing)
3. Search for **"Gmail API"** and **Enable** it
4. Go to **Google Auth Platform**  → Click **"Get started"**
5. Fill in the wizard:
   - **App Information**: Enter app name (e.g., "Gmail Cleanup"), select your email
   - **Audience**: Select **External**
   - **Contact Information**: Add your email address
   - Click **Create**
6. Go to **Audience** (left sidebar) → Scroll to **Test users**
   - Click **Add Users** → Add your Gmail address → **Save**
7. Go to **Clients** (left sidebar) → **Create Client**
   - Choose the application type based on your setup:
   
   | Setup | Application Type | Redirect URI |
   |-------|------------------|--------------|
   | **Local/Desktop** (Python with browser) | Desktop app | Not needed |
   | **Docker/Remote Server** | Web application | `http://YOUR_HOST:8767/` |
   
   - Name: "Gmail Cleanup" (or anything)
   - Click **Create**
   - Click **Download** (downloads JSON file)
   - Rename the downloaded file to `credentials.json`

> **💡 Which should I choose?**
> - Running locally with Python (`uv run python main.py`)? → **Desktop app**
> - Running with Docker or on a remote server? → **Web application**

### 2. Clone the Repository

1. Clone the repo:
```bash
git clone https://github.com/Gururagavendra/gmail-cleaner.git
```

2. Navigate to the folder:
```bash
cd gmail-cleaner
```

3. Put your `credentials.json` file in the project folder.

## Usage

### Option A: Docker (Recommended)

1. Start the container:
```bash
docker compose up -d
```

2. Open the app in your browser:
```
http://localhost:8766
```

3. Click **"Sign In"** button in the web UI

4. Check logs for the OAuth URL (only after clicking Sign In!):
```bash
docker logs $(docker ps -q --filter ancestor=ghcr.io/gururagavendra/gmail-cleaner)
```
Or if you built locally:
```bash
docker logs $(docker ps -q --filter name=gmail-cleaner)
```

5. Copy the Google OAuth URL from lo