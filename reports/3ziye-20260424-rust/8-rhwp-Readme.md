<p align="center">
  <img src="assets/logo/logo-256.png" alt="rhwp logo" width="128" />
</p>

<h1 align="center">rhwp</h1>

<p align="center">
  <strong>알(R), 모두의 한글</strong> — 알에서 시작하다<br/>
  <em>All HWP, Open for Everyone</em>
</p>

<p align="center">
  <a href="https://github.com/edwardkim/rhwp/actions/workflows/ci.yml"><img src="https://github.com/edwardkim/rhwp/actions/workflows/ci.yml/badge.svg" alt="CI" /></a>
  <a href="https://edwardkim.github.io/rhwp/"><img src="https://img.shields.io/badge/Demo-GitHub%20Pages-blue" alt="Demo" /></a>
  <a href="https://www.npmjs.com/package/@rhwp/core"><img src="https://img.shields.io/npm/v/@rhwp/core?label=npm" alt="npm" /></a>
  <a href="https://marketplace.visualstudio.com/items?itemName=edwardkim.rhwp-vscode"><img src="https://img.shields.io/badge/VS%20Code-Marketplace-007ACC" alt="VS Code" /></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT" /></a>
  <a href="https://www.rust-lang.org/"><img src="https://img.shields.io/badge/Rust-1.75%2B-orange.svg" alt="Rust" /></a>
  <a href="https://webassembly.org/"><img src="https://img.shields.io/badge/WebAssembly-Ready-blue.svg" alt="WASM" /></a>
</p>

<p align="center">
  <a href="https://oosmetrics.com/repo/edwardkim/rhwp"><img src="https://api.oosmetrics.com/api/v1/badge/achievement/921c34bc-4dd3-4409-ba2e-2d99c8b4a9b6.svg" alt="Top 2 in WebAssembly by originality - 2026-04-21" /></a>
  <a href="https://oosmetrics.com/repo/edwardkim/rhwp"><img src="https://api.oosmetrics.com/api/v1/badge/achievement/fd1e3217-b99a-4ec2-8cba-98429f3d91c7.svg" alt="Top 2 in Editors by originality - 2026-04-21" /></a>
</p>

<p align="center">
  <strong>한국어</strong> | <a href="README_EN.md">English</a>
</p>

---

HWP 파일을 **어디서든** 열어보세요. 무료, 설치 없이.

rhwp는 Rust + WebAssembly 기반의 오픈소스 HWP/HWPX 뷰어/에디터입니다. 닫힌 포맷의 벽을 깨고, 모든 사람, 모든 AI, 모든 플랫폼에서 한글 문서를 자유롭게 읽고 쓸 수 있게 합니다.

