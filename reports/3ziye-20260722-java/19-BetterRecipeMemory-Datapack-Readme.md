# BetterRecipeMemory

移除原版約 1,572 條**配方成就**(`minecraft:recipes/*`),把每位上線玩家物化的成就物件從
**1688 → 127**(記憶體 -92%);同時用「首登一次性觸發」把每位玩家的**配方書塞滿** ——
玩家「點配方一鍵帶料」的合成體驗完全不變,甚至更好。

*crafted by 廢土貓大 LogoCat · 廢土 · mcfallout.net*

本 repo 含兩個部分:

| 目錄 | 產物 | 角色 |
|---|---|---|
| [`datapack/`](datapack/) | `dist/BetterRecipeMemory.zip` | **主體** —— 移除配方成就 + 首登塞滿配方書 |
| [`paper-plugin/`](paper-plugin/) | `dist/BetterRecipeMemoryPlugin-26.2-1.jar` | **配套** —— 吞掉 datapack 造成的「孤兒成就」log 洪水(成就存檔開=可選;關=必裝,見 E4) |

- 適用:Paper / MC 26.2(pack_format 107;其他版本見〔技術版〕的 pack_format 一節)
- 安裝:zip 丟進主世界 `datapacks/`;jar 丟進 `plugins/`;重啟生效
- 實測:一台外掛數量龐大的 Paper 26.2 伺服器通過 —— `Loaded 1688 advancements → 127`、recipes 數不變、零載入錯誤

### 作者 / 查詢指令

| 位置 | 指令 | 顯示 |
|---|---|---|
| 外掛 | `/brm about` · `/brm help` · `/brm version` | 作者與專案卡片 |
| datapack | `/function fallout:about` | 作者與專案卡片(遊戲內) |
| 後台 | 伺服器啟動時 | 兩者都印出 `crafted by … LogoCat · mcfallout.net` |

## 🔬 實驗區(正式環境實測)

| 文件 | 內容 |
|---|---|
| [`experiments/EXPERIMENTS.md`](experiments/EXPERIMENTS.md) | 五組實驗 + 完整算式:比值(127 vs 1688,精確整除)、時間序列 lockstep、每玩家 bytes 精算(E6)、log 噪音 A/B |
| [`experiments/data/`](experiments/data/) | **原始證據** —— `jcmd GC.class_histogram` 直方圖。官方列(net.minecraft / org.bukkit / io.papermc / JDK)逐字保留;第三方 class 名稱一律隱去,見 [`experiments/data/README.md`](experiments/data/README.md) |
| [`experiments/REPRODUCE.md`](experiments/REPRODUCE.md) | 逐步教學:用 JDK 內建 `jcmd` + `grep` 在你自己的伺服器上量出同樣的數字 |

一句話結論:**每玩家成就物件 1688 → 127(-92.5%);數量與線上玩家數完全 lockstep,六次取樣比值全部整除 —— 機制級因果,不是統計巧合。**

---

## 一、白話版

### 問題是什麼

為了做「撿到鐵錠 → 配方書自動出現鐵劍」這個功能,原版 Minecraft 替**每一位玩家**掛了
**約 1,572 個感應器**(配方成就),每個全天候盯著「他撿到某某材料了嗎?」。感應器又肥又重
—— 每人約 **1,688 個活物件(≈0.5–1 MB)**,玩家每次上線重新掛一整套、下線變垃圾。玩家多、
重登頻繁的伺服器,記憶體就是被這個灌爆的。

### 玩家真正用到的是什麼

玩家在意的體驗 —— 開工作台、點配方、材料自動排好 —— 讀的是**配方書**(哪些配方打了勾),
根本不看感應器。感應器唯一的工作就是幫那張清單慢慢打勾,順便跳一個沒人看的 toast。

### 這個 datapack 做的事

1. **把約 1,572 個感應器整批拆掉**(datapack `filter` 把配方成就從遊戲移除)
2. **玩家第一次進服的瞬間,直接把整本配方書打滿勾**(隱形成就觸發 `recipe give`,一次性、之後永不重跑)

配方書只是一張名字列表(~65 KB),而被拆掉的感應器約 1 MB。

### 配套外掛在幹嘛

拆掉感應器後,**既有玩家**的存檔裡還留著舊感應器紀錄。他們下次上線,遊戲會對每一條印一行
警告(每人最多 ~1,572 行)。無害,但會洗版後台。配套外掛就是把**這一種訊息**(只有這種)吞掉。
要不要裝取決於你的成就存檔設定(見 [E4](experiments/EXPERIMENTS.md)):vanilla 存檔開 →
下次存檔即清、數天自然消退,可裝可不裝;vanilla 成就存檔**關**(持久化交給外部同步系統)→
檔案永不重寫,**每次登入重印一整批**,此時實質必裝。

