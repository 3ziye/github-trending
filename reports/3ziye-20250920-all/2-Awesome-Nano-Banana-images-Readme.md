<div align="center">

<img src="images/logo.jpg"  alt="输入图片"> 

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE) 
[![简体中文](https://img.shields.io/badge/简体中文-点击查看-orange)](README.md)
[![English](https://img.shields.io/badge/English-Click_to_View-yellow)](README_en.md)
[![Japanese](https://img.shields.io/badge/日本語-クリックして表示-green)](README_ja.md)
[![Korean](https://img.shields.io/badge/한국어-눌러서_보기-blue)](README_kr.md)
[![Turkish](https://img.shields.io/badge/Türkçe-Görüntülemek_için_Tıklayın-red)](README_tr.md)

</div>

> [!NOTE]
> 我们提出 Nano-consistent-150k——首个基于 Nano-Banana 构建、规模超过 150k 的高质量数据集，专为在多样而复杂的编辑场景中保持人物身份一致性而设计。其一大特点是卓越的身份一致性：针对同一人像，我们在多种任务与指令下提供了 35 种以上不同的编辑结果。以一致的人物身份为锚点，该数据集使得围绕同一主体在多种编辑任务、指令与模态之间无缝衔接的交错（interleaved）数据构建成为可能。
<a href='https://picotrex.github.io/Awesome-Nano-Banana-images/'><img src='https://img.shields.io/badge/🌐 Website-Blog-orange' height="25"></a>
<a href='https://huggingface.co/datasets/Yejy53/Nano-consistent-150k'><img src='https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow' height="25"></a>

## 🍌 Introduction

欢迎来到 Nano-banana 精选图片库！🤗 

**我们收集了Nano-banana在各个任务场景下生成的令人惊艳的图片和提示词**，全方位展示Google在图像生成与编辑的无限可能。希望能帮助你更好地了解Nano-banana。快一起解锁 Nano-banana 的多图融合与创意编辑力量吧！✨

这些案例主要来源于Twitter/ X 🐦、小红书📕等自媒体平台。

喜欢就点 ⭐ Star 收藏起来吧！

## 📰 News

- **2025年9月18日：** 我们发布了 [**Nano-consistent-150k**](https://picotrex.github.io/Awesome-Nano-Banana-images/) 数据集
- **2025年9月16日：** 4️⃣ 第四次仓库更新
- **2025年9月9日：** 3️⃣ 第三次仓库更新
- **2025年9月3日：** 2️⃣ 第二次仓库更新
- **2025年8月28日：** 🎉 1️⃣ ${\color{red} 第一次\ Awesome-Nano-Banana-images \ 更新!}$

## 📑 Menu

- [🍌 Introduction](#-introduction)
- [📰 News](#-news)
- [📑 Menu](#-menu)
- [🖼️ 例子](#️-例子)
  - [例 1: 插画变手办（by @ZHO\_ZHO\_ZHO）](#例-1-插画变手办by-zho_zho_zho)
  - [例 2: 根据地图箭头生成地面视角图片（by @tokumin）](#例-2-根据地图箭头生成地面视角图片by-tokumin)
  - [例 3: 真实世界的AR信息化（by @bilawalsidhu）](#例-3-真实世界的ar信息化by-bilawalsidhu)
  - [例 4: 分离出3D建筑/制作等距模型（by @Zieeett）](#例-4-分离出3d建筑制作等距模型by-zieeett)
  - [例 5: 不同时代自己的照片（by @AmirMushich）](#例-5-不同时代自己的照片by-amirmushich)
  - [例 6: 多参考图像生成（by @MrDavids1）](#例-6-多参考图像生成by-mrdavids1)
  - [例 7: 自动修图（by @op7418）](#例-7-自动修图by-op7418)
  - [例 8: 手绘图控制多角色姿态（by @op7418）](#例-8-手绘图控制多角色姿态by-op7418)
  - [例 9: 跨视角图像生成（by @op7418）](#例-9-跨视角图像生成by-op7418)
  - [例 10: 定制人物贴纸（by @op7418）](#例-10-定制人物贴纸by-op7418)
  - [例 11: 动漫转真人Coser（by @ZHO\_ZHO\_ZHO）](#例-11-动漫转真人coserby-zho_zho_zho)
  - [例 12: 生成角色设定（by @ZHO\_ZHO\_ZHO）](#例-12-生成角色设定by-zho_zho_zho)
  - [例 13: 色卡线稿上色（by @ZHO\_ZHO\_ZHO）](#例-13-色卡线稿上色by-zho_zho_zho)
  - [例 14: 文章信息图（by @黄建同学）](#例-14-文章信息图by-黄建同学)
  - [例 15: 更换多种发型（by @balconychy）](#例-15-更换多种发型by-balconychy)
  - [例 16: 模型标注讲解图（by @berryxia\_ai）](#例-16-模型标注讲解图by-berryxia_ai)
  - [例 17: 定制大理石雕塑（by @umesh\_ai）](#例-17-定制大理石雕塑by-umesh_ai)
  - [例 18: 根据食材做菜（by @Gdgtify）](#例-18-根据食材做菜by-gdgtify)
  - [例 19: 数学题推理（by @Gorden Sun）](#例-19-数学题推理by-gorden-sun)
  - [例 20: 旧照片上色（by @GeminiApp）](#例-20-旧照片上色by-geminiapp)
  - [例 21: OOTD穿搭（by @302.AI）](#例-21-ootd穿搭by-302ai)
  - [例 22: 人物换衣（by @skirano）](#例-22-人物换衣by-skirano)
  - [例 23: 多视图结果生成（by @Error\_HTTP\_404）](#例-23-多视图结果生成by-error_http_404)
  - [例 24: 电影分镜（by @GeminiApp）](#例-24-电影分镜by-geminiapp)
  - [例 25: 人物姿势修改（by @arrakis\_ai）](#例-25-人物姿势修改by-arrakis_ai)
  - [例 26: 线稿图生成图像（by @ZHO\_ZHO\_ZHO）](#例-26-线稿图生成图像by-zho_zho_zho)
  - [例 27: 为图像添加水印（by @AiMachete）](#例-27-为图像添加水印by-aimachete)
  - [例 28: 知识推理生成图像（by @icreatelife）](#例-28-知识推理生成图像by-icreatelife)
  - [例 29: 红笔批注（by @AiMachete）](#例-29-红笔批注by-aimachete)
  - [例 30: 爆炸的食物（by @icreatelife）](#例-30-爆炸的食物by-icreatelife)
  - [例 31: 制作漫画书（by @icreatelife）](#例-31-制作漫画书by-icreatelife)
  - [例 32: 动作人偶（by @icreatelife）](#例-32-动作人偶by-icreatelife)
  - [例 33: 地图生成等距建筑（by @demishassabis）](#例-33-地图生成等距建筑by-demishassabis)
  - [例 34: 参考图控制人物表情（by @ZHO\_ZHO\_ZHO）](#例-34-参考图控制人物表情by-zho_zho_zho)
  - [例 35: 插画绘画过程四格（by @ZHO\_ZHO\_ZHO）](#例-35-插画绘画过程四格by-zho_zho_zho)
  - [例 36: 虚拟试妆（by @ZHO\_ZHO\_ZHO）](#例-36-虚拟试妆by-zho_zho_zho)
  - [例 37: 妆面分析（by @ZHO\_ZHO\_ZHO）](#例-37-妆面分析by-zho_zho_zho)
  - [例 38: Google地图视角下的中土世界（by @TechHallo）](#例-38-google地图视角下的中土世界by-techhallo)
  - [例 39: 印刷插画生成（by @Umesh）](#例-39-印刷插画生成by-umesh)
  - [例 40: 超多人物姿势生成（by @tapehead\_Lab）](#例-40-超多人物姿势生成by-tapehead_lab)
  - [例 41: 物品包装生成（by @ZHO\_ZHO\_ZHO）](#例-41-物品包装生成by-zho_zho_zho)
  - [例 42: 叠加滤镜/材质（by @ZHO\_ZHO\_ZHO）](#例-42-叠加滤镜材质by-zho_zho_zho)
  - [例 43: 控制人物脸型（by @ZHO\_ZHO\_ZHO）](#例-43-控制人物脸型by-zho_zho_zho)
  - [例 44: 光影控制（by @ZHO\_ZHO\_ZHO）](#例-44-光影控制by-zho_zho_zho)
  - [例 45: 乐高玩具小人（by @ZHO\_ZHO\_ZHO）](#例-45-乐高玩具小人by-zho_zho_zho)
  - [例 46: 高达模型小人（by @ZHO\_ZHO\_ZHO）](#例-46-高达模型小人by-zho_zho_zho)
  - [例 47: 硬件拆解图（by @AIimagined）](#例-47-硬件拆解图by-aiimagined)
  - [例 48: 食物卡路里标注（by @icreatelife）](#例-48-食物卡路里标注by-icreatelife)
  - [例 49: 提取信息并放置透明图层（by @nglprz）](#例-49-提取信息并放置透明图层by-nglprz)
  - [例 50: 图像外扩修复（by @bwabbage）](#例-50-图像外扩修复by-bwabbage)
  - [例 51: 古老地图生成古代场景（by @levelsio）](#例-51-古老地图生成古代场景by-levelsio)
  - [例 52: 时尚服装拼贴画（by @tetumemo）](#例-52-时尚服装拼贴画by-tetume