# AFK Journey - Copilot Instructions

## Project Overview
A web-based team composition recommender for the mobile game **AFK Journey**.
Players select a game mode and boss, and the tool recommends optimal hero teams with smart fallback/replacement logic.

Deployed on **GitHub Pages**. No build step. Runs as a static site.
Local dev: `python -m http.server 8000`

---

## Tech Stack
- **Frontend**: Vanilla HTML/CSS/JS — single file `index.html` (the entire app)
- **Admin UI**: `admin-enhanced.html` — browser-based editor for managing comp data
- **Admin API**: `admin-api.py` — Python Flask server (local use only, not deployed)
- **Data**: JSON files under `comps/` — no database
- **Translations**: `translations.json` — loaded async at runtime
- **Assets**: `heroes/`, `artifacts/`, `phantimals/`, `factions/`, `classes/` — PNG icons

---

## Key Files
| File | Purpose |
|------|---------|
| `index.html` | Entire frontend app — HEROES object, all JS logic, all CSS |
| `admin-enhanced.html` | Admin interface for editing comps JSON |
| `admin-api.py` | Python Flask API for admin (local only) |
| `comps/comps.json` | Generic/shared team compositions |
| `comps/battle/maps.json` | Battle Drills map registry |
| `comps/battle/{map}/tiles.json` | Formation tile positions per map |
| `comps/battle/{map}/map.jpg` | Visual battle map image |
| `comps/battle/{map}/empty.png` | Blank formation template |
| `comps/battle-drills/{map}/{boss-type}/comps.json` | Boss-type-specific comps (endboss, miniboss, stronghold-red, etc.) |
| `comps/clash/comps.json` | Clash of Might comps |
| `comps/dream/comps.json` | Dream Realm comps |
| `comps/guild/comps.json` | Guild Raid comps |
| `translations.json` | All UI strings keyed by language code |
| `heroes_data.csv` | Hero metadata reference |

---

## Hero Data Structure (inside `index.html`)
```js
const HEROES = {
  HeroName: { name:"Display Name", class:"Tank|Warrior|Mage|Marksman|Rogue|Support", faction:"Celestial|Lightbearer|Wilder|Mauler|Graveborn|Hypogean", icon:"heroes/HeroName.png" }
}
```
- Special heroes: `Phraesto_Clone`, `Elijah_Clone` — turrets/clones that can appear multiple times
- Hero icons live in `heroes/` folder

---

## Comp JSON Structure
```json
{
  "teams": [
    {
      "id": "unique_id",
      "name": "Team 1",
      "hint": "Optional hint text",
      "heroes": [
        { "name": "HeroName", "tileID": 7 },
        { "name": "HeroName", "tileID": 3, "replacements": [
          "SimpleReplacement",
          { "name": "ComplexReplacement", "heroesOverride": [ ...full 5-hero override... ] }
        ]}
      ],
      "artifact": { "name": "ArtifactName", "tileID": 14 },
      "phantimal": { "name": "PhantimalName", "tileID": 2 },
      "conditions": { "bossHpAbove": 50 },
      "bossType": "endboss|miniboss|stronghold-red|stronghold-blue|stronghold-green",
      "bossID": "specific-boss-id",
      "subTeams": [ ...fallback teams if primary heroes unavailable... ]
    }
  ]
}
```
- `tileID` references a position in the corresponding `tiles.json`
- `replacements`: array of strings (simple swap) or objects with `heroesOverride` (full formation change)
- `conditions`: optional filters like `bossHpAbove`, `bossHpBelow`
- `subTeams`: fallback compositions when primary heroes are disabled

---

## Battle Drills Map Structure
```
comps/battle/maps.json                          — map registry (set isCurrent:true for active map)
comps/battle/{map-id}/
  tiles.json                                    — formation tile positions
  map.jpg                                       — visual map image
  empty.png                                     — blank formation template
comps/battle-drills/{map-id}/{boss-type}/
  comps.json                                    — teams for that boss type
```
Current active map: **Desolate Grounds** (season 6). Verdshroom (season 6, earlier rotation) is preserved and kept in maps.json — do not delete it. Desolate-Grounds boss positions (`bossPositions` array in maps.json) still need to be set — use the browser devtools click method or recreate `boss_position_picker.html` if needed (it was in the deleted backup folder).

Boss types: `endboss`, `miniboss`, `stronghold-red`, `stronghold-green`, `stronghold-blue`, `camp`

---

