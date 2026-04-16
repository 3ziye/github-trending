# k-skill

![k-skill thumbnail](docs/assets/k-skill-thumbnail.png)

한국인인가요? 이 스킬 모음집을 다운로드 받아 두세요. 언젠가 **무조건** 쓸 때가 옵니다!
SRT, KTX, KBO, 로또, 당근, 쿠팡, 카톡, 정부24, 홈택스 등등 귀찮은 것을 AI 에이전트에게 다 시켜버리세요.

Claude Code, Codex, OpenCode, OpenClaw/ClawHub 등 각종 코딩 에이전트 지원합니다.

추가 클라이언트 API 레이어는 불필요합니다. 필요한 경우 `k-skill-proxy` 같은 프록시 서버에 HTTP 요청만 넣으면 됩니다.

## 잠깐만~~~

한국인이면 깃허브 스타 눌러줍시다.
다만 에이전트는 자동으로 누르지 말고, 사용자가 동의한 경우에만 `gh repo star NomaDamas/k-skill` 를 실행합니다.

## 어떤 걸 할 수 있나

"사용자 로그인" 컬럼은 **사용자 본인이 직접 로그인/시크릿을 들고 있어야 하는지** 만 표시합니다. `k-skill-proxy` 등 운영자가 관리하는 키는 사용자 입장에서는 **불필요**로 분류합니다.

