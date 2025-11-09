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
