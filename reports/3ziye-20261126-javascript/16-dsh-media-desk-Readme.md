<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/hero-zh-dark.webp">
    <img src="docs/assets/hero-zh-light.webp" alt="自媒体工作台：DSH 上最爽的创作工作台" width="100%">
  </picture>
</p>

<h1 align="center">自媒体工作台</h1>

<p align="center"><b>DeepSeek Harness 的一个插件。记一句灵感，一键做出脚本、封面、配图和分镜。</b></p>

<p align="center">由小红书科技博主 <a href="https://www.xiaohongshu.com/user/profile/5faedce8000000000101c8a3"><b>蜗牛的科技笔记</b></a> 开发，一个每天要发内容的人，给自己做的工作台。</p>

<p align="center">
  <a href="https://bozhufarm.com/dsh/"><b>介绍页和安装方法</b></a> ·
  <a href="#三步上手">安装</a> ·
  <a href="#要花钱吗">要花钱吗</a> ·
  <a href="#问答">问答</a> ·
  <a href="README.en.md">English</a>
</p>

<p align="center">
  <img alt="DeepSeek Harness 0.2.x" src="https://img.shields.io/badge/DeepSeek%20Harness-0.2.x-111?style=flat-square">
  <img alt="Mac 桌面版与网页版" src="https://img.shields.io/badge/Mac%20%E6%A1%8C%E9%9D%A2%E7%89%88-%E7%BD%91%E9%A1%B5%E7%89%88-111?style=flat-square">
  <a href="LICENSE"><img alt="MIT" src="https://img.shields.io/badge/MIT-%E5%BC%80%E6%BA%90-111?style=flat-square"></a>
  <a href="https://github.com/woniuniuniu/dsh-media-desk/stargazers"><img alt="Star" src="https://img.shields.io/github/stars/woniuniuniu/dsh-media-desk?style=flat-square&color=111&label=Star"></a>
</p>

<br>

<table>
<tr>
<td width="24%" align="center">
  <a href="https://bozhufarm.com"><img src="docs/assets/bozhufarm-woo.webp" width="100%" alt="博主农场的农民蜗"></a>
</td>
<td valign="top">
<h3>想用满血版？来博主农场</h3>
<p>这个插件目前还是实验项目，是跟着 DeepSeek Harness 的生态做的。</p>
<p>如果你想体验更多不同的模型，用原汁原味的满血版，可以来 <a href="https://bozhufarm.com"><b>博主农场</b></a>。写内容的模型已经帮你配好，生图模型也配好了，封面一键就能画。不用自己找密钥、配接口，打开就能做内容。</p>
<p><a href="https://bozhufarm.com"><b>打开 bozhufarm.com →</b></a></p>
</td>
</tr>
</table>

<br>

## 它是什么

装在 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 侧栏里的一个页面。打开是一面灵感墙，一句话记一个灵感；点开任何一条，一键生成口播脚本、标题、视频封面、配图和黑白线稿分镜；左边聊一句，右边就改。做好的稿子拖到日历上排期，发布之后回来看数据。

五个页面：**灵感 · 内容 · 排期 · 复盘 · 风格**。界面有中文和英文，默认跟随 DeepSeek Harness 的语言，也可以在插件设置里固定；切到英文后，脚本、标题和分镜也用英文写。网页版在手机浏览器里也能打开。

除了小红书、抖音、B 站、公众号，也支持 TikTok、Instagram、YouTube 和 X，发海外也能用。

<br>

## 一键成稿

<table>
<tr>
<td width="62%">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/f-studio-dark.webp">
    <img src="docs/assets/f-studio-light.webp" width="100%" alt="成稿工作区：左边对话，右边是标题、封面、脚本和六格分镜">
  </picture>
</td>
<td valign="top">
<p><b>整页一起长出来。</b></p>
<p>点开灵感，稿面的格子一开始就排好了。标题、脚本、视频封面、配图和六格分镜同时生成，一边生成一边填满。</p>
<p><b>脚本还是文章，你来选。</b></p>
<p>脚本一句话一行、一段一段，照着念就行；文章按自然段写，可以直接发。两种都带大标题，也都会贴着你选的风格和参考内容来写。</p>
<p><b>说一句，就改。</b></p>
<p>「表达再直接一点」「第 3 镜换成俯拍」「封面字更有冲击力」，右边实时更新，每一步都能撤销。</p>
<p><b>拿走就能用。</b></p>
<p>脚本直接编辑、一键复制；或者连封面、配图和分镜图一起，保存成一个文件夹。</p>
</td>
</tr>
</table>

