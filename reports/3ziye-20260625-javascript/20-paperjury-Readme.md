**中文** · [English](README.en.md)

<p align="center">
  <img src="docs/paperjury-mark.png" alt="PaperJury logo" width="120">
</p>

<h1 align="center">PaperJury</h1>

<p align="center">真正投稿前，先让 AI reviewer 把该挑的坑挑出来。</p>

<p align="center">
  <a href="https://arxiv.org/abs/2606.16322"><img alt="阅读论文（arXiv）" src="https://img.shields.io/badge/arXiv-2606.16322-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white"></a>
  <a href="https://u7079256.github.io/paperjury/overview.html?lang=zh"><img alt="打开在线交互式总览" src="https://img.shields.io/badge/在线交互式总览-d6a14b?style=for-the-badge&logo=githubpages&logoColor=white"></a>
  <a href="samples/dogfood/"><img alt="查看真实样例" src="https://img.shields.io/badge/真实样例-Dogfood-2f7d55?style=for-the-badge"></a>
  <a href="https://github.com/u7079256/paperjury/stargazers"><img alt="Star this repo" src="https://img.shields.io/badge/GitHub-Star-3b3d47?style=for-the-badge&logo=github&logoColor=white"></a>
  <a href="https://github.com/u7079256/paperjury/releases"><img alt="Open releases" src="https://img.shields.io/badge/Releases-Open-3b3d47?style=for-the-badge"></a>
  <img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-3b3d47?style=for-the-badge">
</p>

<p align="center">
  <a href="https://u7079256.github.io/paperjury/overview.html?lang=zh">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="docs/overview-card-dark.png">
      <source media="(prefers-color-scheme: light)" srcset="docs/overview-card-light.png">
      <img src="docs/overview-card.png" alt="PaperJury 交互式总览" width="760">
    </picture>
  </a>
</p>

> **一句话版：** PaperJury 会在投稿前替你的论文做一轮“刻薄但有证据”的 AI 预审：先找 reviewer 可能会抓住的问题，再判断这些问题到底成不成立；能安全修改的只给最小补丁，缺实验、缺证据的交回作者，不靠谱的意见直接驳回。

刚写完初稿、投稿前想再自查一遍，或者只想先让它挑一遍风险，都可以直接用日常话描述需求；不用先研究它的内部机制。

## News

