## 🚀 Quick Deploy Checklist

Copy-paste these commands one by one:

### Initialize Git
```powershell
git init
git add .
git commit -m "Initial deployment"
git branch -M main
```

### Push to GitHub
⚠️ First create repo at https://github.com/new then:

```powershell
# Replace YOUR_USERNAME and REPO_NAME
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
git push -u origin main
```

### Enable Pages
1. Go to repository Settings → Pages
2. Source: **main** branch
3. Save
4. Wait 2 minutes
5. Visit: `https://YOUR_USERNAME.github.io/REPO_NAME/`

---

## 🔄 Future Updates
```powershell
git add .
git commit -m "Updated teams"
git push
```

Done! 🎉
