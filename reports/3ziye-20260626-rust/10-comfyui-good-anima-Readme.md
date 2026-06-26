# ComfyUI Good Anima 🎨

> 一套面向 AI 编程助手的 ComfyUI + Anima 二次元生图技能包。当前主线是 v2mini：去掉多层代理式路由，只保留 Anima 生图所需的核心约束、Danbooru tag 精确校验和 ComfyUI 执行链路，让 AI 和人类把更多注意力留给画面本身。
>
> v2mini 的新核心是“情境因果 → 三层 prompt → 精确执行”：先让模型根据角色、画师、场景和用户意图形成有故事感的画面瞬间，再拆成 `hard_tags`、`soft_phrases`、`nltags_block`，由 `danbooru-tags` 只确认真正的 Danbooru 硬锚点，最后交给 ComfyUI workflow 执行。
>
> 🌐 **[English Version](./README_EN.md)**

![Anima Base v1.0 预览图](./samples/anima_base_v1_0-rella-sea-margatroid_marisa_00001_.png)

---

## 主线设计目标

- **返璞归真**：v2mini 不再依赖 master / composition-director / random-gen 多层链路，默认从 `comfyui-animatool` 进入生图。
- **把创作权还给模型和用户**：skill 不替代审美、构图常识和角色理解；只保留 Anima 工作流中容易丢失或容易出错的硬边界。
- **情境因果优先**：先确定事件起因、角色反应、环境参与和可见后果，再补齐画面八维信息。
- **三层 prompt 组装**：`hard_tags` 放确认过的硬锚点，`soft_phrases` 放模型审美短语，`nltags_block` 放空间、动作归属、光影、景深和因果后果。
- **不可丢事实**：Anima prompt 顺序、三层分离、双 LoRA 质量前缀、负向动态组装、workflow args、seed 行为、`submit` 非阻塞和 PowerShell JSON 编码。
- **硬锚点精确校验**：角色、作品、画师、服装、道具等 hard anchors 由 `danbooru-tags` 先做 exact / prefix 验证；模糊结果只作候选，不冒充 confirmed tag。
- **执行层纯粹**：`comfyui-manager` 只执行准备好的 workflow 和 args，不写 prompt、不选画师、不决定构图。
- **按需参考**：失败模式、画师风格研究等内容留在 references，只有遇到对应问题才读取。

---

## 兼容的 AI 编程助手

本项目的 Skills 为 **AI 编程代理（AI Coding Agent）** 设计，任何能执行 Shell 命令的 AI 助手均可使用：

| 助手                 | 支持状态    | 说明                                              |
| -------------------- | ----------- | ------------------------------------------------- |
| **🟢 Snow**          | ✅ 完美支持 | **国内首选推荐** — 原生支持 Skills 系统，即开即用 |
| **🟢 Claude Code**   | ✅ 完美支持 | Anthropic 官方 CLI，支持 Shell 命令执行           |
| **🟢 Codex**         | ✅ 完美支持 | 全功能 AI 编程代理，完全兼容                      |
| **🟢 PI**            | ✅ 完美支持 | 轻量级 AI 编程代理，支持 Skills 系统              |
| **🟢 OpenClaw**      | ✅ 支持     | 支持 ComfyUI_Skill_CLI 集成的 Agents              |
| **🟡 其他 AI Agent** | ✅ 完美支持 | 只要能执行 PowerShell/Shell 命令即可              |

> 💡 **推荐使用 [Snow](https://snowcli.com/docs) — 目前国内体验最好的 AI 编程代理**。

---

## 架构设计

v2mini 采用三段式链路：

| 层级          | 组件                | 角色                                                 | 加载时机             |
| ------------- | ------------------- | ---------------------------------------------------- | -------------------- |
| **L1 — 入口** | `comfyui-animatool` | 情境因果、八维补全、三层 prompt、冲突检查、args 输出 | Anima 生图触发时     |
| **L2 — 校验** | `danbooru-tags`     | exact / prefix 校验、批量验证、必要候选              | 需要 hard anchors 时 |
| **L3 — 执行** | `comfyui-manager`   | validate / submit / run / 排障 / 缓存输出            | args 准备完成后      |

这条链路不做多代理分工，不创建 route contract，不把用户需求拆成过度流程。模型先理解画面和故事因果，skill 只兜住 Anima、Danbooru 和 ComfyUI 的硬规则。

---

## 技能包结构

```
comfyui-good-anima/
├── README.md
├── README_EN.md
├── comfyui-animatool/
│   ├── SKILL.md                # Anima 生图唯一入口：情境因果、三层 prompt、args
│   └── references/
│       └── anima-reference.md  # 画师风格研究 + 出图失败/畸形/归属混乱排障（按需读取）
├── danbooru-tags/
│   ├── SKILL.md                # Danbooru tag 检索与校验
│   ├── bin/danbooru-tags.exe   # Rust CLI（预编译）
│   ├── anima-1.0.csv           # Anima 标签主索引
│   ├── Anima-preview.csv       # 预览版 tag 数据
│   ├── Anima-preview-alternate.csv
│   ├── tags_index.json         # JSON 索引
│   ├── tags_index.sqlite       # SQLite 高速索引
│   ├── *.py                    # 索引构建脚本
│   └── rust-cli/               # danbooru-tags Rust 源码
├── comfyui-manager/
│   ├── SKILL.md                # ComfyUI 执行与运维
│   ├── workspace/              # workflow JSON + 执行脚本
│   │   ├── config.json
│   │   ├── run_workflow_args.js
│   │   ├── cache_anima_outputs.js
│   │   └── data/               # 工作流定义 + local/ 导入映射
├── samples/                    # 示例图
├── legacy/v1/                  # V1 归档版本，仅历史参考，保留在 git
├── legacy/V3/                  # V3 本地封存版本，不纳入 git
└── LICENSE
```

### 版本归档规则

- 当前主线只维护 v2mini：`comfyui-animatool`、`danbooru-tags`、`comfyui-manager`。
- `legacy/v1/` 作为早期硬约束链路归档，可用于对照规则退化，不作为运行入口。
- `legacy/V3/` 作为本地封存版本保留，不提交到 git，不作为安装路径或技能根目录。
- 新规则优先进入三大核心 skill；失败排查和画师研究只放入 `comfyui-animatool/references/`。

---

## 🔍 danbooru-tags 是什么？

**danbooru-tags** 是本项目中最关键的检索基础设施。它是一个 Rust 编写的命令行工具，负责对 **Anima 官方标签索引（anima-1.0.csv）** 进行高速检索和锚点校验。

### 它解决的核心问题

Anima 模型是在 Danbooru 标签系统上训练的，想要精确控制生成内容，就必须使用 **Danbooru 体系内的有效标签**。但 Danbooru 有数百万个标签，人工记忆和拼写几乎不可能。danbooru-tags 解决了以下痛点：

| 痛点           | 没有 danbooru-tags 会怎样                                                                | 有 danbooru-tags 后                                                  |
| -------------- | ---------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **画师校验**   | 用户说"用 rella 画风"，AI 不知道 `@rella` 是不是有效 tag，可能写出无效画师名导致模型忽略 | `--group artist --prefix "@rella"` 直接返回 confirmed 画师           |
| **角色确认**   | "立华奏"在 Danbooru 里叫 `kanade tachibana`，AI 可能猜错或漏掉                           | 批量查询 `--group character --keyword "kanade tachibana"` 精准命中   |
| **标签准确性** | 随便写的 `巫女服` 不是有效 Danbooru tag，模型不理解                                      | 拆解为 `miko`, `hakama`, `wide sleeves` 等多角