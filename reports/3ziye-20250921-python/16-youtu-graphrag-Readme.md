<div align="center">

# <img src="assets/logo.svg" alt="Youtu-agent Logo" height="26px"> Youtu-GraphRAG: <br>Vertically Unified Agents for Graph Retrieval-Augmented Complex Reasoning

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Paper](https://img.shields.io/badge/Paper-Latest-blue.svg)](https://arxiv.org/abs/2508.19855)
[![WeChat Community](https://img.shields.io/badge/Community-WeChat-32CD32)](assets/wechat_qr.png)
[![Discord Community](https://img.shields.io/badge/Community-Discord-8A2BE2)](https://discord.gg/QjqhkHQVVM)
[![GitHub stars](https://img.shields.io/github/stars/TencentCloudADP/youtu-graphrag?style=social)](https://github.com/TencentCloudADP/youtu-graphrag)

*🚀 Revolutionary framework moving Pareto Frontier with 33.6% lower token cost and 16.62% higher accuracy over SOTA baselines*

[🔖 中文版](README-CN.md) • [⭐ Contributions](#contributions) • [📊 Benchmarks](https://huggingface.co/datasets/Youtu-Graph/AnonyRAG) • [🚀 Getting Started](#quickstart)

</div>

## 🎯 Brief Introduction
**Youtu-GraphRAG** is a vertically unified agentic paradigm that jointly connects the entire framework as an intricate integration based on graph schema. We allow seamless domain transfer with minimal intervention on the graph schema, providing insights of the next evolutionary GraphRAG paradigm for real-world applications with remarkable adaptability.

<img src="assets/logo.png" alt="Youtu-GrapHRAG Logo" width="140" align="left" style="margin-right:20px;">


### 🎨 When and Why to use Youtu-GraphRAG

🔗 Multi-hop Reasoning/Summarization/Conclusion: Complex questions requiring multi-step reasoning<br>
📚 Knowledge-Intensive Tasks: Questions dependent on large amounts of structured/private/domain knowledge<br>
🌐 Domain Scalability: Easily support encyclopedias, academic papers, commercial/private knowledge base and other domains with minimal intervention on the schema<br><br>


## 🏗️ Framework Architecture

<div align="center">
<img src="assets/framework.png" alt="Youtu-GraphRAG Framework Architecture" width="95%"/><br>
A sketched overview of our proposed framework Youtu-GraphRAG.
</div>

## 📲 Interactive interface

<div align="center">

[//]: # (<img src="assets/dashboard_demo.png" alt="Dashboard" width="32%"/>)
<img src="assets/graph_demo.png" alt="Graph Construction" width="45.9%"/>
<img src="assets/retrieval_demo.png" alt="Retrieval" width="49.4%"/>
</div>

<a id="contributions"></a>
## 🚀 Contributions and Novelty

Based on our unified agentic paradigm for Graph Retrieval-Augmented Generation (GraphRAG), Youtu-GraphRAG introduces several key innovations that jointly connect the entire framework as an intricate integration:


<strong>🏗️ 1. Schema-Guided Hierarchical Knowledge Tree Construction</strong>

- 🌱 **Seed Graph Schema**: Introduces targeted entity types, relations, and attribute types to bound automatic extraction agents
- 📈 **Scalable Schema Expansion**: Continuously expands schemas for adaptability over unseen domains
- 🏢 **Four-Level Architecture**: 
  - **Level 1 (Attributes)**: Entity property information
  - **Level 2 (Relations)**: Entity relationship triples
  - **Level 3 (Keywords)**: Keyword indexing
  - **Level 4 (Communities)**: Hierarchical community structure
- ⚡ **Quick Adaptation to industrial applications**: We allow seamless domain transfer with minimal intervention on the schema


<strong>🌳 2. Dually-Perceived Community Detection</strong>

- 🔬 **Novel Community Detection Algorithm**: Fuses structural topology with subgraph semantics for comprehensive knowledge organization
- 📊 **Hierarchical Knowledge Tree**: Naturally yields a structure supporting both top-down filtering and bottom-up reasoning that performs better than traditional Leiden and Louvain algorithms
- 📝 **Community Summaries**: LLM-enhanced community summarization for higher-level knowledge abstraction

<div align="center">
<img src="assets/comm.png" alt="Youtu-GraphRAG Community Detection" width="60%"/>
</div>

<strong>🤖 3. Agentic Retrieval</strong>

- 🎯 **Schema-Aware Decomposition**: Interprets the same graph schema to transform complex queries into tractable and parallel sub-queries
- 🔄 **Iterative Reflection**: Performs reflection for more advanced reasoning through IRCoT (Iterative Retrieval Chain of Thought)

<div align="center">
<img src="assets/agent.png" alt="Youtu-GraphRAG Agentic Decomposer" width="50%"/>
</div>

<strong>🧠 4. Advanced Construction and Reasoning Capabilities for real-world deployment</strong>

- 🎯 **Performance Enhancement**: Less token costs and higher accuracy with optimized prompting, indexing and retrieval strategies
- 🤹‍♀️ **User friendly visualization**: In ```output/graphs/```, the four-level knowledge tree supports visualization with neo4j import，making reasoning paths and knowledge organization vividly visable to users
- ⚡ **Parallel Sub-question Processing**: Concurrent handling of decomposed questions for efficiency and complex 