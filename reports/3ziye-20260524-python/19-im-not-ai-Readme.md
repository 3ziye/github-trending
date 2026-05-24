<p align="center">
  <img src="assets/social-preview.png" alt="im-not-ai — 한글 AI 티 제거기" width="820">
</p>

# Humanize KR — 한글 AI 티 제거기 v2.0.0

AI(ChatGPT · Claude · Gemini 등)가 쓴 한글 글을 **내용은 한 글자도 건드리지 않고** 문체 · 리듬 · 표현만 자연스러운 한국어로 되돌리는 Claude Code 스킬입니다. 

번역투, 과도한 영어 인용, 기계적 병렬 ("첫째 · 둘째 · 셋째"), "결론적으로 / 시사하는 바가 크다" 같은 AI 특유 관용구, 피동태 남용, 문두 접속사 남발, 이모지·불릿 남용 등 **10대 카테고리 × 40+ 서브 패턴**을 심각도(S1/S2/S3)로 분류해 스팬 단위로 탐지한 뒤, 윤문합니다. 

## 왜 한글 특화인가

영어권 humanizer(QuillBot · Hix · Undetectable AI)는 한국어에 약합니다. 한글 AI 글의 티는 대부분 **영어 번역투**에서 나옵니다. 

- "AI 기술을 **통해** 효율을 높**일 수 있다**" → "AI로 효율을 높인다"
- "이에 **있어서** 중요한 **점은**" → "여기서 중요한 건"
- "~**에 의해** 생성된" → "~가 만든"
- "**결론적으로**, 이는 **시사하는 바가 크다**" → (삭제)

이 하네스는 그 한글 고유 패턴을 SSOT로 정리하고, 탐지·윤문·내용 감사·자연스러움 검증을 분리된 에이전트로 수행합니다.

## 4대 철칙

1. **의미 불변** — 사실 · 주장 · 수치 · 고유명사 · 직접 인용은 100% 원문 보존.
2. **근거 기반** — 탐지된 span에만 수술적 수정. 탐지 없는 구간은 건드리지 않음.
3. **장르 유지** — 칼럼을 문학으로, 리포트를 에세이로 옮기지 않음.
4. **과윤문 금지** — 변경률 30% 초과 시 경고, 50% 초과 시 강제 중단.

## 아키텍처 (v1.6)

**Fast 모드 (디폴트, 5,000자 이하)**

```
입력 텍스트
    ↓
[humanize-monolith]   ── 한 콜 안에서 탐지 → 윤문 → 자체검증 일괄
    ↓                     (도구 호출 4~5회 캡, opus, ~3분)
final.md + summary.md
```

**Strict 모드 (`--strict` 또는 8,000자+ 자동 승급)**

```
입력 텍스트
    ↓
[ai-tell-detector]        ── 탐지 (span · category · severity)
    ↓
[korean-style-rewriter]   ── finding 기반 수술적 윤문
    ↓
[병렬 검증 팀]
    ├─ [content-fidelity-auditor]  ── 13항 체크리스트로 의미 동등성 감사
    └─ [naturalness-reviewer]      ── 탐지 재실행으로 잔존·과윤문 판정
    ↓
[오케스트레이터 종합]
    ├─ accept              → final.md + summary.md
    ├─ rewrite_round_2     → 2차 윤문 (최대 3회)
    ├─ rollback_and_rewrite → 문제 edit 롤백
    └─ hold_and_report     → 사람 검토 권고
```

## 7인 에이전트

| 에이전트 | 모드 | 역할 |
|---------|---|------|
| `humanize-monolith` | **Fast 디폴트** | 단일 호출 윤문 (탐지·윤문·자체검증 일괄, 도구 호출 4~5회 캡) |
| `ai-tell-detector` | Strict | span 단위 JSON 탐지 리포트 생성 |
| `korean-style-rewriter` | Strict | finding 기반 수술적 윤문, 변경률 모니터링 |
| `content-fidelity-auditor` | Strict | 의미 동등성 감사 (13항), 훼손 시 롤백 지시 |
| `naturalness-reviewer` | Strict | 잔존 AI 티 · 과윤문 · 자연도 판정, 품질 등급 A~D |
| `korean-ai-tell-taxonomist` | 별도 명령 | 분류 체계(SSOT) 관리, 신규 패턴 심사 승격 |
| `humanize-web-architect` | 옵션 | Next.js 15 + Vercel 웹 서비스 확장 설계 |

## AI 티 분류 체계 (요약)

