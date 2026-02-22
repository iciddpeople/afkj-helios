# How to Update Your Live Site

Every time you make changes, run these 3 commands:

## Step 1: Stage all changes
```powershell
git add .
```

## Step 2: Commit with a message
```powershell
git commit -m "Disabled Desolate Grounds map"
```

## Step 3: Push to GitHub
```powershell
git push
```

**Wait 1-2 minutes** and your site will update automatically!

---

## Quick Template

```powershell
git add .
git commit -m "Your change description here"
git push
```

---

## Check Deployment Status
Go to your repo → **Actions** tab to see if the deployment succeeded.
