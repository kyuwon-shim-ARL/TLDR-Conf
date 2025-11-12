#!/usr/bin/env python3
"""
Generate Notion-compatible CSV with sub-categories and full titles
"""

import json
import csv
import re
from collections import defaultdict

# Load improved poster data
with open('parsed_posters_v3.json', 'r', encoding='utf-8') as f:
    posters = json.load(f)

print(f"Loaded {len(posters)} posters")

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

    for zone_info in zones:
        match = re.search(r'Zone (\d+): ([A-H]\d+)-([A-H]\d+)', zone_info)
        if match:
            zone_num, start_code, end_code = match.groups()
            start_num = int(start_code[1:])
            end_num = int(end_code[1:])
            if start_code[0] == category and start_num <= num <= end_num:
                return session, f'Zone {zone_num}'

    return session, zones[0].split(':')[0] if zones else 'Unknown'

# Enhanced MECE categories with sub-categories
mece_categories = {
    '🦠 항생제 내성 (AMR)': {
        'keywords': [
            'resistance', 'resistant', 'antibiotic', 'antimicrobial',
            'carbapenem', 'beta-lactam', 'esbl', 'mrsa', 'vre', 'mdr',
            'efflux', 'lactamase', 'methicillin', 'vancomycin',
            'colistin', 'aminoglycoside', 'quinolone', 'cephalosporin'
        ],
        'sub_categories': {
            'Resistance mechanisms': ['efflux', 'lactamase', 'beta-lactam', 'permeability'],
            'MRSA/VRE': ['mrsa', 'vre', 'methicillin', 'vancomycin'],
            'Carbapenem-resistant': ['carbapenem', 'cre'],
            'Novel strategies': ['phage', 'peptide', 'antimicrobial peptide', 'novel']
        },
        'posters': []
    },
    '🔬 병원성 메커니즘': {
        'keywords': [
            'virulence', 'pathogen', 'infection', 'toxin', 'secretion',
            'adhesion', 'invasion', 'biofilm', 'quorum', 'immune evasion',
            't3ss', 't4ss', 't6ss', 'type iii', 'type iv', 'type vi',
            'pathogenesis', 'hemolys', 'cytolysin'
        ],
        'sub_categories': {},
        'posters': []
    },
    '🧬 마이크로바이옴': {
        'keywords': [
            'microbiome', 'microbiota', 'gut', 'intestinal', 'fecal',
            'oral', 'skin', 'vaginal', 'dysbiosis', '16s rrna',
            'metagenome', 'metatranscriptome', 'community', 'diversity',
            'probiot', 'prebiotic', 'human microb'
        ],
        'sub_categories': {
            'Gut microbiome': ['gut', 'intestinal', 'fecal', 'colon', 'gastrointestinal'],
            'Oral microbiome': ['oral', 'dental', 'saliva', 'mouth'],
            'Skin microbiome': ['skin', 'dermal', 'cutaneous'],
            'Disease-associated': ['disease', 'cancer', 'obesity', 'diabetes', 'ibd', 'crohn']
        },
        'posters': []
    },
    '🧪 유전 및 대사': {
        'keywords': [
            'crispr', 'genome editing', 'plasmid', 'gene expression',
            'transcriptome', 'metabol', 'pathway', 'regulation',
            'gene cluster', 'operon', 'promoter', 'horizontal gene',
            'recombina', 'mutation', 'evolution', 'phylogen'
        ],
        'sub_categories': {},
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
        'sub_categories': {
            'Fermentation/Food': ['fermentation', 'kimchi', 'lactic acid', 'dairy', 'probiotic'],
            'Industrial production': ['production', 'enzyme', 'bioreactor', 'biosynthesis', 'biofuel'],
            'Bioremediation': ['bioremediation', 'degradation', 'cleanup', 'pollutant'],
            'Diagnostics': ['diagnosis', 'detection', 'sensor', 'biosensor', 'assay']
        },
        'posters': []
    },
    '🌍 생태 및 환경': {
        'keywords': [
            'ecology', 'environmental', 'soil', 'marine', 'ocean',
            'sediment', 'water', 'extreme', 'thermophil', 'halophil',
            'arctic', 'antarctic', 'hot spring', 'isolate',
            'diversity', 'community structure', 'niche'
        ],
        'sub_categories': {
            'Marine/Ocean': ['marine', 'ocean', 'sea', 'coastal', 'seawater'],
            'Soil': ['soil', 'rhizosphere', 'sediment'],
            'Freshwater': ['freshwater', 'lake', 'river', 'water'],
            'Extreme environments': ['extreme', 'thermophil', 'halophil', 'arctic', 'antarctic', 'hot spring']
        },
        'posters': []
    },
    '📊 분류 및 신종': {
        'keywords': [
            'sp. nov', 'novel species', 'new species', 'taxonomy',
            'systematic', 'phylogeny', 'classification', 'genus',
            'characterization', 'polyphasic', 'type strain'
        ],
        'sub_categories': {},
        'posters': []
    },
    '🔧 방법론 및 기타': {
        'keywords': [
            'method', 'protocol', 'assay', 'screening', 'platform',
            'tool', 'database', 'software', 'algorithm', 'model',
            'education', 'teaching', 'review', 'survey'
        ],
        'sub_categories': {},
        'posters': []
    }
}

