<p align="center">
  <img src="https://github.com/user-attachments/assets/4f3d1ba3-ea8e-4ecd-b59d-c1c8a501337c" alt="RepShot Logo" width="680"/>
</p>

# ⚡ RepShot  _·_  Security Finding Card for Burp Suite

> **Turn your Burp Suite findings into clean, professional cards, ready for reports, bug bounty submissions, and social sharing.**

<p align="center">
  <img src="https://img.shields.io/badge/Burp%20Suite-Extension-orange?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Java-17%2B-blue?style=for-the-badge&logo=java"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Burp-Champion-red?style=for-the-badge"/>
</p>

---

## The Problem

Every pentester knows the moment: you've just confirmed a `SQL injection`, an `XSS` payload, or a path traversal returned `/etc/passwd`. Now you need to document it.

The usual workflow looks like this:

1. Open _Flameshot_ or a screenshot tool
2. Take a screenshot of the request
3. Take another screenshot of the response
4. Draw red boxes around the relevant parts manually
5. Open your report template
6. Copy/paste the vulnerability name, write the business impact from scratch
7. Repeat for every single finding

When you're running a pentest or a bug bounty session with 10, 15, or 20 findings - this process kills your momentum. You spend more time documenting than hacking.

**RepShot was built to fix that.**

---

## What RepShot Does ?

RepShot is a Burp Suite extension that adds a **"Send to RepShot"** option to your Repeater context menu. From there, you get a dedicated panel where you can:

- **Scroll to the exact part of the request or response** you want to show
- **Capture that exact viewport** — what you see is what gets exported
- **Draw red annotation boxes** directly on the capture before exporting
- **Search** inside request/response with `Cmd+F` / `Ctrl+F`
- **Auto-fill the business impact** based on the vulnerability type selected
- **Export a professional HD PNG card** ready to paste into any report or post on LinkedIn/X

No more context switching. No more Flameshot. No more writing "An attacker could..." from scratch for the tenth time today.

---

## Screenshots

> *Example finding card exported by RepShot*

<img width="2400" height="1522" alt="repshot-finding2" src="https://github.com/user-attachments/assets/7fda7566-aa37-4624-a8ea-ecb6f72fc720" />

---

## Installation

### Option A - Use the prebuilt JAR (recommended)

1. Download `repshot-1.0.0.jar` from the [Releases](../../releases) page
2. Open Burp Suite
3. Go to **Extensions → Add**
4. Extension type: **Java**
5. Select the downloaded JAR
6. Click **Next** - you should see `RepShot loaded` in the Output tab

**Requirements:** Burp Suite 2023.x or later · Java 17+ on your system

<img width="1178" height="638" alt="image" src="https://github.com/user-attachments/assets/f6207039-edd4-4928-ad83-51688a66eb5d" />

<img width="907" height="284" alt="image" src="https://github.com/user-attachments/assets/b204e619-8fd4-4f73-849f-090f9b67073b" />



### Option B - Build from source

```ruby
git clone https://github.com/JFOZ1010/repshot.git
cd repshot
mvn clean package
# JAR will be at target/repshot-1.0.0.jar
```
**Requirements**: Java 17+, Maven 3.8+

<img width="938" height="735" alt="image" src="https://github.com/user-attachments/assets/61025168-8ef3-40b2-829e-5f88cbd16c3f" />

---

## How to Use

### Basic workflow

1. Send a request to **Repeater** and fire it
2. **Right-click** anywhere in the request/response → **📸 Send to RepShot**
   
      <img width="602" height="177" alt="image" src="https://github.com/user-attachments/assets/3a2bd081-dce6-4f0d-8916-8d61e9f5d581" />
      
4. The RepShot panel opens with your request and response loaded

   <img width="1159" height="779" alt="Panel-repshot" src="https://github.com/user-attachments/assets/06b2f99e-ce87-4741-8b29-3eccc5deb9ce" />

### Documenting a finding

1. **Fill in the finding details** - title, vulnerability type, severity, your handle
   - Business impact auto-fills based on the vulnerability type selected
   - Selecting a different type updates the impact automatically
   - Choose "Other..." to type a custom vulnerability name
  
     <img width="1059" height="197" alt="image" src="https://github.com/user-attachments/assets/d44b0f44-2ca3-4d29-be0d-74a6d83af480" />
     <img width="622" height="131" alt="image" src="https://github.com/user-attachments/assets/ab04ddf8-438b-43a4-bbf1-2dbc43a835d2" />


2. **Navigate to the relevant part** of the request or response using scroll

3. **Click `[ 📷 Capture ]`** - this captures exactly what's visible in the panel at that moment (_What You See is What You Get_)

4. **Annotate with red boxes** (optional):
   - Click `[ ✏ Draw Box ]` to enter drawing mode
   - Click and drag to draw annotation rectangles over the payload or evidence
     <img width="1010" height="515" alt="image" src="https://github.com/user-atta