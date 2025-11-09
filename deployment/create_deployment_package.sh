#!/bin/bash
# Conference-Advisor Skill - Deployment Package Creator
# Creates distributable packages for team members

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
DEPLOY_DIR="$PROJECT_ROOT/deployment"

echo "=================================================="
echo "Conference-Advisor Skill - Deployment Package Creator"
echo "=================================================="
echo ""

# Color codes
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Create deployment directory
mkdir -p "$DEPLOY_DIR/packages"

# Package 1: Skill Only (Minimal)
echo -e "${BLUE}[1/3] Creating minimal package (skill only)...${NC}"
cd "$PROJECT_ROOT"

tar -czf "$DEPLOY_DIR/packages/conference-advisor-skill-minimal.tar.gz" \
  --exclude='*.pyc' \
  --exclude='__pycache__' \
  --exclude='.DS_Store' \
  .claude/skills/conference-advisor/SKILL.md \
  .claude/skills/conference-advisor/comprehensive_background_template.md \
  .claude/skills/conference-advisor/conference_plan_template.md \
  .claude/skills/conference-advisor/speaker_analysis_template.md \
  .claude/skills/conference-advisor/README.md \
  .claude/skills/conference-advisor/conferences/MSK2025.yml \
  .claude/skills/conference-advisor/conferences/IAMRT2025.yml \
  conferences/_template/

MINIMAL_SIZE=$(du -h "$DEPLOY_DIR/packages/conference-advisor-skill-minimal.tar.gz" | cut -f1)
echo -e "${GREEN}✓ Minimal package created: ${MINIMAL_SIZE}${NC}"
echo ""

# Package 2: Skill + Example Data (Full)
echo -e "${BLUE}[2/3] Creating full package (skill + examples)...${NC}"

tar -czf "$DEPLOY_DIR/packages/conference-advisor-skill-full.tar.gz" \
  --exclude='*.pyc' \
  --exclude='__pycache__' \
  --exclude='.DS_Store' \
  --exclude='conferences/MSK2025/archive/*' \
  --exclude='conferences/MSK2025/raw/*.pdf' \
  .claude/skills/conference-advisor/ \
  conferences/README.md \
  conferences/_template/ \
  conferences/MSK2025/README.md \
  conferences/MSK2025/raw/symposia.md \
  conferences/MSK2025/raw/time_table.md \
  conferences/MSK2025/backgrounds/*.md \
  conferences/MSK2025/plans/*.md \
  conferences/IAMRT2025/README.md \
  conferences/IAMRT2025/backgrounds/*.md \
  conferences/IAMRT2025/plans/*.md

FULL_SIZE=$(du -h "$DEPLOY_DIR/packages/conference-advisor-skill-full.tar.gz" | cut -f1)
echo -e "${GREEN}✓ Full package created: ${FULL_SIZE}${NC}"
echo ""

# Package 3: README only
echo -e "${BLUE}[3/3] Copying deployment guide...${NC}"
cp "$PROJECT_ROOT/TEAM_DEPLOYMENT_GUIDE.md" "$DEPLOY_DIR/packages/"
echo -e "${GREEN}✓ Deployment guide copied${NC}"
echo ""

# Generate manifest
echo -e "${BLUE}Generating package manifest...${NC}"
cat > "$DEPLOY_DIR/packages/MANIFEST.md" << 'EOF'
# Conference-Advisor Skill - Deployment Packages

## 📦 Available Packages

### 1. Minimal Package (`conference-advisor-skill-minimal.tar.gz`)

**Contents**:
- Skill definition (SKILL.md)
- Templates (comprehensive_background_template.md, etc.)
- Config examples (MSK2025.yml, IAMRT2025.yml)
- New conference template (_template/)
- README documentation

**Size**: ~50 KB

**Use Case**:
- Team members who want to add their own conferences
- No example data needed
- Minimal disk space

**Installation**:
```bash
cd /path/to/your/project
tar -xzf conference-advisor-skill-minimal.tar.gz
```

---

### 2. Full Package (`conference-advisor-skill-full.tar.gz`)

**Contents**:
- Everything in minimal package
- MSK2025 example (31 background files, ~46,500 lines)
- IAMRT2025 example (4 background files, 6,174 lines)
- Conference READMEs

**Size**: ~5-10 MB

**Use Case**:
- Team members who want to see examples
- Learning from high-quality outputs
- Reference materials

**Installation**:
```bash
cd /path/to/your/project
tar -xzf conference-advisor-skill-full.tar.gz
```

**Note**: Raw PDF files NOT included to reduce size. Regenerate backgrounds if needed.

---

### 3. Deployment Guide (`TEAM_DEPLOYMENT_GUIDE.md`)

**Contents**:
- Complete usage instructions
- Configuration guide
- Troubleshooting
- FAQ

**Use Case**: Give this to all team members!

---

## 🚀 Quick Start for Team Members

### Same Git Repository

```bash
# Deployer
git add .claude/skills/conference-advisor/ conferences/
git commit -m "Add conference-advisor skill v2.0"
git push

# Team members
git pull
# Done! Skill is ready to use
```

### Different Project

```bash
# 1. Extract package
tar -xzf conference-advisor-skill-minimal.tar.gz

# 2. Verify
ls .claude/skills/conference-advisor/SKILL.md

# 3. Use in Claude Code
/conference-advisor
```

---

## 📊 Package Comparison

| Feature | Minimal | Full |
|---------|---------|------|
| Skill executable | ✅ | ✅ |
| Templates | ✅ | ✅ |
| Config examples | ✅ | ✅ |
| _template/ | ✅ | ✅ |
| MSK2025 data | ❌ | ✅ (31 files) |
| IAMRT2025 data | ❌ | ✅ (4 files) |
| Size | ~50 KB | ~5-10 MB |

---

## 🎯 Recommendation

**New users**: Start with **Full Package** to see examples
**Experienced users**: Use **Minimal Package** for clean start
**All users**: Read `TEAM_DEPLOYMENT_GUIDE.md` first!

---

**Package Version**: 2.0
**Generated**: 2025-11-07
**Compatibility**: Claude Code 2025+
EOF

echo -e "${GREEN}✓ Manifest created${NC}"
echo ""

# Summary
echo "=================================================="
echo -e "${GREEN}✓ Deployment packages ready!${NC}"
echo "=================================================="
echo ""
echo "📦 Packages created in: $DEPLOY_DIR/packages/"
echo ""
echo "Files:"
echo "  1. conference-advisor-skill-minimal.tar.gz ($MINIMAL_SIZE)"
echo "  2. conference-advisor-skill-full.tar.gz ($FULL_SIZE)"
echo "  3. TEAM_DEPLOYMENT_GUIDE.md"
echo "  4. MANIFEST.md"
echo ""
echo -e "${YELLOW}Next steps:${NC}"
echo "  1. Review packages in: $DEPLOY_DIR/packages/"
echo "  2. Share with team members via:"
echo "     - Git (recommended): git add/commit/push"
echo "     - File transfer: email/cloud/USB"
echo "  3. Give TEAM_DEPLOYMENT_GUIDE.md to all recipients"
echo ""
echo -e "${BLUE}Test installation:${NC}"
echo "  cd /tmp/test-install"
echo "  tar -xzf $DEPLOY_DIR/packages/conference-advisor-skill-minimal.tar.gz"
echo "  ls .claude/skills/conference-advisor/"
echo ""
echo "Done! 🎉"
