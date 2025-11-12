# MSK2025 Conference Analysis Project

Conference materials analysis and recommendations system for MSK2025 microbiology conference.

## Project Structure

```
MSK2025/
├── scripts/                    # Analysis & processing scripts
│   ├── classify_posters_mece*.py   # Poster classification
│   ├── generate_notion_csv.py      # Notion export generator
│   └── improved_parser*.py         # Conference data parsers
│
├── data/                       # Source data files
│   ├── raw/                        # Original extracted data
│   │   ├── extracted_ebook.txt
│   │   ├── extracted_plenary.txt
│   │   └── extracted_posters.txt
│   └── processed/                  # Parsed & structured data
│       ├── parsed_posters*.json
│       ├── session_poster_connections.json
│       └── topic_top_posters.json
│
├── outputs/                    # Generated results
│   ├── guides/                     # User guides & documentation
│   │   ├── LAB_SHARING_comprehensive_guide.md
│   │   ├── NOTION_*.md
│   │   ├── QUICK_REFERENCE_mobile.md
│   │   └── TEAM_DEPLOYMENT_GUIDE.md
│   ├── posters/                    # Poster classifications
│   │   ├── POSTER_Category_*.md    # A-H categories
│   │   ├── POSTER_MECE_classification.md
│   │   └── SESSION_POSTER_connections.md
│   └── exports/                    # CSV exports for Notion
│       ├── NOTION_sessions_database.csv
│       └── POSTER_MECE_notion.csv
│
├── conferences/                # Conference-specific materials
│   ├── MSK2025/
│   └── IAMRT2025/
│
├── speaker_profiles/           # Speaker analysis & research
└── deployment/                 # Deployment configurations
```

## Quick Start

### 1. Parse Conference Data
```bash
cd scripts
python improved_parser_v2.py
```

### 2. Classify Posters (MECE Framework)
```bash
python classify_posters_mece_v2.py
```

### 3. Generate Notion Import CSV
```bash
python generate_notion_csv.py
```

## Output Files

### For Personal Use
- `outputs/guides/` - Conference planning guides
- `outputs/posters/POSTER_Category_*.md` - Browse by research area
- `outputs/guides/QUICK_REFERENCE_mobile.md` - Mobile quick reference

### For Notion Import
- `outputs/exports/NOTION_sessions_database.csv` - Session database
- `outputs/exports/POSTER_MECE_notion.csv` - Classified posters

### For Lab Sharing
- `outputs/guides/LAB_SHARING_comprehensive_guide.md`
- `outputs/guides/TEAM_DEPLOYMENT_GUIDE.md`

## Data Pipeline

```
Raw Data (data/raw/)
    ↓ [improved_parser_v2.py]
Parsed JSON (data/processed/)
    ↓ [classify_posters_mece_v2.py]
Categorized Markdown (outputs/posters/)
    ↓ [generate_notion_csv.py]
Notion CSV (outputs/exports/)
```

## Key Features

- **MECE Classification**: Mutually Exclusive, Collectively Exhaustive poster categorization
- **Session-Poster Linking**: Connects oral sessions with related posters
- **Topic Recommendations**: Top 10 topics with relevant posters
- **Notion Integration**: Ready-to-import CSV databases
- **Mobile Optimized**: Quick reference guide for on-site use

## Requirements

```bash
# Python dependencies (if needed)
pip install pandas openpyxl
```

## Conference Details

- **Event**: MSK2025 (Microbiology Society of Korea)
- **Focus**: Microbiology, molecular biology, biotechnology
- **Categories**: A-H (Systematics, Ecology, Applied, Pathogenesis, etc.)

## License

Internal research use only.
