# 🔄 Hero Replacement & Formation Override Guide

This guide explains how to handle hero replacements when the original hero is unavailable.

## Overview

The system supports **two types** of replacements:

1. **Simple Replacement** - Replace one hero with another (same or different position)
2. **Formation Override** - Use a completely different formation when primary hero unavailable

---

## 1️⃣ Simple Replacement

### Same Position Replacement
Replace a hero with another hero in the **same tile position**.

**Example:** Replace Rowan with Mikola in position 1
```json
{
  "id": "team_001",
  "name": "Standard Team",
  "heroes": [
    {
      "name": "Rowan",
      "tileID": 1,
      "replacements": ["Mikola"]
    },
    {
      "name": "Brutus",
      "tileID": 2,
      "replacements": []
    }
  ]
}
```

**Result:**
- ✅ If Rowan available → Use Rowan in tile 1
- ❌ If Rowan unavailable → Use Mikola in tile 1

---

### Different Position Replacement
Replace a hero with another hero in a **different tile position**.

**Example:** Replace Rowan (tile 1) with Mikola (tile 5)
```json
{
  "name": "Rowan",
  "tileID": 1,
  "replacements": [
    {
      "name": "Mikola",
      "tileID": 5
    }
  ]
}
```

**Result:**
- ✅ If Rowan available → Rowan in tile 1
- ❌ If Rowan unavailable → Mikola in tile 5 (formation changes slightly)

---

### Multiple Replacements (Priority Chain)
Define multiple fallback options. System tries them in order.

```json
{
  "name": "Eironn",
  "tileID": 1,
  "replacements": ["Lyca", "Arden", "Mikola"]
}
```

**Priority Order:**
1. Try Eironn (primary)
2. If unavailable, try Lyca
3. If unavailable, try Arden
4. If unavailable, try Mikola
5. If all unavailable → Team marked as unplayable

---

## 2️⃣ Formation Override (Complete Formation Change)

When a replacement requires a **completely different formation** (multiple heroes in different positions), use `heroesOverride`.

### Use Cases
- Hero A requires specific synergy partners
- Hero B needs support heroes in different positions
- Formation fundamentally changes without Hero A

### Structure

```json
{
  "id": "team_advanced",
  "name": "Eironn Comp with Override",
  "heroes": [
    {
      "name": "Eironn",
      "tileID": 1,
      "replacements": [
        {
          "name": "Carolina",
          "heroesOverride": [
            {"name": "Carolina", "tileID": 1},
            {"name": "Lyca", "tileID": 2},
            {"name": "Arden", "tileID": 5},
            {"name": "Rowan", "tileID": 8},
            {"name": "Brutus", "tileID": 10}
          ]
        }
      ]
    },
    {
      "name": "Lyca",
      "tileID": 3,
      "replacements": []
    },
    {
      "name": "Arden",
      "tileID": 7,
      "replacements": []
    }
    // ... other heroes
  ]
}
```

### How It Works

**Primary Formation Available:**
```
Tile 1: Eironn
Tile 3: Lyca
Tile 7: Arden
... (other heroes)
```

**Eironn Unavailable → Override Activates:**
```
Tile 1: Carolina  (from override)
Tile 2: Lyca      (from override - NEW POSITION!)
Tile 5: Arden     (from override - NEW POSITION!)
Tile 8: Rowan     (from override)
Tile 10: Brutus   (from override)
```

**Key Points:**
- ✅ **Entire formation replaced** when override activates
- ✅ All heroes must be available for override to work
- ✅ If override heroes unavailable, team marked as unplayable
- ✅ Replacements ignore class/faction filters

---

## 3️⃣ Nested Replacements in Overrides

Heroes in `heroesOverride` can have their own replacements!

```json
{
  "name": "Eironn",
  "tileID": 1,
  "replacements": [
    {
      "name": "Carolina",
      "heroesOverride": [
        {
          "name": "Carolina",
          "tileID": 1,
          "replacements": ["Mikola"]  // ← If Carolina unavailable, use Mikola
        },
        {
          "name": "Lyca",
          "tileID": 2,
          "replacements": ["Arden"]   // ← If Lyca unavailable, use Arden
        }
      ]
    }
  ]
}
```

