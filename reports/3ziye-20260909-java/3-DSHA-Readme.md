# DSHA

<p align="center">
  <b>DeepSeek Harness 安卓启动器</b><br>
  在手机上跑完整的 <a href="https://github.com/deepseek-ai/deepseek-harness">deepseek-harness</a> —— 免 ROOT，免 Termux，装完即用
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT"></a>
  <a href="https://github.com/qiannianhuanxiang/DSHA/releases/latest"><img src="https://img.shields.io/github/v/release/qiannianhuanxiang/DSHA?color=blue" alt="release"></a>
  <a href="https://github.com/qiannianhuanxiang/DSHA/stargazers"><img src="https://img.shields.io/github/stars/qiannianhuanxiang/DSHA?style=flat" alt="stars"></a>
  <img src="https://img.shields.io/badge/Android-8.0%2B-3DDC84?logo=android&logoColor=white" alt="android">
  <img src="https://img.shields.io/badge/arch-arm64--v8a-lightgrey" alt="arch">
</p>

<p align="center">
  <a href="README.en.md">English</a> · <b>简体中文</b> · <a href="CHANGELOG.md">更新记录</a> · <a href="docs/security-model.md">安全模型</a> · <a href="AGENTS.md">AGENTS.md（给 AI / 开发者）</a>
</p>

> 🤖 下一个 AI / 开发者请先读 **[AGENTS.md](AGENTS.md)**（项目结构、启动契约、踩过的坑），不要先全库扫描。

---

## 📣 v1.2.0-rc1.4（体验与可靠性修复 · 预览版）

