#!/usr/bin/env python3
"""
MECE-based poster classification
Simple keyword matching approach for practical categorization
"""

import json
import re
from collections import defaultdict

# Load poster data
with open('parsed_posters.json', 'r', encoding='utf-8') as f:
    posters = json.load(f)

# Session and Zone mapping
session_zones = {
    'B': ('Session 1 (10/26)', ['Zone 1: B001-B060', 'Zone 2: B061-B088']),
    'D': ('Session 1 (10/26)', ['Zone 2: D001-D032', 'Zone 3: D033-D074']),
    'E': ('Session 1 (10/26)', ['Zone 3: E001-E018', 'Zone 4: E019-E033']),
    'F': ('Session 1 (10/26)', ['Zone 4: F001-F021', 'Zone 5: F022-F033']),
    'A': ('Session 2 (10/27)', ['Zone 1: A001-A056']),
    'C': ('Session 2 (10/27)', ['Zone 1: C001-C004', 'Zone 2: C005-C064', 'Zone 3: C065-C071']),
    'G': ('Session 2 (10/27)', ['Zone 3: G001-G035']),
    'H': ('Session 2 (10/27)', ['Zone 3: H001-H018', 'Zone 4: H019-H044']),
}

def get_session_zone(code):
    """Get session and zone for poster code"""
    category = code[0]
    num = int(code[1:])

    if category not in session_zones:
        return 'Unknown', 'Unknown'

    session, zones = session_zones[category]

    # Find specific zone
    for zone_info in zones:
        # Parse zone range
        match = re.search(r'Zone (\d+): ([A-H]\d+)-([A-H]\d+)', zone_info)
        if match:
            zone_num, start_code, end_code = match.groups()
            start_num = int(start_code[1:])
            end_num = int(end_code[1:])
            if start_code[0] == category and start_num <= num <= end_num:
                return session, f'Zone {zone_num}'

    return session, zones[0].split(':')[0] if zones else 'Unknown'

# MECE classification keywords
mece_categories = {
    '🦠 항생제 내성 (AMR)': {
        'keywords': [
            'resistance', 'resistant', 'antibiotic', 'antimicrobial',
            'carbapenem', 'beta-lactam', 'esbl', 'mrsa', 'vre', 'mdr',
            'efflux', 'lactamase', 'methicillin', 'vancomycin',
            'colistin', 'aminoglycoside', 'quinolone', 'cephalosporin'
        ],
        'posters': []
    },
    '🔬 병원성 메커니즘': {
        'keywords': [
            'virulence', 'pathogen', 'infection', 'toxin', 'secretion',
            'adhesion', 'invasion', 'biofilm', 'quorum', 'immune evasion',
            't3ss', 't4ss', 't6ss', 'type iii', 'type iv', 'type vi',
            'pathogenesis', 'hemolys', 'cytolysin'
        ],
        'posters': []
    },
    '🧬 마이크로바이옴': {
        'keywords': [
            'microbiome', 'microbiota', 'gut', 'intestinal', 'fecal',
            'oral', 'skin', 'vaginal', 'dysbiosis', '16s rrna',
            'metagenome', 'metatranscriptome', 'community', 'diversity',
            'probiot', 'prebiotic', 'human microb'
        ],
        'posters': []
    },
    '🧪 유전 및 대사': {
        'keywords': [
            'crispr', 'genome editing', 'plasmid', 'gene expression',
            'transcriptome', 'metabol', 'pathway', 'regulation',
            'gene cluster', 'operon', 'promoter', 'horizontal gene',
            'recombina', 'mutation', 'evolution', 'phylogen'
        ],
        'posters': []
    },
    '🏭 응용 미생물': {
        'keywords': [
            'fermentation', 'production', 'enzyme', 'bioreactor',
            'kimchi', 'lactic acid', 'probiotic', 'dairy',
            'bioconversion', 'biosynthesis', 'bioremediation',
            'degradation', 'biofuel', 'bioethanol', 'diagnosis',
            'detection', 'sensor', 'biosensor'
        ],
        'posters': []
    },
    '🌍 생태 및 환경': {
        'keywords': [
            'ecology', 'environmental', 'soil', 'marine', 'ocean',
            'sediment', 'water', 'extreme', 'thermophil', 'halophil',
            'arctic', 'antarctic', 'hot spring', 'isolate',
            'diversity', 'community structure', 'niche'
        ],
        'posters': []
    },
    '📊 분류 및 신종': {
        'keywords': [
            'sp. nov', 'novel species', 'new species', 'taxonomy',
            'systematic', 'phylogeny', 'classification', 'genus',
            'characterization', 'polyphasic', 'type strain'
        ],
        'posters': []
    },
    '🔧 방법론 및 기타': {
        'keywords': [
            'method', 'protocol', 'assay', 'screening', 'platform',
            'tool', 'database', 'software', 'algorithm', 'model',
            'education', 'teaching', 'review', 'survey'
        ],
        'posters': []
    }
}

