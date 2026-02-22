# Rewrite Git History - Remove Email/Name

## Step 1: Configure New Identity

```powershell
git config user.name "AFK-Dev"
git config user.email "anonymous@example.com"
```

## Step 2: Rewrite ALL Commits

```powershell
git filter-branch --env-filter '
CORRECT_NAME="AFK-Dev"
CORRECT_EMAIL="anonymous@example.com"
export GIT_COMMITTER_NAME="$CORRECT_NAME"
export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
export GIT_AUTHOR_NAME="$CORRECT_NAME"
export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
' --tag-name-filter cat -- --branches --tags
```

## Step 3: Force Push to GitHub

```powershell
git push --force --all
```

## Verify

Check your commits on GitHub - the author should now show as "AFK-Dev <anonymous@example.com>"

---

## ⚠️ Important Notes

- This rewrites **entire history**
- Anyone who cloned your repo will have issues (but since it's new, this shouldn't matter)
- Once pushed, the old email is gone from GitHub
- Your GitHub username (in the URL) remains unchanged

---

## Alternative: Start Fresh (Simpler)

If this seems complicated, it's easier to:
1. Delete GitHub repo
2. Delete local `.git` folder: `Remove-Item -Recurse -Force .git`
3. Set git identity first (Step 1 above)
4. Re-run: `git init`, `git add .`, `git commit -m "Initial deployment"`, etc.
