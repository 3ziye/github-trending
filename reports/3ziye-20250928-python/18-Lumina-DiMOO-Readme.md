<p align="center">
 <img src="./assets/Lumina-DiMOO.png" width="20%"/>
</p>

<div align="center">
 <h1> Lumina-DiMOO: An Omni Diffusion Large Language Model for Multi-Modal Generation and Understanding </h1>

  [[📑 Technical Report ](https://github.com/Alpha-VLLM/Lumina-DiMOO/blob/main/Technical-Report.pdf)] &emsp; [[🌐 Project Page (Demo & Benchmark)](https://synbol.github.io/Lumina-DiMOO/)] &emsp; [[🤗 Model ](https://huggingface.co/Alpha-VLLM/Lumina-DiMOO)]
 
 <b>¹Shanghai AI Laboratory, ²Shanghai Innovation Institute, ³Shanghai Jiao Tong University, ⁴Nanjing University </b>
 
 <b>⁵The University of Sydney, ⁶The Chinese University of Hong Kong, ⁷Tsinghua University</b>

 <img src="./assets/teaser.png" width="95%"/>
</div>

## 📚 Introduction 
We introduce Lumina-DiMOO, an omni foundational model for seamless multimodal generation and understanding. Lumina-DiMOO is distinguished by four key innovations:

 - **Unified Discrete Diffusion Architecture:** Lumina-DiMOO sets itself apart from prior unified models by utilizing a fully discrete diffusion modeling to handle inputs and outputs across various modalities.
 - **Versatile Multimodal Capabilities:** Lumina-DiMOO supports a broad spectrum of multimodal tasks, including text-to-image generation (allowing for arbitrary and high-resolution), image-to-image generation (e.g., image editing, subject-driven generation, and image inpainting, etc.), alongside advanced image understanding.

 - **Higher Sampling Efficiency:** Compared to previous AR or hybrid AR-diffusion paradigms, Lumina-DiMOO demonstrates remarkable sampling efficiency. Additionally, we design a bespoke caching method to further speed up the sampling speed by 2x.

 - **Superior Performance:** Lumina-DiMOO achieves state-of-the-art performance on multiple benchmarks, surpassing existing open-source unified multimodal models, setting a new standard in the field.


   
 <img src="./assets/architecture.png" width="100%"/>


## 🔥 News
- **[2025-09-25]** 🎉🎉🎉 We have released the Technical Report.
- **[2025-09-20]** 🎉🎉🎉 In the latest [UniGenBench Leaderboard](https://huggingface.co/spaces/CodeGoat24/UniGenBench_Leaderboard)(maintained by Tencent Hunyuan Team), Lumina-DiMOO's generation evaluation ranks 1st 🥇 among all open-source unified models. 
- **[2025-09-12]** 🎉🎉🎉 We have open-sourced Image Inpainting & Extrapolation code.
- **[2025-09-11]** 🎉🎉🎉 We have open-sourced the Max Logit-based Cache solution, offering a 2x speed improvement for sampling.
- **[2025-09-10]** 🎉🎉🎉 We release the initial version of **Lumina-DiMOO**, including:
  - 🎯 Model Checkpoints on [HuggingFace](https://huggingface.co/Alpha-VLLM/Lumina-DiMOO)!
  - 🎯 Text-to-Image & Image-to-Image Generation Inference code!
  - 🎯 Image Understanding Inference Code!
  - 🎯 Website & Demo on [Project Page](https://synbol.github.io/Lumina-DiMOO/)!

## 📝 Open-Source Plan
 - [x] Image Inpainting & Extrapolation Code
 - [x] Fast Sampling with Max Logit-based Cache
 - [ ] Gradio Demo
 - [ ] Bechmark Evaluation Code
 - [ ] Fine-Tuning Code
 - [ ] Self-GRPO Training Code
 - [x] Technical Report

## 📽️ Qualitative Results
Here we present some comparative generation results with other models. **For additional visualization results, please see our [Project Page](https://synbol.github.io/Lumina-DiMOO/).**
<details open>
  <summary>Text-to-Image Comparison</summary>
  <img src="./assets/demo_t2i.png" width="100%"/>
<!--   <details open>
  <summary>Effects of Max Logit-Based Cache (A800 GPU, 1536x768 resolution)</summary>
  Without Cache: Latency: 58.2 s; Peak GPU Memory: 38.9 GiB
  <img src="./assets/nocache.png" width="80%"/>


  With Cache: Latency: 32.2 s; Peak GPU Memory: 45.9 GiB
  <img src="./assets/cache.png" width="80%"/>
</details> -->
</details>

<details close>
  <summary>Image Editing Comparison</summary>
  <img src="./assets/demo_editing.png" width="100%"/>
</details>

<details close>
  <summary>Controllable & Subject-Driven Generation Comparison</summary>
  <img src="./assets/qualitative_control_subject.png" width="100%"/>
</details>

<details close>
  <summary>Image Inpainting & Extrapolation</summary>
  <img src="./assets/demo_inpainting.jpg" width="100%"/>
</details>


## 📊 Quantitative Performance
<details open>
  <summary>GenEval Benchmark</summary>
  <img src="./assets/GenEval_benchmark.png" width="100%"/>
</details>


<details close>
  <summary>DPG Benchmark</summary>
  <img src="./assets/DPG_benchmark.png" width="100%"/>
</details>

<details close>
  <summary>OneIG-EN Benchmark</summary>
  <img src="./assets/OneIG-EN_benchmark.png" width="100%"/>
</details>


<details close>
  <summary>TIIF Benchmark</summary>
  <img src="./assets/TIIF_benchmark.png" width="100%"/>
</details>

<details close>
  <summary>Image-to-Image Benchmark</summary>
  <img src="./assets/i2i_benchmark.png" width="100%"/>
</details>

<details close>
  <summary>Image Understanding Benchmark</summary>
  <img src="./assets/understanding_benchmark.png" width="100%"/>
</