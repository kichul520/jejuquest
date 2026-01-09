# Jeju Quest - Design System

## 1. Color Palette

| 용도 | 이름 | HEX | 사용처 |
|------|------|-----|--------|
| **메인** | Jeju Mandarin | `#FF7F00` | CTA 버튼, 강조 요소, 링크 호버 |
| **폰트메인** | Volcanic Dark | `#2D3436` | 제목, 본문 텍스트 |
| **폰트서브** | Stone Grey | `#636E72` | 설명 텍스트, 캡션, 플레이스홀더 |
| **배경메인** | Old Paper | `#F9F7F1` | 페이지 배경, 섹션 배경 |
| **배경서브** | Pure White | `#FFFFFF` | 카드, 입력 필드, 모달 |

### CSS Variables
```css
:root {
  --color-main: #FF7F00;
  --color-main-dark: #E67300;
  --color-font-main: #2D3436;
  --color-font-sub: #636E72;
  --color-bg-main: #F9F7F1;
  --color-bg-sub: #FFFFFF;
}
```

---

## 2. Typography

### Font Family
```css
font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
```

### Font Sizes (4단계)

| 단계 | 크기 | 용도 | CSS Variable |
|------|------|------|--------------|
| **XL** | 32px / 2rem | 히어로 타이틀, 페이지 제목 | `--font-xl` |
| **LG** | 24px / 1.5rem | 섹션 제목, 카드 타이틀 | `--font-lg` |
| **MD** | 16px / 1rem | 본문, 버튼 텍스트 | `--font-md` |
| **SM** | 14px / 0.875rem | 캡션, 라벨, 보조 텍스트 | `--font-sm` |

### Font Weight
- **Bold (700)**: 제목, 버튼, 강조
- **Regular (400)**: 본문, 설명

### Line Height
- 제목: 1.3
- 본문: 1.6

```css
:root {
  --font-xl: 2rem;      /* 32px */
  --font-lg: 1.5rem;    /* 24px */
  --font-md: 1rem;      /* 16px */
  --font-sm: 0.875rem;  /* 14px */
}
```

---

## 3. Spacing System (8px 단위)

| 단계 | 값 | 용도 |
|------|------|------|
| **xs** | 8px | 아이콘-텍스트 간격, 인라인 요소 |
| **sm** | 16px | 폼 요소 간격, 리스트 아이템 |
| **md** | 24px | 카드 내부 패딩, 컴포넌트 간격 |
| **lg** | 32px | 섹션 내부 여백 |
| **xl** | 48px | 섹션 간 간격 |
| **2xl** | 64px | 히어로 섹션 패딩 |

```css
:root {
  --space-xs: 8px;
  --space-sm: 16px;
  --space-md: 24px;
  --space-lg: 32px;
  --space-xl: 48px;
  --space-2xl: 64px;
}
```

---

## 4. Components

### 4.1 Buttons

#### Primary Button (CTA)
```css
.btn-primary {
  background: var(--color-main);
  color: #FFFFFF;
  padding: 16px 32px;
  font-size: var(--font-md);
  font-weight: 700;
  border: none;
  border-radius: 12px;
  box-shadow: 0 4px 0 #E67300;
  cursor: pointer;
  transition: all 0.1s ease;
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 0 #E67300;
}

.btn-primary:active {
  transform: translateY(4px);
  box-shadow: none;
}
```

#### Secondary Button (Outline)
```css
.btn-secondary {
  background: transparent;
  color: var(--color-main);
  padding: 16px 32px;
  font-size: var(--font-md);
  font-weight: 700;
  border: 2px solid var(--color-main);
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-secondary:hover {
  background: var(--color-main);
  color: #FFFFFF;
}
```

#### Button Sizes
| 사이즈 | 패딩 | 폰트 |
|--------|------|------|
| Small | 8px 16px | 14px |
| Medium | 16px 32px | 16px |
| Large | 20px 40px | 18px |

---

### 4.2 Cards

