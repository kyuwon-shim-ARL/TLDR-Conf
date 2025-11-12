#!/usr/bin/env python3
"""
Improved poster parser with better title/author/affiliation separation
"""

import re
import json

# Read extracted text
with open('extracted_ebook.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Find poster section start
poster_section_start = content.find('A. Systematics / 미생물분류', 7000)
if poster_section_start == -1:
    print("Cannot find poster section!")
    exit(1)

poster_content = content[poster_section_start:]

# Extract all poster codes
poster_codes = re.findall(r'^([A-H]\d{3}|GS\d+-?\d*)$', poster_content, re.MULTILINE)
unique_codes = []
seen = set()
for code in poster_codes:
    if code not in seen:
        unique_codes.append(code)
        seen.add(code)

print(f"Found {len(unique_codes)} unique poster codes")

# Parse each poster
lines = poster_content.split('\n')
posters = {}

def is_author_line(line):
    """Check if line looks like an author line"""
    # Author patterns:
    # - Contains "and"
    # - Multiple capitalized words with commas
    # - Has superscript numbers (1, 2, 1,2)
    # - Ends with *

    if not line.strip():
        return False

    # Strong indicators
    if ' and ' in line:
        return True
    if line.strip().endswith('*'):
        return True

    # Check for pattern: Name1, Name2, Name3
    parts = [p.strip() for p in line.split(',')]
    if len(parts) >= 2:
        # Check if parts look like names (start with capital letter)
        name_like = sum(1 for p in parts if p and p[0].isupper() and len(p.split()) <= 4)
        if name_like >= len(parts) * 0.6:  # 60% look like names
            return True

    return False

def is_affiliation_line(line):
    """Check if line looks like an affiliation"""
    affil_keywords = [
        'university', 'institute', 'department', 'college', 'school',
        'laboratory', 'center', 'academy', 'research', 'hospital',
        'univ', 'dept', 'lab', 'co.,', 'corp', 'inc.'
    ]
    line_lower = line.lower()
    return any(kw in line_lower for kw in affil_keywords)

for i, code in enumerate(unique_codes):
    # Find start and end
    code_pattern = f'^{re.escape(code)}$'
    matches = [(m.start(), m.group()) for m in re.finditer(code_pattern, poster_content, re.MULTILINE)]

    if not matches:
        continue

    start_pos = matches[0][0]

    # Find next poster code
    if i + 1 < len(unique_codes):
        next_code = unique_codes[i + 1]
        next_pattern = f'^{re.escape(next_code)}$'
        next_matches = list(re.finditer(next_pattern, poster_content, re.MULTILINE))
        if next_matches:
            end_pos = next_matches[0].start()
        else:
            end_pos = len(poster_content)
    else:
        end_pos = len(poster_content)

    # Extract poster block
    poster_block = poster_content[start_pos:end_pos]
    poster_lines = [l.strip() for l in poster_block.split('\n') if l.strip()]

    # Skip first line (poster code itself)
    content_lines = poster_lines[1:] if len(poster_lines) > 1 else []

    if not content_lines:
        posters[code] = {'title': '', 'authors': '', 'affiliation': ''}
        continue

    # Strategy: Find author line first, everything before is title
    title_lines = []
    author_lines = []
    affiliation_lines = []

    in_title = True
    in_authors = False
    in_affiliation = False

    for line in content_lines:
        # Skip very short lines (numbers, etc.)
        if len(line) <= 2 and line.isdigit():
            continue

        if in_title:
            if is_author_line(line):
                in_title = False
                in_authors = True
                author_lines.append(line)
            else:
                title_lines.append(line)
        elif in_authors:
            if is_affiliation_line(line):
                in_authors = False
                in_affiliation = True
                affiliation_lines.append(line)
            elif len(line) <= 2 and line.isdigit():
                # Skip affiliation numbers
                continue
            else:
                # Continue author or start affiliation
                if is_author_line(line):
                    author_lines.append(line)
                else:
                    in_authors = False
                    in_affiliation = True
                    affiliation_lines.append(line)
        elif in_affiliation:
            affiliation_lines.append(line)

    # If no author found, try heuristic: last 1-2 lines before affiliation
    if not author_lines and title_lines:
        # Look for affiliation
        for idx, line in enumerate(title_lines):
            if is_affiliation_line(line):
                # Everything before is title/author
                if idx > 0:
                    # Last line before affiliation might be author
                    potential_author = title_lines[idx-1]
                    if is_author_line(potential_author) or ',' in potential_author:
                        author_lines = [potential_author]
                        title_lines = title_lines[:idx-1]
                    else:
                        title_lines = title_lines[:idx]
                affiliation_lines = title_lines[idx:]
                break

    # Combine lines
    title = ' '.join(title_lines).strip()
    authors = ' '.join(author_lines).strip()
    affiliation = ' '.join(affiliation_lines).strip()

    posters[code] = {
        'title': title,
        'authors': authors,
        'affiliation': affiliation
    }

# Save improved parsing
with open('parsed_posters_v2.json', 'w', encoding='utf-8') as f:
    json.dump(posters, f, ensure_ascii=False, indent=2)

# Statistics
empty_titles = sum(1 for p in posters.values() if not p['title'] or len(p['title']) <= 3)
short_titles = sum(1 for p in posters.values() if 3 < len(p['title']) < 10)
good_titles = sum(1 for p in posters.values() if len(p['title']) >= 10)

print(f"\n✅ Parsing complete: {len(posters)} posters")
print(f"\n제목 품질:")
print(f"  ✅ 정상 (>=10자): {good_titles} ({good_titles/len(posters)*100:.1f}%)")
print(f"  ⚠️  짧음 (4-9자): {short_titles} ({short_titles/len(posters)*100:.1f}%)")
print(f"  ❌ 없음/실패 (<=3자): {empty_titles} ({empty_titles/len(posters)*100:.1f}%)")
print(f"\n개선율: {good_titles - 305}개 향상")

# Show sample improvements
print("\n샘플 비교 (처음 5개 문제 케이스):")
with open('parsed_posters.json', 'r', encoding='utf-8') as f:
    old_posters = json.load(f)

problem_codes = [code for code, data in old_posters.items()
                 if not data.get('title', '').strip() or len(data.get('title', '')) <= 3]

for code in problem_codes[:5]:
    old = old_posters[code]
    new = posters.get(code, {})
    print(f"\n{code}:")
    print(f"  [OLD] 제목: '{old.get('title', '')[:60]}'")
    print(f"  [NEW] 제목: '{new.get('title', '')[:60]}'")