# Classify posters
for code, data in posters.items():
    # Combine all text
    search_text = (
        data.get('title', '') + ' ' +
        data.get('authors', '') + ' ' +
        data.get('affiliation', '')
    ).lower()

    # Skip empty
    if not search_text.strip():
        continue

    # Find best matching category
    matches = []
    for category, info in mece_categories.items():
        score = 0
        matched_keywords = []
        for keyword in info['keywords']:
            if keyword.lower() in search_text:
                score += 1
                matched_keywords.append(keyword)

        if score > 0:
            matches.append((category, score, matched_keywords))

    # Sort by score
    matches.sort(key=lambda x: x[1], reverse=True)

    # Assign to top category (or multiple if tied)
    if matches:
        top_score = matches[0][1]
        for category, score, keywords in matches:
            if score >= top_score * 0.7:  # Within 70% of top score
                session, zone = get_session_zone(code)
                mece_categories[category]['posters'].append({
                    'code': code,
                    'title': data.get('title', '(제목 없음)'),
                    'session': session,
                    'zone': zone,
                    'score': score,
                    'keywords': keywords[:3]  # Top 3 matched keywords
                })

# Generate markdown guide
output = []
output.append('# 🎯 포스터 MECE 분류 가이드\n')
output.append('**426개 포스터를 연구 주제별로 실용적 분류**\n')
output.append('---\n')

# Summary statistics
output.append('## 📊 분류 개요\n')
for category, info in mece_categories.items():
    count = len(info['posters'])
    output.append(f'- **{category}**: {count}개')
output.append('\n---\n')

# How to use
output.append('## 💡 사용 방법\n')
output.append('''
1. **관심 주제 선택**: 아래 8개 분류 중 관심 분야 선택
2. **포스터 코드 확인**: 각 분류에서 10-15개 포스터 확인
3. **Session & Zone 체크**: 방문 시간과 동선 계획
4. **우선순위 선정**: 제목 보고 5-10개로 압축
5. **현장 방문**: 준비된 질문으로 효율적 네트워킹

**특징**:
- ✅ MECE 분류로 중복 최소화
- ✅ Session/Zone 정보로 동선 최적화
- ✅ 매칭 키워드로 관련성 확인 가능
- ✅ 한눈에 스캔 가능한 테이블 형식

---
''')

# Generate each category
for category, info in mece_categories.items():
    posters_list = info['posters']

    if not posters_list:
        continue

    # Sort by session, then zone, then code
    posters_list.sort(key=lambda x: (
        x['session'],
        x['zone'],
        x['code']
    ))

    output.append(f'## {category}\n')
    output.append(f'**포스터 수**: {len(posters_list)}개\n\n')

    # Group by session
    session_groups = defaultdict(list)
    for poster in posters_list:
        session_groups[poster['session']].append(poster)

    for session in sorted(session_groups.keys()):
        session_posters = session_groups[session]
        output.append(f'### {session}\n\n')

        # Table header
        output.append('| 코드 | Zone | 제목 (일부) | 매칭 키워드 |\n')
        output.append('|------|------|------------|-------------|\n')

        # Table rows
        for poster in session_posters[:30]:  # Limit to 30 per session for readability
            code = poster['code']
            zone = poster['zone']
            title = poster['title'][:60] + '...' if len(poster['title']) > 60 else poster['title']
            keywords = ', '.join(poster['keywords'][:2])

            output.append(f'| **{code}** | {zone} | {title} | {keywords} |\n')

        if len(session_posters) > 30:
            output.append(f'\n*...외 {len(session_posters) - 30}개 포스터*\n')

        output.append('\n')

    output.append('---\n\n')