```css
.card {
  background: var(--color-bg-sub);
  border: 1px solid #E5E0D0;
  border-radius: 16px;
  padding: var(--space-md);
  box-shadow: 0 2px 8px rgba(45, 52, 54, 0.08);
  transition: all 0.2s ease;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(45, 52, 54, 0.12);
}
```

#### Card Variants
| 타입 | 설명 |
|------|------|
| Default | 기본 카드 (흰색 배경) |
| Elevated | 강조 카드 (더 큰 그림자) |
| Interactive | 클릭 가능한 카드 (호버 효과) |

---

### 4.3 Input Fields

```css
.input {
  width: 100%;
  height: 48px;
  padding: 0 16px;
  font-size: var(--font-md);
  font-family: inherit;
  color: var(--color-font-main);
  background: var(--color-bg-sub);
  border: 2px solid #E5E0D0;
  border-radius: 8px;
  transition: all 0.2s ease;
}

.input::placeholder {
  color: var(--color-font-sub);
}

.input:focus {
  outline: none;
  border-color: var(--color-main);
  box-shadow: 0 0 0 4px rgba(255, 127, 0, 0.1);
}

.input:invalid {
  border-color: #E74C3C;
}
```

#### Select Dropdown
```css
.select {
  appearance: none;
  background-image: url("data:image/svg+xml,..."); /* chevron icon */
  background-repeat: no-repeat;
  background-position: right 16px center;
  padding-right: 48px;
}
```

#### Checkbox / Radio
```css
.checkbox {
  width: 20px;
  height: 20px;
  accent-color: var(--color-main);
}
```

---

## 5. Shadows & Borders

### Box Shadows

| 레벨 | 값 | 용도 |
|------|------|------|
| **sm** | `0 2px 4px rgba(45,52,54,0.06)` | 입력 필드, 작은 요소 |
| **md** | `0 4px 12px rgba(45,52,54,0.1)` | 카드, 드롭다운 |
| **lg** | `0 8px 24px rgba(45,52,54,0.15)` | 모달, 플로팅 요소 |
| **button** | `0 4px 0 #E67300` | 스탬프 버튼 효과 |

```css
:root {
  --shadow-sm: 0 2px 4px rgba(45, 52, 54, 0.06);
  --shadow-md: 0 4px 12px rgba(45, 52, 54, 0.1);
  --shadow-lg: 0 8px 24px rgba(45, 52, 54, 0.15);
}
```

### Border Radius

| 레벨 | 값 | 용도 |
|------|------|------|
| **sm** | 4px | 태그, 뱃지 |
| **md** | 8px | 입력 필드, 작은 버튼 |
| **lg** | 12px | 버튼, 카드 |
| **xl** | 16px | 큰 카드, 모달 |
| **full** | 9999px | 원형 버튼, 아바타 |

```css
:root {
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-xl: 16px;
  --radius-full: 9999px;
}
```

### Border Colors
```css
--border-light: #E5E0D0;  /* 기본 테두리 */
--border-focus: #FF7F00;  /* 포커스 상태 */
--border-error: #E74C3C;  /* 에러 상태 */
```

---

## 6. Quick Reference

### CSS Variables 전체
```css
:root {
  /* Colors */
  --color-main: #FF7F00;
  --color-main-dark: #E67300;
  --color-font-main: #2D3436;
  --color-font-sub: #636E72;
  --color-bg-main: #F9F7F1;
  --color-bg-sub: #FFFFFF;

  /* Typography */
  --font-xl: 2rem;
  --font-lg: 1.5rem;
  --font-md: 1rem;
  --font-sm: 0.875rem;

  /* Spacing */
  --space-xs: 8px;
  --space-sm: 16px;
  --space-md: 24px;
  --space-lg: 32px;
  --space-xl: 48px;
  --space-2xl: 64px;

  /* Shadows */
  --shadow-sm: 0 2px 4px rgba(45, 52, 54, 0.06);
  --shadow-md: 0 4px 12px rgba(45, 52, 54, 0.1);
  --shadow-lg: 0 8px 24px rgba(45, 52, 54, 0.15);

  /* Radius */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-xl: 16px;

  /* Borders */
  --border-light: #E5E0D0;
}
```
