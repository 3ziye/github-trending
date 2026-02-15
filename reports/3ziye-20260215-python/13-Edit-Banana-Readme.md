<p align="center">
  <img src="/static/banana.jpg" width="180" alt="Edit Banana Logo"/>
</p>

<h1 align="center">🍌 Edit Banana</h1>
<h3 align="center">Universal Content Re-Editor: Make the Uneditable, Editable</h3>

<p align="center">
Break free from static formats. Our platform empowers you to transform fixed content into fully manipulatable assets.
Powered by SAM 3 and multimodal large models, it enables high-fidelity reconstruction that preserves the original diagram details and logical relationships.
</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache_2.0-2F80ED?style=flat-square&logo=apache&logoColor=white" alt="License"/></a>
  <a href="https://developer.nvidia.com/cuda-downloads"><img src="https://img.shields.io/badge/GPU-CUDA%20Recommended-76B900?style=flat-square&logo=nvidia" alt="CUDA"/></a>
  <a href="#-join-wechat-group"><img src="https://img.shields.io/badge/WeChat-Join%20Group-07C160?style=flat-square&logo=wechat&logoColor=white" alt="WeChat"/></a>
  <a href="https://github.com/BIT-DataLab/Edit-Banana/stargazers"><img src="https://img.shields.io/github/stars/BIT-DataLab/Edit-Banana?style=flat-square&logo=github" alt="GitHub stars"/></a>
</p>

---

<h3 align="center">Try It Now!</h3>
<p align="center">
  <a href="https://editbanana.anxin6.cn/">
    <img src="https://img.shields.io/badge/🚀%20Try%20Online%20Demo-editbanana.anxin6.cn-FF6B6B?style=for-the-badge&logoColor=white" alt="Try Online Demo"/>
  </a>
</p>

<p align="center">
  👆 <b>Click above or https://editbanana.anxin6.cn/ to try Edit Banana online!</b> Upload an image or pdf, get <b>editable DrawIO (XML) or PPTX</b> in seconds. 
  <b>Please note</b>: Our GitHub repository currently trails behind our web-based service. For the most up-to-date features and performance, we recommend using our web platform.
</p>

---

## 📸 Effect Demonstration
### High-Definition Input-Output Comparison (3 Typical Scenarios)
To demonstrate the high-fidelity conversion effect, we provides one-to-one comparisons between 3 scenarios of "original static formats" and "editable reconstruction results". All elements can be individually dragged, styled, and modified.

#### Scenario 1: Figures to Drawio(xml, svg, pptx)

| Example No. | Original Static Diagram (Input · Non-editable) | DrawIO Reconstruction Result (Output · Fully Editable) |
|--------------|-----------------------------------------------|--------------------------------------------------------|
| Example 1: Basic Flowchart | <img src="/static/demo/original_1.jpg" width="400" alt="Original Diagram 1" style="border: 1px solid #eee; border-radius: 4px;"/> | <img src="/static/demo/recon_1.png" width="400" alt="Reconstruction Result 1" style="border: 1px solid #eee; border-radius: 4px;"/> |
| Example 2: Multi-level Architecture Diagram | <img src="/static/demo/original_2.png" width="400" alt="Original Diagram 2" style="border: 1px solid #eee; border-radius: 4px;"/> | <img src="/static/demo/recon_2.png" width="400" alt="Reconstruction Result 2" style="border: 1px solid #eee; border-radius: 4px;"/> |
| Example 3: Technical Schematic | <img src="/static/demo/original_3.jpg" width="400" alt="Original Diagram 3" style="border: 1px solid #eee; border-radius: 4px;"/> | <img src="/static/demo/recon_3.png" width="400" alt="Reconstruction Result 3" style="border: 1px solid #eee; border-radius: 4px;"/> |
| Example 4: Scientific Formula Diagram | <img src="/static/demo/original_4.jpg" width="400" alt="Original Diagram 4" style="border: 1px solid #eee; border-radius: 4px;"/> | <img src="/static/demo/recon_4.png" width="400" alt="Reconstruction Result 4" style="border: 1px solid #eee; border-radius: 4px;"/> |

#### Scenario 2: PDF to PPTX


#### Scenario 3: Human in the Loop Modification

> ✨ Conversion Highlights:
> 1.  Preserves the layout logic, color matching, and element hierarchy of the original diagram
> 2.  1:1 restoration of shape stroke/fill and arrow styles (dashed lines/thickness)
> 3.  Accurate text recognition, supporting direct subsequent editing and format adjustment
> 4.  All elements are independently selectable, supporting native DrawIO template replacement and layout optimization

## Key Features

*   **Advanced Segmentation**: Using our fine-tuned **SAM 3 (Segment Anything Model 3)** for segmentation of diagram elements.
*   **Fixed Multi-Round VLM Scanning**: An extraction process guided by **Multimodal LLMs (Qwen-VL/GPT-4V)**.
*   **High-Quality OCR**:
    *   **Azure Document Intelligence** for precise text localization.
    *   **Fallback Mechanism**: Automatically switches to VLM-based end-to-end OCR if Azure services are unreachable.
    *   **Mistral Vision/MLLM** for correcting text and converting mathematical formulas to **LaTeX** ($\int f(x) dx$).
    *   **Crop-Guided Strategy**: Extr