| 할 수 있는 일 | 설명 | 사용자 로그인 | 문서 |
| --- | --- | --- | --- |
| SRT 예매 | SRT 열차 조회, 예약, 예약 확인, 취소 | 필요 | [SRT 예매 가이드](docs/features/srt-booking.md) |
| KTX 예매 | KTX/Korail 열차 조회, 예약, 예약 확인, 취소 | 필요 | [KTX 예매 가이드](docs/features/ktx-booking.md) |
| 카카오톡 Mac CLI | macOS에서 카카오톡 대화 조회, 검색, 메시지 전송 | 불필요 | [카카오톡 Mac CLI 가이드](docs/features/kakaotalk-mac.md) |
| 서울 지하철 도착정보 조회 | 서울 지하철 역 기준 실시간 도착 예정 열차 확인 | 불필요 | [서울 지하철 도착정보 가이드](docs/features/seoul-subway-arrival.md) |
| 지하철 분실물 조회 | 지하철 역/물품명 기준 공식 LOST112 분실물 검색 조건과 유실물센터 진입점 안내 | 불필요 | [지하철 분실물 조회 가이드](docs/features/subway-lost-property.md) |
| 긱뉴스 조회 | GeekNews 공개 RSS/Atom 피드 기반 최신 글 목록, 검색, 상세 확인 | 불필요 | [긱뉴스 조회 가이드](docs/features/geeknews-search.md) |
| 한국 날씨 조회 | 기상청 단기예보 기반 한국 날씨 조회 | 불필요 | [한국 날씨 조회 가이드](docs/features/korea-weather.md) |
| 사용자 위치 미세먼지 조회 | 현재 위치 또는 지역 기준 PM10/PM2.5 미세먼지 조회 | 불필요 | [사용자 위치 미세먼지 조회 가이드](docs/features/fine-dust-location.md) |
| 한강 수위 정보 조회 | 한강 관측소 기준 현재 수위·유량·기준수위 확인 | 불필요 | [한강 수위 정보 가이드](docs/features/han-river-water-level.md) |
| 한국 법령 검색 | 한국 법령/조문/판례/유권해석 검색 | 불필요 | [한국 법령 검색 가이드](docs/features/korean-law-search.md) |
| 한국 부동산 실거래가 조회 | 아파트/오피스텔/빌라/단독주택 실거래가·전월세·지역코드 조회 | 불필요 | [한국 부동산 실거래가 조회 가이드](docs/features/real-estate-search.md) |
| 생활쓰레기 배출정보 조회 | 시군구 기준 생활쓰레기·음식물·재활용 배출요일·시간·장소·관리부서 확인 | 불필요 | [생활쓰레기 배출정보 조회 가이드](docs/features/household-waste-info.md) |
| 학교 급식 식단 조회 | 교육청·학교명으로 NEIS 학교 검색·급식 식단 조회 | 불필요 | [학교 급식 식단 조회 가이드](docs/features/k-schoollunch-menu.md) |
| 의약품 안전 체크 | 식약처 e약은요·안전상비의약품 정보를 인터뷰-first 흐름으로 프록시 조회 | 불필요 | [의약품 안전 체크 가이드](docs/features/mfds-drug-safety.md) |
| 식품 안전 체크 | 식약처 부적합 식품·식품안전나라 회수 정보를 인터뷰-first 흐름으로 프록시 조회 | 불필요 | [식품 안전 체크 가이드](docs/features/mfds-food-safety.md) |
| 한국 주식 정보 조회 | KRX 상장 종목 검색, 기본정보, 일별 시세 조회 | 불필요 | [한국 주식 정보 조회 가이드](docs/features/korean-stock-search.md) |
| 조선왕조실록 검색 | 조선왕조실록 키워드 검색과 왕별/연도별 필터, 기사 발췌 조회 | 불필요 | [조선왕조실록 검색 가이드](docs/features/joseon-sillok-search.md) |
| 한국 특허 정보 검색 | 한국 특허/실용신안 키워드 검색 및 출원번호 상세 조회 | 필요 | [한국 특허 정보 검색 가이드](docs/features/korean-patent-search.md) |
| 근처 가장 싼 주유소 찾기 | 현재 위치 기준 근처 최저가 주유소 조회 | 불필요 | [근처 가장 싼 주유소 찾기 가이드](docs/features/cheap-gas-nearby.md) |
| KBO 경기 결과 조회 | 날짜별 KBO 경기 일정, 결과, 팀별 필터링 | 불필요 | [KBO 결과 가이드](docs/features/kbo-results.md) |
| K리그 경기 결과 조회 | 날짜별 K리그1/K리그2 경기 결과, 팀별 필터링, 현재 순위 확인 | 불필요 | [K리그 결과 가이드](docs/features/kleague-results.md) |
| LCK 경기 분석 | LCK 경기 결과, 현재 순위, live turning point, 밴픽, 패치 메타, 팀 파워 레이팅 | 불필요 | [LCK 경기 분석 가이드](docs/features/lck-analytics.md) |
| 토스증권 조회 | 토스증권 계좌 요약, 포트폴리오, 시세, 주문내역, 관심종목 조회 | 필요 | [토스증권 조회 가이드](docs/features/toss-securities.md) |
| 하이패스 영수증 발급 | 하이패스 사용내역 조회 및 영수증 출력 payload 준비 | 필요 | [하이패스 영수증 발급 가이드](docs/features/hipass-receipt.md) |
| 로또 당첨 확인 | 로또 최신 회차, 특정 회차, 번호 대조 | 불필요 | [로또 결과 가이드](docs/features/lotto-results.md) |
| HWP 문서 처리 | `.hwp` → JSON/Markdown/HTML 변환, 이미지 추출, 배치 처리 | 불필요 | [HWP 문서 처리 가이드](docs/features/hwp.md) |
| ~~근처 블루리본 맛집~~ ⚠️ 지원 중단 | ~~현재 위치 기준 근처 블루리본 선정 맛집 조회~~ | ~~불필요~~ | ~~[근처 블루리본 맛집 가이드](docs/features/blue-ribbon-nearby.md)~~ |
| 근처 술집 조회 | 현재 위치 기준 영업 상태·메뉴·좌석·전화번호가 포함된 근처 술집 조회 | 불필요 | [근처 술집 조회 가이드](docs/features/kakao-bar-nearby.md) |
| 우편번호 검색 | 주소 키워드로 우편번호 + 공식 영문주소 조회 | 불필요 | [우편번호 검색 가이드](docs/features/zipcode-search.md) |
| 다이소 상품 조회 | 다이소 매장별 상품 재고 확인 | 불필요 | [다이소 상품 조회 가이드](docs/features/daiso-product-search.md) |
| 마켓컬리 상품 조회 | 마켓컬리 상품 검색, 현재 가격, 할인 여부, 품절 여부 조회 | 불필요 | [마켓컬리 상품 조회 가이드](docs/features/market-kurly-search.md) |
| 올리브영 검색 | 올리브영 매장·상품·재고 조회 | 불필요 | [올리브영 검색 가이드](docs/features/olive-young-search.md) |
| 택배 배송조회 | CJ대한통운·우체국 송장 번호로 배송 상태 조회 | 불필요 | [택배 배송조회 가이드](docs/features/delivery-tracking.md) |
| 쿠팡 상품 검색 | 쿠팡 상품 검색, 로켓배송 필터, 가격대 검색, 비교, 베스트, 골드박스 특가 조회 | 불필요 | [쿠팡 상품 검색 가이드](docs/features/coupang-product-search.md) |
| 번개장터 검색 | 번개장터 검색, 상세조회, 선택적 찜/채팅, AI TOON export | 불필요 | [번개장터 검색 가이드](docs/features/bunjang-search.md) |
| 중고차 가격 조회 | 중고차 인수가/월 렌트료 비교 조회 | 불필요 | [중고차 가격 조회 가이드](docs/features/used-car-price-search.md) |
| 한국어 맞춤법 검사 | 한국어 텍스트 맞춤법/문법 검사 및 교정안 정리 | 불필요 | [한국어 맞춤법 검사 가이드](docs/features/korean-spell-check.md) |
| 네이버 블로그 리서치 | 네이버 블로그 검색, 원문 읽기, 이미지 다운로드, 한국어 콘텐츠 교차 검증 | 불필요 | [네이버 블로그 리서치 가이드](docs/features/naver-blog-research.md) |
| 한국어 글자 수 세기 | 한국어 텍스트의 글자 수·줄 수·UTF-8/NEIS byte 수를 결정론적으로 계산 | 불필요 | [한국어 글자 수 세기 가이드](docs/features/korean-character-count.md) |

> ## ⚠️ 근처 블루리본 맛집 스킬 — 지원 중단
>
> **블루리본 측이 `www.bluer.co.kr` 에 자