# Aifei

世界首个 AI Coding 框架。

## 简介

Aifei 是世界首个 AI Coding 框架。

Aifei 开创 Just Service 开发范式，面向 AI Coding 设计，从结构层面减少 Token 消耗、缩短上下文长度、提升 Attention 浓度，极大提升代码生成质量、生成稳定性与开发体验。

Aifei 采用极简设计，内核仅 3333 行代码且无第三方依赖，将极简推至全新高度。从 JFinal 到 Aifei，专注极简设计 15 年。

Aifei 大幅消除传统框架中被视为必需的概念，如 Controller、Render、Repository、Mapper，极小化认知负荷与上下文噪音，极大化模型注意力浓度。

Just Service. Only Aifei can do.

## 为什么是 Aifei

过去三年，AI 写代码的能力快速跃升，代码生成正从辅助走向主导。人类完全手写代码的时代正在过去，开发者角色将转向决策与审查。

围绕 AI Coding 的模型、IDE 与各类工具快速发展，但从框架层面为 AI Coding 而设计的服务端 framework 仍然缺位。

现有主流框架几乎都诞生于**人类手写代码**的时代，它们服务的是人类开发者的认知方式、组织方式与工程习惯。

但 AI Coding 需要的第一性约束已经不同。AI 更需要的是：

- 更少的 Token 消耗
- 更高的 Attention 浓度
- 更低的上下文噪音
- 更高的上下文信噪比
- 更稳定的生成模式
- 更直接的业务表达方式

框架不再只是人类组织代码的工具，也会成为大模型理解、生成与维护代码的上下文结构。现有框架并未围绕这些核心需求构建。Aifei 正是为此而生。

## 快速上手

### Service

Just Service 开发范式之下，在框架搭好之后，模型只需专注生成业务代码。

在 AI Coding 场景中，这意味着模型只需围绕单一 Service 层生成代码，无需在 Controller、Service、Dao、Repository、Mapper、Render 等多层结构之间进行映射、拆分与补全，从而显著减少 Token 消耗，降低上下文噪音，并提升生成稳定性与代码质量：

```java
@Path("/vip")
public class VipService {

    // 查询、排序、分页
    public Page<Vip> index(Map<?, ?> filter, int pageNum, int pageSize) {
        String sql = "select * from vip #where(...) #and(...) ...";
        return Vip.sql(sql, filter).paginate(pageNum, pageSize);
    }

    // 插入
    public Out insert(Vip vip) {
        vip.insert();
        return Out.ok("插入成功");
    }
    
    // 修改
    public Vip edit(int id) {
        return Vip.findById(id);
    }

    // 更新
    public Out update(Vip vip) {
        vip.update();
        return Out.ok("更新成功");
    }

    // 删除
    public Out delete(int id) {
        Vip.deleteById(id);
        return Out.ok("删除成功");
    }
}
```

### 配置

Aifei 配置在 AifeiConfig 接口中集中管理。

集中式配置避免了分散式约定、隐式行为与多入口配置带来的上下文噪音，使 AI 在生成、理解与修改项目结构时更稳定、更直接、更可预测。

以 VIP 订阅会员项目配置为例：

```java
/**
 * Aifei 配置中心
 */
public class AppConfig implements AifeiConfig<In, Out> {

    Prop p;

    /**
     * 偏好配置
     */
    public void config(Settings<In, Out> settings) {
        // 加载配置
        p = PropKit.use("app-config.txt");

        // 配置日志
        settings.setLogFactory(new Log4jLogFactory());

        // 配置 Server、Dispatcher、Handler
        settings.setServer(new UndertowServer(), new IoDispatcher());
        settings.addHandler(new IoHandler());

        // 定制 action 注入参数，注入登录账号
        settings.configArgument(kit -> {
            kit.register(Account.class, LoginAccountArgument.class);
        });
    }

    /**
     * 路由配置
     */
    public void config(Routes routes) {
        routes.scan("cn.aifei.vip", new AuthInterceptor());
    }

    /**
     * 插件配置
     */
    public void config(Plugins plugins) {
        DruidSupplier druidSupplier = new DruidSupplier(p.get("jdbcUrl"), p.get("user"), p.get("password"));
        AifeiDbPlugin dbPlugin = new AifeiDbPlugin("main", druidSupplier);
        dbPlugin.addModelSet(new ModelSet());
        dbPlugin.config(c -> c.setPrintSql(true));
        plugins.add(dbPlugin);
    }
}
```

