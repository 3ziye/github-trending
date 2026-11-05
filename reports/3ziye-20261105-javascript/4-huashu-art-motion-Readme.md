<div align="center">

**简体中文** | [English](README.en.md)

<img src="assets/showcase/hero.png" alt="huashu-art-motion电影画廊：35种艺术风格，9种解说语法" width="100%" />

# huashu-art-motion · 艺术动画

让你的coding agent，把艺术风格写成会动的画。

36种艺术风格 · 9种解说语法 · 8种参数化片段 · 口播整片参考代码

```sh
npx skills add alchaincyf/huashu-art-motion
```

[看动画](#动画样片) · [看风格](#看效果) · [开始使用](#里面有什么) · [下载完整样片](https://github.com/alchaincyf/huashu-art-motion/releases/latest)

</div>

## 动态

- 2026-10：[Open Design](https://github.com/nexu-io/open-design)（nexu-io 出品的开源 AI 设计工作区）的 [motion-design skill](https://github.com/nexu-io/open-design/blob/main/skills/motion-design/SOURCES.md) 把 huashu-art-motion 列为设计来源之一，并在 [skills/huashu-art-motion](https://github.com/nexu-io/open-design/tree/main/skills/huashu-art-motion) 收录了一份适配版，保留了 MIT 许可和上游出处。很高兴这套艺术动画的做法被另一个开源项目用起来，谢谢 Open Design 团队。也欢迎更多项目使用、反馈和贡献。

## 动画样片

### 核心案例：花叔闯进超级玛丽

把自己做成像素主角，跑完一整关。砖块、水管、关卡运动与转场用代码完成，人物用生成帧合成；下面直接截自65秒成片。

<img src="assets/showcase/mario-claude.gif" alt="花叔顶砖触发会员选择，光标从OpenAI移到Claude，获得星芒道具后变大" width="100%" />

连吃蘑菇都得先选会员：OpenAI，还是Claude？选完Claude，星芒道具落下来，花叔变大。

<table><tr>
<td width="50%"><img src="assets/showcase/mario-combo.gif" alt="花叔踩下像素敌人，踢出缩成球的敌人撞飞前方角色，接着顶碎砖块" width="100%" /><br/>连踩带踢 · 像素Sam与Dario客串敌人</td>
<td width="50%"><img src="assets/showcase/mario-pipe.gif" alt="花叔钻进水管，镜头穿过绿色隧道进入金币密室，再用扫描线甩镜返回地面" width="100%" /><br/>钻进水管 · 金币密室与扫描线甩镜</td>
</tr></table>

这组展示的是成片效果；GIF无声、循环播放。[片段时间点与导出参数](assets/showcase/mario-clips.md)。

### Clawd 博物馆奇妙夜

Claude Code 的像素吉祥物 Clawd 从保安电脑的终端里蹦出来，打着手电夜巡纽约大都会博物馆，再穿过中央公园去自然史博物馆，天亮前赶回来装成展品。98秒，16个场景，无口播，配乐也是代码合成的。

<img src="assets/showcase/clawd-vangogh.gif" alt="Clawd跳进梵高《麦田与柏树》，被重画成厚涂笔触，在麦浪里奔跑" width="100%" />

跳进梵高《麦田与柏树》：笔触方向取自原作的结构张量，Clawd被重画成厚涂。

<table><tr>
<td width="50%"><img src="assets/showcase/clawd-trex.gif" alt="霸王龙骨架像猫追激光点一样追着手电光斑扑来扑去" width="100%" /><br/>霸王龙骨架 · 追手电光斑</td>
<td width="50%"><img src="assets/showcase/clawd-dawn.gif" alt="天亮，Clawd在画框里装展品，保安的手放下咖啡，Clawd眨了一下眼" width="100%" /><br/>天亮 · 装成展品眨一下眼</td>
</tr></table>

暗处是炭笔夜景，只有手电照到的地方显出颜色；入画的五幅（梵高、修拉、维米尔、伦勃朗、勒茨）都是大都会开放获取的CC0原作，按各自画家的笔法用代码重画。完整成片在[Releases](https://github.com/alchaincyf/huashu-art-motion/releases/latest)，[片段时间点与说明](assets/showcase/clawd-clips.md)。

### 花叔穿越名画

画里真的会动。下面三段来自同一支穿越短片，场景用代码画，角色用生成帧合成。

<img src="assets/showcase/monet.gif" alt="莫奈日本桥：打水漂，水面泛起涟漪" width="100%" />

日本桥上的一次水漂。

<table><tr>
<td width="50%"><img src="assets/showcase/egypt.gif" alt="古埃及：与圣甲虫互动" width="100%" /><br/>古埃及 · 圣甲虫</td>
<td width="50%"><img src="assets/showcase/pixel.gif" alt="8-bit：顶方块出金币" width="100%" /><br/>8-bit · 顶出金币</td>
</tr></table>

## 看效果

<img src="assets/全风格总览.jpg" alt="35种艺术风格真实样片总览" width="100%" />

35段样片各取一帧：同一位少女、同一只橘白猫、同一张桌子，从公元前 40000 年的岩洞一路穿到 2026 年。每一段都在动：梵高的星空在转，马赛克的颜色从石块上流过去，水墨晕染把画面带进下一个时代。

注意：这 35 格用的是同一个构图，那是艺术史速通片的机制（风格在变、场景不变），不是这些风格的构图。做新题材要为题材重新构图，别把这间屋搬过去。

👉 [下载全风格样片（MP4）](https://github.com/alchaincyf/huashu-art-motion/releases/latest)

长卷穿越片：一个人从左走到右，跨过边界的那一刻，世界和他自己的画风一起换（下图是收进仓库的 3 段示范：埃及壁画 → 莫奈《日本桥》→ 8-bit）：

<img src="assets/长卷穿越_总览.jpg" alt="长卷穿越片示范：埃及壁画、莫奈日本桥、8-bit 像素" width="100%" />

8种解说语法各有一支可运行示范片（下图每镜取一帧）。此外还有第9种「讲解员式财经科普」，提供语法卡和需自备角色的整片代码快照。白板适合跟着口播画关系，Vox适合图形与信息拼贴：

| | |
|---|---|
| <img src="assets/动画语法/y1_kurzgesagt_总览.jpg" alt="Kurzgesagt 风格" /> Kurzgesagt：扁平无描边、尺度穿行 | <img src="assets/动画语法/y2_vox_总览.jpg" alt="Vox 风格" /> Vox：剪报、红线、荧光笔 |
| <img src="assets/动画语法/y3_whiteboard_总览.jpg" alt="白板风格" /> 白板：笔尖揭开线稿 | <img src="assets/动画语法/t1_3b1b_总览.jpg" alt="3Blue1Brown 风格" /> 3Blue1Brown：一个对象形变成下一个 |
| <img src="assets/动画语法/y4_storytime_总览.jpg" alt="storytime 风格" /> Storytime：反应特写、笑点停顿 | <img src="assets/动画语法/y5_kinetic_type_总览.jpg" alt="动态文字" /> 动态文字：主词砸进来 |
| <img src="assets/动画语法/t2_keynote_ui_总览.jpg" alt="发布会风格" /> 发布会：光斑底、毛玻璃卡、大数字 | <img src="assets/动画语法/t3_finance_chart_总览.jpg" alt="财经图表" /> 财经图表：先轴、后数据、只标一件事 |

---

## 能做什么

| 你说 | 它做 |
|---|---|
| 「复刻这个动画」「拆一下这段」 | 先跑拆解脚本量出转场、节拍网格、每段运动热图，再按机制用代码复刻 |
| 「做个梵高／莫奈／包豪斯那种的动画」 | 先设计一帧，再让它动起来；36张风格配方卡当起点 |
| 「用我的口播做一段艺术动画」 | 镜头表 → 定风格 → 世界画布加镜头 → 输出一条画面轨 |
| 「做一个人穿过一幅幅名画的片子」 | 长卷骨架：每个世界一个段文件，主角一路往右走，跨边界换画风，镜头只进不退 |
| 「做解说视频的动画段」 | 按口播选语法，喂一份 JSON，出一段时长精确到帧的片段（横竖屏、可透明底） |
| 「画面里要有人」 | 人交给生图模型出帧，代码负责合成、换帧和材质 |
| 「配个乐、卡节奏」 | BPM 网格、动机换乐器、结尾音效序列，纯代码合成 |

交付前有一道数字验收：`qa.py` 量稳定、效率、动感、流畅及文字框景线索，再派一个没参与制作的 agent 只看成片挑问题；最后 `deliver.py` 一条命令交付——成片先过反 PPT 门禁（整片几乎没有镜头内快动作就红灯，不出片），过了才复制成片、写交付说明，说明里的事实由脚本写。

---

## 里面有什么

| | 数量 |
|---|---|
| 艺术风格配方卡（参数、母题动作、签名转场、当前短板） | 53张，`references/风格配方/`；其中 38–55 是按原作锚定重做的研究配方（含敦煌壁画） |
| 对应的场景代码 | 53个，`scripts/engine/scenes/` |
| 解说动画语法卡 | 9份；其中8种附示范片、参数化片段与示例spec |
| 口播整片参考代码 | 混合风格、白板、Vox、讲解员；需自备部分素材，详见目录README |
| 长卷穿越片示范（骨架＋3 段＋角色帧库） | 1 支，`scripts/engine/demos/long_scroll/` |
| 版面审计与压测（出界／叠字／字太小、竖屏／超长／英文变体、示例回归） | `render.py --audit`、`scripts/clip_lint.py`、`scripts/analyze/stress_clip.py`、`regress_clips.py` |
| 转场 | 艺术风格签名转场与解说转场，包含淡入、硬切和纸面转场 |
| 绘画与动画库（笔刷、渲染器、后期、骨架、镜头、图表、排版……） | 17 个，`scripts/engine/lib/` |
| 方法文档（拆解、机制、一帧先行、纯代码绘制、节奏配乐、角色、长卷……） | 核心12篇