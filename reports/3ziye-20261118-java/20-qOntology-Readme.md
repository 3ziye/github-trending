![qOntology 本体工程平台横幅](.gitee/banner-qontology-final.png)
<p align="center">
 <img src="https://img.shields.io/badge/JDK-17+-brightgreen.svg" alt="JDK">
 <img src="https://img.shields.io/badge/Spring%20Boot-3.x-blue.svg" alt="Spring Boot">
 <img src="https://img.shields.io/badge/Vue-3.x-blue.svg" alt="Vue">
 <img src="https://img.shields.io/badge/license-Apache--2.0-green" alt="License">
 <img src="https://img.shields.io/badge/qOntology-Ontology%20Engineering-blue.svg" alt="qOntology">
 <img src="https://gitee.com/qiantongtech/qOntology/badge/star.svg" alt="Gitee Stars"/>
 <img src="https://img.shields.io/github/stars/qiantongtech/qOntology?label=Github%20Stars" alt=""/>
<a href="https://atomgit.com/qiantongtech/qOntology">
  <img src="https://atomgit.com/qiantongtech/qOntology/star/badge.svg" alt="AtomGit Star"/>
</a>
</p>

<p align="center">
  📖简体中文 | <a href="README.en.md">📖English</a>
</p>

## 🌈 平台简介

qOntology 是面向企业级知识工程的开源本体工程平台，以本体论为基础，遵循 OWL、RDF、SHACL 等语义网标准，聚焦企业本体治理与语义治理，通过统一建模与语义资产管理，连接知识图谱、企业运行本体与本体驱动 AI，构建统一、开放、可演进的企业语义基础设施。

✨✨✨**在线文档**✨✨✨ <a href="https://docs.qontology.cn/" target="_blank">https://docs.qontology.cn/</a>

✨✨✨**开源版演示地址**✨✨✨ <a href="https://demo.qontology.cn" target="_blank"> https://demo.qontology.cn </a> ，账号：qOntology 密码：qOntology123

> 如果 qOntology 对您有帮助，请点个 **Star ⭐️**，这是我们持续更新的最大动力！ 🚀

## 🎯 qOntology 能帮你解决哪些场景？

你可以使用 qOntology 规划和建设：

- 面向领域项目的统一术语和概念体系
- 对象类型、属性、关系与约束组成的本体模型
- 基于建模目标（CQ）的模型覆盖检查
- 从业务数据到对象类型和属性的轻量映射与样例预览
- 可版本化、可交换的本体资产
- 基于已发布本体的知识抽取与知识图谱


## ✨ 为什么选择 qOntology？

| 能力亮点         | 说明                                        |
|--------------|-------------------------------------------|
| 🎯 目标驱动建模    | 以业务问题（CQ）记录建模目标，并检查本体对目标的覆盖情况。            |
| 📚 术语与语义统一   | 管理术语、别名、数据类型与枚举，统一领域语言。                   |
| 🔗 对象关系建模    | 维护对象类型、属性、关系及 SHACL 基础约束。                 |
| ✅ 质量与版本管理    | 对模型结构和基础约束进行检查，保留版本及变更记录。                 |
| 🔄 标准格式交换    | 开源版规划支持 Turtle RDF/OWL 与 SHACL Turtle 导出。 |
| 🧱 模块化架构     | 系统管理、基础管理、本体建模分别组织，便于按能力扩展。               |
| ☕ Java 技术栈友好 | 后端采用 JDK 17 + Spring Boot 3，适合私有化部署与二次开发。 |


## 🍱 典型应用场景

| 场景          | 说明                          |
|-------------|-----------------------------|
| **领域本体设计**  | 从建模目标和术语出发，定义对象类型、属性、关系与约束。 |
| **业务语义治理**  | 统一维护项目资料、数据类型、枚举和业务术语。      |
| **数据映射验证**  | 将数据表字段映射到本体，预览少量对象实例样例。     |
| **模型质量与发布** | 检查本体结构和基础约束，比较并发布版本。        |
| **知识图谱建设**  | 基于本体及抽取结果展示对象及其关系。          |


## 🚀 核心优势

