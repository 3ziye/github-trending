# pordee (พอดี)

> ทำไมใช้คำเยอะ ตอบสั้นๆ ก็เข้าใจ

ได้แรงบันดาลใจมาจาก [caveman](https://github.com/JuliusBrussee/caveman) — pordee เป็นรุ่นภาษาไทยที่ตัด token ทิ้งโดยไม่เสียความถูกต้องทาง technical

---

`pordee` คือ Claude Code plugin สั่งให้ agent ตอบภาษาไทยกระชับ — ตัดคำสุภาพ (ครับ/ค่ะ/นะคะ), คำลังเล (อาจจะ/น่าจะ), และคำเชื่อมที่ไม่จำเป็นทิ้ง เก็บ technical term อังกฤษไว้ตามเดิม

ผล: ใช้ token น้อยลง 60-75% เนื้อหาเท่าเดิม

---

## ติดตั้ง

### ผ่าน Claude Code plugin (แนะนำ)

```bash
claude plugin marketplace add kerlos/pordee
claude plugin install pordee@pordee
```

หลังติดตั้งเสร็จ hooks จะถูก register อัตโนมัติ — เริ่ม session ใหม่แล้ว `/pordee` ใช้ได้ทันที

---

## วิธีใช้

### Slash command

| คำสั่ง | ผล |
|---|---|
| `/pordee` | เปิด default level (full) |
| `/pordee lite` | โหมดเบา — ตัดคำสุภาพและ filler ออก แต่ grammar เต็ม |
| `/pordee full` | โหมดเต็ม — ตัดให้สั้นที่สุด |
| `/pordee stop` | ปิด |
| `/pordee-stats` | ดูสถิติ token ของ session ปัจจุบัน |
| `/pordee-stats --share` | สรุปสถิติ 1 บรรทัด (copy-paste ได้) |

### Keyword (ไม่ต้องพิมพ์ slash)

พิมพ์คำเหล่านี้เป็นข้อความปกติในแชต — pordee จะเปิด/ปิดให้อัตโนมัติ ต้องเป็นข้อความทั้งบรรทัด ไม่ใช่ส่วนหนึ่งของประโยค

| Keyword | ผล |
|---|---|
| `พอดี` | เปิด |
| `พอดีโหมด` | เปิด |
| `พูดสั้นๆ` | เปิด |
| `หยุดพอดี` | ปิด |
| `พูดปกติ` | ปิด |

---

## ระดับ (Levels)

### 🪶 Lite — `/pordee lite`

ตัดคำสุภาพ (ครับ/ค่ะ/นะคะ), คำลังเลใจ (อาจจะ/น่าจะ/จริงๆแล้ว), และคำทักทาย (ได้เลยครับ/แน่นอน) ทิ้ง แต่เก็บ grammar เต็ม อ่านแล้วยังเป็นภาษาไทยปกติ professional

### ⚡ Full — `/pordee` หรือ `/pordee full` (default)

ตัดเหมือน lite + ตัด particle ที่ซ้ำซ้อน (ที่/ซึ่ง/ว่า/อยู่/กำลัง) + ตัด nominalizer (การ-, ความ-) + ใช้คำสั้น (ดู ไม่ใช่ ตรวจสอบ) + ประโยคสั้นได้

Pattern: `[ของ] [ทำ] [เหตุผล]. [ขั้นต่อ].`

---

## ก่อน / หลัง (Before / After)

### ตัวอย่าง 1 — "ทำไม React component ถึง re-render?"

<table>
<tr>
<th width="34%">🗣️ Normal<br><sub>~80 tokens</sub></th>
<th width="33%">🪶 Lite<br><sub>~45 tokens · 44% saved</sub></th>
<th width="33%">⚡ Full<br><sub>~22 tokens · 73% saved</sub></th>
</tr>
<tr>
<td>"แน่นอนครับ ผมยินดีจะอธิบายให้นะครับ จริงๆ แล้วเหตุผลที่ React component ของคุณ re-render นั้น น่าจะเกิดจากการที่คุณส่ง object reference ใหม่เป็น prop ในทุกครั้งที่ component ถูก render ซึ่งทำให้ React มองว่า prop เปลี่ยน และทำการ re-render component ลูก ดังนั้นคุณอาจจะลองใช้ useMemo เพื่อ memoize object นั้นดูครับ"</td>
<td>"React component re-render เพราะส่ง object reference ใหม่เป็น prop ทุกครั้งที่ render ทำให้ React มองว่า prop เปลี่ยน และ re-render component ลูก ลองใช้ useMemo เพื่อ memoize object นั้น"</td>
<td>"Object ref ใหม่ทุก render. Inline object prop = ref ใหม่ = re-render. ห่อด้วย <code>useMemo</code>."</td>
</tr>
</table>

```
┌─────────────────────────────────────┐
│  Lite  ████░░░░░░  44% saved        │
│  Full  ███████░░░  73% saved        │
└─────────────────────────────────────┘
```

---

### ตัวอย่าง 2 — "อธิบาย database connection pooling"

<table>
<tr>
<th width="34%">🗣️ Normal<br><sub>~70 tokens</sub></th>
<th width="33%">🪶 Lite<br><sub>~35 tokens · 50% saved</sub></th>
<th width="33%">⚡ Full<br><sub>~18 tokens · 74% saved</sub></th>
</tr>
<tr>
<td>"ครับ การทำ database connection pooling นั้น โดยทั่วไปแล้วก็คือการที่เราเก็บ connection ของ database ที่เปิดไว้แล้ว เพื่อนำกลับมาใช้ใหม่อีกครั้ง แทนที่จะต้องเปิด connection ใหม่ทุกครั้งที่มี request เข้ามา ซึ่งจะช่วยลด overhead ของการทำ TCP handshake และ authentication ได้อย่างมีประสิทธิภาพ"</td>
<td>"Connection pooling เก็บ connection database ที่เปิดไว้แล้ว เพื่อนำกลับมาใช้ใหม่ ไม่ต้องเปิดใหม่ทุก request ลด overhead ของ TCP handshake และ authentication"</td>
<td>"Pool reuse connection ที่เปิดไว้. ไม่เปิดใหม่ทุก request. ข้าม TCP handshake."</td>
</tr>
</table>

```
┌─────────────────────────────────────┐
│  Lite  █████░░░░░  50% saved        │
│  Full  ███████░░░  74% saved        │
└─────────────────────────────────────┘
```

---

### ตัวอย่าง 3 — Bug report (auth middleware)

<table>
<tr>
<th width="34%">🗣️ Normal<br><sub>~55 tokens</sub></th>
<th width="33%">🪶 Lite<br><sub>~30 tokens · 45% saved</sub></th>
<th width="33%">⚡ Full<br><sub>~14 tokens · 75% saved</sub></th>
</tr>
<tr>
<td>"ครับ ผมตรวจสอบให้แล้วนะครับ ปัญหาที่คุณเจอน่าจะเกิดจาก bug ใน auth middleware ครับ จริงๆ แล้วในส่วนของ token expiry check นั้น โค้ดใช้เครื่องหมาย <code>&lt;</code> แทนที่จะเป็น <code>&lt;=</code> ซึ่งทำให้ token ที่หมดอายุพอดีไม่ถูก reject ดังนั้นเราควรจะแก้ตรงจุดนี้ครับ"</td>
<td>"Bug อยู่ที่ auth middleware ส่วน token expiry check ใช้ <code>&lt;</code> แทนที่จะเป็น <code>&lt;=</code> ทำให้ token ที่หมดอายุพอดีไม่ถูก reject แก้:"</td>
<td>"Bug ที่ auth middleware. Token expiry ใช้ <code>&lt;</code> ไม่ใช่ <code>&lt;=</code>. Fix:"</td>
</tr>
</table>

```
┌─────────────────────────────────────┐
│  Lite  █████░░░░░  45% saved        │
│  Full  ████████░░  75% saved        │
└─────────────────────────────────────┘
```

---

### ตัวอย่าง 4 — "แนะนำอาหารกลางวันให้หน่อย"

<table>
<tr>
<th wid