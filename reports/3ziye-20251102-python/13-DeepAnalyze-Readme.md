<p align="center" width="100%">
<img src="assets/logo.png" alt="DeepAnalyze" style="width: 60%; min-width: 300px; display: block; margin: auto;">
</p>

# DeepAnalyze: Agentic Large Language Models for Autonomous Data Science
[![arXiv](https://img.shields.io/badge/arXiv-2510.16872-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2510.16872)
[![homepage](https://img.shields.io/badge/%F0%9F%8C%90%20Homepage%20-DeepAnalyze%20Cases-blue.svg)](https://ruc-deepanalyze.github.io/)
[![model](https://img.shields.io/badge/%F0%9F%A4%97%20Huggingface%20-DeepAnalyze--8B-orange.svg)](https://huggingface.co/RUC-DataLab/DeepAnalyze-8B)
[![data](https://img.shields.io/badge/%F0%9F%93%9A%20Datasets%20-DataScience--Instruct--500K-darkgreen.svg)](https://huggingface.co/datasets/RUC-DataLab/DataScience-Instruct-500K)
[![star](https://img.shields.io/github/stars/ruc-datalab/DeepAnalyze?style=social&label=Code+Stars)](https://github.com/ruc-datalab/DeepAnalyze)
![Badge](https://hitscounter.dev/api/hit?url=https%3A%2F%2Fgithub.com%2Fruc-datalab%2FDeepAnalyze&label=Visitors&icon=graph-up&color=%23dc3545&message=&style=flat&tz=UTC)  [![wechat](https://img.shields.io/badge/WeChat-%E5%8A%A0%E5%85%A5DeepAnalyze%E4%BA%A4%E6%B5%81%E8%AE%A8%E8%AE%BA%E7%BE%A4-black?logo=wechat&logoColor=07C160)](./assets/wechat.jpg) 

[![twitter](https://img.shields.io/badge/@Brian%20Roemmele-gray?logo=x&logoColor=white&labelColor=black)](https://x.com/BrianRoemmele/status/1981015483823571352) [![twitter](https://img.shields.io/badge/@Dr%20Singularity-gray?logo=x&logoColor=white&labelColor=black)](https://x.com/Dr_Singularity/status/1981010771338498241) [![twitter](https://img.shields.io/badge/@Gorden%20Sun-gray?logo=x&logoColor=white&labelColor=black)](https://x.com/Gorden_Sun/status/1980573407386423408) [![twitter](https://img.shields.io/badge/@AIGCLINK-gray?logo=x&logoColor=white&labelColor=black)](https://x.com/aigclink/status/1980554517126246642) [![twitter](https://img.shields.io/badge/@Python%20Developer-gray?logo=x&logoColor=white&labelColor=black)](https://x.com/Python_Dv/status/1980667557318377871) [![twitter](https://img.shields.io/badge/@meng%20shao-gray?logo=x&logoColor=white&labelColor=black)](https://x.com/shao__meng/status/1980623242114314531) 


> **Authors**: **[Shaolei Zhang](https://zhangshaolei1998.github.io/), [Ju Fan*](http://iir.ruc.edu.cn/~fanj/), [Meihao Fan](https://scholar.google.com/citations?user=9RTm2qoAAAAJ), [Guoliang Li](https://dbgroup.cs.tsinghua.edu.cn/ligl/), [Xiaoyong Du](http://info.ruc.edu.cn/jsky/szdw/ajxjgcx/jsjkxyjsx1/js2/7374b0a3f58045fc9543703ccea2eb9c.htm)**
>
> Renmin University of China, Tsinghua University


**DeepAnalyze** is the first agentic LLM for autonomous data science. It can autonomously complete a wide range of data-centric tasks without human intervention, supporting:
- 🛠 **Entire data science pipeline**: Automatically perform any data science tasks such as data preparation, analysis, modeling, visualization, and report generation.
- 🔍 **Open-ended data research**: Conduct deep research on diverse data sources, including structured data (Databases, CSV, Excel), semi-structured data (JSON, XML, YAML), and unstructured data (TXT, Markdown), and finally produce analyst-grade research reports.
- 📊 **Fully open-source**: The [model](https://huggingface.co/RUC-DataLab/DeepAnalyze-8B), [code](https://github.com/ruc-datalab/DeepAnalyze), [training data](https://huggingface.co/datasets/RUC-DataLab/DataScience-Instruct-500K), and [demo](https://huggingface.co/RUC-DataLab/DeepAnalyze-8B) of DeepAnalyze are all open-sourced, allowing you to deploy or extend your own data analysis assistant.

<p align="center" width="100%">
<img src="./assets/deepanalyze.jpg" alt="deepanalyze" style="width: 70%; min-width: 300px; display: block; margin: auto;">
</p>


## 🔥 News
- **[2025.10.28]**: We welcome all contributions, including improving the DeepAnalyze and sharing use cases (see [`CONTRIBUTION.md`](CONTRIBUTION.md)). All merged PRs will be listed as contributors.
- **[2025.10.27]**: DeepAnalyze has attracted widespread attention, gaining **1K+** GitHub stars and **200K+** Twitter views within a week.
- **[2025.10.21]**: DeepAnalyze's [paper](https://arxiv.org/abs/2510.16872), [code](https://github.com/ruc-datalab/DeepAnalyze), [model](https://huggingface.co/RUC-DataLab/DeepAnalyze-8B), [training data](https://huggingface.co/datasets/RUC-DataLab/DataScience-Instruct-500K) are released!

## 🖥 Demo


<p align="center" width="100%">
Upload the data, DeepAnalyze can perform data-oriented deep research 🔍 and any data-centric tasks 🛠
</p>

https://github.com/user-attachments/assets/04184975-7ee7-4ae0-8761-7a7550c5c8fe

> [!TIP]
>
> Clone this repository to deploy DeepAnalyze locally as your data analyst, completing any data science tasks without any workflow or closed-source APIs.
>
> 🔥 The UI of the demo is an initial version. Welcome to further develop it, and we will include you as a contributor.


- Clone this repo and dow