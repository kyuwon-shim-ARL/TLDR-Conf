# AI/ML Research: Manual Curation Guide

**Why this guide exists**: AI/ML fields change too fast (1-3 month cycles) for citation-based tools. This guide provides efficient manual curation strategies.

## The Problem

**Citation-based tools (like Research Landscape Analyzer) fail for AI/ML**:

```
Citation stabilization time: 1-2 years
AI/ML innovation cycle:      1-3 months

Gap: 10-20x difference
→ By the time citations accumulate, field has moved 3 generations ahead
```

**Real examples**:
- GPT-4 (Mar 2023) → GPT-4 Turbo (Nov 2023) → GPT-4o (May 2024)
- Transformer (Jun 2017): 6 months for 50 citations, but BERT/GPT already out
- Claude 3.5 Sonnet: No academic paper, just blog posts

**Conclusion**: Manual curation is the only viable approach.

---

## Efficient Manual Curation Workflow

### Daily (10 minutes)

**1. ArXiv Sanity Lite** (http://www.arxiv-sanity-lite.com/)
- Create account, set preferences
- Subscribe to: `cs.AI`, `cs.LG`, `cs.CL`, `cs.CV`
- Daily email digest (top papers by your interests)
- Save papers to library, add tags

**Setup**:
```
1. Visit http://www.arxiv-sanity-lite.com/
2. Sign in with Google/GitHub
3. Settings → Email preferences → Daily digest ON
4. Browse → Set filters → Save
```

**2. Twitter Lists** (5 min scan)
- Follow key researchers & aggregators
- Create private list: "AI Research"

**Recommended follows**:
- @_akhaliq (daily AI papers, very active)
- @AK92 (ML papers summary)
- @omarsar0 (NLP progress)
- @weights_biases (ML engineering)
- @huggingface (models & datasets)
- @paperswithcode (SOTA tracking)

**Setup**:
```
Twitter → Lists → Create list "AI Research"
→ Add accounts above
→ Check list daily (5 min)
```

---

### Weekly (30 minutes)

**3. Papers with Code** (https://paperswithcode.com/)
- Browse "Trending" and "Latest" pages
- Check SOTA tables for your area of interest
- Filter by task (e.g., "Image Classification", "Question Answering")

**Workflow**:
```
1. Visit PapersWithCode.com
2. Trending → Last 7 days
3. Filter by your domain:
   - Computer Vision
   - NLP
   - Reinforcement Learning
   - etc.
4. Bookmark papers with code available
5. Check leaderboards for your specific tasks
```

**4. GitHub Trending** (https://github.com/trending)
- AI section weekly scan
- Look for implementations of recent papers
- Star repos with >1000 stars in "AI/ML" category

**Workflow**:
```
1. GitHub Trending → This week
2. Language: Python
3. Spoken Language: Any
4. Look for repos with keywords:
   - "LLM", "transformer", "diffusion"
   - "GPT", "BERT", "stable diffusion"
5. Check repo stars, commits, and recent activity
```

**5. Reddit r/MachineLearning** (https://reddit.com/r/MachineLearning)
- Sort by "Top this week"
- Focus on `[R]` (Research) and `[D]` (Discussion) tags
- Read comments (often more insightful than papers)

**Workflow**:
```
1. r/MachineLearning
2. Sort: Top → This Week
3. Filter: [R] Research tag
4. Read top 10 posts
5. Read top comment threads (signal of importance)
```

---

### Monthly (1-2 hours)

**6. Conference Proceedings** (Official papers)
- **NeurIPS**: December (https://neurips.cc/)
- **ICML**: July (https://icml.cc/)
- **ICLR**: April (https://iclr.cc/)
- **CVPR**: June (Computer Vision)
- **ACL**: July (NLP)
- **EMNLP**: November (NLP)

**How to use**:
```
1. When conference proceedings released:
   - Download accepted papers list (CSV/PDF)
   - Scan titles for your keywords
   - Read abstracts of ~20-30 papers
   - Deep dive into ~5-10 papers

2. Watch for:
   - Best Paper awards (always read these)
   - Oral presentations (top ~3% of submissions)
   - Workshop papers (emerging topics)
```

**7. Benchmark Leaderboard Updates**
- ImageNet, SQuAD, GLUE, SuperGLUE
- Check monthly for SOTA changes
- If new method achieves >2% improvement → likely important

**8. Industry Blog Posts**
- OpenAI blog (https://openai.com/blog/)
- Google AI blog (https://ai.googleblog.com/)
- Meta AI (https://ai.meta.com/blog/)
- Anthropic research (https://www.anthropic.com/research)
- DeepMind blog (https://deepmind.google/discover/blog/)

**Why**: Industry releases (GPT, Claude, Gemini) often have no papers, only blog posts.

---

## Organization System

### Bookmark Manager (Browser)

**Structure**:
```
AI/ML Research/
├── Must Read (High priority)
├── To Read (Queue)
├── Read (Archive)
│   ├── 2024/
│   │   ├── LLMs/
│   │   ├── Computer Vision/
│   │   └── RL/
│   └── 2025/
├── Tools & Code
│   ├── Libraries
│   └── Implementations
└── Datasets
```

### Notion/Obsidian Database

**Template for each paper**:
```markdown
# [Paper Title]

**Date Added**: 2024-11-12
**Source**: ArXiv / NeurIPS / Twitter
**Status**: To Read / Reading / Read
**Priority**: High / Medium / Low

## Key Idea (1 sentence)
[Write after reading abstract]

## Why Important?
- [ ] New SOTA on benchmark X
- [ ] Novel architecture/method
- [ ] Addresses known limitation
- [ ] Surprising result

## Tags
#llm #attention #efficiency

## Notes
[Take while reading]

## Code
[GitHub link if available]

## Related Papers
- Paper A (builds on)
- Paper B (competes with)
```

### Spreadsheet Tracking

**Columns**:
| Title | Date | Source | Category | SOTA? | Code? | Priority | Status | Notes |
|-------|------|--------|----------|-------|-------|----------|--------|-------|
| ... | 2024-11 | ArXiv | LLM | Yes | GitHub | High | Read | Scaling laws... |

**Benefits**:
- Sortable by date, priority, status
- Filterable by category
- Exportable for sharing with team

---

## Advanced Strategies

### 1. Follow the Money

**Track funding announcements**:
- NSF grants (https://www.nsf.gov/awardsearch/)
- NIH grants for AI in medicine
- DARPA AI programs
- Industry research labs hiring

**Why**: Big funding → active research area → likely breakthroughs coming

### 2. Author Tracking

**Identify prolific authors in your niche**:
- Check their Google Scholar profiles monthly
- Set up Google Scholar alerts for their names
- Follow them on Twitter

**How to find them**:
1. Papers with Code → Leaderboard → Top methods → Authors
2. Recent best paper awards → Authors
3. Twitter → See who @_akhaliq retweets often

### 3. Citation Graph (Manual)

**For important papers**:
1. Read the paper
2. Check "Cited By" (Google Scholar)
3. Check "References" (what it builds on)
4. Create manual map:
   ```
   Foundation Paper A (2020)
    ├→ Improvement B (2022)
    └→ Application C (2023)
        └→ Current Paper D (2024) ← You're here
   ```

### 4. Preprint Alerts

**Set up Google Scholar alerts**:
```
1. Google Scholar → My Profile → Follow
2. Set alerts for:
   - Authors you care about
   - Keywords ("large language model", "diffusion model")
   - Specific papers (get cited-by updates)
```

**RSS Feeds**:
- ArXiv RSS for categories
- Feed reader: Feedly, Inoreader
- Check daily (5 min)

### 5. Community Signals

**Discord/Slack communities**:
- Eleuther AI Discord (LLM research)
- LAION Discord (open source AI)
- Hugging Face Discord
- r/LocalLLaMA (community experiments)

**Why**: Catch buzz before it hits mainstream
- People discuss failures (not in papers)
- Real-world performance issues
- Implementation tricks

---

## Red Flags (What to Ignore)

### Hype Detection

**Ignore if**:
- No code available (just claims)
- Results only on synthetic datasets
- No comparison to baselines
- "Revolutionary" in title (usually not)
- Company press release with no paper

**Be skeptical if**:
- Results too good to be true (check for bugs)
- Only tested on one task
- No error bars / confidence intervals
- Authors won't release model weights

### Time Wasters

**Don't spend time on**:
- Incremental improvements (<1% on benchmarks)
- Papers that just combine existing methods
- "Yet another transformer variant" (unless SOTA)
- Papers with no adoption after 6 months

---

## Quarterly Review (4 hours)

**Every 3 months**:

1. **Synthesize trends** (What changed?)
   - New architectures emerged?
   - Old methods deprecated?
   - Benchmark shifted?

2. **Clean bookmarks**
   - Archive read papers
   - Delete irrelevant bookmarks
   - Update priority of queue

3. **Write summary** (For yourself or team)
   ```markdown
   # Q4 2024 AI/ML Update

   ## Major Breakthroughs
   - Method X achieved new SOTA on Y
   - Technique Z addresses problem W

   ## Emerging Trends
   - Multimodal models taking off
   - Efficiency becoming priority

   ## Dead Ends
   - Approach A didn't scale
   - Method B has reproducibility issues

   ## Recommended Reading (Top 5)
   1. Paper A - [why]
   2. Paper B - [why]
   ...
   ```

4. **Adjust workflow**
   - New sources to follow?
   - Drop inactive sources
   - Refine keywords

---

## Comparison: Manual vs Citation-Based

### Research Landscape Analyzer (Citation-based)
✅ **Works for**: Traditional biology, chemistry, medicine
✅ **Coverage**: 80-95% (5+ year old fields)
✅ **Effort**: 1 hour → Full analysis
❌ **Lag**: 1-2 years
❌ **AI/ML**: 10-20% coverage only

### Manual Curation (This guide)
✅ **Works for**: AI/ML, fast-moving fields
✅ **Lag**: 0-1 week (real-time)
✅ **Coverage**: 60-80% with effort
❌ **Effort**: 10 min/day + 30 min/week + 2 hours/month
❌ **Scalability**: Doesn't scale to many topics

---

## Hybrid Approach (Best of Both)

**For computational biology** (e.g., AlphaFold, protein structure prediction):

1. **Use Research Landscape Analyzer** for:
   - Foundational papers (5+ years old)
   - Review papers
   - Established methods

2. **Use manual curation** for:
   - Latest methods (0-2 years)
   - SOTA tracking (Papers with Code)
   - Industry releases (DeepMind, Google)

**Workflow**:
```
Step 1: Run Research Landscape Analyzer
→ Get solid foundation (10-50 papers, 5-10 years)

Step 2: Manual curation (weekly)
→ ArXiv cs.LG + cs.AI for "protein structure"
→ Papers with Code leaderboard for CASP
→ DeepMind blog for AlphaFold updates

Step 3: Merge
→ Foundation (automated) + Latest (manual)
→ Comprehensive landscape in 2 hours instead of 2 days
```

---

## Tools Summary

| Tool | Frequency | Time | Purpose |
|------|-----------|------|---------|
| ArXiv Sanity | Daily | 5 min | New papers |
| Twitter Lists | Daily | 5 min | Buzz & trends |
| Papers with Code | Weekly | 15 min | SOTA tracking |
| GitHub Trending | Weekly | 10 min | Implementations |
| r/MachineLearning | Weekly | 15 min | Community signal |
| Conference Proceedings | Monthly | 2 hours | Official papers |
| Benchmark Updates | Monthly | 30 min | SOTA changes |
| Quarterly Review | 3 months | 4 hours | Synthesis |

**Total time**: ~50 min/week + 2 hours/month + 4 hours/quarter
**= ~2.5 hours/week average**

---

## Conclusion

**Key Takeaways**:

1. **Citation-based tools fail for AI/ML** (10-20x lag vs field pace)
2. **Manual curation is the only way** for bleeding edge
3. **Efficient workflow exists**: 10 min/day, 30 min/week gets 60-80% coverage
4. **Use hybrid approach** for computational biology (automated foundation + manual latest)

**Final Recommendation**:

- **Traditional biology, chemistry**: Use Research Landscape Analyzer ✅
- **AI/ML, LLMs, generative AI**: This manual curation guide ✅
- **Computational biology, bioinformatics**: Hybrid (80% automated, 20% manual) ✅

---

**Version**: 1.0
**Last Updated**: 2024-11-12
**Maintained By**: Research Landscape Analyzer Project

