# Gmail Bulk Unsubscribe & Cleanup Tool

A **free**, privacy-focused tool to bulk unsubscribe from emails, delete emails by sender, and mark emails as read. No subscriptions, no data collection - runs 100% on your machine.


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
| **Delete by Sender** | Scan and see who sends you the most emails, delete in bulk |
| **Bulk Delete Multiple Senders** | Delete emails from multiple senders simultaneously with progress tracking |
| **Mark as Read** | Bulk mark thousands of unread emails as read |
| **Archive Emails** | Archive emails from selected senders (remove from inbox) |
| **Label Management** | Create, delete, and apply/remove labels to emails from specific senders |
| **Mark Important** | Mark or unmark emails from selected senders as important |
| **Email Download** | Download email metadata for selected senders as CSV |
| **Smart Filters** | Filter by date range, email size, category (Promotions, Social, Updates, Forums, Primary), sender, and labels |
| **Privacy First** | Runs locally - your data never leaves your machine |
| **Super Fast** | Gmail API with batch requests (100 emails per API call) |
| **Gmail-style UI** | Clean, familiar interface with real-time progress tracking |

## Platform Support

Works on **all major platforms** - both Docker and local installation:

| Platform | Docker | Local (Python) |
|----------|--------|----------------|
| Linux (x86_64) | Native | Native |
| Windows (x86_64) | Native | Native |
| macOS Intel | Native | Native |
| macOS Apple Silicon (M1/M2/M3/M4) | Native | Native |

## Security & Privacy

- **100% Local** - No external servers, no data collection
- **Open Source** - Inspect all the code yourself
- **Minimal Permissions** - Only requests read + modify (for mark as read)
- **Your Credentials** - You control your own Google OAuth app
- **Gitignored Secrets** - `credentials.json` and `token.json` never get committed

## 🆘 Need Help Setting Up?
A few people reached out to me on Reddit and via email saying they love the idea, but don’t have the technical expertise to run this software themselves. I’d also like to grow the project further, so support would really help make the time I invest in it more worthwhile.<br>Struggling with Docker, Google Cloud Console, or `credentials.json`? I can help you set it up personally!<br>
I offer a **1-on-1 Setup Service ($8)** where we hop on a Google Meet, you share your screen, and I guide you through the entire installation until it's working perfectly.

- **Secure:** I guide you; I never see your passwords.
- **Fast:** We'll get it running in under 20 minutes.
- **Support the Project:** Your $8 helps keep this tool free and open source.

Book a Setup Session Here - mail me at guruvelu85@gmail.com, i will reply and setup an gmeet call

## Demo

![Gmail Cleaner Demo](media/demo.gif)

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
7. Go to **Client