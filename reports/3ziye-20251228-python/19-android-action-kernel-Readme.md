# Android Use

<div align="center">

<h1>AI Agents for Android Devices</h1>

<h3>Open-source library for AI agents to control native Android apps</h3>

**Built for field workers, logistics, gig economy, and mobile-first industries**

<br>

[![Twitter](https://img.shields.io/badge/5.3M+-views-1DA1F2?style=for-the-badge&logo=x&logoColor=white)](https://x.com/ethanjlim/status/1999152070428148108?s=20)
[![Stars](https://img.shields.io/github/stars/actionstatelabs/android-action-kernel?style=for-the-badge)](https://github.com/actionstatelabs/android-action-kernel/stargazers)
[![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

<br>

### Demo

**[Watch it automate a logistics workflow in 60 seconds](https://x.com/ethanjlim/status/1999152070428148108?s=20)**

<sub>Driver texts a photo → Agent handles WhatsApp → Scanner app → Banking app → Invoice submitted</sub>

<br>

**[⭐ Star this repo (1100+ → 1,500 goal!)](https://github.com/actionstatelabs/android-action-kernel) • [Quick Start](#quick-start) • [Book Partnership Meeting](https://build.fillout.com/editor/ctqhgaBkaKus/share)**

**5.3M+ views. 1100+ stars in days. Help us reach 1,500!** • **Priority partnerships:** Mobile QA testing • Consumer Productivity • [Request meeting →](https://build.fillout.com/editor/ctqhgaBkaKus/share)

</div>

---

## The Problem

Browser agents only work on websites. Computer Use requires a desktop.

But the real economy runs on mobile devices, in places where laptops don't fit:

- **Truck drivers** submit invoices from the cab using factoring apps (RTS Pro, OTR Capital)
- **Delivery drivers** scan packages on handheld devices—200+ per route
- **Gig workers** accept orders on phones between rides—losing 20% earnings to slow manual switching
- **Field technicians** log work orders on tablets at job sites
- **Mobile banking** happens on native apps with 2FA, not web browsers

**3 billion Android devices. $40 trillion in GDP from mobile-first workflows. Zero AI agent solutions that actually work on these devices.**

---

## Real Example: Logistics Automation

**Priority partnership area.** Android Use automating an entire logistics workflow:

### Before (Manual - 10+ minutes)
```
1. Driver takes photo of Bill of Lading
2. Opens WhatsApp, sends to back office
3. Back office downloads image
4. Opens banking app, fills invoice form
5. Uploads documents
6. Submits for payment
```

### After (Automated - 30 seconds)
```python
# Driver just texts the photo. Agent does the rest.
run_agent("""
1. Get latest image from WhatsApp
2. Open native scanner app and process it
3. Switch to RTS Pro factoring app
4. Fill invoice form with extracted data
5. Upload PDF and submit for payment
""")
```

**Result:** Driver gets paid same day instead of waiting weeks. Back-office work eliminated. No laptop needed.

---

## Why This Works

<table>
<tr>
<td width="50%">

### Computer Use (Anthropic)
- Requires desktop/laptop
- Takes screenshots → OCR
- Sends images to vision model
- **$0.15 per action**
- 3-5 second latency
- Doesn't work on phones

</td>
<td width="50%">

### Android Use (This Library)
- Works on handheld devices
- Reads accessibility tree (XML)
- Structured data → LLM
- **$0.01 per action (95% cheaper)**
- <1 second latency
- Native mobile app control

</td>
</tr>
</table>

**The breakthrough:** Android's accessibility API provides structured UI data (buttons, text, coordinates) without expensive vision models.

**Real impact:** 95% cost savings + 5x faster + works where laptops can't.

---

## Traction

Launched with the logistics demo:

- **5.3M+ views** on X/Twitter ([watch demo](https://x.com/ethanjlim/status/1999152070428148108?s=20))
- **1100+ GitHub stars** (from 12 stars at launch - help us reach 1,500!)
- **150+ inbound messages** from logistics companies, gig platforms, field service providers  
- **5 active pilot programs** with trucking companies and delivery fleets
- **3 factoring companies** exploring partnership integrations
- Validated product-market fit within first 24 hours

**Star growth shows real demand.** Help us reach 1,500 stars → **[Star this repo now](https://github.com/actionstatelabs/android-action-kernel/stargazers)**

**Current priority partnerships:**
- **Trucking/logistics companies** - Factoring app automation, invoice processing, driver workflows
- **QA testing teams** - Automated mobile app testing at scale

Due to overwhelming demand, we created a meeting scheduler. **[Request a partnership meeting →](https://build.fillout.com/editor/ctqhgaBkaKus/share)**

---

## The Market: Mobile-First Industries

| Industry | Why They Need This | Market Size | Current State |
|----------|-------------------|-------------|---------------|
| **Logistics** | Drivers use factoring apps (RTS Pro, OTR Capital) in truck cabs | **$10.5T** | Manual, no laptop ac