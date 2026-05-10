# MHR-CFW

### MITM Domain-Fronted HTTP Relay + Cloudflare Worker Exit

[![GitHub](https://img.shields.io/badge/GitHub-MHR_CFW-red?logo=github)](https://github.com/denuitt1/mhr-cfw)


| [English](README.md) | [Persian](README_FA.md) |
| :---: | :---: |

---

## How It Works

### 1 - GAS + Cloudflare Worker Exit
```
Client -> Local Relay -> Google/CDN Front -> GAS (Google Apps Script) Relay -> Cloudflare Worker -> Exit
            |
            +-> Shows www.google.com to network DPI filter
```

### 2 - GAS + Cloudflare Worker Middle + Self-Hosted Upstream Forwarder Relay Exit
```
Client -> Local Relay -> Google/CDN Front -> GAS (Google Apps Script) Relay -> Cloudflare Worker -> Self-Hosted Upstream Forwarder -> Exit
            |
            +-> Shows www.google.com to network DPI filter
```

In normal use, the browser sends traffic to the proxy running on your computer.
The proxy sends that traffic through Google-facing infrastructure so the network only sees an allowed domain such as `www.google.com`.
Your deployed relay then fetches the real website through cloudflare worker and sends the response back through the same path.

This means the filter sees normal-looking Google traffic, while the actual destination stays hidden inside the relay request.


--- 

## How to Use

### 1 - Download project and extract 

```bash
git clone https://github.com/denuitt1/mhr-cfw.git
cd mhr-cfw
pip install -r requirements.txt
```
> **Can't reach PyPI directly?** Use this mirror instead:
> ```bash
> pip install -r requirements.txt -i https://mirror-pypi.runflare.com/simple/ --trusted-host mirror-pypi.runflare.com
> ```


### 2 - Set Up the Cloudflare Worker (worker.js)

1. Open [Cloudflare Dashboard](https://dash.cloudflare.com/) and sign in with your Cloudflare account.
2. From the sidebar, navigate to **Compute > Workers & Pages**
3. Click **Create Application**, Choose **Start with Hello World** and click on **Deploy**
4. Click on **Edit code** and **Delete** all the default code in the editor.
5. Open the [`worker.js`](deploy/cloudflare-worker/worker.js) file from this project (under `deploy/`), **copy everything**, and paste it into the Apps Script editor.
6. **Important:** Change the worker on this line to the worker you created:
   ```javascript
   const WORKER_URL = "myworker.workers.dev";
   ```
7. Click **Deploy**.

### 3 - Set Up the Google Relay (Code.gs)

1. Open [Google Apps Script](https://script.google.com/) and sign in with your Google account.
2. Click **New project**.
3. **Delete** all the default code in the editor.
4. Open the [`Code.gs`](deploy/gas/Code.gs) file from this project (under `deploy/`), **copy everything**, and paste it into the Apps Script editor.
5. **Important:** Change the password on this line to something only you know, also replace the worker url with your cloudflare worker:
   ```javascript
   const AUTH_KEY = "your-secret-password-here";
   const WORKER_URL = "https://myworker.workers.dev";
   ```
6. Click **Deploy** → **New deployment**.
7. Choose **Web app** as the type.
8. Set:
   - **Execute as:** Me
   - **Who has access:** Anyone
9. Click **Deploy**.
10. **Copy the Deployment ID** (it looks like a long random string). You'll need it in the next step.

> ⚠️ Remember the password you set in step 3. You'll use the same password in the config file below.

### 4 - Run

Click on the `run.bat` file (on windows) or `run.sh` file (on linux) to start the relay.

If you're running for the first time it will prompt a setup wizard where you have to enter the AUTH_KEY and Google Apps Script Deployment ID.
You should see a message saying the HTTP proxy is running on `127.0.0.1:8085`

### 5 - Usage

We recommend using [v2rayN client](https://github.com/2dust/v2rayn) and configuring a socks5 proxy.

You can also use [FoxyProxy](https://getfoxyproxy.org/)'s [Chrome extension](https://chromewebstore.google.com/detail/foxyproxy/gcknhkkoolaabfmlnjonogaaifnjlfnp?hl=en) or [Firefox extension](https://addons.mozilla.org/en-US/firefox/addon/foxyproxy-standard/) to use this proxy in your browser.

### 6 - Test your connection

Open [ipleak.net](https://ipleak.net) in your browser, you should see your ip address set as cloudflare's.

<img width="1454" height="869" alt="image" src="https://github.com/user-attachments/assets/dfd3316d-69b6-4b0e-b564-fdb055dbdafd" />


---

## Optional: Stable Exit IP via Upstream Forwarder

CAPTCHAs (Cloudflare Turnstile/bot challenge, reCAPTCHA, hCaptcha) bind tokens
to the IP that solved the challenge. Cloudflare Workers exit through different
edge IPs per request, so verification on the target site fails even when you
solve the challenge. This optional add-on lets the Worker forward all `fetch()`
calls through a small Node server you run on a VPS with a stable IP — giving
the target site one consistent exit address.

### When you need this

- Sites b