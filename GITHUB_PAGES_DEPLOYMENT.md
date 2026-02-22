# GitHub Pages Deployment Guide

## Prerequisites
- GitHub account (free)
- Git installed on your computer

## Step-by-Step Deployment

### 1️⃣ Create GitHub Repository
1. Go to https://github.com/new
2. Repository name: `afk-journey-optimizer` (or any name)
3. Set to **Private** (to hide source code) OR **Public** (up to you)
4. ⚠️ **Do NOT** initialize with README, .gitignore, or license
5. Click "Create repository"

### 2️⃣ Initialize Git in Your Project
Open PowerShell in your project folder and run:

```powershell
git init
git add .
git commit -m "Initial deployment"
git branch -M main
```

### 3️⃣ Link to GitHub and Push
Replace `YOUR_USERNAME` and `REPO_NAME` with your actual values:

```powershell
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
git push -u origin main
```

💡 **First time?** You may be prompted to login to GitHub.

### 4️⃣ Enable GitHub Pages
1. Go to your repository on GitHub
2. Click **Settings** (top right)
3. Click **Pages** (left sidebar)
4. Under "Source", select **main** branch
5. Click **Save**

### 5️⃣ Wait for Deployment
- Takes 1-2 minutes
- Your site will be live at: `https://YOUR_USERNAME.github.io/REPO_NAME/`
- GitHub will show the URL in the Pages settings

---

## 🔄 Updating Your Site

Whenever you make changes:

```powershell
git add .
git commit -m "Description of your changes"
git push
```

Changes go live in 1-2 minutes automatically!

---

## ✅ What Gets Deployed

The following files will be publicly accessible:
- ✅ `index.html` - Main user interface
- ✅ All images (heroes, factions, classes)
- ✅ Team composition data (comps folder)
- ✅ Translations

**Not deployed** (blocked by `.gitignore`):
- ❌ `admin-enhanced.html`
- ❌ `admin-api.py`
- ❌ Documentation files

---

## 🔒 Privacy Notes

**Private Repository:**
- Source code is hidden from public
- Website is still publicly accessible
- Only you can see/edit the code

**Public Repository:**
- Source code is visible to everyone
- Website is publicly accessible
- Anyone can suggest changes (pull requests)

---

## 🆘 Troubleshooting

**404 Error after deployment?**
- Wait 2-5 minutes for GitHub to build
- Check the correct URL: `username.github.io/repo-name/`
- Make sure Pages is enabled in Settings

**Images not loading?**
- Check that folders (heroes/, classes/, factions/) were committed
- Verify file paths are lowercase (case-sensitive on servers)

**Want to use a custom domain?**
- In Pages settings, add your custom domain
- Update DNS records at your domain provider
- GitHub provides instructions

---

## 💰 Cost
**$0.00** - Completely free forever!