def find_sub_category(category_name, sub_cats, search_text):
    """Find best matching sub-category"""
    if not sub_cats:
        return 'General'

    matches = []
    for sub_cat, keywords in sub_cats.items():
        score = sum(1 for kw in keywords if kw.lower() in search_text.lower())
        if score > 0:
            matches.append((sub_cat, score))

    if matches:
        matches.sort(key=lambda x: x[1], reverse=True)
        return matches[0][0]

    return 'Others'

# Classify posters
all_rows = []

for code, data in posters.items():
    # Combine all text for classification
    title = data.get('title', '').strip()
    authors = data.get('authors', '').strip()
    affiliation = data.get('affiliation', '').strip()

    search_text = f"{title} {authors} {affiliation}".lower()

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

                # Find sub-category
                sub_cats = mece_categories[category]['sub_categories']
                sub_category = find_sub_category(category, sub_cats, search_text)

                # Parsing status
                parsing_status = 'Success' if len(title) > 3 else 'Failed'
                display_title = title if len(title) > 3 else "⚠️ 제목 미파싱 (PDF 확인 필요)"

                # Create row
                row = {
                    'Code': code,
                    'Main_Category': category,
                    'Sub_Category': sub_category,
                    'Title': display_title,
                    'Authors': authors,
                    'Affiliation': affiliation,
                    'Session': session,
                    'Zone': zone,
                    'Keywords_Matched': ', '.join(keywords[:5]),
                    'Parsing_Status': parsing_status
                }

                all_rows.append(row)

                # Also add to category for markdown
                mece_categories[category]['posters'].append({
                    'code': code,
                    'title': display_title,
                    'session': session,
                    'zone': zone,
                    'score': score,
                    'keywords': keywords[:3],
                    'parsing_failed': len(title) <= 3,
                    'sub_category': sub_category,
                    'authors': authors,
                    'affiliation': affiliation
                })

# Sort rows by Main Category, Sub Category, Session, Zone, Code
all_rows.sort(key=lambda x: (x['Main_Category'], x['Sub_Category'], x['Session'], x['Zone'], x['Code']))

# Write CSV
csv_filename = 'POSTER_MECE_notion.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8-sig') as f:  # UTF-8 with BOM for Excel
    fieldnames = ['Code', 'Main_Category', 'Sub_Category', 'Title', 'Authors', 'Affiliation',
                  'Session', 'Zone', 'Keywords_Matched', 'Parsing_Status']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(all_rows)

print(f'\n✅ CSV 생성 완료: {csv_filename}')
print(f'✅ 총 행 수: {len(all_rows)}')

# Statistics
print('\n📊 카테고리별 통계:')
category_counts = defaultdict(lambda: defaultdict(int))
for row in all_rows:
    category_counts[row['Main_Category']][row['Sub_Category']] += 1

for main_cat in sorted(category_counts.keys()):
    sub_cats = category_counts[main_cat]
    total = sum(sub_cats.values())
    print(f'\n{main_cat}: {total}개')
    for sub_cat in sorted(sub_cats.keys()):
        count = sub_cats[sub_cat]
        print(f'  └─ {sub_cat}: {count}개')

# Parsing status
success = sum(1 for row in all_rows if row['Parsing_Status'] == 'Success')
failed = sum(1 for row in all_rows if row['Parsing_Status'] == 'Failed')
print(f'\n파싱 상태:')
print(f'  ✅ 성공: {success}개 ({success/len(all_rows)*100:.1f}%)')
print(f'  ❌ 실패: {failed}개 ({failed/len(all_rows)*100:.1f}%)')