| ID | 대분류 | 대표 서브 패턴 |
|----|-------|---------------|
| A | 번역투 | "~를 통해", "~에 대해", "~에 있어서", 이중 피동 "~되어진다", "가지고 있다", **"그/그녀" 강박적 사용 (A-16)**, **관계절 좌향 수식 (A-18)**, **"~에서의/~에로의" 이중 조사 (A-19)** |
| B | 영어 인용·용어 과다 | 과도한 괄호 병기, 번역 가능한 영어 그대로 |
| C | 구조적 AI 패턴 | 기계적 "첫째/둘째/셋째", 과도한 불릿·헤딩·이모지, 연결어미 뒤 쉼표 (C-11) |
| D | AI 특유 관용구 | "결론적으로", "시사하는 바가 크다", "주목할 만하다", "혁신적인" |
| E | 리듬 균일성 | 문장 길이 표준편차 낮음, 동일 종결어미 반복, **청자 경어법 일관성 손실 (E-7)** |
| F | 수식·중복 | "매우", "정말", 동의어 이중 수식, "~적/~성/~화/-tion/-ment" 남발 |
| G | Hedging 남용 | "~할 수 있을 것으로 보인다" 다중 완곡 |
| H | 접속사 남발 | 문두 "또한/따라서/즉/나아가" 연속 |
| I | 형식명사 과다 | "것이다", "점", "수", "바", "~할 필요가 있다" |
| J | 시각 장식 남용 | 과도한 **볼드**, "따옴표", 대시(—) 남발 |

전체 60+ 서브 패턴과 처방: [`ai-tell-taxonomy.md`](.claude/skills/humanize-korean/references/ai-tell-taxonomy.md) · [`rewriting-playbook.md`](.claude/skills/humanize-korean/references/rewriting-playbook.md) · 학술 인용 외부 SSOT: [`scholarship.md`](.claude/skills/humanize-korean/references/scholarship.md) (v2.0 신규)

## 심각도 & 품질 등급

**심각도**
- **S1 결정적**: 한 번만 나와도 AI 확신. 무조건 제거.
- **S2 강함**: 1~2회 허용, 3회+ 반복 시 제거.
- **S3 약함**: 다른 패턴과 중첩될 때만 문제.

**품질 등급 (윤문 후)**
- **A**: S1 0건, S2 ≤2건, 점수 개선 70%+
- **B**: S1 0건, S2 ≤4건, 개선 50%+
- **C**: S1 1~2건 or 과윤문 시그널 2개 → 2차 윤문
- **D**: S1 3건+ or 심각한 과윤문 → 사람 검토

## 사용법 — 5분이면 따라합니다

### 0. 전제

[Claude Code](https://claude.com/claude-code)가 설치돼 있어야 합니다. Mac · Windows · Linux 모두 지원합니다.

설치 확인:
```bash
claude --version
```

> Claude Code는 터미널에서 Claude(Anthropic의 AI)와 대화하며 파일을 같이 편집하는 CLI입니다. 이 리포의 스킬·에이전트는 Claude Code에서만 작동합니다. (웹 버전 Claude.ai나 일반 ChatGPT에서는 안 됩니다.)

### 1. 리포 받기

```bash
git clone https://github.com/epoko77-ai/im-not-ai.git
cd im-not-ai
```

### 2. 이 폴더 안에서 Claude Code 켜기

```bash
claude
```

> **중요:** 꼭 `im-not-ai` 폴더 **안에서** 실행하세요. 다른 위치에서 켜면 이 리포의 스킬이 로드되지 않아 일반 Claude Code처럼 동작합니다.

### 3. AI가 쓴 한글 글 붙여넣고 부탁하기

Claude Code에서는 세 가지 방법 중 편한 쪽으로 사용합니다. Codex 사용자는 아래 **방법 D**의 community port를 참고하세요.

**방법 A — 자연어 한 문장 (가장 쉬움)**

평소 말투 그대로 쓰면 됩니다:

```
이 AI 글 자연스럽게 윤문해줘:

[ChatGPT / Claude / Gemini 초안 여기에 붙여넣기]
```

아래 표현 중 아무거나 쓰면 스킬이 자동 발동합니다:
- "AI 티 없애줘"
- "GPT 문체 제거해줘"
- "사람이 쓴 것처럼 윤문해줘"
- "번역투 제거"
- "한글 AI 윤문"

**방법 B — 슬래시 커맨드** *(v1.2~)*

```
/humanize [윤문할 텍스트 또는 파일 경로]
```

옵션을 인자 끝에 자연어로 적을 수 있습니다: `장르: 칼럼`, `강도: 적극`, `최소심각도: S1`. 결과가 마음에 안 들면 `/humanize-redo "번역투만 다시"` 같은 식으로 재실행. 두 커맨드 정의: [`commands/`](.claude/commands/)

**방법 C — Plugin / 자동 설치기** *(@gaebalai 포크)*

[`gaebalai/im-not-ai`](https://github.com/gaebalai/im-not-ai) 포크가 Claude Code Plugin/Marketplace 규격으로 패키징되어 있습니다. `/plugin install humanize-korean@epoko77-ai-plugins` 또는 `./scripts/install.sh --target ~/my-project` 한 줄로 설치 가능합니다. 본체 정식 Plugin 지원은 v1.6 검토 중입니다 ([Issue 추적 예정](https://github.com/epoko77-ai/im-not-ai/issues)