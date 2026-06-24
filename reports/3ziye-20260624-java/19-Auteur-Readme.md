<div align="center">

# 🎬 Auteur

### 一个由 16 位 AI 角色组成的剧组，端到端自动化生产中文短视频

**一句话发起 → 选题、编剧、分镜、生图、配音、配乐、剪辑、复盘 全部跑完 → 落地 MP4**

[![Java 21](https://img.shields.io/badge/Java-21-orange?logo=openjdk)](https://openjdk.org/)
[![Spring Boot 3.3](https://img.shields.io/badge/Spring%20Boot-3.3-6DB33F?logo=springboot)](https://spring.io/)
[![Vue 3](https://img.shields.io/badge/Vue-3-42b883?logo=vuedotjs)](https://vuejs.org/)
[![Remotion](https://img.shields.io/badge/Remotion-Renderer-9333ea)](https://www.remotion.dev/)
[![ffmpeg](https://img.shields.io/badge/ffmpeg-Compositor-darkgreen)](https://ffmpeg.org/)
[![CI](https://github.com/nxin-github/Auteur/actions/workflows/ci.yml/badge.svg)](https://github.com/nxin-github/Auteur/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/License-MIT-yellow)](./LICENSE)
[![Live Demo](https://img.shields.io/badge/🎮_Live_Demo-nxin--github.github.io%2FAuteur-success?style=flat-square)](https://nxin-github.github.io/Auteur/)
[![国内镜像](https://img.shields.io/badge/🇨🇳_国内镜像-CloudBase-blue?style=flat-square)](https://auteur-demo-auteur-demo-d5gklniiyc5672606.webapps.tcloudbase.com)

[English](./README.en.md) ｜ 中文

### 🎮 在线 Demo · 点这里直接玩

[🌍 海外（GitHub Pages）](https://nxin-github.github.io/Auteur/) ｜ [🇨🇳 国内镜像（腾讯云 CloudBase）](https://auteur-demo-auteur-demo-d5gklniiyc5672606.webapps.tcloudbase.com)

*基于真实流水线产出的「今天体验的人生副本：偷外卖的人的一生」打包成可点击演示，30 秒看完整剧组协作 + 自动剪辑 + 数据复盘全流程，无需安装。*

</div>

---

## ✨ Auteur 是什么？

Auteur 把"做一条短视频"拆成一个**完整的虚拟剧组**——不是一串 prompt，是一个**有分工、有审稿、有反馈、有数据复盘**的生产体系。

```
🎯 选题策划  →  📝 编剧（+🔍 自审 +📚 史实核查）  →  🎙️ 配音演员
                                  ↓
🎬 摄影指导（+🎬 自审）→ 🎨 美术指导（+🖼️ 审片官）→ 🎵 作曲 → 🖼️ 封面 → 🎞️ 制片合成
                                  ↓
                          📊 数据分析师  ←  🌐 浏览器扩展（抖音 / B 站 / 视频号 / 快手 数据回写）
                                  ↓
                          反哺下一轮 🎯 选题脑暴
```

**给一个主题，按一下生成，剧组就把流水线跑完——脚本、字幕、分镜、生图、配音、BGM、封面、合成视频，全部落库可追溯，每一步都可中断、人工介入、单独重做。**

---

## 1️⃣ 16 位 AI 角色协作，不是 prompt 链

<div align="center">
  <img src="./docs/screenshot-brainstorm.png" alt="AI 头脑风暴 - 多个 AI 角色协作产出选题候选" width="900" />
  <p><i>AI 头脑风暴工作台:多角色 + 历史数据 + 系列脉络共同生成选题候选</i></p>
</div>

> 业内常见做法是把 LLM 的 prompt 串成一条链——一个出错全盘重跑，中间产物看不到摸不着。
>
> **Auteur 不一样：每个角色都是一个独立的 Spring Service，有自己的 prompt 模板、自己的 LLM 调用与重试策略、自己的 DB 产物表。**

| 类别 | 角色 | 干什么                                                          |
|---|---|--------------------------------------------------------------|
| **创意层** | 🎯 选题策划 | 基于历史数据 + 系列脉络给 5–10 个候选，按题材/钩子打分                             |
| | 📝 编剧 | 拆多段叙事结构，高分走旗舰模型，普通走批量便宜模型                                    |
| | 🔍 编剧自审 | LLM 自审打分，低于阈值把审稿意见塞回去重写一稿                                    |
| | 📚 史实核查 | 抽脚本中的事实声明，逐条验证，给修复建议或自动改写                                    |
| | 🪝 钩子分析师 | 反向提取"下集预告"作为下期种子（系列连续性）                                      |
| **视觉层** | 🎬 摄影指导 | 拆 20–28 个分镜，可选 PRECISE_BY_CUE 模式按 SRT **逐字锚定**               |
| | 🎬 摄影自审 | 校验景别多样性、特写比例、anchor 命中率等硬指标                                  |
| | 🎨 美术指导 | 批量出图，并发限速 + 失败重试 + 锁脸 reference 注入                           |
| | 🖼️ 审片官 | 出图后自动检查：构图 / 手部 / 水印 / 锁脸一致性                                 |
| | 🖼️ 封面设计 | 抽脚本要点出多版封面，含品牌识别                                             |
| **声音层** | 🎙️ 配音演员 | 火山豆包 TTS 合成 narration + SRT，回写真实音频时长                         |
| | 🎵 作曲选曲 | LLM 打 mood 标签 → Jamendo CC 协议曲库选曲 → 锁定                       |
| **统筹层** | 🎬 总导演 | 跨角色的视觉风格 + 叙事弧线 + 关键节拍中央笔记，所有人都读                             |
| | 🎞️ 制片 | SRT → ShotTimingResolver → ImageClip 拼接 → ffmpeg/Remotion 渲染 |
| **复盘层** | 📊 数据分析师 | 拉浏览器扩展回写的真实播放数据，做完播率/钩子归因/周复盘                                |
| | 🧭 系列规划 | 把上一期 hook 转成下一期 topic 种子                                     |

<div align="center">
  <img src="./docs/screenshot-topic-pool.png" alt="选题池 - 跨预设管理选题候选,潜力分自动排序" width="900" />
  <p><i>选题池:跨预设管理候选选题,系统自动按"潜力分"排序,数据回写后权重持续校准</i></p>
</div>

**协作的关键设计：**

- 🔗 **显式产物交接** — 每个角色读上游 DB 表、写下游 DB 表。任何一步失败都可单独重跑，中间产物 UI 里全部能看、能改、能删
- 🔄 **自审反馈环** — 自审角色（编剧 / 摄影 / 美术）打分低于阈值时，审稿意见塞回原角色重写一次。把 LLM 的不确定性局限到"自己给自己改一稿"的小循环里，**不污染整条流水线**
- 📓 **导演笔记共享** — `DirectorNoteService` 维护一个跨角色的视觉/叙事中央笔记，编剧、摄影、美术、制片都读。**避免每个角色各自漂移**
- 🚦 **流水线状态机** — `pipeline_run` 表跟踪每段 PENDING / RUNNING / DONE / FAILED，前端实时进度，断点续跑

---

## 2️⃣ 自动化剪辑：让画面与字幕一帧不差

> 普通流水线最让人崩溃的事：**画面和字幕掐不准**。
>
> Auteur 在生成时就把这个问题堵掉了。

### 🎯 PRECISE_BY_CUE：分镜与音频字面对齐

启用后，摄影指导给每个 shot 一段**精确的字面 anchor_text**（必须是脚本里的连续子串）。后端在 SRT 解析后把 anchor 在音频时间轴上反查出真实秒数：

```
镜头时长 = anchor 在 SRT 里实际占的秒数  ✅ 不再交给 LLM 估算
```

后端会自动校验：
- ✅ anchor 是否真的是脚本子串（normalize 后比对）
- ✅ 相邻 shot 的 anchor 在脚本里位置是否单调递增（防 LLM 乱排）
- ⚠️ 没命中 anchor 的镜头会标 `anchor_match=false`，视频还能渲，但日志和 UI 都提示

<div align="center">
  <img src="./docs/screenshot-storyboard.png" alt="分镜工作台 - 每镜的中文/英文 prompt + 锚点 + 时长" width="900" />
  <p><i>分镜工作台:中英 prompt + anchor + 真实时长,一镜一卡片,可单镜重生成</i></p>
</div>

### 🎞️ 一键合成，制片角色全自动接管

`VideoAssemblyService` + `FfmpegVideoRenderer` / `RemotionVideoRenderer` 自动完成：

- 📐 解析 SRT → `ShotTimingResolver` 算每镜真实时长
- 🎬 拼接 ImageClip