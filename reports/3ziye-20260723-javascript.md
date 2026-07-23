## 📝 热点项目-20260723-javascript

<div style="background-color: #f5f5f5; padding: 15px; border-radius: 8px; margin: 20px 0;">
- 🤖 本报告基于 GitHub API 自动生成
- 📅 数据更新时间: 2026-07-23 12:09:55 (上海时区)
- 🌟 星标数等统计信息为生成时的实时数据
- 📚 项目信息来源于各项目的 README 文档
- 💡 热度指数计算方式: 星标数 + Fork数 × 0.5
- 本报告由 三子叶开源 github-trending项目分析工具自动生成
</div>

## 🔗 相关链接

- [GitHub API 文档](https://docs.github.com/en/rest)
- [项目数据获取器源码](https://github.com/3ziye/github-trending)

---

# 热点项目-20260723-javascript

<div align="center">
📊 <strong>生成时间</strong>: 2026年07月23日 12:09  •  
🎯 <strong>项目数量</strong>: 20 个  •  
⏱️ <strong>热度时间</strong>: 月榜  •  
🔥 <strong>数据来源</strong>: GitHub API
</div>

---

## 🚀 热门项目详情

### 1. Codex-Dream-Skin

**🔥 热度指数**: 12,483

**项目名称**: [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin)
**项目描述**: Codex Dream Skin
**主要语言**: JavaScript
**许可证**: None
**⭐ 星标数**: 11,887
**🍴 Fork 数**: 1,193
**👀 关注数**: 11,887
**🐛 开放问题**: 129
**最后更新**: 2026-07-23 (13分钟前)
**📖 项目文档**: [README](3ziye-20260723-javascript/1-Codex-Dream-Skin-Readme.md)

**🏠 项目主页**: https://www.dreamskin.cc

**📂 克隆地址**: `https://github.com/Fei-Away/Codex-Dream-Skin.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🎯 核心特性
- macOS：打开 `CodexDreamSkin-vX.Y.Z.dmg`，把 App 拖进 Applications。
- Windows：双击 `CodexDreamSkin-Setup-vX.Y.Z.exe`，按安装向导完成。

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 2. wloc

**🔥 热度指数**: 6,745

**项目名称**: [Yu9191/wloc](https://github.com/Yu9191/wloc)
**项目描述**: 修改 Apple 网络定位（gs-loc）返回坐标 · 支持 Surge / Quantumult X / Loon / Stash · 快捷指令一键设置/恢复定位
**主要语言**: JavaScript
**许可证**: None
**⭐ 星标数**: 6,142
**🍴 Fork 数**: 1,207
**👀 关注数**: 6,142
**🐛 开放问题**: 48
**最后更新**: 2026-07-23 (4分钟前)
**📖 项目文档**: [README](3ziye-20260723-javascript/2-wloc-Readme.md)

**🏠 项目主页**: https://wloc-pages.pages.dev/

**📂 克隆地址**: `https://github.com/Yu9191/wloc.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🎯 核心特性
**wloc 设置地理位置**：https://www.icloud.com/shortcuts/a82717d8fdad4e6280866fcf911173f7
**wloc 清理恢复位置**：https://www.icloud.com/shortcuts/f42632d406504f24a2cd163af4fe012f
**设置位置：** 在地图 App 里选好位置（长按地图选点）→ 共享 → 选「wloc 设置地理位置」即可切换。
**清理位置：** 点「wloc 清理恢复位置」即可恢复真实定位。
**高德**：分享出来是短链，真实坐标只藏在 302 跳转的 `Location` 头里，且是 GCJ-02 偏移坐标。快捷指令既读不到跳转头、也难做坐标换算，所以由 worker 跟跳转 → 抠坐标 → GCJ-02→WGS84 → 返回经纬度。
**苹果地图**：链接里直接带 `coordinate=纬度,经度`，但在**中国大陆同样是 GCJ-02 偏移坐标**，所以和高德一样由 worker 做 GCJ-02→WGS84 换算后返回；境外坐标会自动跳过换算（`out_of_china` 判断）原样返回。除了统一坐标系，走同一接口也方便统一处理短链、文本夹链接、名称解码等。
- 解析逻辑：[`worker/src/parse.js`](worker/src/parse.js)，路由：[`worker/src/index.js`](worker/src/index.js)
- 部署后把快捷指令里的 `wloc-spoofer.wloc.workers.dev` 换成你自己的 worker 域名即可。

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 3. scroll-world

**🔥 热度指数**: 5,137

**项目名称**: [oso95/scroll-world](https://github.com/oso95/scroll-world)
**项目描述**: A skill that turn any brand into a scrollable 3D world
**主要语言**: JavaScript
**许可证**: MIT License
**⭐ 星标数**: 4,857
**🍴 Fork 数**: 561
**👀 关注数**: 4,857
**🐛 开放问题**: 5
**最后更新**: 2026-07-23 (41分钟前)
**📖 项目文档**: [README](3ziye-20260723-javascript/3-scroll-world-Readme.md)

**🏠 项目主页**: 无

**📂 克隆地址**: `https://github.com/oso95/scroll-world.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🎯 核心特性
- <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 4. os-taxonomy

**🔥 热度指数**: 3,903

**项目名称**: [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy)
**项目描述**: 暂无描述
**主要语言**: JavaScript
**许可证**: Open Data Commons Open Database License v1.0
**⭐ 星标数**: 3,595
**🍴 Fork 数**: 616
**👀 关注数**: 3,595
**🐛 开放问题**: 13
**最后更新**: 2026-07-23 (19分钟前)
**📖 项目文档**: [README](3ziye-20260723-javascript/4-os-taxonomy-Readme.md)

**🏠 项目主页**: 无

**📂 克隆地址**: `https://github.com/withmarbleapp/os-taxonomy.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🎯 核心特性
- | **The textual content Marble authored** — topic `description`/`name`/`evidence`/`assessmentPrompt`, dependency `reason`s, cluster `summary`s | [**CC BY-SA 4.0**](LICENSE-

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 5. ios-location-spoofer

**🔥 热度指数**: 2,795

**项目名称**: [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer)
**项目描述**: Standalone iOS app to spoof GPS location without jailbreak. Includes Shadowrocket/Surge/Loon/QX/Stash module.
**主要语言**: JavaScript
**许可证**: GNU Affero General Public License v3.0
**⭐ 星标数**: 2,583
**🍴 Fork 数**: 424
**👀 关注数**: 2,583
**🐛 开放问题**: 11
**最后更新**: 2026-07-23 (24分钟前)
**📖 项目文档**: [README](3ziye-20260723-javascript/5-ios-location-spoofer-Readme.md)

**🏠 项目主页**: 无

**📂 克隆地址**: `https://github.com/mekos2772/ios-location-spoofer.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🎯 核心特性
**多平台支持** — 从单一 iOS App 扩展到五个代理软件，覆盖更多用户
**蜂窝基站坐标修改** — 原版 Go 只改了 WiFi 热点坐标，JS 版额外处理了 CellTower（字段 22/24）的坐标替换
**多响应格式兼容** — 自动检测 Apple 回应的封装格式（ARPC / synthetic / marker / bare），确保改后还能被 iOS 正确识别
**运动状态伪造** — 一并改写 motionActivityType 和 motionActivityConfidence，减少被系统识破的可能

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 6. knockoff

**🔥 热度指数**: 1,990

**项目名称**: [Shpigford/knockoff](https://github.com/Shpigford/knockoff)
**项目描述**: Chrome extension that filters pseudo-brand junk out of Amazon. Buy from real, established brands.
**主要语言**: JavaScript
**许可证**: Other
**⭐ 星标数**: 1,955
**🍴 Fork 数**: 71
**👀 关注数**: 1,955
**🐛 开放问题**: 16
**最后更新**: 2026-07-23 (6小时前)
**📖 项目文档**: [README](3ziye-20260723-javascript/6-knockoff-Readme.md)

**🏠 项目主页**: https://knockoff.co

**📂 克隆地址**: `https://github.com/Shpigford/knockoff.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🏷️ 项目标签
- `amazon`
- `browser-extension`
- `chrome-extension`
- `firefox-addon`
- `ios-extension`
- `safari-extension`

#### 🎯 核心特性
- [Fast Company](https://www.fastcompany.com/91570721/amazon-shopping-slop-viral-new-tool-filters-out-knockoff-brands)
- [Gizmodo](https://gizmodo.com/new-browser-extension-helps-you-dodge-amazons-sea-of-knock-off-products-2000783054)
- [404 Media](https://www.404media.co/knockoff-browser-extension-hides-sketchy-brands-on-amazon/)
- [PC Gamer](https://www.pcgamer.com/hardware/this-chrome-extension-hides-knockoff-brands-on-amazon-sorry-to-brands-like-wnpethome-eheyciga-yxy/)
- [Yahoo](https://tech.yahoo.com/apps/articles/chrome-extension-removes-unknown-brands-162002361.html)
- [Lifehacker](https://lifehacker.com/tech/knockoff-browser-extension-hides-shady-items-on-amazon)

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 7. wardrobe

**🔥 热度指数**: 1,459

**项目名称**: [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe)
**项目描述**: Your clothes, extracted and organized with gpt-image.
**主要语言**: JavaScript
**许可证**: MIT License
**⭐ 星标数**: 1,362
**🍴 Fork 数**: 195
**👀 关注数**: 1,362
**🐛 开放问题**: 6
**最后更新**: 2026-07-23 (16分钟前)
**📖 项目文档**: [README](3ziye-20260723-javascript/7-wardrobe-Readme.md)

**🏠 项目主页**: 无

**📂 克隆地址**: `https://github.com/tandpfun/wardrobe.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🎯 核心特性
**Web UI:** Help the user configure their own `OPENAI_API_KEY` and `data/model-reference.png`, then let them import through the app.
- Detects every garment in a photo with the OpenAI Responses API
- Extracts clean product cutouts with the OpenAI Images API
- Generates an optional modeled editorial preview
- Keeps originals, jobs, generated images, and the JSON database local in `data/`
- Supports drag, drop, paste, editing, review, regeneration, and approval

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 8. hermes-browser-extension

**🔥 热度指数**: 1,143

**项目名称**: [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension)
**项目描述**: Browser-native side panel for Hermes Agent — connect web context to your local Hermes runtime.
**主要语言**: JavaScript
**许可证**: MIT License
**⭐ 星标数**: 1,090
**🍴 Fork 数**: 106
**👀 关注数**: 1,090
**🐛 开放问题**: 4
**最后更新**: 2026-07-23 (6小时前)
**📖 项目文档**: [README](3ziye-20260723-javascript/8-hermes-browser-extension-Readme.md)

**🏠 项目主页**: 无

**📂 克隆地址**: `https://github.com/abundantbeing/hermes-browser-extension.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🏷️ 项目标签
- `ai-agent`
- `browser-extension`
- `chrome-extension`
- `edge-extension`
- `hermes-agent`
- `local-first`
- `nous-research`
- `sidepanel`

#### 🎯 核心特性
- ## Highlig

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 9. penecho

**🔥 热度指数**: 1,094

**项目名称**: [penecho/penecho](https://github.com/penecho/penecho)
**项目描述**: Think with AI beyond the chat box. A shared canvas for handwriting, equations, diagrams, and spatial reasoning.
**主要语言**: JavaScript
**许可证**: GNU Affero General Public License v3.0
**⭐ 星标数**: 1,042
**🍴 Fork 数**: 104
**👀 关注数**: 1,042
**🐛 开放问题**: 12
**最后更新**: 2026-07-23 (2分钟前)
**📖 项目文档**: [README](3ziye-20260723-javascript/9-penecho-Readme.md)

**🏠 项目主页**: 无

**📂 克隆地址**: `https://github.com/penecho/penecho.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🏷️ 项目标签
- `ai`
- `canvas`
- `claude`
- `codex`
- `education`
- `handwriting`
- `nodejs`
- `visual-thinking`

#### 🎯 核心特性
**[Kimi Code](https://www.kimi.com/code?aff=penecho)** — Kimi's coding subscription, available worldwide
**[Kimi Open Platform · China](https://platform.kimi.com?aff=penecho)** — API access for mainland China
**[Kimi Open Platform · Global](https://platform.kimi.ai?aff=penecho)** — API access for the rest of the world
- [Quick start](#quick-start)
- [Think on the canvas](#think-on-the-canvas)
- [What's new in 0.7.0](#whats-new-in-070)
- [What's new in 0.6.0](#whats-new-in-060)
- [Animation scenes](#animation-scenes-in-060)

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 10. cdk-redeem-only-extension

**🔥 热度指数**: 1,120

**项目名称**: [kui123456789/cdk-redeem-only-extension](https://github.com/kui123456789/cdk-redeem-only-extension)
**项目描述**: UPI redeem only extension
**主要语言**: JavaScript
**许可证**: MIT License
**⭐ 星标数**: 1,017
**🍴 Fork 数**: 206
**👀 关注数**: 1,017
**🐛 开放问题**: 1
**最后更新**: 2026-07-22 (13小时前)
**📖 项目文档**: [README](3ziye-20260723-javascript/10-cdk-redeem-only-extension-Readme.md)

**🏠 项目主页**: 无

**📂 克隆地址**: `https://github.com/kui123456789/cdk-redeem-only-extension.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🎯 核心特性
- GitHub 首页可直接打开：[教程.docx](教程.docx)
- Release 下载页也提供同一份教程：[tutorial.docx](https://github.com/kui123456789/cdk-redeem-only-extension/releases/latest/download/tutorial.docx)
- 自动注册邮箱账号并读取邮箱验证码。
- 设置 GPT 登录密码。
- 第 7 步开通 TOTP 2FA、读取 access token、检测是否有试用资格。
- 资格通过后保存到 Free 组；有可用 CDK 时主流程可自动提交兑换。
- Free 组导入、导出、补充 AT、一键识别 Plus、一键兑换 UPI、一键兑换 IDEAL、一键兑换全部。
- UPI 和 IDEAL CDK 池分开导入、删除、启用、刷新状态。

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 11. quantskills

**🔥 热度指数**: 948

**项目名称**: [quantskills/quantskills](https://github.com/quantskills/quantskills)
**项目描述**: QuantSkills组织的全景导航 ——Panoramic navigator for the QuantSkills organization
**主要语言**: JavaScript
**许可证**: None
**⭐ 星标数**: 935
**🍴 Fork 数**: 26
**👀 关注数**: 935
**🐛 开放问题**: 0
**最后更新**: 2026-07-23 (0分钟前)
**📖 项目文档**: [README](3ziye-20260723-javascript/11-quantskills-Readme.md)

**🏠 项目主页**: 无

**📂 克隆地址**: `https://github.com/quantskills/quantskills.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🎯 核心特性
- [01 数据接口与数据仓库](#cat-01)
- [02 因子研发工具箱](#cat-02)
- [03 市场与标的分析](#cat-03)
- [04 风险监控与预警](#cat-04)
- [05 策略回测与交易工具](#cat-05)
- [06 投研模型与研究复现](#cat-06)
- [07 研究验证与质量工具](#cat-07)
- [08 资讯搜索与知识分析](#cat-08)

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 12. cue

**🔥 热度指数**: 805

**项目名称**: [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue)
**项目描述**: Open-source macOS AI copilot that floats over your screen, sees/hears your meetings, and stays hidden from screen shares...
**主要语言**: JavaScript
**许可证**: GNU General Public License v3.0
**⭐ 星标数**: 727
**🍴 Fork 数**: 157
**👀 关注数**: 727
**🐛 开放问题**: 8
**最后更新**: 2026-07-23 (2小时前)
**📖 项目文档**: [README](3ziye-20260723-javascript/12-cue-Readme.md)

**🏠 项目主页**: 无

**📂 克隆地址**: `https://github.com/Blueturboguy07/cue.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🎯 核心特性
- | **OpenAI** | [platform.openai.com/api-keys](https://platform.openai.com/api-keys) | One key does everything — **but** for the *listening* features the key must have **Whisper / audio** access (a "restricted"

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 13. age-verification-bypass

**🔥 热度指数**: 689

**项目名称**: [helloyanis/age-verification-bypass](https://github.com/helloyanis/age-verification-bypass)
**项目描述**: Extension to bypass age verification on some websites
**主要语言**: JavaScript
**许可证**: MIT License
**⭐ 星标数**: 675
**🍴 Fork 数**: 29
**👀 关注数**: 675
**🐛 开放问题**: 18
**最后更新**: 2026-07-23 (1小时前)
**📖 项目文档**: [README](3ziye-20260723-javascript/13-age-verification-bypass-Readme.md)

**🏠 项目主页**: https://addons.mozilla.org/addon/age-verification-bypass?utm_source=github_about_link

**📂 克隆地址**: `https://github.com/helloyanis/age-verification-bypass.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🏷️ 项目标签
- `age-verification`
- `ageverif`
- `bypasser`
- `firefox-addon`
- `webextension`

#### 🎯 核心特性
- Make sure it is allowed to run on all websites (or at least on the website you are trying to use it on), and in private browsing mode if you use it, from the extension settings.
- Try to access a page gated by age verification, you will be directly let through. You can try on [ageChecker's demo page](https://agechecker.net/demo)
**[AgeChecker.net](https://agechecker.net/demo)** Fully bypassed, unless the site's server does a double check with the AgeChecker server
**[AgeVerif.com](https://demo.ageverif.com/)** Basic and advanced integrations bypassed, not for the oAuth2 flow
**[AliExpress](https://aliexpress.com/)** for viewing items categorized as "For adults".
**[Bluesky](https://bsky.app)** for viewing sensitive posts without logging in. The posts are visible, and the medias are revealed by clicking on "Show" in the Sensitive Media banner

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 14. agent-plugin

**🔥 热度指数**: 652

**项目名称**: [ChatCut-Inc/agent-plugin](https://github.com/ChatCut-Inc/agent-plugin)
**项目描述**: Plugin for agents to interact with Chatcut
**主要语言**: JavaScript
**许可证**: None
**⭐ 星标数**: 625
**🍴 Fork 数**: 54
**👀 关注数**: 625
**🐛 开放问题**: 0
**最后更新**: 2026-07-23 (57分钟前)
**📖 项目文档**: [README](3ziye-20260723-javascript/14-agent-plugin-Readme.md)

**🏠 项目主页**: 无

**📂 克隆地址**: `https://github.com/ChatCut-Inc/agent-plugin.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🎯 核心特性
- `codex/` - the Codex plugin package.
- `claude/` - the Claude Code plugin package.
- `codex/.codex-plugin/plugin.json` - Codex plugin metadata.
- `claude/.claude-plugin/plugin.json` - Claude Code plugin metadata.
- `codex/.mcp.json` - Codex MCP server configuration.
- `codex/skills/` - direct symlinks to the canonical repository skills.
- `claude/skills/` - Claude-specific skills link to the repository; shared skills link to `codex/skills/`.
- `codex/assets/` - plugin icons and brand assets, shared with Claude through a symlink.

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 15. skills

**🔥 热度指数**: 644

**项目名称**: [dzhng/skills](https://github.com/dzhng/skills)
**项目描述**: 暂无描述
**主要语言**: JavaScript
**许可证**: MIT License
**⭐ 星标数**: 623
**🍴 Fork 数**: 42
**👀 关注数**: 623
**🐛 开放问题**: 2
**最后更新**: 2026-07-22 (1天前)
**📖 项目文档**: [README](3ziye-20260723-javascript/15-skills-Readme.md)

**🏠 项目主页**: 无

**📂 克隆地址**: `https://github.com/dzhng/skills.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 16. kubeez-scroll-world-video

**🔥 热度指数**: 609

**项目名称**: [KubeezMedia/kubeez-scroll-world-video](https://github.com/KubeezMedia/kubeez-scroll-world-video)
**项目描述**: Scroll-scrubbed 'fly through the world' burger demo, generated with Kubeez. Live: meepcastana.github.io/kubeez-scroll-wo...
**主要语言**: JavaScript
**许可证**: None
**⭐ 星标数**: 607
**🍴 Fork 数**: 5
**👀 关注数**: 607
**🐛 开放问题**: 0
**最后更新**: 2026-07-23 (6小时前)
**📖 项目文档**: [README](3ziye-20260723-javascript/16-kubeez-scroll-world-video-Readme.md)

**🏠 项目主页**: https://kubeezmedia.github.io/kubeez-scroll-world-video/

**📂 克隆地址**: `https://github.com/KubeezMedia/kubeez-scroll-world-video.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🎯 核心特性
- Kubeez MCP — see [`AGENTS.m

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 17. spec-superflow

**🔥 热度指数**: 622

**项目名称**: [MageByte-Zero/spec-superflow](https://github.com/MageByte-Zero/spec-superflow)
**项目描述**: 源码级融合 OpenSpec 规划引擎 + Superpowers 执行纪律的 AI 编程工作流插件。17 平台支持，9 skills，Spec-first，契约驱动。
**主要语言**: JavaScript
**许可证**: MIT License
**⭐ 星标数**: 593
**🍴 Fork 数**: 58
**👀 关注数**: 593
**🐛 开放问题**: 2
**最后更新**: 2026-07-23 (3小时前)
**📖 项目文档**: [README](3ziye-20260723-javascript/17-spec-superflow-Readme.md)

**🏠 项目主页**: https://www.npmjs.com/package/spec-superflow

**📂 克隆地址**: `https://github.com/MageByte-Zero/spec-superflow.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🏷️ 项目标签
- `ai-coding`
- `amazon-q`
- `claude-code`
- `cline`
- `codex`
- `copilot-cli`
- `cursor`
- `gemini-cli`

#### 🎯 核心特性
- 启动新的变更 → `用 workflow-start 开始`
- 恢复旧的变更 → `继续上次的工作流`
- 不确定当前状态 → `帮我看看现在该干什么`

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 18. OpenTag

**🔥 热度指数**: 573

**项目名称**: [linxidnju/OpenTag](https://github.com/linxidnju/OpenTag)
**项目描述**: Open-source, channel-native agent gateway for Slack. Route team threads to Claude Code, Codex, OpenCode, Docker, HTTP ag...
**主要语言**: JavaScript
**许可证**: Other
**⭐ 星标数**: 573
**🍴 Fork 数**: 0
**👀 关注数**: 573
**🐛 开放问题**: 0
**最后更新**: 2026-07-23 (8小时前)
**📖 项目文档**: [README](3ziye-20260723-javascript/18-OpenTag-Readme.md)

**🏠 项目主页**: 无

**📂 克隆地址**: `https://github.com/linxidnju/OpenTag.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🏷️ 项目标签
- `agent-gateway`
- `ai-agents`
- `automation`
- `claude`
- `claude-code`
- `claude-tag`
- `codex`
- `developer-tools`

#### 🎯 核心特性
- Ask an agent to investigate a bug from a Slack thread.
- Let teammates add context before or during the agent run.
- Route work to different agent backends such as Codex, Claude Code, OpenCode, Docker-based agents, HTTP agents, or custom CLIs.
- Teach OpenTag an explicit team fact, decision, convention, preference, or procedure; corrections are versioned, scoped, sourced, and reused by every configured runtime.
- Use Channel Profiles / Access Bundles so different projects can have different permissions, memories, default agents, and run limits.
- Require approvals before write actions or risky operations.
- Keep a record of sessions, decisions, outputs, and generated artifacts.
**Shared by default**: the conversation, context, and result stay in the team thread.

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 19. expression-trainer

**🔥 热度指数**: 618

**项目名称**: [fxy2311-youyou/expression-trainer](https://github.com/fxy2311-youyou/expression-trainer)
**项目描述**: 宇宙无敌表达训练系统 — 实时语音转文字 + 27000词情感词库 + AI表达分析报告。离线运行，对着它说话，它帮你看见自己的表达问题。
**主要语言**: JavaScript
**许可证**: MIT License
**⭐ 星标数**: 561
**🍴 Fork 数**: 115
**👀 关注数**: 561
**🐛 开放问题**: 5
**最后更新**: 2026-07-23 (45分钟前)
**📖 项目文档**: [README](3ziye-20260723-javascript/19-expression-trainer-Readme.md)

**🏠 项目主页**: 无

**📂 克隆地址**: `https://github.com/fxy2311-youyou/expression-trainer.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🎯 核心特性
- 🎤 **实时语音识别**：基于 Sherpa-ONNX，完全离线，中文优化
- 📝 **全屏字幕显示**：黑底大字，实时显示你说的每一句话
- 🔍 **词库分析**：自动检测填充词、犹豫词、笼统词，给出精准替代
- 🤖 **AI反馈**：支持 Groq/OpenAI/DeepSeek/Ollama 多后端
- 📊 **分析报告**：6维度深度分析（逻辑/直接性/填充词/密度/词汇/亮点）
**130+ 情绪词**：分类（喜怒哀惧恶惊）+ 强度（1-9）
**笼统词→精准词映射**：25组高频替代建议
**填充词表**：24个常见口头禅

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 20. motion-anything

**🔥 热度指数**: 558

**项目名称**: [nexu-io/motion-anything](https://github.com/nexu-io/motion-anything)
**项目描述**: ✨ The agentic motion layer — an open-source, chat-native motion engine. Describe the feeling; your AI ships the animatio...
**主要语言**: JavaScript
**许可证**: Apache License 2.0
**⭐ 星标数**: 530
**🍴 Fork 数**: 56
**👀 关注数**: 530
**🐛 开放问题**: 4
**最后更新**: 2026-07-23 (18分钟前)
**📖 项目文档**: [README](3ziye-20260723-javascript/20-motion-anything-Readme.md)

**🏠 项目主页**: 无

**📂 克隆地址**: `https://github.com/nexu-io/motion-anything.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🏷️ 项目标签
- `ai-agent`
- `animation`
- `claude`
- `design-tools`
- `figma-motion-alternative`
- `motion-design`
- `motion-graphics`
- `webgl`

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---