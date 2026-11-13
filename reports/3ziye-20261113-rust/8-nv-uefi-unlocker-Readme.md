# nv-uefi-unlocker 之 老黄刀法回退器   · [常见问题 FAQ](docs/faq.md)

## UPDATE:2026/11/12 UTC+8 不是哥们，怎么给老黄职位也回退了？？！！

[中文](README.md) | [English](README.en.md)

**你的 GeForce 正以半速跑 AI——这个工具在驱动加载前把它修复。**

## **[“震惊！老黄刀法还能被回退？？？”](https://physicsdolphin.github.io/nv-uefi-unlocker/tools/tflops-ceiling.html)**

[![version](https://img.shields.io/badge/version-2.1.10-brightgreen)](https://github.com/physicsdolphin/nv-uefi-unlocker/releases/latest)
[![GeForce](https://img.shields.io/badge/GeForce-GTX%2016%20%7C%20RTX%2020%2F30%2F40-green)](docs/compatibility.md)
[![platform](https://img.shields.io/badge/platform-UEFI%20%E9%A2%84%E9%A9%B1%E5%8A%A8%20%7C%20Win%20%2F%20Linux%20%2F%20Hackintosh-blue)](docs/faq.md)
[![license](https://img.shields.io/badge/license-GPL--2.0-blue)](LICENSE)
[![stars](https://img.shields.io/github/stars/physicsdolphin/nv-uefi-unlocker?label=stars&color=yellow)](https://github.com/physicsdolphin/nv-uefi-unlocker/stargazers)

## GTX 16 + RTX 20 + RTX 30 + RTX 40 系列通用的 UEFI 预驱动 NVIDIA GPU 解锁工具 ##

解开 NVIDIA 显卡的 Tensor 计算性能限制。从 U 盘启动，解锁后自动进入 Windows 或 Linux 或任意操作系统，无需刷写 VBIOS；断电后恢复原状。

**先看 → [常见问题](docs/faq.md)**（USB 文件放置 / 回锁与睡眠 / 雷电与 eGPU / Secure Boot / 安全约束——绝大多数操作问题已有答案；背景概念见 [什么是 UEFI / DXE / 链式引导](docs/faq.md#uefi-primer)）

[观看项目宣传片 ↗](https://www.bilibili.com/video/BV1d6xN66ECM/)
[官方视频：工具概览 ↗](https://www.youtube.com/watch?v=y11Pluqoqhg) · [完整实操走录 ↗](https://www.youtube.com/watch?v=hrw1KBTM1EQ)

**实测 FP16 / BF16 / TF32 张量吞吐最高约 2.6× · FP8 最高约 1.9× · 图像 / 视频生成 +14–75% · DirectML 推理算子最高 +94% · LLM 推理 prefill 最高 +19%（decode +5%）· 无 VBIOS 刷写，断电即复原**（逐卡数据见[兼容性矩阵](docs/compatibility.md)；增益受功耗墙与精度路径制约——LLM 行为双卡 MoE 实测，非微基准外推）

[![理论解锁上限天梯图](docs/tools/tflops-ceiling.svg)](https://physicsdolphin.github.io/nv-uefi-unlocker/tools/tflops-ceiling.html)

*理论解锁上限天梯图（FP16 · 桌面卡）——[打开可交互版](https://physicsdolphin.github.io/nv-uefi-unlocker/tools/tflops-ceiling.html)：FP32/TF32/FP16/BF16/FP8 五个精度页签、含 GTX 9 – RTX 50 桌面/笔记本/专业卡/移动工作站/矿卡/数据中心全量、可切换显示出厂现值；[`?k=fp8`](https://physicsdolphin.github.io/nv-uefi-unlocker/tools/tflops-ceiling.html?k=fp8) 直达指定精度。理论标尺与上方实测数字口径不同，见[理论提升分析](docs/theoretical-uplift.md)。*

## 兼容性速览

| 系列 | 支持情况 |
| --- | --- |
| GTX 16 · Turing | 理论兼容，欢迎实机验证 |
| RTX 20 · Turing | 全系兼容；部分型号有已知问题，见完整矩阵 |
| RTX 30 · Ampere GA10x | 全系兼容，支持笔记本与台式 |
| RTX 40 · Ada | 全系兼容，支持笔记本与台式 |
| Pascal 及更早 / GA100 / RTX 50 | 不支持 |

## 社区成功反馈与复现

以下 **硬件型号 / 形态分组** 用于大家直观查找自己的卡名字有没有成功先例（因为你第一时间可能不知道里面的pci id或者芯片代号!!!）
来源自[视频评论区](https://www.bilibili.com/video/BV1d6xN66ECM/)，部分选自[社区验证汇总](docs/community-reports.md)；评论区部分是观众报告，因为他们可能受相关限制无法访问github，我们帮助收集了他们的结果分享。同一型号多条报告时取信息量最大的一条。现行支持与已知限制仍以全量[兼容性矩阵](docs/compatibility.md)为准。

表中分别注明前后实测、只有解锁后截图和文字自述。基准算力增幅不等于实际应用增幅；同时超频或改变功耗条件的报告单独标注。

| 硬件型号 / 形态 | 社区报告的结果与条件 | 来源 |
| --- | --- | --- |
| RTX 2050 Laptop 4GB | EFI 全链通过且 Windows ssdiag 判 UNLOCKED（PLM 全开、SS 覆盖值在效）；初步 PyTorch 峰值 FP16 25.13 / BF16 25.33 TFLOPS，尚无严格锁定态 A/B | [#142](https://github.com/physicsdolphin/nv-uefi-unlocker/issues/142) |
| RTX 3050 Laptop 6GB（MUXless） | GA107 家族第二个 in-OS 机型：v2.1.10 全链 + Windows ssdiag `UNLOCKED`；同机 A/B FP16 16.03 → 29.14（**+82%**）、BF16 +75%、TF32 +72%、FP32 双对照平；**驱动 init 存活但 S3/S5 清除**——混合本按"每引导重跑"使用 | [#188](https://github.com/physicsdolphin/nv-uefi-unlocker/issues/188) |
| RTX 2060 12GB | 修复后通过；六轮单变量与 PROM 离线分析把 staging 钉在 4 GiB 边界（未给性能数值） | [#89](https://github.com/physicsdolphin/nv-uefi-unlocker/issues/89) |
| RTX 2060 Super 8GB | 全链通过：FWSEC → WPR2 → BOOT_DIRECT → PLM 开启 → SS0/SS1 读回；签名还原、Windows 交棒正常 | [#12](https://github.com/physicsdolphin/nv-uefi-unlocker/issues/12) |
| RTX 2070 Laptop 8GB | v2.1.3 通过；首个 Turing 笔记本成功记录，跨芯片同签名推动 >4G 分配修复（未给性能数值） | [#16](https://github.com/physicsdolphin/nv-uefi-unlocker/issues/16) |
| RTX 2070 8GB（开发者自测） | 全链通过（FWSEC → BOOT_DIRECT booter → PLM 全开 → SS0/SS1 读回）；FP32 累加 GEMM 36 → 60–63 TFLOPS（+67~75%），需 GSP 模式前置 | [最终结果](docs/evidence/m3-tu106/host-and-final-result.md) |
| RTX 2070 Super Max-Q（笔记本） | 首个 `1ed1` in-OS：同盘两轮 A/B——默认 HIGH staging 必 0x89，`\tx-low-staging.txt` 后全绿；PyTorch FP16 26.63 → 35.15 TFLOPS（**+32%**），FP32 对照持平；Linux 专有驱动下 `UNLOCKED` | [#191](https://github.com/physicsdolphin/nv-uefi-unlocker/issues/191) |
| RTX 2080 8GB | v2.1.8 修复后通过；报告者以 8 轮单变量和与成功机逐位 diff 定位 0x91（未给性能数值） | [#62](https://github.com/physicsdolphin/nv-uefi-unlocker/issues/62) |
| RTX 2080 Super 8GB | 0x91 修复后复测通过：46 → 68 TFLOPS（+47.8%）；该修复链的首个成功验证 | [#14](https://github.com/physicsdolphin/nv-uefi-unlocker/issues/14) |
| RTX 2080 Ti | 同卡精确 A/B：FP16（FP32 累加）持续 58.70 → 94.97 TFLOPS（+62%），每时钟 ×1.80，60 s 浸泡 0 停顿、无 TDR/WHEA；FP32/INT8/带宽不变（300 W 墙、GSP 开启）。另有原厂 11GB 在 Linux 专有驱动下 60.31 → 89.57 TFLOPS 的跨平台全链记录；H3 收益不明显 | [#125](https://github.com/physicsdolphin/nv-uefi-unlocker/issues/125) · [#103](https://github.com/physicsdolphin/nv-uefi-unlocker/issues/103) · [S41](https://www.bilibili.com/video/BV1d6xN66ECM/?comment_on=1&comment_root_id=318838634673&comment_secondary_id=318838634673) |
| RTX 2080 Ti 22GB 改卡 | 自述最后一次尝试成功；未给性能对比 | [S33](https://www.bilibili.com/video