<br>

## 灵感墙

<table>
<tr>
<td valign="top" width="38%">
<p><b>一句话，一个灵感。</b></p>
<p>文字、链接、图片、视频、金句，贴进来就是一张卡片。散落在无限画布上，或者切成按时间排的信息流。</p>
<p><b>相关的灵感自己凑过来。</b></p>
<p>在中间输入「agent」回车，新灵感记下的同时，以前提到 agent 的灵感会按相关程度挪到它旁边，一眼看全。</p>
<p><b>右边有个助手。</b></p>
<p>「把今天最好的灵感一键成稿」「接下来有什么排期」「以后标题都不要超过 20 个字」，一句话就办。</p>
</td>
<td>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/f-home-dark.webp">
    <img src="docs/assets/f-home-light.webp" width="100%" alt="灵感墙的散落视图和信息流视图">
  </picture>
</td>
</tr>
</table>

<br>

## 排期

<table>
<tr>
<td width="62%">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/f-schedule-dark.webp">
    <img src="docs/assets/f-schedule-light.webp" width="100%" alt="排期日历，右边是下一条和待排期的内容">
  </picture>
</td>
<td valign="top">
<p><b>一张日历，两件事。</b></p>
<p>每天一张灵感邮票，记录你的连续天数；做好的稿子从右边拖到某一天，就排好了。</p>
<p>右上角永远是下一条要发的。</p>
</td>
</tr>
</table>

<br>

## 复盘

<table>
<tr>
<td valign="top" width="38%">
<p><b>数据进来，规则出去。</b></p>
<p>手动录入、粘贴 CSV，或者导入你自己的账号。趋势、平台分布、表现最好的内容，一眼看完。</p>
<p>从数据里提炼出来的建议，点一下就写进写作规则，以后每篇都遵守。规则还能导出成 DeepSeek Harness 的 Skill。</p>
</td>
<td>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/f-insights-dark.webp">
    <img src="docs/assets/f-insights-light.webp" width="100%" alt="复盘页：一句话总结、每日播放、平台分布、最好的内容和建议">
  </picture>
</td>
</tr>
</table>

<br>

## 风格

<table>
<tr>
<td width="62%">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/f-style-dark.webp">
    <img src="docs/assets/f-style-light.webp" width="100%" alt="风格页的分板块预设，和内容管理看板">
  </picture>
</td>
<td valign="top">
<p><b>按谁的风格写，你定。</b></p>
<p>科技数码、旅行探店、Vlog 生活、观点认知、干货教程、种草测评、情感故事、热点资讯，8 个板块 15 种博主预设，选一种就能开写。</p>
<p><b>也可以是你自己的。</b></p>
<p>导入自己的账号，或者贴几篇写过的稿子，提炼成专属风格卡，随时改。</p>
<p>内容页把所有稿子按灵感、成稿、待发布、已发布排好。</p>
</td>
</tr>
</table>

<br>

## 三步上手

要求 DeepSeek Harness `0.2.1-rc.5` 及以上的 `0.2.x`，已在 `0.2.2-rc.1` 的桌面版和网页版上测过。

**1. 安装。** 打开 DeepSeek Harness 侧栏的「插件」，先打开实验性的索引功能：DSH `0.2.2` 及以上在「实验性插件」下启用「自定义插件索引」；`0.2.1` 系列里它叫「自定义插件市场」，在「实验性插件」旁的「更多」里。打开后页面会多出「已安装」和「发现」两个标签。

切到「发现」，添加这条索引地址（加一次就够）：

```
https://raw.githubusercontent.com/woniuniuniu/dsh-media-desk/main/index.json
```

GitHub 直连不通时，换成这个 CDN 镜像，代价是它最多可能比最新发布晚 12 小时：

``