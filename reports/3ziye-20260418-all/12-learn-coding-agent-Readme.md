# Claude Code Architecture Study

> **Introduction**: This project is a learning and research repository focused on CLI Agent architecture. All materials are compiled entirely from publicly available online references and discussions, with a particular focus on public information regarding the highly popular CLI Agent `claude-code`. Our intention is to help developers better understand and utilize Agent technologies. We will continue to share more insights and practical discussions on Agent architecture in the future. Thank you for your support!

> **Disclaimer**: All content in this repository is provided strictly for technical research, study, and educational exchange among enthusiasts. **Commercial use is strictly prohibited.** No individual, organization, or entity may use this content for commercial purposes, profit-making activities, illegal activities, or any other unauthorized scenarios. If any content infringes upon your legal rights, intellectual property, or other interests, please contact us and we will verify and remove it immediately.


**Language**: **English** | [中文](README_CN.md) | [한국어](README_KR.md) | [日本語](README_JA.md)

---

## Table of Contents

- [Deep Analysis Reports (`docs/`)](#deep-analysis-reports-docs) — Telemetry, codenames, undercover mode, remote control, future roadmap
- [Directory Reference](#directory-reference) — Code structure tree
- [Architecture Overview](#architecture-overview) — Entry → Query Engine → Tools/Services/State
- [Tool System & Permissions](#tool-system-architecture) — 40+ tools, permission flow, sub-agents
- [The 12 Progressive Harness Mechanisms](#the-12-progressive-harness-mechanisms) — How Claude Code layers production features on the agent loop

---

## Deep Analysis Reports (`docs/`)

Deep analysis reports compiled from publicly available online references and community discussions on Claude Code v2.1.88. Quadrilingual (EN/JA/KO/ZH).

```
docs/
├── en/                                        # English
│   ├── [01-telemetry-and-privacy.md]          # Telemetry & Privacy — what's collected, why you can't opt out
│   ├── [02-hidden-features-and-codenames.md]  # Codenames (Capybara/Tengu/Numbat), feature flags, internal vs external
│   ├── [03-undercover-mode.md]                # Undercover Mode — hiding AI authorship in open-source repos
│   ├── [04-remote-control-and-killswitches.md]# Remote Control — managed settings, killswitches, model overrides
│   └── [05-future-roadmap.md]                 # Future Roadmap — Numbat, KAIROS, voice mode, unreleased tools
│
├── ja/                                        # 日本語
│   ├── [01-テレメトリとプライバシー.md]          # テレメトリとプライバシー — 収集項目、無効化不可の理由
│   ├── [02-隠し機能とコードネーム.md]           # 隠し機能 — モデルコードネーム、feature flag、内部/外部ユーザーの違い
│   ├── [03-アンダーカバーモード.md]             # アンダーカバーモード — オープンソースでのAI著作隠匿
│   ├── [04-リモート制御とキルスイッチ.md]       # リモート制御 — 管理設定、キルスイッチ、モデルオーバーライド
│   └── [05-今後のロードマップ.md]               # 今後のロードマップ — Numbat、KAIROS、音声モード、未公開ツール
│
├── ko/                                        # 한국어
│   ├── [01-텔레메트리와-프라이버시.md]          # 텔레메트리 및 프라이버시 — 수집 항목, 비활성화 불가 이유
│   ├── [02-숨겨진-기능과-코드네임.md]          # 숨겨진 기능 — 모델 코드네임, feature flag, 내부/외부 사용자 차이
│   ├── [03-언더커버-모드.md]                   # 언더커버 모드 — 오픈소스에서 AI 저작 은폐
│   ├── [04-원격-제어와-킬스위치.md]            # 원격 제어 — 관리 설정, 킬스위치, 모델 오버라이드
│   └── [05-향후-로드맵.md]                     # 향후 로드맵 — Numbat, KAIROS, 음성 모드, 미공개 도구
│
└── zh/                                        # 中文
    ├── [01-遥测与隐私分析.md]                    # 遥测与隐私 — 收集了什么，为什么无法退出
    ├── [02-隐藏功能与模型代号.md]                # 隐藏功能 — 模型代号，feature flag，内外用户差异
    ├── [03-卧底模式分析.md]                     # 卧底模式 — 在开源项目中隐藏 AI 身份
    ├── [04-远程控制与紧急开关.md]                # 远程控制 — 托管设置，紧急开关，模型覆盖
    └── [05-未来路线图.md]                       # 未来路线图 — Numbat，KAIROS，语音模式，未上线工具
```

> Click any filename above to jump to the full report.

| # | Topic | Key Findings |
|---|-------|-------------|
| 01 | **Telemetry & Privacy** | Two analytics sinks (1P, Datadog). Environment fingerprint, process metrics, repo hash on every event. **No UI-exposed opt-out** for 1st-party logging. `OTEL_LOG_TOOL_DETAILS=1` enables full tool input capture. |
| 02 | **Hidden Features & Codenames** | Animal codenames (Capybara v8, Tengu, Fennec→Opus 4.6, **Numbat** next). Feature flags use random word pairs (`tengu_frond_boric`) to obscure purpose. Internal users get better prompts, verification agents, and effort anchors. Hidden commands: `/btw`, `/stickers`. |
| 03 | **Undercover Mode** | Official employees auto-enter undercover mode in public repos. Model instructed: *"Do not blow your cover"* — strip all AI attribution, write commits "as a human developer would." **No force-OFF exists.** Raises transparency questions for open-source communities. |
| 04 | **Remote Control** | Hourly polling of `/api/claude_code/settings`. Dangerous changes show blocking dialog — **reject = app exits**. 6+ killswitches (bypass permissions, fast mode, voice mode, an