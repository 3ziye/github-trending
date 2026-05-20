# **快速开始**

本项目是一个基于Spring AI的AI Agent应用（**纯Demo，仅学习用途**），集成了 RAG 检索增强生成、Function Calling 工具调用、MCP 协议、SubAgent 子代理、Skill 技能系统等核心能力。本文将从六个核心模块出发，深入剖析其架构设计和实现细节。

## **环境要求**

- Java 21+
- Maven 3.9+

## **核心模块**

| **模块**                     | **说明**                                                     |
| ---------------------------- | ------------------------------------------------------------ |
| **AgentCore**                | 核心编排器，具备意图识别、记忆管理与大模型调用等能力。       |
| **ChatMemory**               | 对话记忆管理，支持三层上下文压缩（摘要压缩 → Assistant 裁剪 → 滑动窗口）。 |
| **Tool（Function Calling）** | 可插拔的工具注册机制，通过 `InnerTool` 统一接口注册，LLM 自主决策调用 |
| **RAG**                      | 完整的检索增强生成流水线：文档加载 → 文档分块 → 向量化 → 向量存储 → 多路召回（语义 + BM25 + 查询改写）→ RRF 融合 → Rerank 重排 → LLM → 内容生成 |
| **Command & Skill**          | 两种 Markdown 驱动的 Prompt 模板机制：Command 由用户主动调用，Skill 本质作为Tool由 LLM 决策调用。 |
| **SubAgent**                 | 拥有独立记忆的子代理，支持内部 SubAgent 和外部 IdeaLab Agent 两种形态 |
| **MCP**                      | 双向 MCP 支持：作为 Client 动态连接外部 MCP 服务，作为 Server 对外暴露服务 |

## **配置**

编辑 `src/main/resources/application.properties`，配置大模型 API

```
spring.ai.openai.base-url=https://open.bigmodel.cn/api/paas/v4
spring.ai.openai.api-key=你的API密钥
spring.ai.openai.chat.options.model=glm-4
spring.ai.openai.embedding.options.model=embedding-3
```

## **启动**

```
./mvnw spring-boot:run
```

## **访问**

### **前端页面**

启动成功后，打开浏览器访问：

```
http://localhost:8080
```

项目内置了一个完整的 Web 聊天界面（`src/main/resources/static/index.html`），支持：

- **流式对话**：实时逐字输出 AI 回复（SSE）
- **Markdown 渲染**：自动渲染代码块、表格、列表等
- **命令面板**：输入 `/` 唤起快捷命令列表
- **会话管理**：支持清空对话历史

![img](https://oss-ata.alibaba.com/article/2026/04/23d39606-5fa4-4e3a-aa6b-7603e823e42c)

### **API 直接调用**

```
# 非流式对话
curl -X POST http://localhost:8080/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "你好，介绍一下你的能力", "sessionId": "test-001"}'
# 流式对话（SSE）
curl -X POST http://localhost:8080/api/chat/stream \
  -H "Content-Type: application/json" \
```

# **一、核心编排器：AgentCore**

`AgentCore` 是整个系统的"大脑"，负责编排对话的完整流程：**意图识别 → RAG 注入 → 记忆管理 → 模型调用 → 工具执行**。

## **1.1 对话流程**

```
用户输入
  │
  ▼
意图识别（IntentRecognizer）
  │ 判断：这是知识问答还是通用对话？
  ▼
RAG 注入（RagService）
  │ 如果是知识问答，检索知识库，将参考资料拼入上下文
  ▼
记忆管理（ChatMemory）
  │ 自动摘要压缩 → 构建消息列表
  ▼
模型调用（ChatClient + ToolCallbacks）
  │ LLM 决策：直接回答 or 调用工具？
  │ 如果调用工具 → 执行工具 → 将结果返回 LLM → 继续决策（ReAct 循环）
  ▼
返回最终回复
```

核心代码（`AgentCore.chat()`）：

```
public String chat(String sessionId, String userInput) {
    ChatMemory memory = getOrCreateMemory(sessionId);
    // 1. 意图识别
    Intent intent = intentRecognizer.recognize(userInput);
    // 2. 如果是 RAG 意图，先检索知识库并注入上下文
    if (intent == Intent.RAG && ragService.isKnowledgeLoaded()) {
        String ragContext = ragService.query(userInput);
        if (ragContext != null && !ragContext.isBlank()) {
            String enrichedInput = "以下是从知识库中检索到的相关参考资料，"
                    + "请结合这些资料回答用户的问题：\n\n"
                    + ragContext + "\n\n用户问题：" + userInput;
            memory.addMessage(new UserMessage(enrichedInput));
        } else {
            memory.addMessage(new UserMessage(userInput));
        }
    } else {
        memory.addMessage(new UserMessage(userInput));
    }
    // 3. 构建 Prompt 并调用大模型（getMessages 内部自动触发摘要压缩）
    List<Message> messages = memory.getMessages();
    Prompt prompt = new Prompt(messages, buildChatOptions());
    ChatClient.ChatClientRequestSpec requestSpec = chatClient.prompt(prompt);
    if (!toolCallbacks.isEmpty()) {
        requestSpec.toolCallbacks(toolCallbacks.toArray(new ToolCallback[0]));
    }
    String response = requestSpec.call().content();
    memory.addMessage(new AssistantMessage(response != null ? response : ""));
    return response != null ? response : "";
}
```

## **1.2 Agent Loop**

Spring AI已实现Agent Loop，具体路径为org.springframework.ai.chat.client.advisor.ToolCallAdvisor#adviseCall

```
boolean isToolCall = false;

do {

    // Before Call
    var processedChatClientRequest = ChatClientRequest.builder()
       .prompt(new Prompt(instructions, optionsCopy))
       .context(chatClientRequest.context())
       .build();

    // Next Call
    processedChatClientRequest = this.doBeforeCall(processedChatClientRequest, callAdvisorChain);

    chatClientResponse = callAdvisorChain.copy(this).nextCall(processedChatClientRequest);

    chatClientResponse = this.doAfterCall(chatClientResponse, callAdvisorChain);

    // After Call

    // TODO: check that this tool call detection is sufficient for all chat models
    // that support tool calls. (e.g. Anthropic and Bedrock are checking for
    // finish status as well)
    ChatResponse chatResponse = chatClientResponse.chatResponse();
    isToolCall = chatResponse != null && chatResponse.hasToolCalls();

    if (isToolCall) {
       Assert.notNull(chatResponse, "redundant check that should never fail, but here to help NullAway");
       ToolExecutionResult toolExecutionResult = this.toolCallingManager
          .executeToolCalls(processedChatClientRequest.prompt(), chatRespo