**Fallback Chain:**
1. Try primary formation (Eironn + original team)
2. If Eironn unavailable → Try override formation
3. If Carolina unavailable → Try Mikola in override
4. If all fail → Team unplayable

---

## 4️⃣ Priority System

The system checks replacements in this order:

### For Simple Replacements:
```
1. Primary hero available? → Use primary
2. First replacement available? → Use first replacement
3. Second replacement available? → Use second replacement
... continue until one works
```

### For Formation Overrides:
```
1. Primary hero available? → Use primary formation
2. Primary unavailable + simple replacement exists? → Use simple replacement
3. No simple replacement works? → Check heroesOverride
4. All override heroes available? → Use override formation
5. Override impossible? → Team unplayable
```

**Priority:** Simple replacements are tried **before** formation overrides.

---

## 5️⃣ Admin Interface Usage

### How to Add Replacements

**Coming Soon:** The admin interface will have a visual replacement editor.

**Current Method:** Manually edit comps.json files

**Simple Replacement:**
```json
"replacements": ["HeroName1", "HeroName2"]
```

**Position Change:**
```json
"replacements": [
  {
    "name": "HeroName",
    "tileID": 5
  }
]
```

**Formation Override:**
```json
"replacements": [
  {
    "name": "ReplacementName",
    "heroesOverride": [
      {"name": "Hero1", "tileID": 1},
      {"name": "Hero2", "tileID": 2}
    ]
  }
]
```

---

## 6️⃣ Best Practices

### ✅ DO:
- Use simple replacements for direct swaps
- Use formation overrides when formation fundamentally changes
- Test all replacement paths with hero filtering
- Provide 2-3 replacement options per hero
- Document why override is used

### ❌ DON'T:
- Don't use override for single hero tile changes (use simple replacement with tileID)
- Don't create circular replacement chains
- Don't override with formations requiring unavailable heroes
- Don't skip testing override formations

---

## 7️⃣ Examples

### Example 1: Tank Replacement (Same Position)
```json
{
  "name": "Thoran",
  "tileID": 1,
  "replacements": ["Brutus", "Lucius"]
}
```
**Behavior:** Thoran → Brutus → Lucius (all in tile 1)

---

### Example 2: Carry Replacement (Different Position)
```json
{
  "name": "Eironn",
  "tileID": 3,
  "replacements": [
    {
      "name": "Lyca",
      "tileID": 7
    }
  ]
}
```
**Behavior:** Eironn (tile 3) → Lyca (tile 7)

---

### Example 3: Complete Formation Change
```json
{
  "name": "Eironn",
  "tileID": 1,
  "replacements": [
    {
      "name": "Carolina",
      "heroesOverride": [
        {"name": "Carolina", "tileID": 1, "replacements": []},
        {"name": "Lyca", "tileID": 2, "replacements": ["Arden"]},
        {"name": "Mikola", "tileID": 5, "replacements": []},
        {"name": "Rowan", "tileID": 8, "replacements": ["Valen"]},
        {"name": "Brutus", "tileID": 10, "replacements": ["Thoran"]}
      ]
    }
  ]
}
```

**Behavior:**
- Primary: Eironn comp (normal formation)
- Override: Carolina comp (completely different positions + heroes)
- Override heroes also have their own replacements

---

## 8️⃣ Technical Notes

**Filter Behavior:**
- Primary heroes: Respect class/faction filters
- Replacement heroes: **IGNORE** filters (always try if available)
- Override heroes: **IGNORE** filters (always try if available)

**Global Hero Tracking:**
- Heroes used in one team cannot be used in another
- Applies to primary AND replacement heroes
- System tracks usage across all recommended teams

**Validation:**
- Team marked "unplayable" if no valid configuration exists
- User sees red warning icon
- Team still displayed with missing heroes shown

---

## Summary

| Feature | Use Case | Example |
|---------|----------|---------|
| **Simple Replacement (String)** | Direct swap, same position | `"replacements": ["Mikola"]` |
| **Position Change (Object)** | Swap + move to different tile | `{"name": "Mikola", "tileID": 5}` |
| **Formation Override** | Completely different formation | `{"name": "X", "heroesOverride": [...]}` |

**Question:** Need to change formation when hero unavailable?  
**Answer:** Use `heroesOverride`! ✅
