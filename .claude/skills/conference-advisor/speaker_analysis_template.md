# Speaker Analysis Template

Use this template for each speaker when creating background materials.

## 1. Web Search Strategy

For each speaker, search for:
```
"[Speaker Name] [Institution] [Key Topic from Talk Title]"
```

Example:
```
"Eun-Kyung Lim KRIBB portable biosensing airborne antibiotic"
```

## 2. Information to Extract

### From Search Results:
- [ ] Recent publications (2023-2025 preferred)
- [ ] Research lab/group website
- [ ] Key methodologies used
- [ ] Collaborators and institutions
- [ ] Funding sources (indicates research direction)

### Key Details:
- **Position**: Professor, Research Scientist, etc.
- **Affiliation**: University, Institute, Department
- **Recent major publication**: Title, Journal, Year
- **Research focus**: 1-2 sentence summary
- **Key findings**: Bullet points (3-5)

## 3. Content to Generate

### For Each Talk:

#### Background Section
```markdown
**연사**: [Name in Korean (English)]
**소속**: [Institution, Department]
**제목**: [Talk title]

#### 최근 연구 배경
[2-3 paragraphs about recent work, with citations]

**핵심 발견**:
- [Key finding 1]
- [Key finding 2]
- [Key finding 3]
```

#### Expected Content Section
```markdown
#### 예상 발표 내용

**1. [Topic 1]**
[What they'll likely cover]

**2. [Topic 2]**
[What methodology/results]

**3. [Clinical/Practical Implications]**
[How it applies]
```

#### Connection to User Research
```markdown
#### 당신의 연구와의 연결점

**[User's Research Focus] 관점**:
- [Specific connection 1]
- [Specific connection 2]

**도심 환경 적용**:
- [Application 1]
- [Application 2]

**메타지노믹스 응용**:
- [Metagenomics angle]
```

#### Background Knowledge Section
```markdown
#### 필수 배경 지식

**1. [Key Concept 1]**
- **정의**: [Definition]
- **원리**: [How it works]
- **응용**: [Applications]
- **도구/방법**: [Tools/methods]

**2. [Key Concept 2]**
[Same structure]
```

#### Questions Section
```markdown
#### 예상 질문 & 토론 포인트

**당신이 물어볼 질문**:
1. "[Specific question connecting to urban AMR surveillance]"
2. "[Question about methodology application]"
3. "[Question about metagenomics integration]"

**토론 예상**:
- [Discussion point 1]
- [Discussion point 2]
```

## 4. Notion-Optimized Format

Use these Notion features:

### Toggle Blocks
```markdown
<details>
<summary><b>🎯 추천: [Session Name]</b></summary>

[Content here]

</details>
```

### Callouts
```markdown
> **💡 Key Insight**: [Important point]
```

### Tables
```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Data     | Data     | Data     |
```

### Checkboxes
```markdown
- [ ] Task item
- [x] Completed item
```

### Code Blocks
```markdown
\`\`\`yaml
Key: Value
\`\`\`
```

## 5. Session Priority Template

```markdown
### ⏰ [Time Slot] | [Session Number]

<details open>
<summary><b>🎯 추천: [Session Name] ([Score]점)</b> ← [Priority Label]</summary>

**핵심 토픽**
1. **[Topic 1]**
   → [Why important]
2. **[Topic 2]**
   → [Why important]

**연사 하이라이트**
- [Speaker]: [Recent work]

**왜 필수인가**
- [Reason 1]
- [Reason 2]

</details>

| 세션 | 점수 | 키워드 |
|------|------|--------|
| ✅ **[Recommended]** | [Score] | [Keywords] |
| [Alternative 1] | [Score] | [Keywords] |
```

## 6. Networking Priority Template

```markdown
### 우선순위 [N]: [Speaker Name] - [Institution]

**Why?**
- [Reason 1]
- [Reason 2]
- [Geographic/collaboration advantage]

**접근 전략**:
1. [During talk action]
2. [Post-talk action]
3. [Follow-up action]
4. [Email timing and content]
```

## 7. Metagenomics Marker Template

```markdown
### [Session] AMR/Diagnostic Markers

\`\`\`yaml
[Category] Markers:
  - gene1 (function)
  - gene2 (function)
  - gene3 (function)
\`\`\`

**Application**:
- [How to use in metagenomics]
- [Expected abundance patterns]
```
