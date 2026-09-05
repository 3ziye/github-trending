# ASu-skills

<div align="center">
  <img src="assets/asu-avatar-circle.png" width="180" height="180" alt="ASu-skills 图标">
  <h3>中文求职工作流插件</h3>
  <p>用八个独立入口完成开源贡献、证据复盘、项目导学面经、简历提升、简历制作、简历投递填写、面试准备和校招进度管理。</p>
</div>

<div align="left">
  <a href="README_en.md">English</a> | <a href="README.md">中文</a> | <a href="https://hisn00w.github.io/ASu-skills/">官网</a>
</div>

<br>

<div align="center">
  <a href="LICENSE"><img src="https://img.shields.io/github/license/Hisn00w/ASu-skills?logo=github" alt="License: MIT"></a>
  <a href="https://deepwiki.com/Hisn00w/ASu-skills"><img src="https://deepwiki.com/badge.svg" alt="Ask DeepWiki"></a>
  <a href="https://www.dsh.so/artifact/asu-skills"><img src="https://www.dsh.so/badge/asu-skills.svg" alt="dsh.so security"></a>
  <a href="https://www.dsh.so/artifact/asu-skills"><img src="https://www.dsh.so/badge/install/asu-skills.svg" alt="dsh.so install"></a>
  <br>
  <a href="https://trendshift.io/repositories/139058?utm_source=trendshift-badge&utm_medium=badge&utm_campaign=badge-trendshift-139058" target="_blank" rel="noopener noreferrer"><img src="https://trendshift.io/api/badge/trendshift/repositories/139058/daily" alt="Hisn00w%2FASu-skills | Trendshift" width="250" height="55"></a>
</div>

<p align="center">
  <img src="assets/asu-skills-overview-landscape-v2.png" alt="ASu-skills 八个技能总览" width="1100">
</p>

## 目录

