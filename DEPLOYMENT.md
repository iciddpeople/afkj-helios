# 🚀 Deployment Guide - AFK Journey Team Recommender

## Pre-Deployment Checklist

### ✅ Essential Checks
- [ ] All team compositions configured and tested locally
- [ ] Hero data is complete and accurate
- [ ] All asset folders present (heroes/, artifacts/, phantimals/, etc.)
- [ ] Translations file (translations.json) is complete
- [ ] Test all game modes work correctly
- [ ] Mobile testing completed (see MOBILE_TESTING.md)
- [ ] Admin changes saved to comps/ folder

### ✅ File Verification
Required files for deployment:
```
index.html              # Main user interface
admin-enhanced.html     # Admin interface (read-only after deployment)
translations.json       # Language translations
netlify.toml           # Netlify configuration
logo.png               # Site logo
comps/                 # Team composition data
heroes/                # Hero images
artifacts/             # Artifact images
phantimals/            # Phantimal images
classes/               # Class icons
factions/              # Faction icons
```

Files to EXCLUDE (handled by .gitignore):
```
.venv/                 # Python virtual environment
admin-api.py           # Backend API (won't work on Netlify)
requirements.txt       # Python dependencies
backup_*/              # Backup folders
__pycache__/           # Python cache
```

## Deployment Options

### Option 1: Netlify (Recommended - Free & Easy)

**Deploy via Drag & Drop:**
1. Go to [app.netlify.com](https://app.netlify.com)
2. Sign up or log in
3. Drag the entire AFK folder to the deployment area
4. Wait 30-60 seconds for deployment
5. Your site is live! 🎉

**Deploy via Git (Recommended for Updates):**
1. Create a GitHub repository
2. Push your code:
   ```bash
   git init
   git add .
   git commit -m "Initial deployment"
   git branch -M main
   git remote add origin YOUR_REPO_URL
   git push -u origin main
   ```
3. Connect repository to Netlify:
   - Go to Netlify → New Site → Import from Git
   - Select your repository
   - Build settings: Leave empty (static site)
   - Publish directory: `.` (root)
   - Click "Deploy site"

**Netlify Configuration:**
- The `netlify.toml` file is already configured
- Handles SPA routing automatically
- Admin route: `/admin` → serves `admin-enhanced.html`

### Option 2: Vercel

1. Go to [vercel.com](https://vercel.com)
2. Sign up or log in
3. Import from Git or drag & drop
4. Framework preset: Other
5. Build command: (leave empty)
6. Output directory: `.`
7. Deploy

### Option 3: GitHub Pages

1. Create a GitHub repository
2. Enable GitHub Pages in Settings → Pages
3. Select branch: main
4. Folder: / (root)
5. Save

**Note:** GitHub Pages doesn't support custom routing like Netlify, so the admin route won't work as cleanly.

## Post-Deployment

### Testing Your Deployed Site

Visit these URLs and test:
- `https://your-domain.com/` - Main app
- `https://your-domain.com/admin` - Admin interface (read-only)
- Test all game modes
- Test hero filtering
- Test language switching
- Test on mobile devices

### Expected Behavior

**User Interface (index.html):**
- ✅ Fully functional
- ✅ All team recommendations work
- ✅ Hero filtering works
- ✅ Language switching works
- ✅ Export to PNG works
- ✅ All data loads from comps/ folder

**Admin Interface (admin-enhanced.html):**
- ✅ Page loads and displays
- ❌ Save/Load buttons will fail (no backend)
- ❌ Cannot make live changes
- ℹ️ Read-only reference only

### How to Update Content After Deployment

**Workflow:**
1. Run admin interface locally with `python admin-api.py`
2. Make changes (add/edit/delete teams)
3. Changes save to `comps/` folder locally
4. Commit changes: `git add . && git commit -m "Update teams"`
5. Push to repository: `git push`
6. Netlify/Vercel auto-deploys (30-60 seconds)
7. Changes now live! 🎉

**Quick Manual Update (Without Git):**
1. Edit JSON files directly in `comps/` folder
2. Re-deploy via drag & drop
3. Or push via Git

## Domain Configuration

### Custom Domain (Optional)

**On Netlify:**
1. Go to Site Settings → Domain Management
2. Click "Add custom domain"
3. Enter your domain (e.g., `afk.yourdomain.com`)
4. Follow DNS configuration instructions
5. SSL certificate auto-generated (free)

**On Vercel:**
1. Go to Settings → Domains
2. Add your domain
3. Configure DNS as instructed
4. SSL auto-enabled

## Password Protection (Optional)

**On Netlify:**
1. Go to Site Settings → Visitor Access
2. Enable "Password Protection"
3. Set password
4. Share URL + password with community

**On Vercel:**
1. Requires Pro plan for password protection
2. Alternative: Use Cloudflare Access (free tier available)

## Performance Optimization

Your site is already optimized:
- ✅ Lazy-loaded translations (async)
- ✅ Minimal external dependencies
- ✅ Cached hero/artifact images
- ✅ Efficient JSON data loading
- ✅ Mobile-optimized CSS

**Expected Load Times:**
- First visit: < 2 seconds
- Subsequent visits: < 500ms (cached)

## Troubleshooting

**Issue: Admin interface doesn't save**
- Expected behavior after deployment
- Admin API only works locally
- Update workflow: Local changes → Git push → Auto-deploy

**Issue: 404 errors on refresh**
- Check netlify.toml is deployed
- Verify SPA redirect rules are active

**Issue: Images not loading**
- Verify all asset folders are deployed
- Check file paths are relative (not absolute)
- Check case sensitivity (Linux servers)

**Issue: Teams not showing**
- Verify comps/ folder structure is correct
- Check JSON syntax in comps.json files
- Use browser console to see errors

## Security Notes

**Public Admin Interface:**
- Admin UI is accessible but read-only
- No security risk (cannot modify data)
- Consider removing admin-enhanced.html from deployment if desired

**Data Exposure:**
- All team compositions are public (in comps/ folder)
- This is intentional for the app to work
- No sensitive data stored

## Monitoring (Optional)

**Netlify Analytics:**
- View visitor count
- See popular pages
- Monitor performance
- No external scripts needed

**Google Analytics (if desired):**
- Add tracking code to index.html
- Monitor user behavior
- Track popular game modes

## Rollback Procedure

**Via Git:**
```bash
git log                          # Find commit hash
git revert COMMIT_HASH           # Revert changes
git push                         # Deploy old version
```

**Via Netlify:**
1. Go to Deploys
2. Find previous working deployment
3. Click "Publish deploy"
4. Site reverted immediately

## Support & Maintenance

**Regular Updates:**
- Update team compositions as meta changes
- Add new heroes when released
- Update translations if needed
- Test on new mobile devices/browsers

**Backup Strategy:**
- Git repository serves as backup
- Netlify keeps deployment history (1 year)
- Export comps/ folder periodically

---

## Quick Deploy Command Summary

```bash
# First time setup
git init
git add .
git commit -m "Initial deployment"
git remote add origin YOUR_REPO_URL
git push -u origin main

# Future updates
git add .
git commit -m "Update: description of changes"
git push

# The end - Netlify/Vercel auto-deploys! 🚀
```

---

**Ready to deploy?** Follow Option 1 (Netlify) for the easiest experience!
