<div align="center">

**简体中文** | [English](README.en.md)

<img src="docs/media/hero.gif" alt="huashu-motion发布片开场：一整面墙的片子，说一句，出一支片" width="100%" />

# huashu-motion

> *「一键直出商业级产品宣传片。」*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Standard-green)](https://agentskills.io)
[![Runtime](https://img.shields.io/badge/Runtime-Claude%20Code%20·%20Codex%20·%20WorkBuddy%20·%20Grok%20Bot%20·%20Muse%20·%20Dots-blueviolet)](#安装)

**让你的agent做动画、作曲，指着画面改。**

跟Claude Code、Codex这些agent说一句「给我的产品做个30秒的发布片」，<br>
它会先读你的产品，给你三个方向挑，写出整支片子，自己写谱配乐，<br>
然后在浏览器里打开一个编辑器等你。哪里不满意，在画面上点一下，写下要改什么，它就只改那一处。

```sh
npx skills add alchaincyf/huashu-motion
```

[看效果](#看效果) · [安装](#安装) · [能做什么](#能做什么) · [怎么做到的](#怎么做到的) · [背后的故事](#背后的故事)

</div>

---

## 看效果

这篇README里的每一段动画都是huashu-motion做的。上面那段取自它给自己做的53秒发布片，👉 [下载完整发布片（MP4，带声音）](https://github.com/alchaincyf/huashu-motion/releases/latest)，下面Grok Bot、huashu-design、DeepSeek这几支的完整版也在同一个页面。

### 指着画面改

<img src="docs/media/point-to-edit.gif" alt="在编辑器里按C，点中开场画面，写下「第一帧开场的效果我觉得很差，还不如核心聚焦在typing呢」，agent接单改完，预览停在原处刷新" width="100%" />

按C，在画面上点一下，写下要改什么。评论发过去的时候带着时间点、场景、点中的元素和它在源码里的位置，agent先把那一帧和你点的那一小块截图放大看一眼，再只改那一处，改完回一句人话，预览停在原来的位置刷新。每一版都留着，⌘Z随时撤回；标题、数字、颜色、停留时长这些会变成编辑器右边的输入框，自己改，不用等agent。

（这段里的编辑器和终端是照真实界面重建的，代码细节是示意；评论是真实提过的意见。）

### 先写谱，再拍片

<img src="docs/media/score-first.gif" alt="agent写的ABC乐谱变成五线谱往前走，红色场景标记落在哪一拍，画面就在哪一拍切" width="100%" />

做发布片用的是作曲家模式：agent按节奏单先写一份谱（ABC记谱法，纯文本的乐谱），谱里的标记对齐每个场景，再由三角钢琴、弦乐和鼓组的采样演奏出来（真乐器采样要先跑一次`om samples build`，不跑就用合成音色）；画面上每个东西落地的那一帧，再配一个音效。配乐全部在本机现场生成，不调用任何收费接口。

### 一天，二十支

<img src="docs/media/sixteen-cuts.gif" alt="16个镜头来自七支不同的片子，按拍子快切" width="100%" />

16个镜头，来自同一天做的七支片子，按拍子切。

<img src="docs/media/grok-bot.gif" alt="Grok Bot粉丝片：Sending to Chief…的气泡钉住不动，背后每个agent各占一屏颜色，最后汇成八宫格" width="100%" />

Grok Bot（粉丝自制，非官方）· 30秒：傍晚交代任务，夜里几个agent各干各的，早上7点手机上收到汇报。这段是汇报一张张送往Chief of Staff的那几拍。

<table><tr>
<td width="50%"><img src="docs/media/huashu-design.gif" alt="huashu-design宣传片：一句「给社区旧书店做一份众筹PPT」钉在画面中间，背后的风格按拍子一格一格地换" width="100%" /><br/>huashu-design 3.0 · 一句提示词钉住不动，背后的风格按拍子换</td>
<td width="50%" align="center"><img src="docs/media/catlight-pro.gif" alt="小猫补光灯Pro竖屏片：八种补光色，一拍换一种" width="60%" /><br/>小猫补光灯Pro · 八种补光色，一拍换一种</td>
</tr></table>

### 不依赖Opus：DeepSeek V4.1 Flash也能做

<img src="docs/media/deepseek-flash.gif" alt="DeepSeek V4.1 Flash做的动效片：鲸鱼logo、MOTION、MASK、GLITCH，一个圆点贯穿全片" width="100%" />

这支22秒的动效片，是把Claude Code背后的模型换成DeepSeek V4.1 Flash（1017版）做的。中间我给了三轮意见（比如加上DeepSeek的鲸鱼logo、删掉几个镜头），带配乐和音效，前后不到半小时，按当时的价格花了1块9毛5（缓存命中率99.4%）。统一的配色、贯穿全片的那颗圆点、卡在124BPM上的配乐，是skill带出来的，我一句都没提过。方法写进了skill，便宜的模型也能拍出像样的片子。

---

## 安装

### 方式一：跟你的agent说（推荐）

```
帮我安装huashu-motion这个skill（github.com/alchaincyf/huashu-motion），装好后跑一遍demo
```

### 方式二：一行命令

```sh
npx skills add alchaincyf/huashu-motion
```

[skills](https://github.com/vercel-labs/skills)会认出你在用的agent，把skill放进对应目录；要指定的话加`-a claude-code`、`-a codex`等参数。

Claude Code、Codex、WorkBuddy、Grok Bot、Muse、Dots等产品都能跑；它遵循[Agent Skills](https://agentskills.io)协议，支持skill的agent都能装。

### 方式三：克隆整个仓库

<details>
<summary>展开查看</summary>

```sh
git clone https://github.com/alchaincyf/huashu-motion.git
ln -s "$PWD/huashu-motion/skills/huashu-motion" ~/.claude/skills/huashu-motion   # Codex换成~/.codex/skills/
```

skill里的`bin/om`会直接调用仓库里的命令行工具，改仓库就是改skill，本机只有一份。

</details>

### 需要什么

- Node 22以上。
- Chrome（或Chromium、Edge）：截帧、检查、导出都用你电脑上已经装好的浏览器，不额外下载渲染器。
- FFmpeg：导出视频、合成配乐要用。
- 真乐器音色（可选）：想要三角钢琴、弦乐、鼓组，让agent跑一次`om samples build`，下载约55MB的免费采样（CC0和CC-BY授权）；不跑就用合成音色。
- 口播（可选）：macOS的系统音色不用装；想用Kokoro念中文稿，第一次用时会给出一行安装命令（要uv和Python 3.12，模型约325MB）；逐字对齐要装whisper-cli（`brew install whisper-cpp`）。

缺什么跑`om doctor`就知道，这些都可以直接让agent帮你装。目前只在macOS上实测过。Codex的沙箱会拦本地预览和浏览器，遇到时手动批准一下。

---

## 能做什么

装好以后，直接跟agent说：

| 你说 | 它做 |
|---|---|
| 「用huashu-motion给我的产品做一支30秒的发布片，官网是xxx.com」 | 先读产品，出三个方向的关键帧给你挑，写节奏单，再写片、作曲配乐，打开编辑器等你 |
| 「把data/funnel.csv做成30秒解说，讲清楚为什么注册率翻倍了」 | 按数据讲故事：先轴、后数据、只标一件事，数字变成可以直接改的输入框 |
| 「做一支发布片，要口播，用我自己的录音：voice.m4a」 | 逐字对齐，画面落在说到的那个词上，自动出字幕，配乐在说话时让位 |
| 「这条口播视频加个包装」 | 名字条、数字卡、关键词花字、章节卡，导出带透明通道的叠层，直接拖进剪映或Premiere |
| 「改成竖屏」 | 复制一份1080×1920的版本，重新排版的活儿进收件箱，接着改 |
| 「导出GIF」「要透明底」「做成网页分享」 | MP4、MOV（透明）、WebM、GIF；或者导出一个带播放器和源码的分享页 |

开工前，它会先读你以前的偏好和过去片子留下的经验；每支片子做完，再把你这次说过的话、在编辑器里提的评论收一遍，值得留下的记下来。你的偏好只存在你自己电脑上。

---

## 怎么做到的

### 一支片子就是一个`index.html`

画面用代码写，GSAP、Canvas、Three.js、SVG，浏览器能画的都能用；不调用视频生成模型，每一帧只由代码和时间决定。没有私有格式，片子就是一个网页，带走就能用。

```
你的agent ──写──▶ my-film/index.html ◀──盯着── om studio（浏览器里的编辑器）
    ▲                                              │
    └── om inbox --wait ◀── .om/inbox.jsonl ◀── 你在画面上点一下、写一句
```

### 导演规则，不是模板

skill最大的一块是导演方法：先读产品、找出它的气质，再选片子的结构和运动语言。这些规则来自实测，不是拍脑袋：

- 拿21支真实的发布片（Apple、Nothing、GoPro、Google、Vercel、Linear、Anthropic等），用FFmpeg逐支量切点、节拍、响度和能量曲线；
- 拆了142支高互动的发布片和动效片，按产品类型整理出20种运动语言，每种写清楚它在说什么、适合什么产品；
- 每支片子开工前先写一张节奏单：3秒内要有钩子，中段要有一次爆发，最响的那一下前面先停一拍。

颜色也量过：顶级发布片的颜色几乎都是找来的（品牌色、产品外壳和界面、实拍里的光），所以三个方向先从产品里找颜色，`om swatch`把色板和对比度摆出来看。

