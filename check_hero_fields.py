import json

filepath = r'c:\Users\Ilir\Desktop\AFK\comps\battle-drills\verdshroom\endboss\comps.json'

with open(filepath) as f:
    data = json.load(f)

subteam = data['teams'][0]  # sub1_unrivaled_boss1

print("=== SUB-TEAM HERO DETAILS ===\n")
print(f"Sub-team: {subteam.get('name')}\n")

for h in subteam['heroes']:
    print(f"Hero: {h['name']} (tile {h['tileID']})")
    for key, value in h.items():
        if key not in ['name', 'tileID']:
            print(f"  {key}: {value}")
    print()
