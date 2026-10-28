<div align="center">

<img src="icon/wordmark.svg" alt="OpenTRAP" height="56">

<p><strong>Open Traffic Replay and Analysis Proxy</strong><br>
A free and open-source alternative to Burp Suite, built on the trusted OWASP ZAP engine.</p>

<p>
<img src="https://img.shields.io/badge/licence-AGPL--3.0-e5484d?style=flat-square" alt="Licence">
<img src="https://img.shields.io/badge/Java-17%2B-5b8def?style=flat-square" alt="Java">
<img src="https://img.shields.io/badge/platform-Linux-9aa7b4?style=flat-square&logo=linux&logoColor=white" alt="Platform">
<img src="https://img.shields.io/badge/status-active%20development-3fb950?style=flat-square" alt="Status">
</p>

<p>
<a href="https://github.com/opentrap/opentrap/releases/latest/download/opentrap-x86_64.appimage"><img src="https://img.shields.io/badge/Download-AppImage%20for%20Linux-3fb950?style=for-the-badge&logo=linux&logoColor=white" alt="Download the latest AppImage for Linux"></a>
&nbsp;
<a href="https://github.com/opentrap/opentrap/stargazers"><img src="https://img.shields.io/github/stars/opentrap/opentrap?style=for-the-badge&logo=github&logoColor=white&label=Star&color=e5484d" alt="Star on GitHub"></a>
&nbsp;
<a href="https://github.com/opentrap/opentrap/releases/latest"><img src="https://img.shields.io/badge/All%20releases-30363d?style=for-the-badge&logo=github&logoColor=white" alt="All releases"></a>
</p>

<sub><b>Share:</b>
<a href="https://twitter.com/intent/tweet?text=OpenTRAP%2C%20an%20open-source%20web%20security%20testing%20suite&url=https%3A%2F%2Fgithub.com%2Fopentrap%2Fopentrap">X</a> &middot;
<a href="https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fgithub.com%2Fopentrap%2Fopentrap">LinkedIn</a> &middot;
<a href="https://www.reddit.com/submit?url=https%3A%2F%2Fgithub.com%2Fopentrap%2Fopentrap&title=OpenTRAP">Reddit</a> &middot;
<a href="https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fgithub.com%2Fopentrap%2Fopentrap&t=OpenTRAP">Hacker News</a>
</sub>

</div>

<p align="center"><b>One command to download and run the tool:</b></p>

```
wget https://github.com/opentrap/opentrap/releases/latest/download/opentrap-x86_64.appimage && chmod +x opentrap-x86_64.appimage && ./opentrap-x86_64.appimage
```

<div align="center">

<a href="docs/images/dashboard.png"><img src="docs/images/dashboard.png" width="100%" alt="OpenTRAP dashboard with a crawl and an audit finished, their cards showing locations found and issues by severity, and the live table of the most serious vulnerabilities found"></a>

<p><sub>The Dashboard after a scan: the crawl's locations and requests, the audit's findings by severity, and the most serious vulnerabilities as they were confirmed.</sub></p>

</div>

---

## Proudly free and open source

OpenTRAP is free and open source software, released under the GNU AGPL v3.0 with
no licence gate on anything. We stand with the organisations that make free and
open source software possible - if OpenTRAP is useful to you, consider supporting them.

<p align="center">
<a href="https://www.fsf.org/"><img src="docs/images/orgs/fsf.png" height="32" alt="Free Software Foundation"></a>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://opensource.org/"><img src="docs/images/orgs/osi.svg" height="44" alt="Open Source Initiative"></a>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://sfconservancy.org/"><img src="docs/images/orgs/sfc.svg" height="40" alt="Software Freedom Conservancy"></a>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://fsfe.org/"><img src="docs/images/orgs/fsfe.svg" height="44" alt="Free Software Foundation Europe"></a>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://www.eff.org/"><img src="docs/images/orgs/eff.svg" height="32" alt="Electronic Frontier Foundation"></a>
</p>

---

## Why we built it

The most capable intercepting proxies, such as Burp Suite, are commercial and
closed, with their most useful features behind a paid licence. OWASP ZAP is a
powerful open engine, but its interface is unfamiliar to the many testers who work
proxy-first. OpenTRAP brings the two together: the familiar Burp-style workflow on
top of the trusted OWASP ZAP detection engine, genuinely **open**, genuinely useful
day to day, and immediately **familiar** to anyone who has worked with an
intercepting proxy before.

OpenTRAP is that tool. A complete testing workspace with a clean, recognisable
workflow, that any practitioner can run, inspect, and extend, with no licence gate
on its core capabilities. It is built to be improved by the people who use it
rather than steered by a single vendor's roadmap. If a security tester can describe
a better way to work, OpenTRAP should be the tool that lets them build it.

## What it is

A proxy-first workspace for web application testing. Capture, inspect, replay and
tamper with the traffic between a browser and a web application. Map an
application's attack surface, and drive repeatable manual and automated testing
from one window: interception, HTTP history, a target site map