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

这篇README里的每一段动画都是huashu-motion做的。上面那段取自它给自己做的53秒发布片，👉 [下载完整发布片（MP4，带声音）](https://github.com/alchaincyf/huashu-motion/releases/latest)，下面Grok Bot（非官方）、huashu-design、DeepSeek、Claude Duet（非官方）这几支的完整版也在同一个页面。

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

### Claude Duet（粉丝自制，非官方）：一次给足需求，全程没找我确认

<img src="docs/media/claude-duet.gif" alt="Claude Duet粉丝片：像素小人Claude Code在终端里等你敲键，炸散后收拢成Duet的图标，通知先来找你，入夜后一条连笔线穿过各个应用替你把活干完" width="100%" />

Anthropic发布Claude Duet当天做的，29秒英文版。像素小人Claude Code在终端里等你敲键，变形成Duet以后主动来找你，你睡着了它接着干。完整版在[Release页面](https://github.com/alchaincyf/huashu-motion/releases/latest)。

---

## 样片是怎么做出来的

很多人问这些样片用的是什么提示词。下面是我当时的原话，一字没改，语音输入的错字也留着；本机路径和截图换成了方括号里的说明，跟这支片无关的话删掉了，用……标出；圆括号里是我补的上下文。

可以看出来，效果不全来自第一句话：有的片子我一次把需求说清楚，就放手让它做；有的片子我盯着改了好几轮。一句话也能出片，想到这个水准，要么第一句给足，要么后面有人当导演。

<details>
<summary><b>Claude Duet</b>（非官方）· 一份需求、两条追加，中间没有修改意见</summary>

> anthropic刚刚发布了claude duet，我希望你帮我充分调研信息，然后帮我做三个版本的视频 /huashu-motion  
> 版本一：16：9 英文版本，30秒以内  
> 版本二：16：9 中文版本 我希望除了品牌信息外，主要元素都是中文 ，30秒以内  
> 版本三：带中文口播，2：3比例，主要界面内容包含官方英文，以及我们制作的中文版本，目标是发在抖音上给用户介绍Claude duet，1分钟以内
>
> 这三个版本我们都需要体现三个方面，但你可以通过不同的方式强调和和体现：  
> 1、Claude duet和Claude code这种coding agent之间的区别  
> 2、目前的使用门槛：大致是pro、max会员可以用上，但是需要申请waitlist  
> 3、ChatGPT dots、muse、grok bot这三个都是personal agent，一定程度上可以认为面对前面三个personal agent，claude选择了claude duet出击。[一张Claude Code像素形象的截图] 这是Claude code原本的形象，我觉得你可以用一个比较视觉化的，动效出色的语言比较有趣的去表达这件事。  
> 三个版本都需要被认为超过了90分才能算制作完成。以及第三个版本我们做完后，你制作封面和标题简介，然后发到抖音和视频号
>
> 除了huashu-motion之外，你也可以使用 /huashu-video-pipeline  /huashu-art-motion 这两个skill辅助你完成内容创作

随后追加了两条，一条在11秒后，一条在5分钟后：

> 不需要找我做任何确认，请完全独立执行

> 用更多的动效和视觉隐喻去表达，而非用过多的字幕与语言。
>
> 抖音版本里可以用x截图之类的方式辅助口播去表达anthropic刚刚发布了这个新产品

之后除了交代做完发到X，没再给过意见。方向是agent自己选的，「过了90分」由另开的评审agent按评分标准打分，英文版改到第9版拿到91分才交。

</details>

<details>
<summary><b>DeepSeek V4.1 Flash动效片</b> · 一句话＋三轮意见，全程不到半小时</summary>

> 用 /huashu-motion skill尽情展示你的动效制作能力，不要关心传达什么，做尽可能多的快切和不同类型的动效展示，30秒以内。最后展示这个动画是由DeepSeek v4.1 flash 1017制作的即可

做的过程中：

> 哦对，开头也可以加一点DeepSeek的logo、鲸鱼，然后快速转动画

看第1版：

> [截了一帧] 这部分画面动效就去掉吧，我觉得很差，不需要展示。以及最后的结尾也长了一些。我觉得爆点可以更早开始！

看第2版：

> [又截了两帧] 这两个动效画面也可以去掉，很差

之后就没再改过，最后交的是第8版。

</details>

<details>
<summary><b>Grok Bot粉丝片</b> · 一句话＋选方向＋一轮意见</summary>

> 我们去给马斯克新推出的personal agent：grok bot做一个产品发布的宣传片

agent给了三个方向（团队上线、夜班、八只手），推荐用夜班的故事做骨架、中间插一段色块快切、电脑窗口用真界面。我回：

> 没问题，按你的推荐结构

看第4版：

> 整体不错，但是第一帧开场的效果我觉得很差，还不如核心聚焦在typing呢

看第6版：

> 非常非常棒！！我觉得我们的huashu-motion比昨晚又强了很多很多。……

</details>

<details>
<summary><b>huashu-design 3.0发布片</b> · 一句话＋选方向，第一版就过了，后来又往上提</summary>

> 你再打开两个fanbox窗口，分别去做