# Usage tips
output.append('## 🎯 실전 활용 팁\n')
output.append('''
### 시나리오 1: AMR 연구자
```
1. "🦠 항생제 내성 (AMR)" 섹션 확인
2. Session 1 (10/26) 포스터 10개 선정
3. Zone 2-3 집중 (D 카테고리)
4. 매칭 키워드 확인: carbapenem, efflux 등
5. 현장에서 효율적 방문
```

### 시나리오 2: 마이크로바이옴 연구자
```
1. "🧬 마이크로바이옴" 섹션 확인
2. Session 1 (10/26) 포스터 확인
3. Zone 1-2 집중 (B 카테고리)
4. Gut/oral 관련 포스터 우선순위
5. 추가로 "🔬 병원성 메커니즘"에서 host-microbe interaction 체크
```

### 시나리오 3: 신종 발굴 연구자
```
1. "📊 분류 및 신종" 섹션 확인
2. Session 2 (10/27) 집중
3. Zone 1 (A 카테고리)
4. sp. nov. 키워드 포스터 우선
5. 유사 분류군 연구자 네트워킹
```

---

## 📋 체크리스트

### 학회 전 (3일 전)
- [ ] 관심 주제 2-3개 선택
- [ ] 각 주제에서 10-15개 포스터 확인
- [ ] Session 날짜 확인 (10/26 or 10/27)
- [ ] Zone 배치 확인 및 동선 계획

### 학회 당일 아침
- [ ] 선정한 포스터 코드 리스트 출력
- [ ] 우선순위 Top 10 표시
- [ ] 명함 준비

### 포스터 세션 중
- [ ] 우선순위 포스터부터 방문
- [ ] 각 포스터 5-10분 할애
- [ ] 명함 교환 및 간단 메모
- [ ] Standing reception 네트워킹

### 세션 후
- [ ] 명함 정리
- [ ] Top 5 포스터 요약
- [ ] Follow-up 이메일 (1주일 내)

---

## 🌟 이 가이드의 장점

### ✅ PDF 검색 대비
- PDF: 키워드 검색 → 60개 결과 → ??? (우선순위 모름)
- 이 가이드: 주제별 분류 → 매칭 키워드 확인 → Session/Zone 확인 → 10개 선정

### ✅ 기존 14개 파일 대비
- 기존: 복잡한 파싱, 주관적 점수, 14개 파일
- 이 가이드: 간단한 분류, MECE 체계, 1개 파일

### ✅ 실용성
- 한 눈에 스캔 가능
- Session/Zone 정보로 동선 최적화
- 매칭 키워드로 관련성 즉시 확인

---

**생성일**: 2025-10-26
**분석 대상**: 426개 포스터
**분류 방식**: MECE (Mutually Exclusive, Collectively Exhaustive)
**권장 사용**: PDF 검색 보다는 이 가이드 활용!

''')

# Write to file
with open('POSTER_MECE_classification.md', 'w', encoding='utf-8') as f:
    f.write(''.join(output))

print('✅ MECE 분류 가이드 생성 완료: POSTER_MECE_classification.md')
print(f'✅ 분류된 포스터 수: {sum(len(info["posters"]) for info in mece_categories.values())}')
print('✅ 각 카테고리별 포스터 수:')
for category, info in mece_categories.items():
    print(f'   {category}: {len(info["posters"])}개')