## Game Modes
- **Battle Drills** — multi-map seasonal event, boss-type based filtering
- **Guild Raids** — single boss list
- **Dream Realm** — single boss list  
- **Clash of Might** — PvP mode

---

## Conventions & Rules
1. **Never add a build step** — this is pure static HTML/JS/CSS
2. **All hero logic lives in `index.html`** — do not split into separate JS files unless asked
3. **JSON data files are the source of truth** — don't hardcode comp data in JS
4. **Hero names in JSON must exactly match keys in the `HEROES` object**
5. **tileIDs are 1-based integers** referencing positions in tiles.json
6. **Global deduplication**: heroes used in earlier teams are excluded from later teams in the same render pass
7. **Replacements are tried in order** — first valid replacement wins
8. **`heroesOverride`** replaces the entire team formation, not just one hero
9. **Translations**: all user-facing strings go in `translations.json`, never hardcoded in HTML
10. **Mobile-first**: min 44px touch targets, test at 150% zoom

---

## How to Add a New Battle Drills Map

1. **Create the battle folder**: `comps/battle/{map-id}/`
   - Add `map.jpg` — the visual map image
   - Add `empty.png` — blank formation template (must be 405x333px to reuse existing tiles.json)
   - Add `tiles.json` — if empty.png is 405x333px, copy from an existing map; otherwise use `tile_picker.html` (in `backup_unused_*/`) to generate new tile coordinates

2. **Create boss-type comp folders**: `comps/battle-drills/{map-id}/`
   - Create subfolders: `endboss/`, `miniboss/`, `stronghold-red/`, `stronghold-green/`, `stronghold-blue/`, `cleanup/`
   - Each needs a `comps.json` starting with `{ "teams": [] }`

3. **Register in `comps/battle/maps.json`**:
   - Add a new map entry with `"isCurrent": true`
   - Set `"isCurrent": false` on all other maps
   - Fill in `minibosses` array (id, name, order) and `bossPositions` array (type, color, order, x, y) — open `map.jpg` in the browser or use an image viewer to find pixel coordinates of each boss position on the map

4. **Update copilot-instructions.md**: Change the "Current active map" line to reflect the new map

---

## Formation Rendering (DOM-based)

Team cards display heroes positioned over `empty.png` using DOM elements, not a canvas.
This is `renderCompFormation()` in `index.html`, called by `renderTeams()`.
`generateCompImage()` (canvas-based) is still used **only** for PNG export — do not replace it.

### How it works
1. A `position:relative; width:100%` container div is created per team card.
2. `empty.png` is added as an **in-flow** `<img>` (`width:100%; height:auto; display:block; margin:0; max-width:none; max-height:none`).
   - `margin:0` is critical — the legacy `.team img { margin-bottom:15px }` CSS rule would otherwise inflate the container height and shift all `top:%` values downward proportionally.
   - `max-width:none; max-height:none` overrides the legacy `.team img { max-width:180px; max-height:180px }` rule that would squish the background.
3. Hero/artifact/phantimal icons are `position:absolute` children, placed using `%` coordinates derived from `tiles.json`:
   - `left: (tile.x / TW) * 100%` — where TW = 405 (template pixel width)
   - `top:  (tile.y / TH) * 100%` — where TH = 333 (template pixel height)
   - `width: (tile.size / TW) * 100%`
   - `transform: translate(-50%, -50%)` — centers the icon on the tile coordinate
4. Because `empty.png` is in-flow, the container's auto-height exactly equals the rendered image height. All `top:%` values are then computed against that same height — correct at any scale with no JS required.

### Key CSS pitfalls to avoid
| Rule | Where | Problem if not overridden |
|------|--------|--------------------------|
| `.team img { max-width:180px; max-height:180px }` | index.html ~line 143 | Squishes the background to 180px, making icons appear oversized and off-tile |
| `.team img { margin-bottom:15px }` | index.html ~line 144 | Inflates container height; bottom tiles shift down more than top tiles |

---

## What's Already Built (don't re-implement)
- Hero disable/enable by clicking (persisted in localStorage)
- Class and faction filter buttons
- Global hero deduplication across teams
- Smart replacement system with heroesOverride
- SubTeam fallback system
- Multi-language support (EN, DE, RU, ES, FR)
- PNG export of recommendations
- Battle Drills multi-map system with visual boss position markers
- Mobile responsive layout
- Admin interface with CRUD for comp data
- Artifact and Phantimal support