### 启动

main 方法中调用 Aifei.start(...) 即可启动：

```java
public class AifeiVip {
    public static void main(String[] args) {
        Aifei.start(new AppConfig(), args);
    }
}
```

### HIO

Aifei 顶层采用 HIO 结构，即 Handler、Input、Output 组成的处理模型。

该模型将请求处理流程收敛为明确、稳定且可预测的结构，有助于 AI 在生成代码时形成一致模式，减少理解成本与结构歧义。

三者均由用户自行定义，不依赖 Servlet，可按需切换底层 IO 实现。

## 核心理念

### Just Service

Just Service 是 Aifei 成为 AI Coding 框架的核心。

它消除了传统框架中的 Controller、Render、Dao、Repository、Mapper 等非业务性结构，将代码收敛为单一的 Service 层。

这一设计并非只是**更少代码**，而是直接作用于大模型的工作机制：

- 显著减少 Token 消耗，缩短上下文长度
- 提升注意力浓度，让模型聚焦于业务语义
- 降低上下文噪音，减少无关结构对生成的干扰
- 提供更稳定的生成模式，避免结构复杂导致输出波动

在传统框架中，大量分层结构与样板代码会占据上下文预算，稀释模型对核心业务的关注。而 Just Service 将上下文尽可能留给业务逻辑本身。

在框架搭好之后，AI 只需围绕 Service 生成代码，无需在多层结构之间来回映射与补全，从而获得更直接、更稳定的生成结果。

例如：

```java
@Path("/user")
public class UserService {
    public User getById(int id) {
        return User.findById(id);
    }
}
```

在 Web 场景下，以上代码可通过访问 `/user?id=...` 直接调用。

注：Aifei 是通用服务端框架，不限定于 Web 系统，Web 只是应用场景之一。

### 上下文腐化

上下文腐化（Context Rot）是 AI Coding 的隐性瓶颈。大模型虽然拥有越来越长的上下文窗口，但**可容纳**并不等于**可稳定使用**。随着上下文不断变长，模型并不会稳定、均匀、无损地利用其中所有信息。

在传统框架中，Controller、Dao、Repository、Mapper、Render 等非业务结构，以及样板代码、重复配置、历史上下文与无关文件，会持续占据上下文预算，稀释模型对当前业务目标的注意力。

AI Coding 的关键不只是让模型拥有更大的上下文窗口，而是让项目结构天然具备更高的上下文信噪比与注意力浓度。换句话说，框架要优化的不是名义上下文窗口，而是**有效上下文窗口**。Just Service 正是通过减少非业务结构，将上下文尽可能留给业务逻辑本身。

## 数据库访问

### 开始

Aifei 的数据库模块继承了 jfinal 数据库模块的大部分核心 API 与使用体验。

从 API 使用层面看，Aifei 相比 jfinal 的主要变化在于：查询改为链式调用，并新增 `sql(...)` 方法统一承载 SQL 与参数。

这一设计并非只是 API 风格变化，而是将数据库访问收敛为统一、稳定、可预测的生成模式：

- SQL 始终通过单一入口表达
- 参数传递方式始终保持一致
- 调用结构不再分散

这使 AI 在生成数据库代码时，无需在多种写法之间选择，从而减少结构分叉、降低上下文复杂度，并提升生成稳定性。

深入底层实现，Aifei 数据库模块采用全新架构，代码量缩减近 50%，进一步减少理解成本与 Token 消耗。

### Db + Row 模式

Aifei db 的所有数据库操作通过 Db + Row 模式实现。

这一模式将数据访问收敛为单一抽象，避免 DAO、Mapper、Entity 等多套体系并存带来的结构分裂问题。

在 AI Coding 场景中，这意味着：

- 所有数据操作路径一致
- 无需在多种访问模型之间切换
- 上下文中只存在一套数据操作语义

从而显著降低上下文噪音，并帮助模型形成稳定的生成模式。

### Model

Aifei db 并不提供独立的 Model 层，而是将 Model 视为一种 Row。

这一设计减少了抽象层级，使数据访问不再存在 Row / Model / DTO 等多重语义切换。

对于大模型来说，这意味着：

- 更少的概念切换
- 更短的上下文路径
- 更稳定