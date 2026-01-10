제주 여행 Gamification 앱 - 시장 검증용 랜딩페이지 요구사항 정의서

1. 프로젝트 개요

프로젝트명: Jeju Quest Landing (가칭)

목적: 제주 여행 게이미피케이션 앱의 수요를 파악하기 위한 시장 검증 및 잠재 고객(Early Access) DB 확보.

핵심 가치: "제주를 여행하지 말고, 게임처럼 플레이하세요." (AR 기술 없는 아날로그 감성의 현실 탐험)

목표: 4주 내 MVP 출시를 위한 사전 예약자 모집 및 바이럴 마케팅 테스트.

2. 디자인 컨셉 (Design System)

테마: "Digital Explorer's Log (디지털 탐험 일지)"

최첨단 기술보다는 '낡은 지도', '스탬프', '종이 질감'을 활용하여 모험의 설렘 강조.

컬러 팔레트:

Primary: Jeju Mandarin (#FF7F00) - 행동 유도(CTA) 버튼.

Secondary: Volcanic Dark (#2D3436) - 본문 텍스트.

Background: Old Paper (#F9F7F1) - 낡은 종이 질감 배경.

Accent: Emerald Sea (#00CEC9) - 강조 포인트.

3. 주요 기능 명세 (Functional Requirements)

3.1 메인 랜딩 페이지 (/)

Hero 섹션:

강렬한 카피: "당신의 여행은 퀘스트가 됩니다."

배경: 제주 풍경 + 낡은 지도 오버레이.

CTA 버튼: "탐험대 합류하고 유료 퀘스트 받기".

Features 섹션:

앱의 핵심 기능(지도 UI, 보상, 퀘스트)을 카드 형태로 소개.

'테이프로 붙인 사진' 느낌의 UI 디자인 적용.

Starter Pack 섹션 (NEW):

무료 스타터 퀘스트 팩(돌하르방, 올레길, 로컬맛집) 및 얼리버드 할인 쿠폰 혜택 소개.

3단계 시작 가이드 (이메일 수신 -> 코드 입력 -> 플레이) 제공.

Social Proof:

가상의 베타 테스터 후기 ("관광지 줄 안 서고 골목 여행하니 너무 좋아요").

3.2 티저 퀴즈 (/quiz)

목적: 사용자의 흥미 유발 및 '관찰형 미션' 간접 체험.

내용: "이 돌하르방의 손 위치는 무엇을 의미할까요?" (또는 관찰형 문제).

기능: 정답 선택 시 즉시 결과 판정 및 DB 로그 저장 (참여율 측정용).

3.3 퀴즈 결과 (/quiz/result)

내용: 정답 여부에 따른 메시지 출력.

유도: "실전에서는 더 많은 보물이 기다립니다" → 사전 예약 버튼 연결.

3.4 사전 예약 및 바이럴 (/pre-register)

입력 항목 (확장됨):
- 이메일 (필수)
- 전화번호 (선택)
- 거주 지역 (선택)
- 연령대 (선택)
- 개인정보 수집 이용 동의 (필수, 별도 페이지 연동)
- 마케팅 정보 수신 동의 (선택)

처리:

중복 이메일 체크.

가입 완료 시 고유 '추천 코드(Referral Code)' 생성.

완료 페이지:

"친구를 초대하면 추가 보상을 드립니다."

내 추천 코드 및 공유 링크 표시.

4. 데이터베이스 설계 (DB Schema)

4.1 PreRegistration (사전 예약자)

email: 사용자 이메일 (ID 역할).
phone: 전화번호 (NEW).
region: 거주 지역 (NEW).
age_group: 연령대 (NEW).
privacy_agreed: 개인정보 동의 여부 (NEW).
marketing_agreed: 마케팅 동의 여부 (NEW).
referral_code: 본인의 추천 코드 (UUID 활용).
referred_by: 나를 초대한 사람 (Viral 추적용).
created_at: 가입 일시.

4.2 TeaserQuestLog (티저 퀴즈 기록)

quiz_name: 퀴즈 종류.
user_answer: 제출한 답.
is_correct: 정답 여부.
created_at: 참여 일시.

4.3 Quest (퀘스트 관리 - NEW)

title: 퀘스트 제목.
description: 퀘스트 설명.
icon: 아이콘/이모지.
is_starter_pack: 스타터팩 포함 여부.
created_at: 생성 일시.

5. 기술 스택 및 배포 환경

Language: Python 3.x

Framework: Django 5.x

Database: SQLite (개발) / PostgreSQL (배포)

Deployment: Render.com (Web Service)

Server: Gunicorn + Whitenoise (정적 파일 처리)

Directory Structure:

Root: jeju-quest-landing/

App Code: jeju-quest-landing/project/

6. 구현 및 변경 내역 (Change Log)

v1.0 (Initial): 기본 랜딩 페이지, 티저 퀴즈, 이메일 수집 기능 구현.

v1.1 (Enhancement):
- 사전 예약 폼: 개인정보(전화번호, 지역 등) 수집 항목 확장 및 약관 동의 절차 추가.
  - 입력 필드: 이메일(필수), 전화번호(선택), 거주지역(선택), 연령대(선택)
  - 동의 항목: 개인정보 수집·이용 동의(필수), 마케팅 정보 수신 동의(선택)
  - 개인정보처리방침 페이지 연동 (/privacy-policy/)
  - 중복 이메일 검증 로직 구현
  - 추천 코드(Referral Code) 자동 생성 및 공유 링크 제공
- UI 개선: 무료 스타터 팩 상세 섹션 추가, 2026년 얼리버드 쿠폰 적용, 푸터 연도 최신화.
- 백엔드: Quest 모델 추가 및 Admin 연동.
- 리소스: 이메일 템플릿(launch_notification.html) 제작.

v1.2 (Design System):
- 디자인 시스템: Pretendard 폰트 적용, 8px 단위 spacing 시스템 구축.
- Hero 섹션: 제주 풍경 배경 이미지 + 낡은 지도 오버레이 효과 추가.
- CTA 버튼: 텍스트 수정 ("무료 퀘스트" → "유료 퀘스트 받기").
- Features 섹션: 카드에 테이프로 붙인 사진 느낌의 UI 효과 적용.
- Accent 색상: #00CEC9 (Emerald Sea) UI 전반에 활용 (뱃지, 후기 카드, 스탬프 등).
- 사전 예약 폼: register-section, register-card, consent-section 등 CSS 스타일 추가.
- 퀴즈 결과: result-section, stamp 효과 등 CSS 스타일 추가.
- 배포: Render.com용 render.yaml 설정 파일 생성.

v1.3 (2026-01-11 - Kakao Share & Mobile UI Fix):

1. 카카오톡 공유 링크 문제 해결
   - 문제: 카카오톡 공유 메시지는 전송되지만, 링크가 클릭되지 않고 "모바일에서 확인해주세요"로 표시됨
   - 원인: 카카오 Developers 콘솔에서 "제품 링크 관리"에 도메인 미등록
   - 해결: 카카오 콘솔 > 제품 링크 관리 > 웹 도메인에 `https://jeju-quest-landing.onrender.com` 등록
   - 참고: JavaScript SDK 도메인(플랫폼 키)과 제품 링크 관리 도메인은 별도로 등록 필요

2. 카카오 공유 URL 변경
   - 변경 전: `/pre-register/?ref=XXX` (사전예약 페이지)
   - 변경 후: `/?ref=XXX` (메인 페이지)
   - 파일: `project/templates/landing/pre_register.html` (line 175)
   - 커밋: `8c47a0e`

3. 모바일 네비게이션 텍스트 줄바꿈 문제 해결
   - 문제: 모바일에서 네비게이션 버튼 텍스트가 두 줄로 나뉨 ("티저 퀴/즈", "탐험대 합/류")
   - 해결:
     - HTML: 텍스트를 `<span class="nav-text">`로 감쌈 (`project/templates/base.html`)
     - CSS: 480px 이하에서 `.nav-text { display: none; }` 적용하여 아이콘만 표시
   - 파일: `project/static/css/style.css` (line 1889-1903)
   - 커밋: `f6e6755`

4. 푸터 텍스트 줄바꿈 문제 해결
   - 문제: 모바일에서 푸터 텍스트가 단어 중간에서 줄바꿈됨 ("플레이하세/요.")
   - 해결:
     - `word-break: keep-all` 추가 (한글 단어 중간 줄바꿈 방지)
     - 480px 이하에서 폰트 크기 축소 (11px)
   - 파일: `project/static/css/style.css` (line 1777-1784, 1919-1931)
   - 커밋: `f6e6755`

커밋 히스토리:
- `f6e6755` - fix: mobile nav shows icons only, optimize footer text
- `1b48e26` - fix: prevent text wrapping in mobile nav buttons and footer
- `8c47a0e` - fix: change kakao share link to main page instead of pre-register
- `b6f8e0a` - fix: hardcode kakao share domain to match console

7. 카카오 설정 정보

| 항목 | 값 |
|------|-----|
| JavaScript 키 | `d3bcb43aeb8f7bfa8227459508ecc356` |
| 앱 이름 | 제주퀘스트 |
| SDK 버전 | 2.5.0 |
| 등록 도메인 | `https://jeju-quest-landing.onrender.com` |

카카오 콘솔 설정 체크리스트:
- [x] 플랫폼 키 > JavaScript SDK 도메인 등록
- [x] 제품 링크 관리 > 웹 도메인 등록
