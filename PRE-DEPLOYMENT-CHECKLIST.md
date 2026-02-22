# 📋 Pre-Deployment Checklist

**Complete before deploying to production:**

## 🔍 Content Verification
- [ ] All Battle Drills maps have team compositions
- [ ] All bosses have at least 1-3 recommended teams
- [ ] Verdshroom endboss/miniboss has teams for BOTH buffs:
  - [ ] ⚔️ Unrivaled Might teams configured
  - [ ] 🏛️ Hall of Legends teams configured
- [ ] All hero names are correct and match image filenames
- [ ] All artifacts are in artifacts/ folder
- [ ] All phantimals are in phantimals/ folder

## ✅ Testing
- [ ] Test each game mode in user UI (index.html)
- [ ] Test all boss types (endboss, miniboss, stronghold, cleanup)
- [ ] Test hero filtering (click heroes to disable)
- [ ] Test class and faction filters
- [ ] Test language switching (EN, DE, RU, ES, FR)
- [ ] Test on mobile device (Android or iOS)
- [ ] Test export to PNG feature
- [ ] Verify no console errors (F12 → Console tab)

## 📁 File Check
- [ ] index.html exists and works
- [ ] admin-enhanced.html exists
- [ ] translations.json exists
- [ ] netlify.toml configured correctly
- [ ] .gitignore created (excludes .venv, admin-api.py, backups)
- [ ] All comps/ subfolders have comps.json files
- [ ] logo.png exists (if used)

## 🧹 Cleanup
- [ ] Remove any test/debug data
- [ ] Delete temporary backup folders (or ensure .gitignore excludes them)
- [ ] Clear any console.log statements (optional)
- [ ] Verify no broken image links

## 🔐 Security
- [ ] No sensitive data in JSON files
- [ ] No API keys or passwords in code
- [ ] Admin backend (admin-api.py) won't be deployed (excluded in .gitignore)

## 📝 Documentation
- [ ] README.md up to date
- [ ] DEPLOYMENT.md reviewed
- [ ] Version number or date updated (optional)

---

## ✅ Ready to Deploy!

**Quick Deploy Steps:**

### Option A: Drag & Drop (Fastest)
1. Go to app.netlify.com
2. Drag the entire AFK folder
3. Done! 🎉

### Option B: Git + Auto-Deploy (Recommended)
```bash
git init
git add .
git commit -m "Production deployment"
git remote add origin YOUR_REPO_URL
git push -u origin main
```
Then connect to Netlify/Vercel and auto-deploy on every push.

---

**Deployment Time:** ~30-60 seconds  
**Expected Result:** Fully functional team recommender at your domain!

**Post-Deployment:**
- Test the live site on mobile and desktop
- Share the URL with your community
- Updates: Make local changes → Git push → Auto-deploys

---

Date: _______________  
Deployed by: _______________  
Site URL: _______________