- 🎉 **RedNote（小红书）里程碑：** 相关分享已经达到 **3 万浏览**、**1.8k 收藏**。感谢大家转发和收藏，也感谢大家把 PaperJury 推荐给更多正在赶论文、改论文的朋友。
- 📄 **2026-06-15：PaperJury 论文已上 arXiv。** arXiv 页面：[*PaperJury: Due-Process Review for Bounded LaTeX Revision*](https://arxiv.org/abs/2606.16322)（arXiv:2606.16322）。论文系统介绍了「审稿 → 裁定 → 修改 → 复查」这套引擎：哪些事交给确定性脚本，哪些判断交给语义 agent；有争议的问题如何进入审议；不同风险的编辑该上什么护栏。
- 🔔 **2026-06-10：v1.0.0 发布。** 这是第一个稳定版，和 Codex 版 v1.0 对齐。新增软更新提醒：发现新的稳定 tag 时只提示，不打断当前工作。
- 🚀 **2026-06-05：PaperJury 的 Codex 版已经推送。** 入口在这里：[paperjury-codex](https://github.com/u7079256/paperjury-codex)。
- 🧪 **Dogfood sample 已加入。** 仓库里放了一个紧凑的 [dogfood sample](samples/dogfood/)：修改前后 PDF，以及人工核对过的运行报告。

---

**PaperJury 以 Claude Code skill 的形式提供**，把投稿前自查组织成一套闭环：**审稿 → 裁定 → 修改 → 复查**。它不会照单全收 AI 反馈，而是先把每条意见分成三类：

| 结果 | 含义 |
|---|---|
| **✅ 安全修复** | 表达不清、claim 过强、结构不顺这类文本问题；不需要补实验，也不会把原意改偏。 |
| **🧑‍💻 作者处理** | 缺实验、缺 ablation、缺数据或证据，必须由作者自己判断。 |
| **🛑 不成立** | AI reviewer 误读了论文，或者提了不该改的问题。 |

> [!IMPORTANT]
> PaperJury 是投稿前的自查工具，**不能替代作者的科学判断，也不能替代 peer review**。它不能用来编造实验、伪造结果、添加没有证据支撑的 claim，或掩盖论文局限。遇到需要新实验、缺证据、需要作者私有知识或研究判断的问题，它都会交回作者处理。

## 适合谁

| 你现在的情况 | 可以直接这样用 |
|---|---|
| **📝 刚写完初稿** | 让它像 reviewer 一样通读全文，先找最可能影响投稿的问题。 |
| **🔍 投稿前最后自查** | 让它检查 claim 是否说过头、实验是否撑得住，以及有没有明显格式风险。 |
| **✍️ 只想改一段话** | 直接说「把这段改紧一点，但不要改变 claim」，它会先起草补丁，等你确认后再改。 |
| **🔁 想多轮打磨但不想一直盯着** | 明确授权 auto 模式；安全修改可以落稿，高风险问题仍会交回作者决定。 |

## 你会得到什么

| 输出 | 内容 |
|---|---|
| **📋 问题清单** | 每条 reviewer-style 问题都会带证据、位置、判断结果和当前状态；不会把一堆意见直接倒进正文。 |
| **🧩 可审阅补丁** | 只有安全修复会进入最小补丁；高风险改动会先放着，等作者决定。 |
| **🛠️ 复查报告** | 有 LaTeX 工具链就真实编译；没有就明说哪些检查做不了，不会假装验证过。 |
| **🧪 真实样例** | [`samples/dogfood/`](samples/dogfood/) 里有修改前后 PDF 和人工核对过的运行报告。 |

---

## 目录

- [News](#news)
- [适合谁](#适合谁)
- [你会得到什么](#你会得到什么)
- [快速上手](#快速上手)
- [能帮你做什么](#能帮你做什么)
- [三种模式](#三种模式)
- [真实跑一遍](#真实跑一遍)
- [安装](#安装)
- [常见问题](#常见问题)
- [深入了解](#深入了解)
- [Roadmap](#roadmap)
- [致谢](#致谢)

---

## 快速上手

在 Claude Code 里安装：

```text
/plugin marketplace add u7079256/paperjury
/plugin install paperjury@u7079256
```

然后在你的论文项目里直接说需求：

```text
审稿，重点看实验和 claim 是否站得住。
```

或者更日常一点：

```text
把 introduction 这段改紧一些，但不要改变 claim。
```

不需要背命令。PaperJury 会根据你的描述选择 direct-edit、review 或 auto 模式；真正落稿前，会先把补丁交给你确认。

## 能帮你做什么

| 场景 | PaperJury 会怎么做 |
|---|---|
| **🔎 投稿前挑问题** | 模拟几位不同方向的 reviewer 通读全文，找出真正可能被抓住的弱点，并把致命问题和小修小补分开。 |
| **✍️ 安全改 LaTeX / Markdown** | 只针对你指定的位置起草补丁，自检后再交给你确认；不会把一处小改扩成整篇重写。 |
| **🛡️ 复查格式风险** | 本机有 LaTeX 工具链时会真实编译，检查报错、未定义引用、overfull box、页数和常见 desk-reject 风险；没有工具链时会明说。 |
| **🔁 多轮打磨** | 在你明确授权的 auto 模式下，多轮跑完「评审-修订-复查」；安全修改可以自动应用，高风险问题会留给作者处理。 |

PaperJury 的重点不是“让 AI 多写一点”，而是让 AI 先像 reviewer 一样认真挑错，再用确定性脚本守住能验证的边界。

## 三种模式

| 模式 | 什么时候用 | 行为 | 人工确认 |
|---|---|---|---|
| **✍️ direct-edit**（常用） | 只想改一处文字、caption、LaTeX 表达或段落结构。 | 不开评审面板，直接用写作工具包起草补丁。 | 作者确认后再应用。 |
| **🔎 review**（偶尔） | 想让它审稿、挑问题、mock-review，或只审某一节 / 某条 claim。 | 启动对抗式评审引擎，先判断问题是否成立，再决定要不要修改。 | 每处改动逐一确认。 |
| **🔁 auto**（无人值守） | 已经明确给出 `/goal` 或配置 `mode: auto`，希望它多轮跑到一个可验证目标。 | 先确认 `spine` 和评审分配，再按 bounded-aggressive + edit-safety 策略迭代。 | 先给整体授权；高风险项仍交回作者。 |

简单说：**改一处 → 直接说；想被挑刺 → 说「审稿」；想无人值守 → 用 `/goal`。**

> [!WARNING]
> **auto 必须明确开启。** 只打开工具权限再发普通 prompt，只会跑一轮就停，不会进入多轮循环。原因见 [`docs/AGENT-GUIDE.md`](docs/AGENT-GUIDE.md) §3。

## 真实跑一遍

想看它真