- **完整的建模要素**：以建模目标、术语、对象类型、属性、关系和约束描述领域语义。
- **明确的质量边界**：开源版聚焦来源完整性、重复标识、循环继承、悬空关系、类型与基础约束检查。
- **可追踪的模型演进**：比较术语和本体元素的版本变化，发布并保存变更记录。
- **轻量的数据连接**：提供字段映射和少量对象实例预览，用于验证模型与数据的对应关系。
- **开放的交换格式**：开源版规划支持 Turtle RDF/OWL 与 SHACL Turtle 导出。


## ✨ 核心功能
| 功能模块            | 描述                                                    |
|-----------------|-------------------------------------------------------|
| 系统管理            | 用户、角色、菜单、部门、岗位、字典、参数、通知公告和日志管理。                       |
| 项目管理            | 维护本体项目的领域、范围、命名空间等基础信息。                               |
| 数据源与文件管理        | 登记数据源，分类、上传和管理 Word、可提取文本的 PDF 与 TXT 文件；按文件记录纯文本解析结果。 |
| 数据类型与枚举         | 维护平台级类型与枚举，并在项目中引用或定义项目特有内容。                          |
| 建模目标（CQ）        | 用自然语言记录业务问题、优先级和验收说明，关联本体元素并检查覆盖情况。                   |
| 术语管理            | 管理定义、别名、来源及术语与本体元素的映射。                                |
| 对象类型与属性         | 定义对象类型及继承关系，配置属性的数据类型、基数、默认值、单位和枚举。                   |
| 对象关系与约束         | 定义对象类型之间的关系，并配置 SHACL 基础约束。                           |
| 本体质量验证          | 开源版规划提供来源完整性、重复标识、循环继承、悬空关系、类型和基础约束检查。                |
| AI 辅助建模         | 开源版规划从纯文本类文件生成候选本体，由人工审核确认。                           |
| 版本管理            | 比较术语、本体元素及建模目标影响，质量检查通过后发布版本。                         |
| 数据映射 Lite 与实例预览 | 完成字段到对象类型和属性的轻量映射，预览少量对象实例样例。                         |
| 导入导出            | 管理模型交换任务；开源版规划导出 Turtle RDF/OWL 与 SHACL Turtle。       |
| 本体应用            | 基于已发布本体进行非结构化抽取、结构化抽取并形成知识图谱。                         |

## 🛠️ 技术栈

qOntology 采用前后端分离架构，后端基于 JDK 17 与 Spring Boot 3.5.8，前端基于 Vue 3 与 Vite 5。下表以当前工程配置为依据；某些组件为按需模块，不代表每次部署都必须启用。

<table>
  <tr>
    <th>技术栈</th><th>技术框架</th><th>描述</th>
  </tr>
  <tr>
    <td rowspan="8">后端技术栈</td><td>JDK 17</td><td>后端运行环境</td>
  </tr>
  <tr>
    <td>Spring Boot 3.5.8</td><td>后端主体框架</td>
  </tr>
  <tr>
    <td>Spring Security</td><td>认证与授权</td>
  </tr>
  <tr>   
    <td>MyBatis 相关组件</td><td>关系型数据库访问与映射</td>
  </tr>
  <tr>
    <td>Spring Framework</td><td>基础架构支持，包括依赖注入、面向切面编程等能力</td>
  </tr>
  <tr>
    <td>Quartz</td><td>定时任务调度（按需）</td>
  </tr>
  <tr>
    <td>Neo4j 模块</td><td>图数据库接入能力（按需）</td>
  </tr>
  <tr>
    <td>Alibaba Druid</td><td>数据库连接池，优化数据库访问性能</td>
  </tr>

  <tr>
    <td rowspan="8">前端技术栈</td><td>Vue 3</td><td>渐进式前端框架</td>
  </tr>
  <tr>
    <td>Vite</td><td>快速构建工具</td>
  </tr>
  <tr>
    <td>Element Plus</td><td>UI 组件库</td>
  </tr>
  <tr>
    <td>Axios</td><td>HTTP 请求库</td>
  </tr>
  <tr>
    <td>Pinia</td><td>前端状态管理</td>
  </tr>
  <tr>
    <td>Vue Router</td><td>前端路由控制</td>
  </tr>
  <tr>
    <td>Vis Network / AntV</td><td>图与关系网络展示组件</td>
  </t