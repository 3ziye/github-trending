<h2 align="center">
  Real-Time Object Detection Meets DINOv3
</h2>

<p align="center">
    <a href="https://github.com/Intellindust-AI-Lab/DEIMv2/blob/master/LICENSE">
        <img alt="license" src="https://img.shields.io/badge/LICENSE-Apache%202.0-blue">
    </a>
    <a href="https://arxiv.org/abs/2509.20787">
        <img alt="arXiv" src="https://img.shields.io/badge/arXiv-2509.20787-red">
    </a>
   <a href="https://intellindust-ai-lab.github.io/projects/DEIMv2/">
        <img alt="project webpage" src="https://img.shields.io/badge/Webpage-DEIMv2-purple">
    </a>
    <a href="https://github.com/Intellindust-AI-Lab/DEIMv2/pulls">
        <img alt="prs" src="https://img.shields.io/github/issues-pr/Intellindust-AI-Lab/DEIMv2">
    </a>
    <a href="https://github.com/Intellindust-AI-Lab/DEIMv2/issues">
        <img alt="issues" src="https://img.shields.io/github/issues/Intellindust-AI-Lab/DEIMv2?color=olive">
    </a>
    <a href="https://github.com/Intellindust-AI-Lab/DEIMv2">
        <img alt="stars" src="https://img.shields.io/github/stars/Intellindust-AI-Lab/DEIMv2">
    </a>
    <a href="mailto:shenxi@intellindust.com">
        <img alt="Contact Us" src="https://img.shields.io/badge/Contact-Email-yellow">
    </a>
</p>

<p align="center">
    DEIMv2 is an evolution of the DEIM framework while leveraging the rich features from DINOv3. Our method is designed with various model sizes, from an ultra-light version up to S, M, L, and X, to be adaptable for a wide range of scenarios. Across these variants, DEIMv2 achieves state-of-the-art performance, with the S-sized model notably surpassing 50 AP on the challenging COCO benchmark.
</p>

---


<div align="center">
  <a href="http://www.shihuahuang.cn">Shihua Huang</a><sup>1*</sup>,&nbsp;&nbsp;
  Yongjie Hou<sup>1,2*</sup>,&nbsp;&nbsp;
  Longfei Liu<sup>1*</sup>,&nbsp;&nbsp;
  <a href="https://xuanlong-yu.github.io/">Xuanlong Yu</a><sup>1</sup>,&nbsp;&nbsp;
  <a href="https://xishen0220.github.io">Xi Shen</a><sup>1†</sup>&nbsp;&nbsp;
</div>

  
<p align="center">
<i>
1. <a href="https://intellindust-ai-lab.github.io"> Intellindust AI Lab</a> &nbsp;&nbsp; 2. Xiamen University &nbsp; <br> 
* Equal Contribution &nbsp;&nbsp; † Corresponding Author
</i>
</p>


<p align="center">
<strong>If you like our work, please give us a ⭐!</strong>
</p>


<p align="center">
  <img src="./figures/deimv2_coco_AP_vs_Params.png" alt="Image 1" width="49%">
  <img src="./figures/deimv2_coco_AP_vs_GFLOPs.png" alt="Image 2" width="49%">
</p>

</details>

 
  
## 🚀 Updates
- [x] **\[2025.10.2\]** [DEIMv2 has been integrated into X-AnyLabeling!](https://github.com/Intellindust-AI-Lab/DEIMv2/issues/25#issue-3473960491) Many thanks to the X-AnyLabeling maintainers for making this possible.
- [x] **\[2025.9.26\]** Release DEIMv2 series.

## 🧭 Table of Content
* [1. 🤖 Model Zoo](#1-model-zoo)
* [2. ⚡ Quick Start](#2-quick-start)
* [3. 🛠️ Usage](#3-usage)
* [4. 🧰 Tools](#4-tools)
* [5. 📜 Citation](#5-citation)
* [6. 🙏 Acknowledgement](#6-acknowledgement)
* [7. ⭐ Star History](#7-star-history)
  
  
## 1. Model Zoo

| Model | Dataset | AP | #Params | GFLOPs | Latency (ms) | config | checkpoint | log |
| :---: | :---: | :---: | :---: | :---: |:------------:| :---: | :---: | :---: |
| **Atto** | COCO | **23.8** | 0.5M | 0.8 |     1.10     | [yml](./configs/deimv2/deimv2_hgnetv2_atto_coco.yml) | [ckpt](https://drive.google.com/file/d/18sRJXX3FBUigmGJ1y5Oo_DPC5C3JCgYc/view?usp=sharing) | [log](https://drive.google.com/file/d/1M7FLN8EeVHG02kegPN-Wxf_9BlkghZfj/view?usp=sharing) |
| **Femto** | COCO | **31.0** | 1.0M | 1.7 |     1.45     | [yml](./configs/deimv2/deimv2_hgnetv2_femto_coco.yml) | [ckpt](https://drive.google.com/file/d/16hh6l9Oln9TJng4V0_HNf_Z7uYb7feds/view?usp=sharing) | [log](https://drive.google.com/file/d/1_KWVfOr3bB5TMHTNOmDIAO-tZJmKB9-b/view?usp=sharing) |
| **Pico** | COCO | **38.5** | 1.5M | 5.2 |     2.13     | [yml](./configs/deimv2/deimv2_hgnetv2_pico_coco.yml) | [ckpt](https://drive.google.com/file/d/1PXpUxYSnQO-zJHtzrCPqQZ3KKatZwzFT/view?usp=sharing) | [log](https://drive.google.com/file/d/1GwyWotYSKmFQdVN9k2MM6atogpbh0lo1/view?usp=sharing) |
| **N** | COCO | **43.0** | 3.6M | 6.8 |     2.32     | [yml](./configs/deimv2/deimv2_hgnetv2_n_coco.yml) | [ckpt](https://drive.google.com/file/d/1G_Q80EVO4T7LZVPfHwZ3sT65FX5egp9K/view?usp=sharing) | [log](https://drive.google.com/file/d/1QhYfRrUy8HrihD3OwOMJLC-ATr97GInV/view?usp=sharing) |
| **S** | COCO | **50.9** | 9.7M | 25.6 |     5.78     | [yml](./configs/deimv2/deimv2_dinov3_s_coco.yml) | [ckpt](https://drive.google.com/file/d/1MDOh8UXD39DNSew6rDzGFp1tAVpSGJdL/view?usp=sharing) | [log](https://drive.google.com/file/d/1ydA4lWiTYusV1s3WHq5jSxIq39oxy-Nf/view?usp=sharing) |
| **M** | COCO | **53.0** | 18.1M | 52.2 |     8.80     | [yml](./configs/deimv2/deimv2_dinov3_m_coco.yml) | [ckpt](https://drive.google.com/file/d/1nPKDHrotusQ748O1cQXJfi5wdShq6bKp/view?usp=sharing) | [log](https://drive.google.com/file/d/1i05Q1-O9UH-2Vb