- [安装](#安装)
- [第一次使用：从哪个入口开始](#第一次使用从哪个入口开始)
- [八个 Skill](#八个入口如何配合)
  - [`/contributor`：做真实的开源贡献](#contributor做真实的开源贡献)
  - [`/project-guide`：项目导学面经](#project-guide项目导学面经)
  - [`/great-resume`：简历提升](#great-resume简历提升)
  - [`/make-resume`：制作简历](#make-resume制作简历)
  - [`/evidence-recap`：把 AI 编程对话还原成证据链](#evidence-recap把-ai-编程对话还原成证据链)
  - [`/interview`：把简历问穿](#interview把简历问穿)
  - [`/offer`：校招进度管理](#offer校招进度管理)
  - [`/job-apply`：简历投递填写](#job-apply简历投递填写)
- [八个入口如何配合](#八个入口如何配合)
- [事实边界](#事实边界)
- [文件结构](#文件结构)
- [参与贡献](#参与贡献)
- [致谢](#致谢)
- [Contributors](#contributors)
- [开源协议](#开源协议)
- [Star History](#star-history)

ASu-skills 现在是一个插件包。安装后会提供八个可单独调用的入口：

| 入口               | 用途         | 主要交付                                                          |
| ------------------ | ------------ | ----------------------------------------------------------------- |
| `/contributor`   | 开源贡献     | 寻找候选、展示 diff，经确认后提交 PR并把贡献交给`/great-resume` |
| `/evidence-recap` | 证据复盘     | 把 AI 编程对话和交付记录整理为可核验的九段证据链                  |
| `/project-guide` | 项目导学面经 | 基于项目仓库生成`导学-{简称}.md`、`面经-{简称}.md` 和交接摘要 |
| `/great-resume`  | 简历提升     | 岗位定位、项目改写、成果证据、HR 开场白                           |
| `/make-resume`   | 简历制作     | 默认使用 ASu 模板，也可指定模板；可编辑 HTML 简历和 PDF 导出       |
| `/job-apply`     | 简历投递填写 | 连接浏览器自动填写求职申请，核对后停在提交前                      |
| `/interview`     | 面试准备     | 面试预测、契约化追问、证据复盘和弱项复练                          |
| `/offer`         | 校招进度     | 投递、测评、面试、Offer、拒信和招聘邮件跟踪                       |

## 安装

ASu-skills 同时支持 Codex、Claude Code 和 TraeWork：仓库根目录的 `.codex-plugin/` 供 Codex 使用，`.claude-plugin/` 供 Claude Code 使用，`.trae-plugin/` 供 TraeWork 使用，三者共用同一套 `skills/`、`assets/` 和 `references/`。

### Codex

最简单的方式是把 GitHub 链接直接发给 Codex，并说明要安装插件

```text
请从这个 GitHub 仓库安装 ASu-skills 插件，并启用其中的 contributor、evidence-recap、project-guide、great-resume、make-resume、job-apply、interview、offer 八个 skills：
https://github.com/Hisn00w/ASu-skills
```

安装完成后建议新建一个 Codex 对话，让新 skills 被重新加载。然后在输入框中输入 `/`，从命令列表选择 `contributor`、`evidence-recap`、`project-guide`、`great-resume`、`make-resume`、`job-apply`、`interview` 或 `offer`。

如果当前 Codex 版本没有把 skill 显示在 `/` 菜单中，也可以使用官方的显式 skill 调用方式：

```text
$contributor 根据我的目标岗位寻找开源贡献候选，先展示 diff；我确认后再提 PR，并在合并后交给 /great-resume 提升。
$evidence-recap 把这段 AI 编程对话复盘为可核验的项目证据链，区分个人动作、交付阶段和效果证据。
$great-resume 请把我的实习经历提升成适合 AI 应用工程师岗位的版本。
$project-guide 基于当前项目生成导学和面经，并整理可交接给 /great-resume 与 /interview 的证据摘要。
$make-resume 根据我的经历制作一份可编辑的中文 HTML 简历；默认使用 ASu 模板，如需其他模板我会指定。
$job-apply 使用我确认的简历资料填写当前招聘网站申请表，连接浏览器并在最终提交前让我核对。
$interview 根据我的简历预测面试问题，并通过连续追问检查我是否真的掌握这些经历。
$offer 把这些招聘邮件整理成校招投递进度表。
```

### Claude Code

在 Claude Code 会话中执行：

```text
/plugin marketplace add Hisn00w/ASu-skills
/plugin install asu-skills@asu
```

也可以在终端里执行等价命令：

```bash
claude plugin marketplace add Hisn00w/ASu-skills
claude plugin install asu-skills@asu
```

安装摘要提示 `Run /reload-plugins to activate.` 时执行 `/reload-plugins`，否则重启 Claude Code。安装后可用 `claude plugin details asu-skills` 确认八个 skill 都已加载。

更新与卸载：

```text
/plugin marketplace update asu
/plugin uninstall asu-skills
```

插件方式的卸载只删除插件缓存，不会动你在项目或用户目录里编辑过的求职进度表。

### TraeWork

TraeWork 通过 `.trae-plugin/plugin.json` 清单把仓库打包成插件，八个 skill 会以 `<publisher>:asu-skills:<skill>` 的形式挂在该插件下。

1. 把本仓库整体复制到 TraeWork 插件目录：`~/.trae-cn/plugins/<publisher>/asu-skills/<version>/`，保留 `.trae-plugin/plugin.json`、`skills/`、`assets/` 和 `references/`；
2. 重启 TraeWork，让新插件被重新加载；
3. 新建对话，在输入框输入 `/`，从命令列表选择 `contributor`、`evidence-recap`、`project-guide`、`great-resume`、`make-resume`、`job-apply`、`interview` 或 `offer`。

其中 `<publisher>` 是插件目录下的命名空间，可自行指定（如 `local`），`<version>` 为 `plugin.json` 中的版本号。卸载时删除