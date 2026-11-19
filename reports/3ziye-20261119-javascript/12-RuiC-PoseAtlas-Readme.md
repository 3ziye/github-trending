<div align="center">

<img src="og-cover.jpg" alt="RuiC-PoseAtlas — 人体姿态 + 衣装 + 人像参考图库" width="100%">

# RuiC-PoseAtlas

**三图鉴 · 三语参考库**<br>
**288 组人体姿态 / 1,439 张多角度人台线稿　　1,407 套无人衣装 / 8 个分类　　1,499 张 AI 人像 / 893 脸部 + 606 造型**

中文 · English · 日本語

<p>
  <a href="https://hruiccc.github.io/RuiC-PoseAtlas/"><strong>姿势图鉴 →</strong></a> ·
  <a href="https://hruiccc.github.io/RuiC-PoseAtlas/costume.html"><strong>衣装图鉴 →</strong></a> ·
  <a href="https://hruiccc.github.io/RuiC-PoseAtlas/face.html"><strong>人像图鉴 →</strong></a> ·
  <a href="https://github.com/HRuiCcc/RuiC-PoseAtlas">GitHub 仓库</a> ·
  <a href="https://github.com/HRuiCcc/RuiC-PoseAtlas/issues">问题反馈</a>
</p>

[![demo](https://img.shields.io/badge/demo-online-2ea44f?style=flat-square)](https://hruiccc.github.io/RuiC-PoseAtlas/)
![poses](https://img.shields.io/badge/poses-288-8fb4ff?style=flat-square)
![images](https://img.shields.io/badge/images-1%2C439-c3d5ff?style=flat-square)
![outfits](https://img.shields.io/badge/outfits-1%2C407-e3c8ff?style=flat-square)
![portraits](https://img.shields.io/badge/portraits-1%2C499-ffd7b0?style=flat-square)
![languages](https://img.shields.io/badge/languages-%E4%B8%AD%E6%96%87%20%7C%20EN%20%7C%20%E6%97%A5%E6%9C%AC%E8%AA%9E-c3d5ff?style=flat-square)
![dependencies](https://img.shields.io/badge/dependencies-0-2ea44f?style=flat-square)
![license](https://img.shields.io/badge/license-MIT%20%28code%29-blue?style=flat-square)
![ai](https://img.shields.io/badge/%E5%85%A8%E9%83%A8%E8%B5%84%E6%BA%90-AI%20%E7%94%9F%E6%88%90-A855F7?style=flat-square)

[界面预览](#界面预览) ·
[赞赏支持](#赞赏支持) ·
[在线体验](#在线体验) ·
[三个图鉴](#三个图鉴) ·
[项目亮点](#项目亮点) ·
[数据概览](#数据概览) ·
[快速开始](#快速开始) ·
[数据构建](#数据构建) ·
[部署](#部署) ·
[致谢与版权](#致谢与版权)

</div>

## ⚠️ 内容提示

> 本项目面向成年创作者，部分内容不适合未成年人。请遵守所在地法律法规与平台规范，未成年人请勿使用。

## 📥 夸克网盘 · AI 资源打包下载

<p>
  <a href="https://pan.quark.cn/s/d775c1471804?pwd=Ahcd">
    <img src="https://img.shields.io/badge/%E5%A4%B8%E5%85%8B%E7%BD%91%E7%9B%98-AI%20%E8%B5%84%E6%BA%90%E5%8C%85%20%C2%B7%20%E6%89%93%E5%8C%85%E4%B8%8B%E8%BD%BD-A855F7?style=for-the-badge" alt="夸克网盘 · AI 资源包打包下载" height="52">
  </a>
</p>

**链接**：<https://pan.quark.cn/s/d775c1471804?pwd=Ahcd> ｜ **提取码**：`Ahcd`（点上面的按钮会自动填入）

| AI 资源包 | 内容 |
| --- | --- |
| 🤖 **AI 作图姿势库.zip**（659 MB） | 姿势图鉴 · 288 组 / 1,439 张多角度参考图 |
| 🤖 **AI 服装库.zip**（1.38 GB） | 衣装图鉴 · 1,407 套无人衣装 |
| 🤖 **AI 作图脸库.zip**（4.86 GB） | 人像图鉴 · 1,499 张虚构人像 |

> **AI 生成声明**：以上三个资源包，以及本项目收录的全部姿势、衣装与人像图像，均为 **AI 生成的虚构参考素材**，不含真实人物照片；请勿用于冒充真人、虚假信息或任何违规用途。

---

## 项目简介

**RuiC-PoseAtlas** 是一个完全静态、零依赖的三图鉴参考站，把「人体怎么摆」「衣服怎么穿」「脸长什么样」三件事放在同一个站点里：

- **姿势图鉴**：288 组 AI 生成的去脸人台姿势，每组提供 **正面、斜侧、侧面、俯视、仰视** 五个视角，共 1,439 张参考图。以「姿态」为单位组织，同一组的五个角度收进一张卡片，打开大图后可以用方向键连续切换，体态、比例、镜头关系一眼可比。
- **衣装图鉴**：1,407 套 AI 生成的**没有人体**的整身穿搭，按 春 / 夏 / 秋 / 冬 / 内衣 / 派对 / 泳装 / 性感 八个分类归档，每套都拆成了可检索的单品标签——颜色、材质、版型、鞋包配饰。因为它本来就没有画人，直接套到你已有的角色上即可，不需要抠图。
- **人像图鉴**：1,499 张 AI 生成的虚构人像，分为「脸部」893 张与「造型」606 张，按短发 / 中发 / 中长发 / 长发四种发型筛选。脸部是正面朝向、纯背景的脸部参考，适合固定角色脸；造型带服装、发丝质感与整体氛围，适合扩展角色设定。

三者合起来的用法很直接：**姿势定骨架，衣装定皮相，人像定脸。** 先在姿势图鉴里挑一个机位和体态，再去衣装图鉴里找一套同气质的搭配，最后从人像图鉴里选一张脸作为角色参考，三份参考一起丢进生图工具。

很多参考图库的问题是：图片分散、视角不统一、难以把同一姿态的不同角度放在一起比较，服装更是只有一张成品图、说不清到底穿了什么。这个项目以「姿态」「衣装」和「人像」为单位重新组织了三批数据，并为衣装补上了中英日三语标签，让检索这件事真正可用。

同时，它也是一个可以独立部署的前端作品：**纯 HTML + CSS + ES Modules**，没有框架、没有打包器、没有运行时依赖。克隆下来用一个静态服务器打开即可；需要部署时，直接交给 GitHub Pages、Cloudflare Pages、Netlify 或任意静态托管即可。

## 界面预览

### 姿势图鉴

<p align="center">
  <img src="docs/preview-gallery.jpg" alt="姿势图鉴网格" width="100%">
</p>

<p align="center">
  <img src="docs/preview-modal.jpg" alt="姿势大图与多角度切换" width="72%">
  <img src="docs/preview-mobile.jpg" alt="姿势移动端大图" width="24%">
</p>

### 衣装图鉴

<p align="center">
  <img src="docs/preview-costume-gallery.jpg" alt="衣装图鉴网格" width="100%">
</p>

<p align="center">
  <img src="docs/preview-costume-modal.jpg" alt="衣装大图与单品标签" width="72%">
  <img src="docs/preview-costume-mobile.jpg" alt="衣装移动端大图" width="24%">
</p>

### 人像图鉴

<p align="center">
  <img src="docs/preview-face-gallery.jpg" alt="人像图鉴网格" width="100%">
</p>

<p align="center">
  <img src="docs/preview-face-modal.jpg" alt="人像大图与发型信息" width="72%">
  <img src="docs/preview-face-mobile.jpg" alt="人像移动端大图" width="24%">
</p>

---

## 赞赏支持

如果这个项目对你有帮助，欢迎微信扫码赞赏，支持后续的整理与维护。

<p align="center">
  <img src="docs/wechat-donate.png" width="280" alt="微信赞赏码">
</p>

<p align="center"><sub>微信扫码赞赏 · 感谢支持</sub></p>

<p align="center">微号：<strong>hrc_rch</strong>（说明来意）</p>

如果暂时不方便赞赏，点一个 **Star ⭐** 或把项目分享给需要姿态 / 衣装参考的朋友，也是很大的支持。

---

## 在线体验

> **姿势图鉴：https://hruiccc.github.io/RuiC-PoseAtlas/**
> **衣装图鉴：https://hruiccc.github.io/RuiC-PoseAtlas/costume.html**
> **人像图鉴：https://hruiccc.github.io/RuiC-PoseAtlas/face.html**

三个页面顶部都有切换器，来回跳转不会丢语言设置；都支持 `?lang=zh|en|ja` 与条目深链接。

### 这个项目适合谁

- **AI 绘画创作者**：姿势定构图，衣装定造型，两份参考可以分开用也可以一起用。
- **3D 建模 / 动画学习者**：快速查看体块关系、比例、四肢走向与机位变化。
- **插画与漫画作者**：寻找动态、透视与多人互动的构图灵感，顺手解决「这身衣服怎么画」。
- **换装 / 角色设定**：无人体的衣装图可以直接贴到已有角色上，省掉一次抠图。
- **摄影与视觉设计**：参考站位、镜头高度、服装搭配与配色。
- **前端学习者**：一个无框架、数据驱动、三语 i18n、三套数据集共用一套设计系统的完整静态项目范例。

---

## 三个图鉴

| | 姿势