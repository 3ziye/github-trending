# story-to-handdrawn-video

[中文](#中文) | [English](#english)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 中文

把中文故事文案或一组有序的手绘图片,转换成 3:4 竖屏**手绘故事动画**。内置 20 种可切换风格,包含彩铅日记、儿童蜡笔、极简线条、水墨、水彩、水粉绘本、Zine 拼贴、白板讲解与木刻社论等视觉家族;未指定时继续使用已确认并锁定的「彩铅日记漫画」默认风格。支持手写体字幕、从左到右的「文字 → 黑白画稿 → 彩色插画」揭示、可选右下角卷页翻书转场和安全不裁剪构图。基于 [Remotion](https://www.remotion.dev/),默认输出无配音、无音乐的 H.264 画面轨,方便后期配音。

本仓库包含两部分:

- **渲染器项目**(根目录):Remotion 工程,负责实际的分镜、动效和渲染。
- **Codex / Agent Skill**(`skill-package/`):可分发的 Skill,装进 Codex 等 Agent 后用自然语言驱动渲染器,无需手动跑脚本。

### 功能特性

- 中文故事自动分句和动态分镜,保留原文措辞
- 上传漫画页或完整图片,保持原顺序和构图
- 自动拆分上方文字区与下方插画区
- 本地生成与彩色插画对齐的黑白层
- `文字 → 黑白画稿 → 彩色插画` 从左到右揭示
- 可选右下角卷页翻书转场(纸背保留淡化的原页纹理)
- 1080×1440 正式渲染和 720×960 快速预览
- Codex Image2 工作流,以及显式选择的 OpenAI API 工作流
- 20 种内置手绘风格,支持编号、英文 id、中文名和别名选择
- 每种风格附带固定示例图,并提供统一场景的风格总览

### 环境要求

- Node.js 20 或更高版本
- Python 3.10 或更高版本
- FFmpeg,且 `ffmpeg`、`ffprobe` 可从终端调用
- npm
- Google Chrome,或由 Remotion 管理的兼容浏览器
- 支持 Skill 的 Agent 运行时(Codex、Claude Code、Kimi Code 等)

### 安装

1. 准备渲染器项目:

```bash
git clone https://github.com/gnipbao/story-to-handdrawn-video.git
cd story-to-handdrawn-video
npm ci
npm run check      # TypeScript 检查 + 分镜结构校验,不访问网络
```

2. 把 Skill 装进 Agent 的 skills 目录:

```bash
# Codex
cp -R skill-package/story-to-handdrawn-video ~/.codex/skills/

# Claude Code / 通用 Agent
cp -R skill-package/story-to-handdrawn-video ~/.claude/skills/

# Kimi Code
cp -R skill-package/story-to-handdrawn-video ~/.agents/skills/
```

3. 告诉 Skill 渲染器项目在哪里(在渲染器项目目录内运行 Agent 时可省略):

```bash
export STORY_VIDEO_PROJECT=/absolute/path/to/story-to-handdrawn-video
```

### 使用方法(Codex Skill 示例)

装好 Skill 后,全部通过自然语言驱动,分句、分镜、图片生成、导入、渲染由 Agent 按 Skill 约定自动完成。

**故事文本 → 手绘动画**(Skill 的默认提示词):

```text
使用 $story-to-handdrawn-video 把这段故事生成可后期配音的手绘动画。

<在这里粘贴故事文本>
```

也可以把故事放在 UTF-8 文本文件里:

```text
使用 $story-to-handdrawn-video 把 /absolute/story.txt 生成手绘动画,标题叫「纸上的夏天」。
```

**上传图片 → 手绘动画**(图片按播放顺序给出):

```text
使用 $story-to-handdrawn-video 把这几张图片按顺序生成手绘动画:
/absolute/01.jpg /absolute/02.jpg /absolute/03.jpg
```

**翻书效果**(保留原始页面,从右下角卷页):

```text
使用 $story-to-handdrawn-video 把这些图片做成翻书效果的手绘动画:
/absolute/01.jpg /absolute/02.jpg
```

**先出预览**(720×960,确认效果后再出正式版):

```text
使用 $story-to-handdrawn-video 先给这个故事生成一个预览版。
```

使用建议:

- 故事文本默认一个完整句子一个节拍;想控制节奏,直接在故事里按句分行即可。
- 遇到时间跳跃、指代不明、医疗场景或年龄敏感角色时,建议先让 Agent 给出视觉规划(两位场景编号为键的 JSON),确认后再生成。
- 默认使用 Codex Image2 生成图片;只有明确要求时才会走 OpenAI API(需 `OPENAI_API_KEY`)。
- 输出是静音画面轨,配音和 BGM 属于后期工作。

### 20 种内置手绘风格

所有示例使用同一组人物、动作和构图生成,便于直接比较画材、线条、色板与完成度。示例图只作为**风格证据**,生成故事时仍由原文和角色锁定控制人物、场景与动作。

![20 种手绘风格总览](references/style-examples/handdrawn-style-library-contact-sheet.jpg)

| # | 示例 | Style id | 中文名 | 视觉特征 | 推荐题材 |
|---:|:---:|---|---|---|---|
| 1 | <a href="references/style-examples/01-colored-pencil-diary.png"><img src="references/style-examples/01-colored-pencil-diary.png" width="120" alt="彩铅日记漫画示例"></a> | `colored-pencil-diary` | 彩铅日记漫画（默认） | 笨拙黑色毡尖笔轮廓、低饱和彩铅乱涂、大留白 | 家庭、生活、纪实情感 |
| 2 | <a href="references/style-examples/02-minimal-line-explainer.png"><img src="references/style-examples/02-minimal-line-explainer.png" width="120" alt="极简黑白线条讲解示例"></a> | `minimal-line-explainer` | 极简黑白线条讲解 | 米白纸、细黑单线、火柴人与极少道具 | 科普、流程、观点 |
| 3 | <a href="references/style-examples/03-kid-crayon.png"><img src="references/style-examples/03-kid-crayon.png" width="120" alt="五岁儿童蜡笔坏画示例"></a> | `kid-crayon` | 五岁儿童蜡笔坏画 | 歪扭比例、线条不闭合、明亮蜡笔涂出边界 | 童年、亲子、轻喜剧 |
| 4 | <a href="references/style-examples/04-rawkid-crayon.png"><img src="references/style-examples/04-rawkid-crayon.png" width="120" alt="潦草家庭投稿蜡笔示例"></a> | `rawkid-crayon` | 潦草家庭投稿蜡笔 | 家长歪线稿、孩子粗乱上色、大片露白 | 家庭连载、温暖日常 |
| 5 | <a href="references/style-examples/05-bean-doodle-infographic.png"><img src="references/style-examples/05-bean-doodle-infographic.png" width="120" alt="小豆人涂鸦信息图示例"></a> | `bean-doodle-infographic` | 小豆人涂鸦信息图 | 黑色圆豆人、白点眼、单一橙色强调 | 步骤、清单、知识卡 |
| 6 | <a href="references/style-examples/06-ms-paint-bad-doodle.png"><img src="references/style-examples/06-ms-paint-bad-doodle.png" width="120" alt="鼠标烂涂鸦示例"></a> | `ms-paint-bad-doodle` | 鼠标烂涂鸦 | 锯齿鼠标线、荒谬比例、粗糙纯色块 | 吐槽、反转、荒诞 |
| 7 | <a href="references/style-examples/07-ballpoint-scribble.png"><img src="references/style-examples/07-ballpoint-scribble.png" width="120" alt="圆珠笔缠绕线速写示例"></a> | `ballpoint-scribble` | 圆珠笔缠绕线速写 | 单色圆珠笔缠绕线、疏密塑形、现场手稿感 | 肖像、动物、独白 |
| 8 | <a href="references/style-examples/08-real-crayon-paper.png"><img src="references/style-examples/08-real-crayon-paper.png" width="120" alt="真实蜡笔纸实拍示例"></a> | `real-crayon-paper` | 真实蜡笔纸实拍 | 可见纸纹、蜡质结块、压力变化与大量漏白 | 儿童视角、成长记录 |
| 9 | <a href="references/style-examples/09-ink-wash.png"><img src="references/style-examples/09-ink-wash.png" width="120" alt="水墨写意示例"></a> | `ink-wash` | 水墨写意 | 宣纸、浓淡干湿、飞白枯笔与朱红点睛 | 文化、寓言、感悟 |
| 10 | <a href="references/style-examples/10-emotional-watercolor-sketch.png"><img src="references/style-examples/10-emotional-watercolor-sketch.png" width="120" alt="情绪叙事淡彩速写示例"></a> | `emotional-watercolor-sketch` |