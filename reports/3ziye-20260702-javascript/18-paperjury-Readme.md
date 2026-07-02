<p align="center">
  <img src="docs/paperjury-mark.png" width="170" alt="PaperJury logo">
</p>

<h1 align="center">PaperJury</h1>

<h2 align="center"><b>真正投稿前，先让 AI reviewer 把该挑的坑挑出来。</b></h2>

<p align="center">
  <b><i><font size="5">直接对 Claude Code 说：「审稿，重点看实验和 claim 是否站得住。」</font></i></b>
</p>

<p align="center">
  📄 <b>论文已上 arXiv，欢迎阅读和引用。</b> <a href="https://arxiv.org/abs/2606.16322"><i>PaperJury: Due-Process Review for Bounded LaTeX Revision</i></a>
</p>

<p align="center">
  <a href="https://u7079256.github.io/paperjury/overview.html?lang=zh">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="docs/overview-card-dark.png">
      <source media="(prefers-color-scheme: light)" srcset="docs/overview-card-light.png">
      <img src="docs/overview-card.png" alt="PaperJury 交互式总览" width="100%">
    </picture>
  </a>
</p>

<p align="center">
  <a href="https://arxiv.org/abs/2606.16322"><img alt="arXiv" src="https://img.shields.io/badge/arXiv-2606.16322-b31b1b?logo=arxiv&logoColor=white"></a>
  <a href="https://u7079256.github.io/paperjury/overview.html?lang=zh"><img alt="Interactive overview" src="https://img.shields.io/badge/Interactive_Overview-online-d6a14b?logo=githubpages&logoColor=white"></a>
  <a href="samples/dogfood/"><img alt="Dogfood sample" src="https://img.shields.io/badge/Sample-Dogfood-2f7d55"></a>
  <a href="https://github.com/u7079256/paperjury/releases"><img alt="Releases" src="https://img.shields.io/badge/Releases-stable-3b3d47"></a>
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
  <a href="https://github.com/u7079256/paperjury"><img alt="GitHub" src="https://img.shields.io/badge/GitHub-paperjury-181717?logo=github"></a>
</p>

<p align="center">
  <b>中文</b> · <a href="README.en.md">English</a>
</p>

<p align="center">
  <a href="https://u7079256.github.io/paperjury/overview.html?lang=zh">🧭 交互式总览</a> ·
  <a href="docs/showcase/SHOWCASE.md">🏆 Dogfood showcase</a> ·
  <a href="docs/AGENT-GUIDE.md">🧑‍✈️ Agent Guide</a> ·
  <a href="CITATION.bib">📌 BibTeX</a> ·
  <a href="https://github.com/u7079256/paperjury-codex">💻 Codex 版</a>
</p>

---

<table>
<tr>
<td width="18%">
<a href="docs/showcase/SHOWCASE.md"><img src="docs/paperjury-mark.png" width="120" alt="PaperJury dogfood showcase"></a>
</td>
<td valign="middle">
<b>🏆 真实 Dogfood 样例</b><br><br>
一篇真实草稿的完整多轮评审：仓库里放了<b>修改前后 PDF</b>，以及<b>人工核对过的运行报告</b>。先看样例，再决定要不要把自己的论文交给它挑刺。<br><br>
<a href="docs/showcase/SHOWCASE.md"><img src="https://img.shields.io/badge/查看完整样例_→-Before_After_Report-d73a49?style=for-the-badge" alt="查看完整样例"></a>
</td>
</tr>
</table>

---

> [!IMPORTANT]
> PaperJury 是投稿前的自查工具，**不能替代作者的科学判断，也不能替代 peer review**。它不能用来编造实验、伪造结果、添加没有证据支撑的 claim，或掩盖论文局限。遇到需要新实验、缺证据、需要作者私有知识或研究判断的问题，它都会交回作者处理。

---

## 🔥 News

