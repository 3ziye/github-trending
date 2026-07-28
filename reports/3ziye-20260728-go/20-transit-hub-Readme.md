# TransitHub

<div align="center">

[![Go](https://img.shields.io/badge/Go-1.25+-00ADD8.svg)](https://golang.org/)
[![Vue](https://img.shields.io/badge/Vue-3.5+-4FC08D.svg)](https://vuejs.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16+-336791.svg)](https://www.postgresql.org/)
[![Redis](https://img.shields.io/badge/Redis-7+-DC382D.svg)](https://redis.io/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)](https://www.docker.com/)

**A multi-upstream operations hub for self-hosted API services built with sub2api or new-api.**

English | [中文](README_CN.md)

</div>

## Important Notice

Please read the following carefully before using this project:

- **Provider policy risk**: TransitHub helps administrators connect to and operate upstream admin platforms. Make sure your use complies with the terms of service of every upstream platform you connect.
- **Compliant use only**: Use this project only in compliance with the laws and regulations of your country or region. Do not use it to bypass authorization, abuse upstream services, or operate accounts you do not control.
- **Self-hosting responsibility**: You are responsible for protecting admin credentials, database backups, network access, and deployment secrets in your own environment.
- **Disclaimer**: This project is for technical learning only. You are responsible for complying with applicable laws and upstream platform policies. The authors assume no liability for service interruptions, account restrictions, data loss, or any direct or indirect damages caused by using this project.

## Sponsors

<table>
<thead>
<tr>
<th align="center" valign="middle" width="130">Name</th>
<th align="left" valign="middle" width="78%">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center" valign="middle" width="130"><a href="https://www.recycleai.vip/"><img src="docs/assets/sponsors/recycleai-logo.png" alt="RecycleAI logo" height="28"><br><strong>RecycleAI</strong></a></td>
<td valign="middle" width="78%">An innovation platform for AI resource reuse and intelligent service circulation, improving coordination across compute, model, and application capabilities.</td>
</tr>
<tr>
<td align="center" valign="middle" width="130"><a href="https://www.xiongxiongai.online"><img src="docs/assets/sponsors/xiongxiongai-logo.png" alt="XiongXiongAI logo" height="30"><br><strong>XiongXiongAI</strong></a></td>
<td valign="middle" width="78%">An AI service brand centered on approachable experiences, stable access, and lightweight intelligent tools for reliable everyday usage.</td>
</tr>
<tr>
<td align="center" valign="middle" width="130"><a href="https://console.qqqrouter.ai"><img src="docs/assets/sponsors/qqqrouter-logo.png" alt="qqqRouter logo" height="24"><br><strong>qqqRouter</strong></a></td>
<td valign="middle" width="78%">An AI infrastructure platform for multi-model access, request routing, and usage governance, helping teams build more flexible and controllable model invocation workflows.</td>
</tr>
<tr>
<td align="center" valign="middle" width="130"><a href="https://sparkcode.top"><img src="docs/assets/sponsors/sparkcode-logo.png" alt="SparkCode logo" height="30"><br><strong>SparkCode</strong></a></td>
<td valign="middle" width="78%">A stable and efficient API relay provider for mainstream AI coding models including Claude Code, Codex, and Gemini with NanoBanana-series models; supports monthly plans, usage-based billing, high-concurrency calls, invoiced top-ups, dedicated enterprise onboarding, technical support, and a long-term invitation rebate program.</td>
</tr>
<tr>
<td align="center" valign="middle" width="130"><a href="https://uuapi.net"><img src="docs/assets/sponsors/uuapi.svg" alt="UU API logo" height="30"><br><strong>UU API</strong></a></td>
<td valign="middle" width="78%">An AI compute gateway for global developers and enterprises, offering one-stop access to ChatGPT, Claude, Gemini, and other major models through transparent official or first-hand channels, with reliable infrastructure built to make every call worthwhile.</td>
</tr>
<tr>
<td align="center" valign="middle" width="130"><a href="https://hk.getelucid.com/"><img src="docs/assets/sponsors/ElucidRelay.png" alt="ElucidRelay logo" height="30"><br><strong>ElucidRelay</strong></a></td>
<td valign="middle" width="78%">An API relay providing stable, high-throughput access to major overseas models including OpenAI, Claude, Gemini, and more through a single OpenAI-compatible endpoint; built for resellers and downstream platforms that need reliable volume and competitive pricing.</td>
</tr>
<tr>
<td align="center" valign="middle" width="130"><a href="https://songsongai.com/"><img src="docs/assets/sponsors/songsongai.png" alt="songsongAi logo" height="30"><br><strong>songsongAi</strong></a></td>
<td valign="middle" width="78%">An AI service brand for polished intelligent application experiences, focused on premium model a