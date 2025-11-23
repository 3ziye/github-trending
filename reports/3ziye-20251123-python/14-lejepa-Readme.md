# LeJEPA
**Lean Joint-Embedding Predictive Architecture (LeJEPA): Provable and Scalable Self-Supervised Learning Without the Heuristics**
[GitHub Repository](https://github.com/rbalestr-lab/lejepa)  
[arXiv:2511.08544](https://arxiv.org/abs/2511.08544)
---

Rush to our [minimal working example](MINIMAL.md) to see a full-fledge working example (ViT, inet).

## Demo

<img src="eval/output1.gif" controls width="400">
<img src="eval/output2.gif" controls width="400">
<img src="eval/output3.gif" controls width="400">
<table>
  <tr>
    <td><img src="eval/n01818515_919_original.png" width="200"/></td>
    <td><img src="eval/n01818515_919_pca.png" width="200"/></td>
  </tr>
  <tr>
    <td><img src="eval/n01818515_14304_original.png" width="200"/></td>
    <td><img src="eval/n01818515_14304_pca.png" width="200"/></td>
  </tr>
</table>

| shots | model                  | params | pretrain | epochs | DTD      | aircr.   | cars     | cifar10  | cifar100 | flowers102 | food     | pets     | avg.    |
|-------|------------------------|--------|----------|--------|----------|----------|----------|----------|----------|------------|----------|----------|---------|
| 1     | LeJEPA ViT-L           | 304M   | IN-1K    | 100    | **33.21**| 9.37     | 3.40     | 51.65    | 27.01    | 48.53      | 17.14    | 46.11    | 29.55   |
| 1     | LeJEPA ConvNeXtV2-H    | 660M   | IN-1K    | 100    | 32.15    | 8.07     | 4.28     | 50.95    | **31.48**| **48.74**  | **17.95**| **58.98**| **31.58**|
| 1     | I-JEPA ViT-H           | 632M   | IN-1K    | 300    | 27.71    | **9.86** | **4.33** | **56.52**| 30.58    | 44.69      | 14.53    | 53.38    | 30.20   |
| 10    | LeJEPA ViT-L           | 304M   | IN-1K    | 100    | **64.72**| **35.25**| 22.25    | 85.15    | 59.77    | **92.53**  | **50.90**| 77.00    | **60.95**|
| 10    | LeJEPA ConvNeXtV2-H    | 660M   | IN-1K    | 100    | 61.84    | 30.67    | **24.46**| 85.74    | 63.29    | 91.78      | 49.32    | 78.53    | 60.70   |
| 10    | I-JEPA ViT-H           | 632M   | IN-1K    | 300    | 57.68    | 33.82    | 21.96    | **88.77**| **66.42**| 88.24      | 43.97    | **83.23**| 60.51   |
| all   | LeJEPA ViT-L           | 304M   | IN-1K    | 100    | **78.30**| 57.01    | **57.28**| 96.50    | 83.71    | **91.21**  | **82.05**| 89.74    | **79.48**|
| all   | LeJEPA ConvNeXtV2-H    | 660M   | IN-1K    | 100    | 76.60    | 52.99    | 54.88    | 96.15    | 81.34    | 91.11      | 77.64    | 89.76    | 77.56   |
| all   | I-JEPA ViT-H           | 632M   | IN-1K    | 300    | 73.32    | **56.61**| 54.47    | **97.54**| **86.42**| 86.47      | 81.02    | **92.11**| 78.50   |

## Overview
LeJEPA is a lean, scalable, and theoretically grounded framework for self-supervised representation learning, based on Joint-Embedding Predictive Architectures (JEPAs). LeJEPA introduces **Sketched Isotropic Gaussian Regularization (SIGReg)**, a novel objective that constrains learned embeddings to an optimal isotropic Gaussian distribution, minimizing downstream prediction risk.
**Key Features:**
- Single trade-off hyperparameter
- Linear time and memory complexity
- Stable training across architectures and domains
- Heuristics-free implementation (no stop-gradient, teacher–student, or schedulers)
- Distributed training-friendly codebase (~50 lines of core code)
- State-of-the-art results across 10+ datasets and 60+ architectures
---

## GOTO hyperparameters


Our data augmentation strategy follows a multi-crop approach inspired by DINO, where we generate multiple views of each image at different scales to encourage the model to learn both global semantic information and local fine-grained features.

### Data augmentation and views

Each training image is augmented to produce **2 global views** and **6 local views** with different spatial scales but the same set of color and geometric transformations:
| **Global Views** | **Local Views** |
|------------------|-----------------|
| **RandomResizedCrop**<br>- Resolution: 224x224<br>- Scale: (0.3, 1.0)<br>- Covers 30-100% of the image | **RandomResizedCrop**<br>- Resolution: 98x98<br>- Scale: (0.05, 0.3)<br>- Covers 5-30% of the image |
| **RandomHorizontalFlip** (p=0.5) | **RandomHorizontalFlip** (p=0.5) |
| **ColorJitter** (p=0.8)<br>- Brightness: 0.4<br>- Contrast: 0.4<br>- Saturation: 0.2<br>- Hue: 0.1 | **ColorJitter** (p=0.8)<br>- Brightness: 0.4<br>- Contrast: 0.4<br>- Saturation: 0.2<br>- Hue: 0.1 |
| **RandomGrayscale** (p=0.2) | **RandomGrayscale** (p=0.2) |
| **GaussianBlur** (p=0.5) | **GaussianBlur** (p=0.5) |
| **RandomSolarize** (p=0.2, threshold=128) | **RandomSolarize** (p=0.2, threshold=128) |
| **Normalization** (mean, std) | **Normalization** (mean, std) |


The key difference between global and local views is the **cropping scale**: global views capture larger portions of the image to learn high-level semantics, while local views focus on smaller regions to learn fine-grained local patterns. All other augmentations are applied iden