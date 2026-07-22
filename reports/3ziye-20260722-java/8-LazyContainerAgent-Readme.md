# LazyContainerAgent

**中文** ｜ [English](README.en.md)

> **箱子物品「延遲反序列化(不急著把資料拆解成遊戲內物件,拖到真的要用才拆)+ 沒碰過就原樣寫回」的 Java agent。**
> 針對 Paper 26.2,把 chunk(遊戲世界切成一塊一塊的地圖區域,伺服器以此為單位載入/卸載)載入時「立刻把每個箱子的物品從 NBT(Minecraft 儲存物品/方塊資料的二進位格式)解包」與卸載時「重新打包」這兩筆白工砍掉。

🧠 **經 Claude Fable 5 對抗審計**(49 個獨立 agent 分工找碴+交叉反駁,詳見 [`FABLE5-AUDIT.md`](FABLE5-AUDIT.md)):14 條發現全數逐一核實、0 條被推翻;確認**記憶體有界不洩漏、存檔淨省不做白工、正常玩家操作零掉物風險**;找到並已修復一個需要管理員指令才會踩到的邊角漏洞(容器複製/直接改存檔資料時可能共用到同一份資料)。

⚠️ **這不是外掛(plugin),是 Java agent** —— 用 `-javaagent:` 掛在 JVM 上,**不要丟 `plugins/`**(丟了沒用)。

> 🔒 **版本敏感(務必先讀)**
> 本 agent 以 bytecode **直接織入 Paper 26.2 / Java 25** 的內部類別(template classfile major 69),屬**版本綁死**的工具。
> - **僅適用於 Paper 26.2 + Java 25。** 任何其他 Minecraft 版本或 Java 版本,**一律不要直接套用**。
> - 換版必須:① 以對應版本的 NMS 重新編譯 `template/`、② 將 ASM 升級到能解析目標 classfile 版本、③ 重新以 shadow 模式驗證。
> - 版本不符時會在**開機或首次載入箱子時直接拋出例外**(`VerifyError` / `NoSuchMethodError`)。這是**刻意的「安全停機」設計——絕不會靜默改壞或弄丟資料**,但該節點會無法啟動,因此**務必先在測試環境驗證**再上線。
> - 測試素材(region / 物品 dump)為目標版格式,請勿在其他版本載入。
> - 26.2 實機測試報告:[`docs/test-reports/26.2.md`](docs/test-reports/26.2.md)。

---

## 快速上手

> 前提:**Paper 26.2 + Java 25**(其他版本請先看上面的「版本敏感」)。

**1. 放 jar** —— 把 `LazyContainerAgent.jar` 放到節點看得到的位置(跟你的伺服器 jar 放同一層最省事)。**不要丟進 `plugins/`**:它是 Java agent、不是外掛,丟了沒作用。

**2. 改啟動參數** —— 在 `java` 那行、`-jar` 的**前面**,加上以下幾段(第一次**請先用 shadow 驗證模式**):

```bash
java ... \
  -javaagent:LazyContainerAgent.jar \
  -Dlazycontainer.shadow=true \
  -Dlazycontainer.verbose=true \
  -jar <你的 Paper>.jar nogui
```

**3. 先驗證,別急著上真效能** —— 開著 `shadow=true` 跑個幾天。它會把優化後的輸出跟原版做法**逐位元組對照**:只要 `shadowMismatch` 一直是 **0**,就代表輸出跟原版完全一致、**資料零風險**。代價是這階段兩套都做、暫時不會變快。
> - 開機 log 應出現 `[LazyContainer] agent installed … [SHADOW mode]`。
> - verbose 每隔一段印一行 `stash=… rawSave=… shadowMismatch=0 …`;`stash` 持續往上爬 = 正在運作。

**4. 確認沒問題,再換真效能** —— 跑數天 `shadowMismatch=0`、也沒玩家回報少東西,就把 `-Dlazycontainer.shadow=true` 拿掉、重啟。這時「沒人碰過的箱子」會直接原樣寫回(跳過打包),效能才真正省下來。

**回滾** —— 把那幾段 `-D` 與 `-javaagent` 拿掉、重啟,立刻回 100% 原版,**不需要任何資料遷移**(硬碟格式從頭到尾沒被改過)。

---

## 這東西在解決什麼

開伺服器開久了,你大概都會撞上一種很微妙的卡頓:

明明沒什麼人在線上,主執行緒卻莫名其妙地忙。

抓 spark 一看,真兇往往不是怪、不是紅石——是**箱子**。

更精確一點,是「箱子裡的東西」。Minecraft 把物品存在硬碟上時是壓縮打包的;每當一塊地圖(chunk)被載進記憶體,伺服器就把那一區**每一個箱子、每一格物品,從 NBT 完整拆包一遍**;這塊地圖要卸載時,又**整批重新打包**寫回去。

問題是——那些箱子,絕大多數從載入到卸載,**根本沒人去開**。

拆了、又包回去,中間沒人看一眼。純白工。

而且 1.21 之後物品帶了 data components(附魔、lore、自訂名稱、容器內容…),拆包打包更貴。一座放滿地圖畫的倉庫、一條塞滿界伏盒的儲存線,光是「被載入」這件事,就能把主執行緒吃掉好幾成——在廢土(約 110 個 Paper 節點)的正式環境裡,負載最重的節點一度有 **45%** 的主執行緒,就卡在這一條鏈上:

