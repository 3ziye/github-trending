This repository hosts Pokee’s state-of-the-art 7B DeepResearch Agent, which integrates web search and content reading capabilities to answer complex questions using the most up-to-date information available online.

*We also offer an API hosting our proprietary deep research agent, which is up to 75% cheaper than OpenAI, Gemini, and Perplexity. It delivers comprehensive, citation-rich research reports with no hidden costs and no API key management required. (For more information about the API, visit [pokee.ai/deepresearch-preview](https://pokee.ai/deepresearch-preview))*

<div align="center">

[![GitHub Stars](https://img.shields.io/github/stars/Pokee-AI/PokeeResearchOSS?style=social)](https://github.com/Pokee-AI/PokeeResearchOSS)
[![arXiv](https://img.shields.io/badge/arXiv-2510.15862-b31b1b.svg)](https://arxiv.org/pdf/2510.15862)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Model-yellow)](https://huggingface.co/PokeeAI/pokee_research_7b)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Follow-blue?style=social&logo=linkedin)](https://linkedin.com/company/pokee-ai)
[![X (Twitter)](https://img.shields.io/badge/X-Follow-1DA1F2?style=social&logo=x)](https://x.com/pokee_ai)
[![Discord](https://img.shields.io/badge/Discord-Join-5865F2?style=social&logo=discord)](https://discord.gg/VJXWQvyd)
[![WeChat](https://img.shields.io/badge/WeChat-Join-07C160?style=social&logo=wechat)](https://i.postimg.cc/wv099v5w/wechat-group-pokee.jpg)

<img src="Logo.png" alt="Pokee AI Logo" width="200"/>
<p style="text-align:center;">
  <a href="https://pokee.ai" target="_blank" rel="noopener noreferrer"><strong>pokee.ai</strong></a>
</p>

</div>

# PokeeResearch-7B Agent

Pokee's state-of-the-art 7B DeepResearch Agent that leverages web search and content reading capabilities to answer complex questions using the most up-to-date information available online.
<div align="center">
<img src="hle_gaia_bro.png" alt="HLE, GAIA and BrowseComp Performance" width="600"/>
</div>
<div align="center">
<img src="qa.png" alt="7 QA Benchmark Performance" width="800"/>
</div>

## 🚀 Features

- **Multi-turn Research**: Performs iterative web searches and content analysis
- **Tool Integration**: Seamlessly integrates web search, content reading, and browsing tools
- **Comprehensive Evaluation**: Includes benchmark evaluation across multiple QA datasets
- **High Performance**: Achieves superior results on complex reasoning tasks
- **Scalable Architecture**: Built on efficient 7B parameter model for optimal performance


## 📋 Requirements

### Hardware
- **Compute Node**: We tested the code on a single 80GB A100 GPU (GPUs with less memory may also work, though we have not tested them). Using multiple GPUs can further accelerate inference. For reference, the driver version is 570.133.20 and the CUDA toolkit version is 12.8.

### Software
- **Docker**: Environment to run the code will be provided as a docker image.

### API Keys
You will need the following API keys:
- **Serper API**: For web search functionality
- **Jina API**: For web content reading and extraction
- **Gemini API**: For content summarization and result evaluation
- **HuggingFace Token**: For downloading the model from HuggingFace

## 🛠️ Quick Start

### 1. Environment Setup
We provide a Docker image for easy deployment:
```bash
docker pull verlai/verl:app-verl0.5-transformers4.55.4-sglang0.4.10.post2-mcore0.13.0-te2.2
docker create --runtime=nvidia --gpus all --net=host --shm-size="80g"  -v .:/workspace/ --name pokeeresearch verlai/verl:app-verl0.5-transformers4.55.4-sglang0.4.10.post2-mcore0.13.0-te2.2 sleep infinity
docker start pokeeresearch
docker exec -it pokeeresearch  bash
ssh-keygen -t ed25519 -C <USER_NAME>
# copy /root/.ssh/id_ed25519.pub to github ssh keys
git clone git@github.com:Pokee-AI/PokeeResearchOSS.git --recursive
cd PokeeResearchOSS
pip install colorlog
pip install -U google-genai
hf auth login # enter your huggingface token, the tokens needs to have permission to use Pokee AI's models
cd verl
pip install -e .
cd ..
```

Create a `.env` file in the project root and add your API keys:
```bash
SERPER_API_KEY=your_serper_api_key_here
JINA_API_KEY=your_jina_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

### 2. Modify ```run.sh``` to use more than one GPUs (optional)
Running the experiment with more GPUs is faster. By default the experiment uses one GPU.
If you want to use more GPUs, simply modify 
```bash
trainer.n_gpus_per_node=1 \
```
in ```run.sh``` to 
```bash
trainer.n_gpus_per_node=<NUM_GPUS_TO_USE> \
```
### 3. Run Benchmark Evaluation

**Step 1: Start the Tool Server**
```bash
python start_tool_server.py \
--port <PORT_NUMBER> \ # to specify the port to listen to (default 8888)
--enable-cache # to enable caching tool results (recommended to save api credits)
```

**Step 2: Run the Evaluation**

Start a new terminal, then run the experiment.
```bash
docker exec -it pokeeresearch bash
cd PokeeResearchOSS
bash run.sh
```
