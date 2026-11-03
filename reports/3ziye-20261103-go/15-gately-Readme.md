<p align="center">
  <a href="https://gately.cn/en/"><img src="docs/images/banner.svg" alt="Gately — The all-in-one network gateway: Open source, ready out of the box" width="100%"></a>
</p>

<p align="center">
  <a href="https://github.com/wangwanjie/gately/releases/latest"><img src="https://img.shields.io/github/v/release/wangwanjie/gately?style=flat-square&color=0e7c66&label=release" alt="Release"></a>
  <a href="https://github.com/wangwanjie/gately/pkgs/container/gately"><img src="https://img.shields.io/badge/docker-ghcr.io%2Fwangwanjie%2Fgately-0e7c66?style=flat-square&logo=docker&logoColor=white" alt="Docker"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/wangwanjie/gately?style=flat-square&color=0e7c66" alt="License"></a>
  <a href="https://github.com/wangwanjie/gately/stargazers"><img src="https://img.shields.io/github/stars/wangwanjie/gately?style=flat-square&color=0e7c66" alt="Stars"></a>
  <a href="https://gately.cn/en/"><img src="https://img.shields.io/badge/Website-gately.cn-0e7c66?style=flat-square&logo=googlechrome&logoColor=white" alt="gately.cn"></a>
  <a href="https://t.me/gately_chat"><img src="https://img.shields.io/badge/Telegram-gately__chat-26A5E4?style=flat-square&logo=telegram&logoColor=white" alt="Telegram"></a>
</p>

<p align="center">
  <a href="https://gately.cn/en/"><b>Website</b></a> &nbsp;·&nbsp; <a href="https://gately.cn/en/docs/guide/quick-start"><b>Quick start</b></a> &nbsp;·&nbsp; <a href="https://gately.cn/en/docs/guide/install"><b>Install guide</b></a> &nbsp;·&nbsp; <a href="https://gately.cn/en/docs/guide/introduction"><b>Docs</b></a> &nbsp;·&nbsp; <a href="https://github.com/wangwanjie/gately/releases/latest"><b>Download</b></a> &nbsp;·&nbsp; <a href="https://gately.cn/en/news/"><b>Changelog</b></a>
</p>

<p align="center">
  <a href="https://gately.cn/en/sponsor"><img src="https://img.shields.io/badge/Buy%20me%20a%20coffee-Gately-FFDD00?style=for-the-badge&logo=buymeacoffee&logoColor=black" alt="Buy me a coffee" height="34"></a>
</p>

<p align="center">
  <b>English</b> | <a href="README.zh-CN.md">简体中文</a> | <a href="README.zh-TW.md">繁體中文</a> | <a href="README.ja.md">日本語</a> | <a href="README.ko.md">한국어</a> | <a href="README.es.md">Español</a> | <a href="README.fr.md">Français</a> | <a href="README.de.md">Deutsch</a> | <a href="README.ru.md">Русский</a> | <a href="README.pt-BR.md">Português (Brasil)</a>
</p>

DNS and NAT traversal, reverse proxy and HTTPS certificates, WAF and intrusion prevention, single sign-on and file sharing: everything your home network and servers need at the edge, managed from one console. Run it on a NAS, a soft router or a cloud server and set it all up in your browser. Open source under Apache-2.0; your config and data stay on your own device, and nothing is collected or reported.

> **fnOS users:** Gately ships as a native fnOS app. It plugs into the **fnOS unified gateway**, so it opens from the fnOS desktop icon and works over the same address you use for fnOS, including your remote domain, with no extra port to open. Once enabled, **fnOS administrators can sign in directly with their fnOS session**, without a Gately password or two-step code. See [fnOS native app](https://gately.cn/en/docs/guide/install#fnos).

https://github.com/user-attachments/assets/ae5b60a4-9402-4a66-86a1-48e40038b4d0

## Quick Start

Three steps: start the container, open `http://<device-ip>:16680`, sign in with `admin` / `gately.cn`. Other platforms are below, and the [install guide](https://gately.cn/en/docs/guide/install) covers every option.

### Docker

Images are available for amd64, arm64, and arm/v7, published to GHCR and to Docker Hub as `vanjayak/gately` (same image and tags; use `vanjayak/gately:latest` if GHCR is hard to reach):

```bash
docker run -d --name gately --network host --cap-add NET_ADMIN \
  -v ./gately-data:/etc/gately \
  -v /var/run/docker.sock:/var/run/docker.sock \
  ghcr.io/wangwanjie/gately:latest
```

Open `http://<device-ip>:16680` and sign in with the default account `admin` and the default password `gately.cn`. Then change the password and enable two-factor authentication under Settings. See [deploy/docker-compose.yml](deploy/docker-compose.yml) for a complete Compose example.

If you forget the password or lose your authenticator, run `gately reset-password` or `gately reset-totp` on the server (`docker exec -it gately gately reset-password` for Docker); the change takes effect once you confirm. See [Reset password and two-factor authentication](https://gately.cn/en/docs/guide/install#reset).

Port forwarding, STUN, and web services listen on host ports, so `--network host` is recommended. If you do not need Docker management, drop the `docker.sock` mount. `--cap-add NET_ADMIN` lets Intrusion Prevention write bans to the host's nftables firewall; without it, bans still apply to Gately's own services.

Prefer another way to install? Pick one below.

<details>
<summary><b>Binary</b></summary>

Download 