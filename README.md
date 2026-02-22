# AFK Journey - Team Composition Recommender

A comprehensive web application for recommending optimal team compositions for various AFK Journey game modes.

## Features

### Core Features
- **Multi-Mode Support**: Battle Drills, Guild Raids, Dream Realm, Clash of Might
- **Dynamic Team Recommendations**: Automatically shows optimal teams based on boss selection
- **Hero Management**: Click heroes to disable them from recommendations
- **Class & Faction Filters**: Quick filter hero display by class or faction
- **Smart Replacement System**: Automatic hero substitution with fallback options
- **Override Formations**: Complex team compositions with alternate hero placements
- **Global Hero Deduplication**: Prevents same hero usage across multiple teams
- **Multi-language Support**: EN, DE, RU, ES, FR (externalized translations for fast loading)
- **Optimized Performance**: Async translation loading, cached data

### Battle Drills Mode
- **Boss Type Selection**: Endboss, Minibosses, or Strongholds (by color)
- **Multi-Map System**: Support for recurring events with different maps
- **Visual Map Display**: Battle map with color-coded boss position overlays
- **Map-Specific Data**: Each map has separate team compositions and tile positions
- **Boss Position Markers**: Shows clear path order with color coding

### Technical Features
- Export recommendations as PNG
- Formation reference guide
- Artifact and Phantimal support
- Special handling for turrets/clones (multiple instances allowed)
- **Mobile Optimized**: Full support for Android and iOS (portrait & landscape)
- **Touch-Friendly**: 44px minimum touch targets, visual tap feedback
- **Responsive Design**: Adapts to phone, tablet, and desktop screens
- **Sticky Navigation**: Header stays visible while scrolling
- **Smart Zoom**: Optimized for 150% zoom with flex-wrap layout protection
- **Auto Scroll**: Returns to top when switching game modes

## Documentation

- **[ARCHITECTURE.md](ARCHITECTURE.md)** - Comprehensive arc42 architecture documentation for developers
- **[DEPLOYMENT.md](DEPLOYMENT.md)** - Full deployment guide with Netlify, Vercel, GitHub Pages
- **[PRE-DEPLOYMENT-CHECKLIST.md](PRE-DEPLOYMENT-CHECKLIST.md)** - Quick checklist before going live
- **[REPLACEMENT_SYSTEM.md](REPLACEMENT_SYSTEM.md)** - Complete guide for hero replacements and formation overrides
- **[SUBTEAM_FEATURE.md](SUBTEAM_FEATURE.md)** - Sub-team (fallback) system for when primary teams can't be formed
- **[MOBILE_TESTING.md](MOBILE_TESTING.md)** - Mobile testing guide for Android and iOS devices
- **[ADMIN_GUIDE.md](ADMIN_GUIDE.md)** - Complete guide for using the admin interface
- **[ADMIN_QUICKSTART.md](ADMIN_QUICKSTART.md)** - Quick 5-minute admin setup guide
- **[README.md](README.md)** - This file (user guide and deployment instructions)

## How to Deploy to Netlify

1. Create a free account at [netlify.com](https://netlify.com)
2. Drag and drop the entire AFK folder to Netlify's deployment area
3. Your site will be live instantly!

### Enable Password Protection (Optional)

1. Go to Site Settings → Visitor Access
2. Enable "Password Protection"
3. Set a password
4. Share the URL and password with your community

## Local Development

To run locally:
```bash
python -m http.server 8000
```
Then open `http://localhost:8000`

## Updating Content

### Battle Drills
- **Add Maps**: Create folder `comps/battle/{map-id}/` with required files
- **Add Boss Positions**: Use `boss_position_picker.html` to mark locations
- **Add Teams**: Edit `comps/battle/{map-id}/comps.json` with bossType filters
- **Update Formations**: Modify `tiles.json` or use `tile_picker.html`

### Heroes & Assets
- **Add/Edit Heroes**: Update the HEROES object in `index.html`
- **Add Artifacts**: Add images to `artifacts/` folder
- **Add Phantimals**: Add images to `phantimals/` folder
- **Add Hero Icons**: Add images to `heroes/` folder

## Tools

- **tile_picker.html** - Calibrate tile positions on formation templates
- **boss_position_picker.html** - Mark boss positions on battle maps

## File Structure

```
AFK/
├── index.html                    # Main application
├── tile_picker.html             # Tool for calibrating tile positions
├── boss_position_picker.html    # Tool for marking boss positions
├── netlify.toml                 # Netlify configuration
├── heroes/                      # Hero icon images
├── artifacts/                   # Artifact images
├── phantimals/                  # Phantimal images
├── classes/                     # Class icons
├── factions/                    # Faction icons
└── comps/
    ├── battle/                  # Battle Drills mode
    │   ├── maps.json           # Map definitions with boss positions
    │   ├── desolate-grounds/   # Current map (Season 1)
    │   │   ├── map.jpg         # Battle map image
    │   │   ├── empty.png       # Formation template
    │   │   ├── comps.json      # Team compositions
    │   │   └── tiles.json      # Tile positions
    │   └── verdshroom/         # Future map
    ├── guild/                   # Guild Raid mode
    ├── clash/                   # Clash of Might mode
    └── dream/                   # Dream Realm mode
```

## Current Battle Drills Data

**Desolate Grounds** (Season 1)
- 1 Endboss (3 teams)
- 2 Minibosses: Wedge of Matter, Wedge of Power (3 teams each)
- 14 Strongholds: Red (6), Blue (5), Green (5) (2-3 teams each)
- Total: 17 boss positions with complete compositions

## License

Personal use only.
