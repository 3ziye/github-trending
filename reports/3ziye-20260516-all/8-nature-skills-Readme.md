# nature-skills
大家好，我是上海交通大学博士生袁一哲，目前主要从事医疗 AI 相关的研究与创业实践。欢迎大家持续关注 nature-skill。如果你有任何需求，欢迎提交 issue；如果我们认为该需求有意义且可行，也会尽量推进实现。我们同样欢迎 PR，但请务必按照 README 后面说明的格式提交，以便我们更高效地审核与合并。

Hello everyone, I’m Yuan Yizhe, a PhD student at Shanghai Jiao Tong University. I’m currently working on research and entrepreneurial projects in medical AI. Thank you for your continued interest in nature-skill. If you have any requests, feel free to open an issue. If we find the request meaningful and feasible, we’ll do our best to implement it. We also welcome PRs, but please make sure to follow the submission format described later in the README so that we can review and merge them more efficiently.

## 📢 课题组诚招“医学 + AI”实习生

<table border="0" cellpadding="10" cellspacing="0">
  <tr>
    <td width="34%" valign="top" align="center" style="border: none; background-color: #f9f9f9; padding: 20px; border-radius: 8px;">
      <span style="font-size: 14px; color: #666;">微信群聊</span><br>
      <img src="https://github.com/user-attachments/assets/7a5daff1-2e82-42fd-87ab-1165f46242d9" width="100%" style="max-width:160px; margin-top:15px; border: 1px solid #eee;">
      <div style="margin-top:10px; font-size: 13px; color: #666;">答疑交流群！进群记得12小时内备注</div>
    </td>
    <td width="66%" valign="top" style="border: none; line-height: 1.6;">
      还在寻找能够落地的 <strong>AI 前沿交叉赛道</strong>吗？我们课题组现向对“医学 + AI”充满热情的你发出邀请！<br><br>
      这里有充足的计算资源，以及深耕医疗大模型（LLM）、视觉预训练、Prompt Engineering 及自动化医疗 AI Agent 的科研团队。我们更看重你的<strong>自驱力、学习能力与科研产出追求</strong>。<br><br>
      项目信息文档链接：https://iigqjt2m4ia.feishu.cn/wiki/VIvDwHu18iTc6mk411xco8chnJb   密码：664#N926<br>
      如果你有相关代码基础或项目经验，渴望在顶级交叉学科中积累成果，请将简历发送至：<br>
      📧 <strong><a href="mailto:sjtu520aimedws@163.com" style="text-decoration: none; color: #0056b3;">sjtu520aimedws@163.com</a></strong><br>
      <small>（标题格式：姓名-专业-医学AI科研申请）</small><br><br>
      期待与你在 AI 赋能医疗的征途中，做出最扎实的科研工作！
    </td>
  </tr>
</table>

---

## Installation

`nature-skills` is a repository of reusable instruction bundles centred on `SKILL.md`.
Each `skills/nature-*` directory is one installable unit. Copy the whole folder, not
only `SKILL.md`, because many skills depend on `references/`, assets, scripts, or
README context.

### 1. Codex

Codex can use these folders directly as local skills. This is the simplest installation path.

**Clone the repo**

```bash
git clone https://github.com/Yuan1z0825/nature-skills.git
cd nature-skills
```

**Install one skill**

```bash
mkdir -p ~/.codex/skills
cp -R skills/nature-reader ~/.codex/skills/
```

**Install all current skills**

```bash
mkdir -p ~/.codex/skills
for d in skills/nature-*; do
  cp -R "$d" ~/.codex/skills/
done
```

**Update after pulling new changes**

```bash
git pull
for d in skills/nature-*; do
  cp -R "$d" ~/.codex/skills/
done
```

**Finish**

- Restart Codex so newly added skills are picked up.
- Then ask naturally, for example: `Translate this paper into a full markdown reader.` or
  `Make this paper into a Chinese journal-club PPT.`

If you prefer not to use the terminal, copying the `skills/nature-*` folder(s) into
`~/.codex/skills/` manually works as well. For a longer walkthrough, see
[`install.md`](install.md).

### 2. Claude Code

**Primary method: Plugin marketplace installation**

This repository is published as a Claude Code plugin, making installation simple.

```bash
# Add the marketplace (one-time)
/plugin marketplace add https://github.com/Yuan1z0825/nature-skills

# Install the plugin
/plugin install nature-skills

# Reload to apply
/reload-plugins
```

All nine skills are available automatically after reload. No manual wrapper setup needed.

**Alternative: subagent wrapper**

If you prefer manual control over individual skills, create a user-level subagent:

```bash
mkdir -p ~/.claude/agents
cp skills/nature-reader/SKILL.md ~/.claude/agents/nature-reader.md
```

Then open `~/.claude/agents/nature-reader.md` and make sure the frontmatter is valid
for Claude Code subagents:

```yaml
---
name: nature-reader
description: Full-paper bilingual, figure-aware, source-grounded Markdown reader for journal or conference papers. Use proactively when the user asks to translate an entire paper or generate a complete markdown reader.
---
```

After that, start a new Claude Code session or open `/agents`, and invoke it naturally or explicitly:

```text
Use the nature-reader subagent to turn this PDF into a full markdown reader.
```

If you prefer commands instead of subagents, create a project or user command under
`.claude/commands/` or `~/.claude/commands/` and paste or adapt the corresponding
`SKILL.md` content there.

Official Claude Code docs:

- [Subagents](https://docs.anthropic.com/en/docs/claude-code/sub-agents)
- [Slash commands](https://docs.anthropic.com/en/docs/claude-code/slash-commands)

### 3. Other agents or manual use

If your agent supports reusable prompt files, system prompts, or agent profiles, the minimum
portable unit is the skill directory itself:

```text
ski