### 玩家會感覺到什麼

| | 之前 | 之後 |
|---|---|---|
| 點配方一鍵帶料 | ✅ | ✅ 一模一樣 |
| 合成本身 | ✅ | ✅(從來不歸這系統管) |
| 新手配方書 | 要慢慢撿材料解鎖 | **進服就全滿** |
| 「配方已解鎖」toast | 常常跳 | 首登跳一批,之後安靜 |

---

## 二、技術版

### datapack 機制

**1. Filter 移除配方成就**(`datapack/pack.mcmeta`):

```json
{
  "pack": {
    "pack_format": 107,
    "min_format": 107,
    "max_format": 107,
    "description": "..."
  },
  "filter": {
    "block": [
      {"namespace": "minecraft", "path": "advancement/recipes/.*"},
      {"namespace": "minecraft", "path": "advancements/recipes/.*"}
    ]
  }
}
```

datapack `filter`(MC 1.19+ 官方機制)把更低優先層(含原版內建 pack)中符合 pattern 的檔案從
載入剔除。26.2 的實際目錄是**單數** `data/minecraft/advancement/recipes/`(1,572 檔,佔全部
1,703 條成就的 92%,已從 server jar 清點);複數那條 pattern 是舊版命名保險,匹配不到任何東西、無害。

> `min_format` / `max_format` 為必填:26.2 的 metadata codec(NMS `packs/metadata/pack/PackFormat.java`)
> 規定 pack_format > 81 的包必須宣告這兩欄;缺少時每次開機噴一行
> `Error reading pack metadata, attempting fallback type`(fallback 仍會正確載入,但別依賴它)。
> int 值 107 會自動展開為 min=107.0、max=107.*;**不可**加 `supported_formats`(>81 已棄用,加了直接報錯)。
>
> `pack_format: 107` 來源:server jar 的 `version.json` → `pack_version.data_major`
> (`unzip -p paper-26.2.jar version.json`)。

移除後:成就登錄表 1703 → 131(含本包 +1);`PlayerAdvancements` 不再為任何玩家物化這些條目
→ 每上線玩家的 `AdvancementProgress` 物件 1688 → 127;join 時的全登錄表掃描
(`checkForAutomaticTriggers` / listener 註冊)規模同步縮減。

**2. 首登一次性塞滿配方書**:

- `datapack/data/fallout/advancement/fill_recipe_book.json`:無 `display`(隱形、無 toast)的成就,
  criterion = `minecraft:tick` trigger → 玩家第一次出現在該伺服器時自動達成
- `rewards.function` = `fallout:fill_recipe_book` → 以該玩家身分執行 `recipe give @s *`
- 達成狀態持久化於玩家成就檔;配方書清單持久化於玩家檔 `recipeBook` → **同一玩家永不重複觸發,零週期工作**

### 配套外掛機制(`paper-plugin/`)

- **一個 log4j filter,別無其他**:`onLoad` 時掛到 root LoggerConfig(vanilla 的
  `net.minecraft.server.PlayerAdvancements` logger 沒有獨立 config,事件流經 root,攔得到)
- 只 `DENY` 同時滿足「以 `Ignored advancement '` 開頭」且「含 `doesn't exist anymore`」的訊息;其餘一律 `NEUTRAL`
- 失敗安全:install 包在 `catch (Throwable)`,掛不上頂多回到「有噪音」的原狀
- 自測掛鉤:`-Dbetterrecipememory.selftest=true` 開機時對 vanilla logger 丟一則同款誘餌訊息;filter 有效則該行不出現在 log
- 建置:`JAVA_HOME=<jdk25> mvn package`(paper-api 26.2;log4j-core 為 provided,Paper runtime 內建)

### 成本 / 收益

| 項目 | 拆掉的 | 加回的 |
|---|---|---|
| 每上線玩家 heap | ~0.5–1 MB(1688 物件 + map) | ~65 KB(recipeBook set,key 為共享實例) |
| 玩家檔磁碟 | 成就 JSON 大幅縮減 | recipeBook 清單 ~10–20 KB(gzip) |
| join 時物化成本 | 1688 物件/次 | 127 物件/次 |

### 安裝

```bash
# datapack(必要):放主世界(server.properties 的 level-name)的 datapacks/,重啟生效
cp dist/BetterRecipeMemory.zip <server>/<level-name>/datapacks/

# 配套外掛(可選,消 log 噪音):
cp dist/BetterRecipeMemoryPlugin-26.2-1.jar <server>/plugins/
```

### 部署前必查:limited_crafting 必須為 false

唯一遊戲性風險:若 gamerule「只能合成已解鎖配方」開啟,拆掉