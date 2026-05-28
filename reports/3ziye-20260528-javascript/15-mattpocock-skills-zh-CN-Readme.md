# Matt Pocock Agent Skills 中文版

## 为什么需要这个中文版？

- 更好适配中文大语言模型
- 方便中文母语开发者
- 方便接入中文开发流程

## 关于这个中文版

这是 [`mattpocock/skills`](https://github.com/mattpocock/skills) 的简体中文本地化版本。文档和技能说明已翻译；目录名、技能名、命令、代码块、路径和工具标识保持不变，以免破坏安装和运行行为。

中文版本不只是为了阅读方便。对中文母语用户来说，中文说明能减少概念转换成本；对以中文为主要交互语言或中文语料优化的模型来说，中文 prompt 和 skill instructions 也更容易贴合中文上下文，减少中英混杂带来的歧义。

本仓库按内容刷新方式同步上游，不同步上游 Git 历史或仓库管理状态。维护规则见 [`.skills/translate-skill/SKILL.md`](./.skills/translate-skill/SKILL.md)。

本仓库的最近一次同步翻译由 OpenAI Codex（GPT-5 coding agent）执行，并由仓库维护者通过提交记录纳入 `main`。翻译策略是 **skill-guided content localization**：把上游 `mattpocock/skills` 当作英文内容来源，只翻译自然语言说明，保留目录名、skill name、frontmatter key、命令、代码块、路径、URL、package/tool/API identifiers 和行为关键 labels。用户可见的安装路径统一保持为 `vinvcn/mattpocock-skills-zh-CN`。

## 发布记录与验证

### 发布记录

- 2026-05-22：同步上游 `mattpocock/skills@b8be62f`，本地提交 `f0b4bd3`。新增 architecture HTML report 指南，更新 handoff 临时文件与 redaction 规则，并收紧 `CONTEXT.md` template。
- 2026-05-15：同步上游 `mattpocock/skills@e74f006`，本地提交 `c323a74`。收紧 `CONTEXT.md` glossary 边界，并更新 `prototype` 的设计细化表述。
- 2026-05-11：同步上游 `mattpocock/skills@9f2e0bd`，本地提交 `210cbac`。将 `handoff` 提升到 productivity，新增 `review` 草稿，并更新 writing skills。
- 2026-05-09：同步上游 `mattpocock/skills@733d312`，本地提交 `c9fe120`。新增 `prototype` 与 `in-progress` 内容的中文翻译，并更新公开 skill 索引。

### 最新 main 验证

针对 `mattpocock/skills@b8be62f` 的同步结果：

- [x] `node scripts/check-translation.mjs` 通过。
- [x] 公开 skill 索引一致：`engineering/`、`productivity/`、`misc/` 已同步到顶层 README 和 `.claude-plugin/plugin.json`，`personal/`、`in-progress/`、`deprecated/` 未进入 plugin。
- [x] 上游 in-scope 文件完整：没有缺失上游文件，也没有 stale translated upstream files。
- [x] 61 个共同 Markdown 文件的保护性检查通过：frontmatter `name` 未漂移，frontmatter key 未缺失，fenced code blocks 平衡。
- [x] `git diff --check` 和 `git diff --cached --check` 通过。
- [x] README 同步记录指向最新上游 `b8be62f`，并记录本地同步提交 `f0b4bd3`。
- [x] 行为关键扫描未发现旧安装路径或旧 skill 路径，例如旧的 `vinvcn` 短仓库路径、已移除的 triage skill 名、已移除的 domain-model 相对路径等。
- [!] `node scripts/audit-english.mjs` 仍会列出大量英文内容；这些主要是保留的 identifiers、命令、示例、触发词和工程术语，作为人工复核队列，不作为阻塞项。

## 30 秒安装

```bash
npx skills@latest add vinvcn/mattpocock-skills-zh-CN
```

选择你想安装的 skills，以及要安装到哪些 coding agents。首次安装时请确保选择 [`/setup-matt-pocock-skills`](./skills/engineering/setup-matt-pocock-skills/SKILL.md)，然后在 agent 中运行它来完成 issue tracker、labels 和 docs 目录配置。

[![skills.sh](https://skills.sh/b/vinvcn/mattpocock-skills-zh-CN)](https://skills.sh/vinvcn/mattpocock-skills-zh-CN)

<p>
  <a href="https://www.aihero.dev/s/skills-newsletter">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://res.cloudinary.com/total-typescript/image/upload/v1777382277/skills-repo-dark_2x.png">
      <source media="(prefers-color-scheme: light)" srcset="https://res.cloudinary.com/total-typescript/image/upload/v1777382277/skill-repo-light_2x.png">
      <img alt="Skills" src="https://res.cloudinary.com/total-typescript/image/upload/v1777382277/skill-repo-light_2x.png" width="369">
    </picture>
  </a>
</p>

## 原版 README 翻译

我每天用于真实工程工作的 agent skills，不是 vibe coding。

开发真实应用很难。GSD、BMAD、Spec-Kit 这类方法试图通过接管流程来帮你。但它们在接管流程的同时，也拿走了你的控制权，并让流程里的 bug 更难解决。

这些 skills 被设计得小、易改、可组合。它们适用于任何模型，背后是数十年的工程经验。你可以 hack 它们，让它们变成自己的东西。

如果你想跟进这些 skills 的更新，以及我后续创建的新 skill，可以加入大约 60,000 名开发者订阅的 newsletter：

[订阅 Newsletter](https://www.aihero.dev/s/skills-newsletter)

### Quickstart（30 秒 setup）

1. 运行 skills.sh installer：

```bash
npx skills@latest add vinvcn/mattpocock-skills-zh-CN
```

2. 选择你想安装的 skills，以及要安装到哪些 coding agents。**确保选择 `/setup-matt-pocock-skills`**。

3. 在你的 agent 中运行 `/setup-matt-pocock-skills`。它会：
   - 询问你要使用哪个 issue tracker（GitHub、Linear 或 local files）
   - 询问你 triage issues 时使用哪些 labels（`/triage` 会使用这些 labels）
   - 询问要把创建的 docs 保存到哪里

4. 完成后即可开始使用。

### 为什么这些 Skills 存在

我创建这些 skills，是为了解决我在 Claude Code、Codex 和其他 coding agents 中反复看到的常见失败模式。

#### #1: Agent 没有做我想要的东西

> "No-one knows exactly what they want"
>
> David Thomas & Andrew Hunt, [The Pragmatic Programmer](https://www.amazon.co.uk/Pragmatic-Programmer-Anniversary-Journey-Mastery/dp/B0833F1T3V)

**问题**：软件开发中最常见的失败模式是 misalignment。你以为开发者理解了你想要什么；等看到做出来的东西，才发现对方完全没理解。

AI 时代也是一样。你和 agent 之间存在沟通缺口。修复方式是一次 **grilling session**，让 agent 针对你要构建的东西提出详细问题。

**解决方式**是使用：

- [`/grill-me`](./skills/productivity/grill-me/SKILL.md) — 用于非代码场景
- [`/grill-with-docs`](./skills/engineering/grill-with-docs/SKILL.md) — 与 [`/grill-me`](./skills/productivity/grill-me/SKILL.md) 类似，但会加入更多文档能力（见下文）

这些是我最常用的 skills。它们帮助你在开始前和 agent 对齐，并深入思考你要做的变更。每次想做变更时都值得使用。

#### #2: Agent 太啰嗦

> With a ubiquitous language, conversations among developers and expressions of the code are all derived from the same domain model.
>
> Eric Evans, [Domain-Driven-Design](https://www.amazon.co.uk/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

**问题**：项目开始时，开发者和真正使用软件的人（domain experts）通常说着不同语言。

我在 agents 身上也感受到同样张力。Agents 往往被丢进一个项目，然后被要求边做边弄懂术语。于是它们用 20 个词解释本来 1 个词就够的东西。

**解决方式**是 shared language。它是一份帮助 agents 解码项目术语的文档。

<details>
<summary>
示例
</summary>

这是我 `course-video-manager` repo