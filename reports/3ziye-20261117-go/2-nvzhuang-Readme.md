# 拍片哥女装 · AI 服装参考图集 (COSTUME-DB-01)

一个深色主题的纯净服装参考图集网站，收录 **2727 套**（写实真人版 1407 套 + 二次元动漫版 1320 套）人物不入镜的 AI 生成纯服装图像（2:3 比例），支持中英文双语浏览、多维检索，并配备可选的 AI 一键换装试穿。

> 👗 **【Linux.do 3级常任理事专属彩蛋】**  
> 听说在 [LINUX DO](https://linux.do/) 社区只要升到 **3 级（常任理事）** 就可以解锁“看女装大佬”的保留节目？身为一名尊贵的 Linux.do 3 级老兵，逛了一圈发现坛里的女装资源还不够看，干脆亲手搓了这个 **「拍片哥女装」** 项目！  
> 不仅收录了写实与动漫双图库合计 2727 套纯净高质量服装图，还顺手接了 AI 虚拟换装后端——这下各位佬友哪怕现实中没有小裙子，直接传张自拍照就能一键无痛变身“女装大佬”出道了 😂！

> 🔗 **在线预览**：https://paipiange.github.io/nvzhuang/  
> ⭐ **GitHub 源码**：https://github.com/paipiange/nvzhuang  
> 📱 **Android APK 下载**：[GitHub Releases 直链](https://github.com/paipiange/nvzhuang/releases/latest/download/nvzhuang-release.apk)（[全部版本](https://github.com/paipiange/nvzhuang/releases)） | 也可[夸克网盘下载](https://pan.quark.cn/s/a914f76fac0b)（「拍片哥女装」`https://pan.quark.cn/s/a914f76fac0b`）  
> 👤 **AI 模特脸部与造型图库**：集成自 [ai-portrait-gallery](https://ai-portrait-gallery.pages.dev/)（あぎ @agi_aibusi · CC0 1.0）  
> 💃 **兄弟项目（AI 姿势参考与生图工坊）**：https://github.com/paipiange/ai-pose-gallery-zh  
> 💡 **原作者推文 / 灵感来源**：X [@giaaibusi](https://x.com/giaaibusi)  
> 🐧 **社区友链**：[LINUX DO (https://linux.do/)](https://linux.do/)

## ⏱️ 10 秒了解本项目

- 🆓 **免费使用（无需部署 / 无需 Key）**：三大图库一键无缝切换：**写实服装 (1407 套) + 动漫服装 (1320 套) + AI 模特库 (1499 位)**，支持分类筛选、中英双语双向检索、大图全屏查看、基础搭配台与同款跳转，由纯前端静态驱动，在线打开即可使用。
- 👤 **内置 1499 位 AI 模特（全量本地化）**：完整集成 CC0 1.0 授权的 AI 模特脸部特写与造型图库，AI 试衣时可直接一键挑选心仪模特，彻底告别“想体验换装却找不到合适人像照片”的困扰。
- ⚙️ **自选扩展（需自建后端 / 需自备 Key）**：真实 AI 试衣换装功能依赖 `backend/` 的 GoFrame 服务。需自行配置大模型（如 GPT Image 2、豆包 Seedream 或 Gemini）的 API Key 与 Base URL，调用将消耗对应的第三方模型配额。
- 📜 **完全可商用 · 免费开源**：基于 [MIT License](LICENSE) 全量开源，代码与图集资源完全开放，支持自由商用创作、设计参考及二次开发。详见 [合规审计报告](docs/LINUXDO_RELEASE_AUDIT.md)。

## 📱 Android 客户端下载

提供离线封装版 Android APK（内置完整前端页面与离线示例图集，安装即可打开使用）：

- **GitHub Releases 直接下载（推荐）**：
  - 最新版 APK 直链：https://github.com/paipiange/nvzhuang/releases/latest/download/nvzhuang-release.apk
  - 历史版本与说明：https://github.com/paipiange/nvzhuang/releases
- **夸克网盘下载（国内备用）**：
  - 「拍片哥女装」链接：https://pan.quark.cn/s/a914f76fac0b

> 💡 **使用提示**：如需连接自建或局域网/公网 AI 换装后端，可在 App 内「我的 → 服务与模型设置」中填写后端 API 地址；若暂未部署后端，打开首页后会弹窗引导至设置页，可切换开启「离线演示模式」浏览内置图集。

## 📸 预览

### 📱 移动端与小程序界面预览

| ① 发现首页（双图库与破壁橱窗） | ② 图库专区（1320套二次元服饰） | ③ AI 虚拟试衣间（模特配置） |
| :---: | :---: | :---: |
| <img src="docs/preview-1-home.png" width="260" alt="拍片哥女装 发现首页" /> | <img src="docs/preview-2-anime.png" width="260" alt="二次元动漫服饰图库" /> | <img src="docs/preview-3-tryon.png" width="260" alt="AI 虚拟试衣间" /> |
| **精选推荐与双图库无缝切换**<br><sub>（二次元穿搭破壁橱窗、热门标签）</sub> | **1320套动漫服饰与风格筛选**<br><sub>（洛丽塔、JK制服、机能风一键过滤）</sub> | **真人/模特与二次元华服双向选择**<br><sub>（动漫插画级渲染专属引导横幅）</sub> |

| ④ 穿搭与生图知识库 | ⑤ 中英提示词词典（一键复制） | ⑥ AI 模特库（1499位商用人像） |
| :---: | :---: | :---: |
| <img src="docs/preview-4-knowledge-index.png" width="260" alt="穿搭与生图知识库" /> | <img src="docs/preview-5-prompt-lexicon.png" width="260" alt="中英提示词词典" /> | <img src="docs/preview-6-models.png" width="260" alt="1499位AI模特库" /> |
| **全方位穿搭与生图秘籍**<br><sub>（换装高成功率技巧、面料质感控制）</sub> | **图鉴级提示词与中英释义卡片**<br><sub>（轻触一键复制中英提示词至剪贴板）</sub> | **1499位免授权模特人像库**<br><sub>（支持短发/中发/长发发型多维挑选）</sub> |

### 💻 网页端界面预览

| 中文模式 | 英文模式 | 关键词搜索 |
|---|---|---|
| ![中文模式](docs/screenshot-zh.png) | ![英文模式](docs/screenshot-en.png) | ![关键词搜索](docs/screenshot-search.png) |

## 👗 AI 换装效果演示

系统支持上传真实人像与选中的服装，通过 AI 生图大模型进行衣物迁移换装，实现精准保留面容、贴合人体形态的虚拟试穿效果，全面支持**写实真人**与**二次元动漫**双重换装风格：

### 1. 写实真人版换装效果

| ① 选中的服装（图 1） | ② 上传的模特照片（图 2） | ③ AI 换装合成效果（图 3） |
|:---:|:---:|:---:|
| <img src="docs/tryon-1.png" width="280" alt="选中的服装" /> | <img src="docs/tryon-2.png" width="280" alt="上传的模特照片" /> | <img src="docs/tryon-3.png" width="280" alt="AI 换装合成效果" /> |
| **参考服装图**<br><sub>（写实图集精选女装）</sub> | **模特原图**<br><sub>（用户上传的人像日常照）</sub> | **AI 换装效果（图 1 + 图 2 ➔ 图 3）**<br><sub>（保留模特五官发型，自然融合服饰材质与剪裁）</sub> |

### 2. 二次元动漫版换装效果

| ① 选中的动漫服装（图 1） | ② 上传的模特照片（图 2） | ③ 二次元换装合成效果（图 3） |
|:---:|:---:|:---:|
| <img src="docs/dm1.png" width="280" alt="选中的二次元动漫服装" /> | <img src="docs/dm2.png" width="280" alt="上传的模特照片" /> | <img src="docs/dm3.png" width="280" alt="二次元动漫换装合成效果" /> |
| **动漫参考服装图**<br><sub>（动漫图集 1320 套精选二次元服饰）</sub> | **模特原图**<br><sub>（用户上传的真人模特人像照）</sub> | **动漫换装效果（图 1 + 图 2 ➔ 图 3）**<br><sub>（完美复刻真人神貌与身材特征，动漫插画级质感穿搭合成）</sub> |

## 🎬 兄弟项目联动：姿势参考 + 人物参考 → AI 生成结果

如果你不仅想为模特挑选服装，还希望**自由掌控人体的拍摄姿势、骨架动作与构图视角**，推荐搭配我的另一个开源项目一起使用：  
👉 **[拍片哥 · AI 姿势参考库与生图工坊 (AI Pose Gallery & Studio)](https://github.com/paipiange/ai-pose-gallery-zh)**

该项目收录了 **288 组 / 1439 张** AI 人体多视角姿势参考图（日文数据完整汉化），内置「拍片哥 AI 姿势生图与试穿工坊」，支持骨架动作锁定、真实面料试穿与面容复刻：

选择姿势骨架控制动作与构图，再上传人物/服装参考，即可生成同时保留目标姿势、人物面容与穿搭特征的完整图片：

| ① 姿势与构图参考 | ② 人物与服装参考 | ③ AI 融合生成结果 |
| :---: | :---: | :---: |
| <img src="docs/pose-studio-pose-reference.png" width="280" alt="输入的 AI 人体姿势骨架参考图" /> | <img src="docs/pose-studio-person-reference.png" width="280" alt="输入的人物面容与服装参考图" /> | <img src="docs/pose-studio-generated-result.png" width="280" alt="保持目标姿势并融合人物与服装特征的 AI 生成结果" /> |
| **锁定身体动作、视角与画面构图**<br><sub>（从 1439 张多角度姿势库中挑选骨架素体）</sub> | **提供面容、发型与服装特征**<br><sub>（结合本项目精选服装或上传的模特穿搭）</su