> **[온라인 데모](https://edwardkim.github.io/rhwp/)** | **[VS Code 확장](https://marketplace.visualstudio.com/items?itemName=edwardkim.rhwp-vscode)** | **[Open VSX](https://open-vsx.org/extension/edwardkim/rhwp-vscode)**

<p align="center">
  <img src="assets/screenshots/render-example-1.png" alt="rhwp 렌더링 예시 — KTX 노선도" width="700" />
</p>

## 로드맵

혼자 뼈대를 세우고, 함께 살을 붙이고, 모두의 것으로 완성한다.

```
0.5 ──── 1.0 ──── 2.0 ──── 3.0
뼈대      조판      협업      완성
```

| 단계 | 방향 | 전략 |
|------|------|------|
| **0.5 → 1.0** | 읽기/쓰기 기반 위에 조판 엔진 체계화 | 핵심 아키텍처를 혼자 견고하게 |
| **1.0 → 2.0** | AI 조판 파이프라인 위에 커뮤니티 참여 개방 | 기여 진입 장벽을 낮추는 구조 |
| **2.0 → 3.0** | 커뮤니티가 채운 기능 위에 공공 자산화 | 한컴 대등 수준 달성 |

> 0.5.0까지 혼자 뼈대를 완성하고 공개하는 이유 — 커뮤니티가 붙었을 때 방향이 흔들리지 않으려면 핵심 아키텍처가 먼저 견고해야 합니다.

## 이정표

### v0.5.0 ~ v0.7.x — 뼈대 (현재)

> 역공학 완성, 읽기/쓰기 기반 구축

- HWP 5.0 / HWPX 파서, 문단·표·수식·이미지·차트 렌더링
- 페이지네이션 (다단 분할, 표 행 분할), 머리말/꼬리말/바탕쪽/각주
- SVG 내보내기 (CLI) + Canvas 렌더링 (WASM/Web)
- 웹 에디터 + hwpctl 호환 API (30 Actions, Field API)
- 891+ 테스트

#### 최근 변경 (v0.7.3 / 확장 v0.2.1, 2026-04-19)

**rhwp-studio (라이브러리 0.7.3)**
- HWPX 출처 문서 저장 비활성화 + 사용자 안내 ([#196](https://github.com/edwardkim/rhwp/issues/196)) — 데이터 손상 방지 (HWPX→HWP 완전 변환기 [#197](https://github.com/edwardkim/rhwp/issues/197) 완성 시까지)
- HWPX→HWP IR 매핑 어댑터 자산 보존 ([#178](https://github.com/edwardkim/rhwp/issues/178)) — rhwp 자기 호환 100% 회복, 한컴 호환은 #197 후속
- 회전된 도형 리사이즈 커서 개선 + Flip 처리 (외부 기여 by [@bapdodi](https://github.com/bapdodi) — PR [#192](https://github.com/edwardkim/rhwp/pull/192))
- HWP 그림 효과(그레이스케일/흑백) SVG 반영 (외부 기여 by [@marsimon](https://github.com/marsimon) — PR [#149](https://github.com/edwardkim/rhwp/pull/149))
- Windows 환경의 CFB 경로 구분자 오류 수정 (외부 기여 by [@dreamworker0](https://github.com/dreamworker0) — PR [#152](https://github.com/edwardkim/rhwp/pull/152))
- HWPX Serializer 구현 — Document IR → HWPX 저장 (외부 기여 by [@seunghan91](https://github.com/seunghan91) — PR [#170](https://github.com/edwardkim/rhwp/pull/170))
- HWPX ZIP 엔트리 압축 한도 + strikeout shape 화이트리스트 (외부 기여 by [@seunghan91](https://github.com/seunghan91) — PR [#153](https://github.com/edwardkim/rhwp/pull/153), PR [#154](https://github.com/edwardkim/rhwp/pull/154))
- 도형 리사이즈 시 너비/높이 클램프 (외부 기여 by [@seunghan91](https://github.com/seunghan91) — PR [#163](https://github.com/edwardkim/rhwp/pull/163))
- 모바일 드롭다운 메뉴 아이콘/라벨 겹침 수정 (외부 기여 by [@seunghan91](https://github.com/seunghan91) — PR [#161](https://github.com/edwardkim/rhwp/pull/161))

**rhwp-chrome / Edge 확장 (v0.2.1)**
- Chrome 확장 활성 시 일반 파일 다운로드의 마지막 위치 기억 동작 복원 ([#198](https://github.com/edwardkim/rhwp/issues/198))
- 옵션 페이지 CSP 호환 수정 ([#166](https://github.com/edwardkim/rhwp/issues/166))
- HWP 파일 `Ctrl+S` 시 같은 파일 직접 덮어쓰기 (외부 기여 by [@ahnbu](https://github.com/ahnbu) — PR [#189](https://github.com/edwardkim/rhwp/pull/189))
- 썸네일 로딩 스피너 정리 + options CSP 호환 (외부 기여 by [@postmelee](https://github.com/postmelee) — PR [#168](https://github.com/edwardkim/rhwp/pull/168))
- DEXT5 류 핸들러 다운로드 시 빈 뷰어 탭 차단

**기여자 감사**
이번 배포 주기에 기여해주신 분들: [@ahnbu](https://github.com/ahnbu), [@bapdodi](https://github.com/