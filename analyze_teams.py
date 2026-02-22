import json

filepath = r'c:\Users\Ilir\Desktop\AFK\comps\battle-drills\verdshroom\endboss\comps.json'

with open(filepath) as f:
    data = json.load(f)

print("=== PRIMARY TEAM ANALYSIS ===\n")

primary = data['teams'][1]  # boss1_unrivaled
print(f"Primary: {primary.get('name')}")
print(f"SubTeamId: {primary.get('subTeamId')}\n")

print("Heroes and their replacements:")
for h in primary['heroes']:
    reps = h.get('replacements', [])
    if reps:
        print(f"  {h['name']} (tile {h['tileID']}) → replacements: {', '.join(reps)}")
    else:
        print(f"  {h['name']} (tile {h['tileID']}) → NO replacements")

print("\n=== SUB-TEAM ANALYSIS ===\n")

subteam = data['teams'][0]  # sub1_unrivaled_boss1
print(f"Sub-team: {subteam.get('name')}")
print(f"IsSubTeam: {subteam.get('isSubTeam')}\n")

print("Heroes:")
for h in subteam['heroes']:
    print(f"  {h['name']} (tile {h['tileID']})")

print("\n=== ANALYSIS ===")
primary_heroes = set([h['name'] for h in primary['heroes']])
subteam_heroes = set([h['name'] for h in subteam['heroes']])

print(f"\nShared heroes: {primary_heroes & subteam_heroes}")
print(f"Only in primary: {primary_heroes - subteam_heroes}")
print(f"Only in sub-team: {subteam_heroes - primary_heroes}")
