# 🔄 Sub-Team (Fallback) Feature

## Overview

The Sub-Team feature allows you to configure **fallback teams** that only appear when a primary team cannot be formed. This ensures users always see 3 recommended teams even when hero availability is limited.

---

## How It Works

### Priority System
```
1. Try to form Primary Team 1
   ├─ Success → Show Primary Team 1
   └─ Fail → Check if Primary Team 1 has a sub-team
       ├─ Has sub-team → Try to form sub-team
       │   ├─ Success → Show Sub-team 1 (with fallback badge)
       │   └─ Fail → Skip this slot
       └─ No sub-team → Skip this slot

2. Repeat for Primary Team 2, Primary Team 3, etc.
```

### Key Rules
- ✅ **Replacements > Sub-teams**: Primary team with replacements is always tried first
- ✅ **Sub-teams are hidden** until needed (not shown in the comp pool)
- ✅ **Cascading is acceptable**: Sub-team 1 can make Primary Team 2 unplayable (as long as Primary Team 2 has its own sub-team)
- ✅ **Hero deduplication**: Sub-teams respect global hero tracking (heroes used in Sub-team 1 can't be used in Team 2)

---

## Configuration (Admin UI - Tab 2)

### Creating a Sub-Team

**Step 1: Mark as Sub-team**
1. Process screenshots in Tab 1 (upload fallback team formation)
2. Go to Tab 2 → Configure team
3. ☑️ Check **"Mark as Sub-team"**
4. Configure team normally (name, heroes, boss type, buffs, etc.)

**Step 2: Link to Primary Team**
1. Find the **primary team** that needs this fallback
2. In the Sub-Team Configuration section
3. Select your sub-team from **"Fallback Sub-team"** dropdown
4. Save in Tab 4

---

## Example Scenario

### Setup
**Primary Team: "Shade Carry"**
- Heroes: Shade, Lyca, Arden, Rowan, Brutus
- Buffs: Unrivaled Might
- Fallback Sub-team: "Marcille Fallback"

**Sub-Team: "Marcille Fallback"**
- Heroes: Marcille, Carolina, Mikola, Valen, Thoran
- Buffs: Unrivaled Might
- Mark as Sub-team: ✅

### User Experience

**Scenario A: Shade Available**
```
User UI shows:
1. Shade Carry (Primary) ✅
2. Another Primary Team ✅
3. Another Primary Team ✅
```

**Scenario B: Shade Unavailable**
```
User UI shows:
1. ⚠️ Marcille Fallback (for: Shade Carry) 
2. Another Primary Team ✅
3. Another Primary Team ✅
```
- Orange badge indicates fallback team
- User sees 3 teams total (one is a sub-team)

**Scenario C: Marcille Also Unavailable**
```
User UI shows:
1. (Empty slot - no fallback possible)
2. Another Primary Team ✅
3. Another Primary Team ✅
```

---

## Visual Indicators

### Admin UI (Tab 3)

**Sub-team Badge** 🔄
- Purple badge: "🔄 Sub-team (Fallback)"
- Indicates this team is configured as a fallback

**Has Fallback Badge** 🔗
- Blue badge: "🔗 Has Fallback"
- Indicates this primary team has a sub-team configured

### User UI

**Fallback Active Badge** ⚠️
- Orange gradient badge: "⚠️ Fallback Team (for: [Primary Name])"
- Shows when sub-team is being used instead of primary
- Hovering shows explanation

---

## Data Structure

### JSON Format
```json
{
  "id": "shade_primary",
  "name": "Shade Carry",
  "isSubTeam": false,
  "subTeamId": "marcille_sub",
  "bossType": "endboss",
  "buffs": ["unrivaled-might"],
  "heroes": [...]
}

{
  "id": "marcille_sub",
  "name": "Marcille Fallback",
  "isSubTeam": true,
  "bossType": "endboss",
  "buffs": ["unrivaled-might"],
  "heroes": [...]
}
```

### Fields
- **isSubTeam** (boolean): `true` if this is a fallback team
- **subTeamId** (string): ID of the sub-team to use as fallback (primary teams only)

---

## Use Cases

### 1. Hero Dependency
**Problem:** Eironn comp doesn't work without Eironn
**Solution:** Create Carolina sub-team as fallback

### 2. Meta Alternatives
**Problem:** Top comp requires specific 5-star heroes
**Solution:** Create budget comp as sub-team fallback

### 3. Buff-Specific Options
**Problem:** Unrivaled Might team uses Shade (single carry)
**Solution:** Fallback to Marcille team if Shade unavailable

### 4. Stronghold Variations
**Problem:** Red Stronghold comp requires specific tank
**Solution:** Fallback sub-team with alternative tank + adjusted formation

---

## Best Practices

### ✅ DO:
- Create sub-teams for high-priority comps that might fail
- Use sub-teams with **completely different heroes** (avoid overlap)
- Test both primary and sub-team scenarios
- Name sub-teams clearly (e.g., "Marcille Fallback for Shade")
- Configure buffs correctly for both primary and sub-team

### ❌ DON'T:
- Don't make sub-teams depend on the same heroes as primary
- Don't create sub-team chains (sub-team referencing another sub-team)
- Don't forget to mark teams as sub-teams
- Don't assume sub-teams will always work (they can also fail if heroes unavailable)

---

## Troubleshooting

**Q: Sub-team not appearing even when primary fails?**
- Check that primary team has `subTeamId` set correctly
- Verify sub-team is marked with `isSubTeam: true`
- Ensure sub-team heroes are available
- Check console logs for validation errors

**Q: Sub-team appears even when primary should work?**
- Check primary team configuration
- Verify replacements are configured correctly
- Replacements should be tried before sub-team

**Q: Multiple teams failing due to sub-team?**
- This is expected behavior (cascading)
- Ensure all primary teams have their own sub-teams
- Consider different hero pools for each sub-team

**Q: Sub-team shows in Tab 3 but not in user UI?**
- Sub-teams only appear when activated (primary fails)
- This is intentional - they're hidden fallbacks

---

## Technical Notes

### Recommendation Algorithm
```javascript
// Separate primary and sub-teams
const primaryTeams = allComps.filter(c => !c.isSubTeam);
const subTeams = allComps.filter(c => c.isSubTeam);

// Try each primary team
for (const primary of primaryTeams) {
  if (compValid(primary)) {
    // Use primary
    recommended.push(primary);
  } else if (primary.subTeamId) {
    // Try sub-team
    const sub = subTeams.find(s => s.id === primary.subTeamId);
    if (sub && compValid(sub)) {
      sub.isFallbackActive = true; // Mark for badge
      recommended.push(sub);
    }
  }
}
```

### Buff-Separated Display
- Sub-team logic applies separately to Unrivaled Might and Hall of Legends teams
- Each buff processes its own primary/sub-team pairs independently
- Hero deduplication works within each buff category

---

## Migration Guide

### Existing Teams
- All existing teams default to `isSubTeam: false`
- No breaking changes - everything works as before
- Add sub-teams gradually as needed

### Adding Sub-Teams to Existing Setup
1. Identify primary teams that often fail
2. Create alternative formations as sub-teams
3. Link them via admin UI
4. Test with different hero availability scenarios
5. Deploy when satisfied

---

## Future Enhancements (Potential)

- [ ] Sub-team priority ordering (if primary has multiple sub-teams)
- [ ] Visual sub-team editor in admin UI
- [ ] Statistics on how often sub-teams are used
- [ ] Recommendation to create sub-teams based on failure patterns
- [ ] Circular dependency detection

---

## Summary

| Feature | Description |
|---------|-------------|
| **Purpose** | Provide fallback teams when primary teams can't be formed |
| **Configuration** | Mark as sub-team + link from primary team dropdown |
| **Priority** | Replacements → Primary → Sub-team |
| **Visibility** | Hidden unless activated (primary fails) |
| **Indicator** | Orange "⚠️ Fallback Team" badge in user UI |
| **Cascading** | Acceptable (if other primaries have sub-teams) |

**Result:** Users always see up to 3 teams, even with limited hero availability! 🎉
