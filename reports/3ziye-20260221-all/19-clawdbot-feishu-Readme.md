# clawd-feishu

Feishu/Lark (飞书) channel plugin for [OpenClaw](https://github.com/openclaw/openclaw).

> **中文社区资料** - 配置教程、常见问题、使用技巧：[Wiki](https://github.com/m1heng/clawdbot-feishu/wiki)
>
> **Contributing / 贡献指南**: [CONTRIBUTING.md](./CONTRIBUTING.md)

[English](#english) | [中文](#中文)

---

## English

### Installation

```bash
openclaw plugins install @m1heng-clawd/feishu
```

> [!IMPORTANT]
> **Windows Troubleshooting (`spawn npm ENOENT`)**
>
> If `openclaw plugins install` fails, install manually:
>
> ```bash
> # 1. Download the package
> curl -O https://registry.npmjs.org/@m1heng-clawd/feishu/-/feishu-0.1.3.tgz
>
> # 2. Install from local file
> openclaw plugins install ./feishu-0.1.3.tgz
> ```

### Upgrade

```bash
openclaw plugins update feishu
```

### Configuration

1. Create a self-built app on [Feishu Open Platform](https://open.feishu.cn)
2. Get your App ID and App Secret from the Credentials page
3. Enable required permissions (see below)
4. **Configure event subscriptions** (see below) ⚠️ Important
5. Configure the plugin:

#### Required Permissions

| Permission | Scope | Description |
|------------|-------|-------------|
| `im:message` | Messaging | Send and receive messages |
| `im:message.p2p_msg:readonly` | DM | Read direct messages to bot |
| `im:message.group_at_msg:readonly` | Group | Receive @mention messages in groups |
| `im:message:send_as_bot` | Send | Send messages as the bot |
| `im:resource` | Media | Upload and download images/files |

#### Optional Permissions

| Permission | Scope | Description |
|------------|-------|-------------|
| `contact:user.base:readonly` | User info | Get basic user info (required to resolve sender display names for speaker attribution) |
| `im:message.group_msg` | Group | Read all group messages (sensitive) |
| `im:message:readonly` | Read | Get message history |
| `im:message:update` | Edit | Update/edit sent messages |
| `im:message:recall` | Recall | Recall sent messages |
| `im:message.reactions:read` | Reactions | View message reactions |

#### Tool Permissions

**Read-only** (minimum required):

| Permission | Tool | Description |
|------------|------|-------------|
| `docx:document:readonly` | `feishu_doc` | Read documents |
| `drive:drive:readonly` | `feishu_drive` | List folders, get file info |
| `wiki:wiki:readonly` | `feishu_wiki` | List spaces, list nodes, get node info, search |
| `bitable:app:readonly` | `feishu_bitable` | Read bitable records and fields |
| `task:task:read` | `feishu_task_get` | Get task details |

**Read-write** (optional, for create/edit/delete operations):

| Permission | Tool | Description |
|------------|------|-------------|
| `docx:document` | `feishu_doc` | Create/edit documents |
| `docx:document.block:convert` | `feishu_doc` | Markdown to blocks conversion (required for write/append/create_and_write; also used by `feishu_drive.import_document`) |
| `drive:drive` | `feishu_doc`, `feishu_drive` | Upload images to documents, create folders, move/delete files |
| `wiki:wiki` | `feishu_wiki` | Create/move/rename wiki nodes |
| `bitable:app` | `feishu_bitable` | Create/update/delete bitable records and manage fields |
| `task:task:write` | `feishu_task_create`, `feishu_task_update`, `feishu_task_delete` | Create/update/delete tasks |

> Task scope names may vary slightly in Feishu console UI. If needed, search for Task-related permissions and grant read/write accordingly.

#### Drive Access ⚠️

> **Important:** Bots don't have their own "My Space" (root folder). Bots can only access files/folders that have been **shared with them**.

To let the bot manage files:
1. Create a folder in your Feishu Drive
2. Right-click the folder → **Share** → search for your bot name
3. Grant appropriate permission (view/edit)

Without this step, `feishu_drive` operations like `create_folder` will fail because the bot has no root folder to create in.

#### Wiki Space Access ⚠️

> **Important:** API permissions alone are not enough for wiki access. You must also add the bot to each wiki space.

1. Open the wiki space you want the bot to access
2. Click **Settings** (gear icon) → **Members**
3. Click **Add Member** → search for your bot name
4. Select appropriate permission level (view/edit)

Without this step, `feishu_wiki` will return empty results even with correct API permissions.

Reference: [Wiki FAQ - How to add app to wiki](https://open.feishu.cn/document/server-docs/docs/wiki-v2/wiki-qa#a40ad4ca)

#### Bitable Access ⚠️

> **Important:** Like other resources, the bot can only access bitables that have been **shared with it**.

To let the bot access a bitable:
1. Open the bitable you want the bot to access
2. Click **Share** button → search for your bot name
3. Grant appropriate permission (view/edit)

The `feishu_bitable` tools support both URL formats:
- `/base/XXX?table=YYY` - Standard bitable URL
- `/wiki/XXX?table=YYY` - Bitable embedded in wiki (auto-converts to app_token)

#### Event Subscriptions ⚠️

> **This is the 