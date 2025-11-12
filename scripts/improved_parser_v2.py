#!/usr/bin/env python3
"""
Improved poster parser v2 - Better author detection
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
posters = {}

def is_author_line_v2(line):
    """
    Improved author detection:
    - Must have comma-separated names with "and"
    - Pattern: "Name1, Name2, ... and NameN*"
    """
    if not line.strip():
        return False

    line = line.strip()

    # Strong pattern: comma + "and" + ending with *
    # Example: "Kim A, Lee B, and Park C*"
    if ', and ' in line and line.endswith('*'):
        return True

    # Count commas
    comma_count = line.count(',')
    if comma_count < 2:
        return False

    # Must have "and"
    if ' and ' not in line:
        return False

    # Check if "and" comes after comma
    # Split by "and", check if there's comma before
    parts = line.split(' and ')
    if len(parts) >= 2:
        before_and = parts[0]
        if ',' in before_and:
            # Additional check: parts look like names
            # Names are typically 2-4 words, capitalized
            words = line.replace(',', ' ').replace('*', '').split()
            # Filter out numbers and short words
            name_words = [w for w in words if len(w) > 1 and not w.isdigit() and w != 'and']
            if len(name_words) >= 3:  # At least 3 name components
                return True

    return False

def is_affiliation_line(line):
    """Check if line looks like an affiliation"""
    affil_keywords = [
        'university', 'institute', 'department', 'college', 'school',
        'laboratory', 'center', 'centre', 'academy', 'research', 'hospital',
        'univ', 'dept', 'lab', 'co.,', 'corp', 'inc.', 'ltd',
        '대학', '연구', '센터'
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
    poster_lines = [l.strip() for l in poster_block.split('\n')]

    # Skip first line (poster code itself) and empty lines
    content_lines = [l for l in poster_lines[1:] if l.strip()]

    if not content_lines:
        posters[code] = {'title': '', 'authors': '', 'affiliation': ''}
        continue

    # Strategy: Find author line (strict criteria), everything before is title
    title_lines = []
    author_lines = []
    affiliation_lines = []

    author_found = False
    affil_found = False

    for line in content_lines:
        # Skip very short lines that are just numbers
        if len(line) <= 2 and line.replace(',', '').isdigit():
            continue

        if not author_found:
            if is_author_line_v2(line):
                author_found = True
                author_lines.append(line)
            else:
                title_lines.append(line)
        elif not affil_found:
            # After author, look for affiliation
            if is_affiliation_line(line):
                affil_found = True
                affiliation_lines.append(line)
            elif is_author_line_v2(line):
                # Continue multi-line author
                author_lines.append(line)
            else:
                # Might be affiliation without keywords
                affiliation_lines.append(line)
        else:
            # Already in affiliation
            affiliation_lines.append(line)

    # If no author found with strict criteria, try relaxed
    if not author_lines and title_lines:
        # Look for lines with multiple commas and capitalized words
        for idx, line in enumerate(title_lines):
            if line.count(',') >= 2:
                # Check if looks like names
                words = [w for w in line.replace(',', ' ').split() if w and not w.isdigit()]
                caps = sum(1 for w in words if w[0].isupper())
                if caps >= len(words) * 0.7:  # 70% capitalized
                    # This might be author
                    author_lines = [line]
                    title_lines = title_lines[:idx]
                    affiliation_lines = title_lines[idx+1:] + affiliation_lines
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
with open('parsed_posters_v3.json', 'w', encoding='utf-8') as f:
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
print(f"\n기존 대비 개선:")
print(f"  v1 (원본): 305개 (71.6%)")
print(f"  v3 (신규): {good_titles}개 ({good_titles/len(posters)*100:.1f}%)")
print(f"  개선: {good_titles - 305}개")

# Show sample improvements
print("\n샘플 확인 (처음 10개):")
with open('parsed_posters.json', 'r', encoding='utf-8') as f:
    old_posters = json.load(f)

for code in ['A001', 'A002', 'A003', 'A005', 'A006', 'A007', 'A008', 'A009', 'A010']:
    if code in posters:
        new = posters[code]
        old = old_posters.get(code, {})
        old_title = old.get('title', '')
        new_title = new.get('title', '')

        if old_title != new_title:
            print(f"\n{code}:")
            print(f"  [OLD] '{old_title[:50]}'")
            print(f"  [NEW] '{new_title[:50]}'")
