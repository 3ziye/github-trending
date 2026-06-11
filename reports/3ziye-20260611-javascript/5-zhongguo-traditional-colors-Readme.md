# 中国传统配色

简体中文 | [English](README.en.md) | [日本語](README.ja.md)

如果你在做设计、写内容、做课件、搭建网页主题，常常需要一套稳妥、好看、能直接使用的中国色参考，这个仓库就是为这件事整理的。

这里收录 742 张中华传统色高清色卡，已按原始 742 色清单完整覆盖。每张色卡包含色名、HEX、RGB、CMYK、配色推荐和气质关键词。你可以在线浏览，也可以直接下载已经打包好的 ZIP，把它当作自己的传统色素材库。

## 快速入口

- [在线浏览色卡](https://nevertoday.github.io/zhongguo-traditional-colors/)
- [中国色配色猎场](https://nevertoday.github.io/zhongguo-traditional-colors/palettes.html)
- [直接下载完整 ZIP](https://github.com/nevertoday/zhongguo-traditional-colors/releases/latest/download/zhongguo-traditional-colors-images.zip)
- [查看 Release](https://github.com/nevertoday/zhongguo-traditional-colors/releases/tag/v0.1.0)
- [原始 742 色清单](docs/chinese-color-master-list.md)
- [742 色配色方案 Markdown](docs/chinese-color-harmony.md)
- [742 色配色关系 CSV](docs/chinese-color-harmony.csv)
- [中国传统色实战 Skills](#中国传统色实战-skills)
- [作者 X 主页](https://x.com/xiaoxiaodong01)

## 这个项目能帮你什么

| 你需要 | 这里提供 |
| --- | --- |
| 快速找中国色参考 | 742 张高清 PNG 色卡 |
| 做设计和内容配图 | 可直接点击下载原图 |
| 搭建色彩资料库 | 文件名与 742 色清单一一对应 |
| 做网页、PPT、海报、课程素材 | README 全量预览，ZIP 一次下载 |
| 校对色名和色值 | 色名、HEX、RGB、CMYK 集中整理 |
| 把传统色真正用进项目 | 10 个面向设计实战的 Agent Skills |

原图约 998 MB。ZIP 文件作为 GitHub Release 附件提供，不直接提交进仓库。

## 中国传统色实战 Skills

这些 skill 不是继续解释色彩理论，而是把 742 色清单和配色关系 CSV 转成设计师能直接使用的工作流。每个 skill 都对应一个真实工作阻塞点：方向太虚、色板太多、落位困难、Token 交付、可读性、品牌治理、图表编码、旧稿迁移、系列内容和印刷生产。

每个 `xxd-*` skill 目录都随包包含完整 `references/chinese-color-master-list.md`、`references/chinese-color-harmony.md` 和 `references/chinese-color-harmony.csv`，单独取用某个 skill 时也能访问完整 742 色清单和每个颜色的配色关系。

| Skill | 适合解决的问题 |
| --- | --- |
| [`xxd-color-brief`](skills/xxd-color-brief/SKILL.md) | 把“高级、东方、年轻、克制”这类模糊方向翻译成冷暖、明度、饱和度、对比和避坑约束 |
| [`xxd-palette-builder`](skills/xxd-palette-builder/SKILL.md) | 从锚点色、HEX、情绪或场景中筛出少量可执行 palette，并分配主辅点缀和比例 |
| [`xxd-palette-applier`](skills/xxd-palette-applier/SKILL.md) | 把一组颜色落到真实版面，决定背景、标题、正文、CTA、结构和装饰的位置 |
| [`xxd-ui-token`](skills/xxd-ui-token/SKILL.md) | 把传统色变成 primitive、semantic、component、mode 四层 UI token 和代码输出 |
| [`xxd-accessible-color`](skills/xxd-accessible-color/SKILL.md) | 用 WCAG ratio 检查文字、按钮、状态和图表，并用同库颜色修复失败组合 |
| [`xxd-brand-system`](skills/xxd-brand-system/SKILL.md) | 为长期品牌建立锚点色、支撑色、比例、渠道规则、禁用组合和治理边界 |
| [`xxd-data-viz`](skills/xxd-data-viz/SKILL.md) | 按分类、顺序、发散、高亮或语义状态生成图表色，而不是套海报色板 |
| [`xxd-existing-design-audit`](skills/xxd-existing-design-audit/SKILL.md) | 盘点旧稿、CSS、Figma styles 或 HEX 清单，判断保留、合并、替换或移除 |
| [`xxd-content-series`](skills/xxd-content-series/SKILL.md) | 为小红书、公众号、视频、课程和栏目建立固定层、变量层、模板层和轮换规则 |
| [`xxd-print-packaging`](skills/xxd-print-packaging/SKILL.md) | 面向包装、书籍、文创、标签和实体材质规划用色，并提示 CMYK、材质和打样风险 |

### 怎么选择这些 Skills

如果你还没有确定方向，先用 `xxd-color-brief`。如果已经有一个主色或一组候选色，用 `xxd-palette-builder` 收敛成色板，再用 `xxd-palette-applier` 放到真实版面。要交给开发、团队或生产环节时，再进入 `xxd-ui-token`、`xxd-brand-system`、`xxd-data-viz` 或 `xxd-print-packaging`。如果你手上是旧稿、旧 CSS 或散乱 HEX，先用 `xxd-existing-design-audit` 做盘点。长期内容矩阵则从 `xxd-content-series` 开始。

下面是每个 skill 的详细使用方案。每一项都按“它帮谁、解决什么、你要输入什么、会得到什么、怎么触发”来写，方便直接复制到自己的项目里改。

<details>
<summary><strong><code>xxd-color-brief</code>：把模糊审美词变成配色方向</strong></summary>

**利他价值**：帮客户、设计师和执行者先对齐判断语言，减少“我觉得不高级”“这个不够东方”这类主观拉扯。

**适合谁用**：项目刚启动的设计师、品牌负责人、内容团队、课程或活动视觉负责人。

**典型场景**：只有 moodboard、参考图、品牌关键词或客户口头反馈，还不适合直接选色。

**输入什么**：项目载体、目标人群、希望传递的气质、必须避开的感觉、已有参考图或竞品。

**得到什么**：冷暖、明度、饱和度、对比强度、风险边界、3 到 5 个起始传统色，以及下一步推荐使用的 skill。

**使用方式**：先让它输出方向简报，再把简报里的锚点色交给 `xxd-palette-builder` 生成具体色板。

示例触发：

<pre><code>/xxd-color-brief 为新中式茶饮品牌做年轻但不俗的配色方向，受众是 20-35 岁女性，避免廉价国潮感</code></pre>

[查看完整 Skill](skills/xxd-color-brief/SKILL.md)

</details>

<details>
<summary><strong><code>xxd-palette-builder</code>：从 742 色里筛出可执行色板</strong></summary>

**利他价值**：把选择困难变成少量可比较方案，让团队不用在几百个颜色里反复试错。

**适合谁用**：已经有锚点色、品牌关键词、HEX 清单、参考图或初步视觉方向的人。

**典型场景**：要做官网、封面、PPT、海报、包装或 UI，但不知道主色、辅色、点缀色怎么分配。

**输入什么**：锚点色或色名、用途、希望稳妥还是更有记忆点、浅色/深色偏好、禁用色或品牌限制。

**得到什么**：主色、辅色、背景色、强调色、推荐比例、替代方案、使用风险和可继续落版的色板。

**使用方式**：先选一个方向最明确的锚点色；如果没有锚点色，先用 `xxd-color-brief`。拿到色板后，用 `xxd-palette-applier` 判断具体放在哪里。

示例触发：

<pre><code>/xxd-palette-builder 以月白为锚点，为文化类网站首页生成主辅点缀色板，要求安静、有层次、适合长文阅读</code></pre>

[查看完整 Skill](skills/xxd-palette-builder/SKILL.md)

</details>

<details>
<summary><strong><code>xxd-palette-applier</code>：把色板放进真实版面</strong></summary>

**利他价值**：让颜色服务信息层级和阅读路径，而不是让所有颜色同时争抢注意力。

**适合谁用**：已经有色板，但不知道背景、标题、正文、按钮、边框、装饰分别用什么颜色的人。

**典型场景**：网页首屏、PPT 封面、课程详情页、文章长图、包装正反面或社媒模板。

**输入什么**：已有色板、页面结构、主要信息层级、用户最应该先看到什么、哪些区域需要克制。

**得到什么**：背景/内容/行动/结构/细节五类角色、面积比例、版面落点、错误用法和替代建议。

**使用方式**：先把色板中的每个颜色分配角色，再按面积比例落版；如果最后要交给开发，继续用 `xxd-ui-token`。

示例触发：

<pre><code>/xxd-palette-applier 把月白、黛蓝、绛紫、银朱这组传统色用到课程封面和详情页首屏，重点突出报名按钮</code></pre>

[查看完整 Skill](skills/xxd-palette-applier/SKILL.md)

</details>

<details>
<summary><strong><code>xxd-ui-token</code>：把传统色变成开发能接的 UI Token</strong></summary>

**利他价值**：让设计、开发和后续维护共用同一套命名规则，减少硬编码、返工和深色模式混乱。

**适合谁用**：做网站、App、后台、工具、设计系统、Figma variables 或 Tailwind 主题的人。

**典型场景**：设计稿已经定色，但开发需要 CSS variables、Tailwind config、Figma token 或浅深色模式规则。

**输入什么**：产品类型、已有色板、组件类型、浅色/深色模式要求、输出格式、需要保留的品牌色。

**得到什么**：primit