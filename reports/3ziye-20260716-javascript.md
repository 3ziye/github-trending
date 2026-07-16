## 📝 热点项目-20260716-javascript

<div style="background-color: #f5f5f5; padding: 15px; border-radius: 8px; margin: 20px 0;">
- 🤖 本报告基于 GitHub API 自动生成
- 📅 数据更新时间: 2026-07-16 11:56:17 (上海时区)
- 🌟 星标数等统计信息为生成时的实时数据
- 📚 项目信息来源于各项目的 README 文档
- 💡 热度指数计算方式: 星标数 + Fork数 × 0.5
- 本报告由 三子叶开源 github-trending项目分析工具自动生成
</div>

## 🔗 相关链接

- [GitHub API 文档](https://docs.github.com/en/rest)
- [项目数据获取器源码](https://github.com/3ziye/github-trending)

---

# 热点项目-20260716-javascript

<div align="center">
📊 <strong>生成时间</strong>: 2026年07月16日 11:56  •  
🎯 <strong>项目数量</strong>: 20 个  •  
⏱️ <strong>热度时间</strong>: 月榜  •  
🔥 <strong>数据来源</strong>: GitHub API
</div>

---

## 🚀 热门项目详情

### 1. wloc

**🔥 热度指数**: 5,435

**项目名称**: [Yu9191/wloc](https://github.com/Yu9191/wloc)
**项目描述**: 修改 Apple 网络定位（gs-loc）返回坐标 · 支持 Surge / Quantumult X / Loon / Stash · 快捷指令一键设置/恢复定位
**主要语言**: JavaScript
**许可证**: None
**⭐ 星标数**: 4,965
**🍴 Fork 数**: 941
**👀 关注数**: 4,965
**🐛 开放问题**: 36
**最后更新**: 2026-07-16 (8分钟前)
**📖 项目文档**: [README](3ziye-20260716-javascript/1-wloc-Readme.md)

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

### 2. Cowart

**🔥 热度指数**: 4,837

**项目名称**: [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart)
**项目描述**: 暂无描述
**主要语言**: JavaScript
**许可证**: None
**⭐ 星标数**: 4,660
**🍴 Fork 数**: 354
**👀 关注数**: 4,660
**🐛 开放问题**: 11
**最后更新**: 2026-07-16 (20分钟前)
**📖 项目文档**: [README](3ziye-20260716-javascript/2-Cowart-Readme.md)

**🏠 项目主页**: 无

**📂 克隆地址**: `https://github.com/zhongerxin/Cowart.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🎯 核心特性
- 在 Codex 中打开一个原生 tldraw 无限画布 widget；正常使用不再通过网页浏览器或 in-app browser 打开本地页面。
- 在当前项目目录中持久化画布页面和图片资源。
- 在画布中创建 AI 图片框，直接输入 prompt、选择参考图，并让 Codex 按选中框的位置和比例生成图片后替换它。
- 创建 16:9 的 `AI HTML` 框，通过 prompt 和参考图生成可运行的单文件 HTML，并直接嵌入画布继续编辑或迭代。
- 创建 `AI Slides`，将图片和 HTML 组织成演示文稿，或让 Codex 按指定页数生成一组 16:9 HTML 页面；支持缩略图预览和全屏播放。
- 标注好图片后，可从画布里直接提交标注截图，让 Codex 根据标注生成干净的新图并放到原图旁边。
- 通过 Cowart MCP 工具读取选择状态、保存画布、插入图片或 HTML，并保存到页面本地资源目录。

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 3. os-taxonomy

**🔥 热度指数**: 3,413

**项目名称**: [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy)
**项目描述**: 暂无描述
**主要语言**: JavaScript
**许可证**: Open Data Commons Open Database License v1.0
**⭐ 星标数**: 3,142
**🍴 Fork 数**: 543
**👀 关注数**: 3,142
**🐛 开放问题**: 13
**最后更新**: 2026-07-16 (17分钟前)
**📖 项目文档**: [README](3ziye-20260716-javascript/3-os-taxonomy-Readme.md)

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

### 4. scroll-world

**🔥 热度指数**: 2,740

**项目名称**: [oso95/scroll-world](https://github.com/oso95/scroll-world)
**项目描述**: A skill that turn any brand into a scrollable 3D world
**主要语言**: JavaScript
**许可证**: MIT License
**⭐ 星标数**: 2,583
**🍴 Fork 数**: 315
**👀 关注数**: 2,583
**🐛 开放问题**: 2
**最后更新**: 2026-07-16 (2分钟前)
**📖 项目文档**: [README](3ziye-20260716-javascript/4-scroll-world-Readme.md)

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

### 5. security-audit-skill

**🔥 热度指数**: 2,622

**项目名称**: [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)
**项目描述**: A coding-agent skill for multi-phase security audits with independently verified, machine-readable findings
**主要语言**: JavaScript
**许可证**: MIT License
**⭐ 星标数**: 2,529
**🍴 Fork 数**: 187
**👀 关注数**: 2,529
**🐛 开放问题**: 2
**最后更新**: 2026-07-16 (2小时前)
**📖 项目文档**: [README](3ziye-20260716-javascript/5-security-audit-skill-Readme.md)

**🏠 项目主页**: 无

**📂 克隆地址**: `https://github.com/cloudflare/security-audit-skill.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 6. ios-location-spoofer

**🔥 热度指数**: 2,266

**项目名称**: [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer)
**项目描述**: Standalone iOS app to spoof GPS location without jailbreak. Includes Shadowrocket/Surge/Loon/QX/Stash module.
**主要语言**: JavaScript
**许可证**: GNU Affero General Public License v3.0
**⭐ 星标数**: 2,105
**🍴 Fork 数**: 323
**👀 关注数**: 2,105
**🐛 开放问题**: 10
**最后更新**: 2026-07-16 (22分钟前)
**📖 项目文档**: [README](3ziye-20260716-javascript/6-ios-location-spoofer-Readme.md)

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

### 7. knockoff

**🔥 热度指数**: 1,949

**项目名称**: [Shpigford/knockoff](https://github.com/Shpigford/knockoff)
**项目描述**: Chrome extension that filters pseudo-brand junk out of Amazon. Buy from real, established brands.
**主要语言**: JavaScript
**许可证**: Other
**⭐ 星标数**: 1,916
**🍴 Fork 数**: 67
**👀 关注数**: 1,916
**🐛 开放问题**: 14
**最后更新**: 2026-07-16 (2小时前)
**📖 项目文档**: [README](3ziye-20260716-javascript/7-knockoff-Readme.md)

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

### 8. zeus

**🔥 热度指数**: 1,495

**项目名称**: [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus)
**项目描述**: ⚡️ پنل کلودفلر زئوس (Zeus Panel) 
**主要语言**: JavaScript
**许可证**: None
**⭐ 星标数**: 1,388
**🍴 Fork 数**: 215
**👀 关注数**: 1,388
**🐛 开放问题**: 0
**最后更新**: 2026-07-16 (5分钟前)
**📖 项目文档**: [README](3ziye-20260716-javascript/8-zeus-Readme.md)

**🏠 项目主页**: https://t.me/ZEUS_PANEL_BOT

**📂 克隆地址**: `https://github.com/IR-NETLIFY/zeus.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 9. codexpro

**🔥 热度指数**: 1,368

**项目名称**: [rebel0789/codexpro](https://github.com/rebel0789/codexpro)
**项目描述**: Use ChatGPT Developer Mode as a local coding agent for your repo through MCP.
**主要语言**: JavaScript
**许可证**: MIT License
**⭐ 星标数**: 1,307
**🍴 Fork 数**: 123
**👀 关注数**: 1,307
**🐛 开放问题**: 9
**最后更新**: 2026-07-16 (2小时前)
**📖 项目文档**: [README](3ziye-20260716-javascript/9-codexpro-Readme.md)

**🏠 项目主页**: https://rebel0789.github.io/codexpro/

**📂 克隆地址**: `https://github.com/rebel0789/codexpro.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🏷️ 项目标签
- `apps-sdk`
- `chatgpt`
- `cloudflare-tunnel`
- `codex`
- `local-development`
- `mcp`
- `ngrok`

#### 🎯 核心特性
- Cloudflare quick tunnel

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 10. hermes-browser-extension

**🔥 热度指数**: 1,065

**项目名称**: [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension)
**项目描述**: Browser-native side panel for Hermes Agent — connect web context to your local Hermes runtime.
**主要语言**: JavaScript
**许可证**: MIT License
**⭐ 星标数**: 1,015
**🍴 Fork 数**: 101
**👀 关注数**: 1,015
**🐛 开放问题**: 2
**最后更新**: 2026-07-16 (6分钟前)
**📖 项目文档**: [README](3ziye-20260716-javascript/10-hermes-browser-extension-Readme.md)

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
- Keeps runtime plugins available in the same Hermes session. For example, a connected social or messaging

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 11. cdk-redeem-only-extension

**🔥 热度指数**: 1,112

**项目名称**: [kui123456789/cdk-redeem-only-extension](https://github.com/kui123456789/cdk-redeem-only-extension)
**项目描述**: UPI redeem only extension
**主要语言**: JavaScript
**许可证**: MIT License
**⭐ 星标数**: 1,010
**🍴 Fork 数**: 204
**👀 关注数**: 1,010
**🐛 开放问题**: 1
**最后更新**: 2026-07-14 (2天前)
**📖 项目文档**: [README](3ziye-20260716-javascript/11-cdk-redeem-only-extension-Readme.md)

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

### 12. cfnew-deployer

**🔥 热度指数**: 712

**项目名称**: [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer)
**项目描述**: 暂无描述
**主要语言**: JavaScript
**许可证**: None
**⭐ 星标数**: 577
**🍴 Fork 数**: 270
**👀 关注数**: 577
**🐛 开放问题**: 5
**最后更新**: 2026-07-16 (3小时前)
**📖 项目文档**: [README](3ziye-20260716-javascript/12-cfnew-deployer-Readme.md)

**🏠 项目主页**: 无

**📂 克隆地址**: `https://github.com/byJoey/cfnew-deployer.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🎯 核心特性
- `CLOUDFLARE_API_TOKEN`
- `CLOUDFLARE_ACCOUNT_ID`
- 用户填写 Cloudflare 邮箱和 Global API Key
- 自动读取账户和可绑定域名
- 默认随机生成项目名称、KV 名称和可选子域名，不使用固定业务前缀
- 自动生成 UUID
- 自动创建或复用 KV，并绑定为 `C`
- 支持读取现有 Worker / Pages / KV 后更新部署

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 13. skills

**🔥 热度指数**: 591

**项目名称**: [dzhng/skills](https://github.com/dzhng/skills)
**项目描述**: 暂无描述
**主要语言**: JavaScript
**许可证**: MIT License
**⭐ 星标数**: 570
**🍴 Fork 数**: 42
**👀 关注数**: 570
**🐛 开放问题**: 2
**最后更新**: 2026-07-16 (11小时前)
**📖 项目文档**: [README](3ziye-20260716-javascript/13-skills-Readme.md)

**🏠 项目主页**: 无

**📂 克隆地址**: `https://github.com/dzhng/skills.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 14. drawio-ai-kit

**🔥 热度指数**: 613

**项目名称**: [sparklabx/drawio-ai-kit](https://github.com/sparklabx/drawio-ai-kit)
**项目描述**: Teach your AI to draw correct, beautiful draw.io diagrams — declarative layout engine, ground-truth stencils, structural...
**主要语言**: JavaScript
**许可证**: MIT License
**⭐ 星标数**: 565
**🍴 Fork 数**: 97
**👀 关注数**: 565
**🐛 开放问题**: 1
**最后更新**: 2026-07-16 (3分钟前)
**📖 项目文档**: [README](3ziye-20260716-javascript/14-drawio-ai-kit-Readme.md)

**🏠 项目主页**: 无

**📂 克隆地址**: `https://github.com/sparklabx/drawio-ai-kit.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🏷️ 项目标签
- `agent-skills`
- `ai-agents`
- `architecture-diagrams`
- `aws`
- `azure`
- `bpmn`
- `claude-code`
- `cli`

#### 🎯 核心特性
- Just one domain instead: `npx skills add sparklabx/drawio-ai-kit --skill drawio-aws` (`--list` previews all 5)
- Optional, for the full experience: the **draw.io desktop app** enables `drawio-ai render` (the vision

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发
- 命令行工具开发

---

### 15. awesome-images

**🔥 热度指数**: 557

**项目名称**: [flatkey-ai/awesome-images](https://github.com/flatkey-ai/awesome-images)
**项目描述**: Try flatkey.ai for 40% saving! Generate practical images ready for all your work needs!!!
**主要语言**: JavaScript
**许可证**: None
**⭐ 星标数**: 557
**🍴 Fork 数**: 0
**👀 关注数**: 557
**🐛 开放问题**: 1
**最后更新**: 2026-07-16 (39分钟前)
**📖 项目文档**: [README](3ziye-20260716-javascript/15-awesome-images-Readme.md)

**🏠 项目主页**: https://flatkey.ai/use-case/image-buddy?utm_source=github&utm_medium=awesome_images

**📂 克隆地址**: `https://github.com/flatkey-ai/awesome-images.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🏷️ 项目标签
- `affordable-ai`
- `affordable-ai-platform`
- `ai-api`
- `gpt-image-2`
- `gpt-image-2-api`
- `gpt-image-2-prompts`
- `nano-banana`
- `nano-banana-pro`

#### 🎯 核心特性
- | ![Music Cover](assets/music-cover.png)<br>**Music Cove

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 16. age-verification-bypass

**🔥 热度指数**: 564

**项目名称**: [helloyanis/age-verification-bypass](https://github.com/helloyanis/age-verification-bypass)
**项目描述**: Extension to bypass age verification on some websites
**主要语言**: JavaScript
**许可证**: MIT License
**⭐ 星标数**: 552
**🍴 Fork 数**: 24
**👀 关注数**: 552
**🐛 开放问题**: 16
**最后更新**: 2026-07-16 (2小时前)
**📖 项目文档**: [README](3ziye-20260716-javascript/16-age-verification-bypass-Readme.md)

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
**[AgeChecker.net](https://agechecker.net/demo)**
**[AgeVerif.com](https://demo.ageverif.com/)** (**NOT** for the oAuth2 flow)
**[AliExpress](https://aliexpress.com/)** for viewing items categorized as "For adults". The posts are visible, and the medias are revealed by clicking on "Show" in the Sensitive Media banner
**[Bluesky](https://bluesky.app)** for viewing sensitive posts without logging in
**[Reddit](https://reddit.com)** for viewing NSFW communities. *(It's a clunky solution, I recommend you use [redlib](https://redlib.catsarch.com/) for a fully private Reddit front-end where you can view NSFW posts!)*

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 17. intruth-factcheck

**🔥 热度指数**: 577

**项目名称**: [rpanigrahi222/intruth-factcheck](https://github.com/rpanigrahi222/intruth-factcheck)
**项目描述**: 暂无描述
**主要语言**: JavaScript
**许可证**: Other
**⭐ 星标数**: 532
**🍴 Fork 数**: 90
**👀 关注数**: 532
**🐛 开放问题**: 3
**最后更新**: 2026-07-16 (50分钟前)
**📖 项目文档**: [README](3ziye-20260716-javascript/17-intruth-factcheck-Readme.md)

**🏠 项目主页**: 无

**📂 克隆地址**: `https://github.com/rpanigrahi222/intruth-factcheck.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🎯 核心特性
- live claim detection: continuously monitors speech from the active tab and identifies check-worthy factual claims in real time
- live claim evaluation: analyzes claim veracity using large language models and external sources to determine whether a statement is:
* TRUE
* SUBSTANTIALLY TRUE
* FALSE
* MISLEADING

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 18. spec-superflow

**🔥 热度指数**: 543

**项目名称**: [MageByte-Zero/spec-superflow](https://github.com/MageByte-Zero/spec-superflow)
**项目描述**: 源码级融合 OpenSpec 规划引擎 + Superpowers 执行纪律的 AI 编程工作流插件。17 平台支持，9 skills，Spec-first，契约驱动。
**主要语言**: JavaScript
**许可证**: MIT License
**⭐ 星标数**: 517
**🍴 Fork 数**: 53
**👀 关注数**: 517
**🐛 开放问题**: 3
**最后更新**: 2026-07-16 (0分钟前)
**📖 项目文档**: [README](3ziye-20260716-javascript/18-spec-superflow-Readme.md)

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

### 19. agent-plugin

**🔥 热度指数**: 533

**项目名称**: [ChatCut-Inc/agent-plugin](https://github.com/ChatCut-Inc/agent-plugin)
**项目描述**: Plugin for agents to interact with Chatcut
**主要语言**: JavaScript
**许可证**: None
**⭐ 星标数**: 512
**🍴 Fork 数**: 43
**👀 关注数**: 512
**🐛 开放问题**: 0
**最后更新**: 2026-07-16 (1小时前)
**📖 项目文档**: [README](3ziye-20260716-javascript/19-agent-plugin-Readme.md)

**🏠 项目主页**: 无

**📂 克隆地址**: `https://github.com/ChatCut-Inc/agent-plugin.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🎯 核心特性
- `chatcut/` - the ChatCut Codex plugin package.
- `chatcut/.codex-plugin/plugin.json` - plugin metadata used by Codex.
- `chatcut/.mcp.json` - MCP server configuration for ChatCut.
- `chatcut/skills/` - workflow skills for common ChatCut editing tasks.
- `chatcut/assets/` - plugin icons and brand assets.
- A ChatCut account.
- Codex with plugin support.
- Access to a ChatCut project you want to edit.

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 20. birds.cafe

**🔥 热度指数**: 512

**项目名称**: [kanavtwtgg/birds.cafe](https://github.com/kanavtwtgg/birds.cafe)
**项目描述**: 暂无描述
**主要语言**: JavaScript
**许可证**: None
**⭐ 星标数**: 511
**🍴 Fork 数**: 2
**👀 关注数**: 511
**🐛 开放问题**: 0
**最后更新**: 2026-07-15 (16小时前)
**📖 项目文档**: [README](3ziye-20260716-javascript/20-birds.cafe-Readme.md)

**🏠 项目主页**: 无

**📂 克隆地址**: `https://github.com/kanavtwtgg/birds.cafe.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🎯 核心特性
- Runs fully in the browser (WebGL / Three.js)
- Physics-based flight with flock V-formation
- Dynamic weather: day, night, storm, rain, lightning
- Ambient music
- Smooth on mobile with touch controls

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---