本次以 **Pre-release（预览版）** 发布，由贡献者 [@ym2025szz](https://github.com/ym2025szz) 推进，感谢原作者 [@qiannianhuanxiang](https://github.com/qiannianhuanxiang) 及其他贡献者。

本版集中修复安装检查慢、详细输出缺失、备份恢复、命令无返回及终端进程残留，并完善后台下载、插件任务、更新状态和双内核对话体验。原生页面按适度紧凑的方向重排，配置保存固定底部，保留右上角日夜切换；“显示与运行”逐项说明作用和生效时机。

[GitHub 预览版说明与下载](https://github.com/DSH-APP/DSHA/releases/tag/v1.2.0-rc1.4) · [完整更新说明](docs/releases/v1.2.0-rc1.4.md) · [功能验收与覆盖边界](docs/functional-audit-rc1.4.md)

| 预览版 | 设备范围 | 下载 | 大小 |
|---|---|---|---:|
| 高安卓标准版 | Android 11+ / arm64，系统 WebView | [dsha-1.2.0-rc1.4.apk](https://github.com/DSH-APP/DSHA/releases/download/v1.2.0-rc1.4/dsha-1.2.0-rc1.4.apk) · [SHA-256](https://github.com/DSH-APP/DSHA/releases/download/v1.2.0-rc1.4/dsha-1.2.0-rc1.4.apk.sha256) | 212.87 MiB |
| 低安卓兼容版 | Android 6+ / arm64，内置 Gecko 备用内核 | [dsha-1.2.0-rc1.4low.apk](https://github.com/DSH-APP/DSHA/releases/download/v1.2.0-rc1.4/dsha-1.2.0-rc1.4low.apk) · [SHA-256](https://github.com/DSH-APP/DSHA/releases/download/v1.2.0-rc1.4/dsha-1.2.0-rc1.4low.apk.sha256) | 289.69 MiB |

版本码 **113**，沿用历史发布签名与环境版本 **9**，同签名覆盖安装保留已有环境。两版共享包名和数据，不能并排安装；dsh 仍为 **0.1.2-rc.1**。

**验证范围：**Android 13 实测六步检查约 **1.9 秒**，完成真实官方模型往返、App 无线 ADB、备份、超时/取消回收和系统 WebView / Gecko 检查。两版构建、签名及相关测试通过；其他 Android 版本、真实 16 KB 内核和厂商后台行为仍需补充覆盖，见验收报告。

📮 预览版反馈：[GitHub Issues](https://github.com/DSH-APP/DSHA/issues) / QQ 群 **975836806**，请附机型、系统版本、复现步骤及 App 脱敏诊断报告。

## 📣 v1.2.0-rc1.3（更新与恢复 · 预览版）

本次以 **Pre-release** 发布，由贡献者 [@ym2025szz](https://github.com/ym2025szz) 推进，感谢原作者 [@qiannianhuanxiang](https://github.com/qiannianhuanxiang) 及其他贡献者。

新增稳定 / 预览更新通道与 APK 下载校验、[官网插件安装入口](https://dsha.cc/install/)、脱敏诊断复制/导出及工具修复、插件更新/上一版回退和安全启动。

[GitHub 预览版说明与下载](https://github.com/DSH-APP/DSHA/releases/tag/v1.2.0-rc1.3) · [官网备用下载](https://dsha.cc/download/) · [完整更新说明](docs/releases/v1.2.0-rc1.3.md)

| 预览版 | 设备范围 | 下载 | 大小 |
|---|---|---|---:|
| 高安卓标准版 | Android 11+ / arm64，系统 WebView | [dsha-1.2.0-rc1.3.apk](https://github.com/DSH-APP/DSHA/releases/download/v1.2.0-rc1.3/dsha-1.2.0-rc1.3.apk) · [SHA-256](https://github.com/DSH-APP/DSHA/releases/download/v1.2.0-rc1.3/dsha-1.2.0-rc1.3.apk.sha256) | 212.45 MiB |
| 低安卓兼容版 | Android 6+ / arm64，内置 Gecko 备用内核 | [dsha-1.2.0-rc1.3low.apk](https://github.com/DSH-APP/DSHA/releases/download/v1.2.0-rc1.3/dsha-1.2.0-rc1.3low.apk) · [SHA-256](https://github.com/DSH-APP/DSHA/releases/download/v1.2.0-rc1.3/dsha-1.2.0-rc1.3low.apk.sha256) | 289.49 MiB |

版本码 **112**，沿用历史发布签名与环境版本 **9**，可覆盖同签名旧版并保留已有环境。两版共享包名与数据，不能并排安装；包内 dsh 仍为 `0.1.2-rc.1`。

**验证范围：**两版构建、Lint 与相关测试通过，Android 13 验证更新、插件安装/回退、安全启动和两种浏览内核。其他系统与正式签名 App Link 自动关联的实测限制，见[验收记录](docs/release-rc1.3-2026-09-07.md)。

📮 预览版反馈：[GitHub Issues](https://github.com/DSH-APP/DSHA/issues) / QQ 群 **975836806**，可附 App 诊断报告和复现步骤。

以下保留上次预览版说明及更早的原有介绍。

## 📣 v1.2.0-rc1.2（重构版 · 预览版）

1.2 系列的重构与适配由贡献者 [@ym2025szz](https://github.com/ym2025szz) 推进，本次仍以 **Pre-release** 发布。感谢原作者 [@qiannianhuanxiang](https://github.com/qiannianhuanxiang) 及其他贡献者。

[查看完整更新说明与下载](https://github.com/qiannianhuanxiang/DSHA/releases/tag/v1.2.0-rc1.2) · [插件选取：dsha.cc](https://dsha.cc/) · [上个预览版 rc1](https://github.com/qiannianhuanxiang/DSHA/releases/tag/v1.2.0-rc1)

| 预览版 | 设备范围 | 下载 | 大小 |
|---|---|---|---:|
| 高安卓标准版 | Android 11+ / arm64，系统 WebView | [dsha-1.2.0-rc1.2.apk](https://github.com/qiannianhuanxiang/DSHA/releases/download/v1.2.0-rc1.2/dsha-1.2.0-rc1.2.apk) · [SHA-256](https://github.com/qiannianhuanxiang/DSHA/releases/download/v1.2.0-rc1.2/dsha-1.2.0-rc1.2.apk.sha256) | 212.39 MiB |
| 低安卓兼容版 | 面向 Android 6—12 / arm64，内置 Gecko 备用内核 | [dsha-1.2.0-rc1.2low.apk](https://github.com/qiannianhuanxiang/DSHA/releases/download/v1.2.0-rc1.2/dsha-1.2.0-rc1.2low.apk) · [SHA-256](https://github.com/qiannianhuanxiang/DSHA/releases/download/v1.2.0-rc1.2/dsha-1.2.0-rc1.2low.apk.sha256) | 289.46 MiB |

**相比此前已发布的 rc1：**

- **插件市场可用**：链接识别与安装、本地导入、多选