```
ChunkFullTask.run → … → ChestBlockEntity.loadAdditional
  → ContainerHelper.loadAllItems     ← 拆包箱子物品 ≈ 45%
```

面對這種卡頓,最輕鬆的解法是**禁止**——限制每個箱子能放幾張地圖、叫大家別蓋大倉庫。但這就像為了省電把冰箱拔掉:LAG 是不見了,玩家的東西也跟著不見了。我一向不信這套——**能用技術克服的,就不該用規則去閹割玩法。**

所以這個 agent 做的事,白話講就一句:

**沒人要看的箱子,別急著拆;沒人動過的箱子,就原封不動地放回去。**

載入時,先把箱子的原始資料**收著**、先不拆;真的有人去開、漏斗去抽、比較器去讀,才當場拆**那一個**。從載入到卸載都沒人碰的,就把當初收著的那包原始 bytes **逐位元組原樣寫回**——完全跳過重新打包。

對玩家來說,箱子裡裝什麼、擺在第幾格,**一模一樣**,你驗證不出任何差別。差別只在伺服器:那一大批「拆了又包、卻根本沒人看」的白工,消失了。

---

## 效能實證(206 層波動拳 → 0%)

vanilla 載入一個放滿地圖畫/唱片的箱子,光把物品從 NBT 解出來,呼叫堆疊就深到 **~206 層**——因為資料是真的巢狀(箱子 → 界伏盒 → 地圖畫 → lore → 不同顏色文字)再乘上 Mojang codec 框架每層疊 15-20 個 frame。最底層那一行只是在 `TextColor.parseColor`(解析 lore 顏色)/ `String.equals`(比對欄位名)。

<p align="center">
<img src="docs/img/callchain-206-before.png" width="360" alt="206 層呼叫鏈(波動拳)">
&nbsp;&nbsp;
<img src="docs/img/improved-after.png" width="440" alt="改善後">
</p>

`.lctest` 同一塊密集容器 chunk、`forceload` churn、跑兩輪:

| Run | 模式 | spark | 容器解碼佔主執行緒 | profile 節點數 | 最深呼叫 |
|---|---|---|---|---|---|
| 1 | vanilla | `WOVkupfiJx` | **62.17%** | 3378 | 200 層 |
| 1 | **agent** | `wGDbUTbZKN` | **0.00%** | 482 | 9 層 |
| 2 | vanilla | `AjXLAdXzTd` | **65.65%** | 4305 | 200 層 |
| 2 | **agent** | `caXFofKSVQ` | **0.00%** | 763 | 36 層 |

整座解碼塔在 agent profile **直接消失**。4 份 spark 原始檔(已靜態存檔避免連結失效)+ 完整 206 行鏈 + 說明:[`docs/spark/`](docs/spark/SUMMARY.md)。

> ⚠️ 62~66% 是「容器解碼**單獨隔離**」的壓力測;真實混合負載下佔比為載入 **~24%** + 卸載 **~11%**(負載最重的節點可達 **~45%**)。省的是解/打包 CPU,不省 I/O / GC。

---

## 怎麼運作

### 白話比喻
像搬家公司本來**每個經過倉庫的箱子都拆開檢查再封回**(連沒人問的也拆)。改成:**沒人要看的別拆;沒動過的原封出貨。**

### 技術機制
注入 NMS 容器類別,加入兩個合成欄位 + 改寫存取點:

| 動作 | 計數器 | 說明 |
|---|---|---|
| **延遲載入** | `stash` | `loadAdditional` 不呼 `ContainerHelper.loadAllItems`,改抓未解碼的原始 `Items` ListTag 暫存、標記 `pending`。**跳過解包。** |
| **存取時物化** | `ensure` | 首次有人呼 `getItems()/getContents()` → 才把暫存的 raw 解進清單(只解這一個)。 |
| **原樣寫回** | `rawSave` | 卸載存檔時若該容器全程沒被碰(`pending`)→ 把原始 bytes 逐位元組寫回。**跳過打包。** |
| **退回 eager** | `eagerLoad` | input 不是 `TagValueInput`(理論上不會)→ 安全退回原本 vanilla 行為。 |

涵蓋型別:`ChestBlockEntity`、`BarrelBlockEntity`、`ShulkerBoxBlockEntity`。
**唯一咽喉 = `getItems()`**:NMS `BaseContainerBlockEntity` 所有容器讀寫(isEmpty/getItem/removeItem/setItem/clearContent/掉落/比較器…)都經它,守一個即覆蓋全部;CraftBukkit 的 `getContents()` 會繞過,額外守。`getContainerSize()` 不經內容(結構性),不守。

---

## 架構(怎麼注入的)

純外掛(plugin)無法覆寫 NMS(Minecraft 伺服器內部程式碼)裡標記 `final`(禁止被子類別覆寫)的方法,所以用 **Java agent + ASM(操作 Java bytecode、能在類別載入當下動態改寫它的工具)注入**:

1. **`LazyContainerAgentMain`**(premain,JVM 啟動時最先跑的進入點):把整個 jar 用 `appendToBootstrapClassLoaderSearch` 掛上 bootstrap classl