- 🎉 **RedNote（小红书）里程碑：** 相关分享已经达到 **3 万浏览**、**1.8k 收藏**。感谢大家转发和收藏，也感谢大家把 PaperJury 推荐给更多正在赶论文、改论文的朋友。
- 📄 **2026-06-15：PaperJury 论文已上 arXiv。** arXiv 页面：[*PaperJury: Due-Process Review for Bounded LaTeX Revision*](https://arxiv.org/abs/2606.16322)（arXiv:2606.16322）。论文系统介绍了「审稿 → 裁定 → 修改 → 复查」这套引擎：哪些事交给确定性脚本，哪些判断交给语义 agent；有争议的问题如何进入审议；不同风险的编辑该上什么护栏。
- 🔔 **2026-06-10：v1.0.0 发布。** 这是第一个稳定版，和 Codex 版 v1.0 对齐。新增软更新提醒：发现新的稳定 tag 时只提示，不打断当前工作。
- 🚀 **2026-06-05：PaperJury 的 Codex 版已经推送。** 入口在这里：[paperjury-codex](https://github.com/u7079256/paperjury-codex)。
- 🧪 **Dogfood sample 已加入。** 仓库里放了一个紧凑的 [dogfood sample](samples/dogfood/)：修改前后 PDF，以及人工核对过的运行报告。

## 📌 引用论文

如果 PaperJury 对你的研究或写作流程有帮助，可以引用这篇 arXiv 论文：

```bibtex
@misc{wang2026paperjurydueprocessreviewbounded,
  title={PaperJury: Due-Process Review for Bounded LaTeX Revision},
  author={Yiran Wang and Ruixuan An and Biao Wu and Wenhao Wang},
  year={2026},
  eprint={2606.16322},
  archivePrefix={arXiv},
  primaryClass={cs.CL},
  url={https://arxiv.org/abs/2606.16322},
}
```

同一条目也放在 [`CITATION.bib`](CITATION.bib)。

---

## ⚡ 快速上手

在 Claude Code 里安装：

```text
/plugin marketplace add u7079256/paperjury
/plugin install paperjury@u7079256
```

然后在你的论文项目里直接说需求：

```text
审稿，重点看实验和 claim 是否站得住。
```

也可以更日常一点：

```text
把 introduction 这段改紧一些，但不要改变 claim。
```

不需要背命令。PaperJury 会根据你的描述选择 direct-edit、review 或 auto 模式；真正落稿前，会先把补丁交给你确认。

---

## 🤔 这是什么？

**PaperJury 以 Claude Code skill 的形式提供**，把投稿前自查组织成一套闭环：**审稿 → 裁定 → 修改 → 复查**。它不会照单全收 AI 反馈，而是先把每条意见分成三类：

| 结果 | 含义 |
|---|---|
| **✅ 安全修复** | 表达不清、claim 过强、结构不顺这类文本问题；不需要补实验，也不会把原意改偏。 |
| **🧑‍💻 作者处理** | 缺实验、缺 ablation、缺数据或证据，必须由作者自己判断。 |
| **🛑 不成立** | AI reviewer 误读了论文，或者提了不该改的问题。 |

## 🎯 适合谁

| 你现在的情况 | 可以直接这样用 |
|---|---|
| **📝 刚写完初稿** | 让它像 reviewer 一样通读全文，先找最可能影响投稿的问题。 |
| **🔍 投稿前最后自查** | 让它检查 claim 是否说过头、实验是否撑得住，以及有没有明显格式风险。 |
| **✍️ 只想改一段话** | 直接说「把这段改紧一点，但不要改变 claim」，它会先起草补丁，等你确认后再改。 |
| **🔁 想多轮打磨但不想一直盯着** | 明确授权 auto 模式；安全修改可以落稿，高风险问题仍会交回作者决定。 |

## 📦 你会得到什么

| 输出 | 内容 |
|---|---|
| **📋 问题清单** | 每条 reviewer-style 问题都会带证据、位置、判断结果和当前状态；不会把一堆意见直接倒进正文。 |
| **🧩 可审阅补丁** | 只有安全修复会进入最小补丁；高风险改动会先放着，等作者决定。 |
| **🛠️ 复查报告** | 有 LaTeX 工具链就真实编译；没有就明说哪些检查做不了，不会假装验证过。 |
| **🧪 