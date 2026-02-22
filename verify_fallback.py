import json

filepath = r'c:\Users\Ilir\Desktop\AFK\comps\battle-drills\verdshroom\endboss\comps.json'

with open(filepath) as f:
    data = json.load(f)

print("=== FALLBACK CONFIGURATION CHECK ===\n")

# Find all sub-teams
sub_teams = [t for t in data['teams'] if t.get('isSubTeam')]
print(f"Found {len(sub_teams)} sub-team(s):\n")
for st in sub_teams:
    print(f"  - {st.get('name', st.get('compID'))} (ID: {st.get('compID')})")
    print(f"    Heroes: {', '.join([h['name'] for h in st['heroes']])}")
    print()

# Find primary teams with fallbacks
primary_with_fallback = [t for t in data['teams'] if t.get('subTeamId') and not t.get('isSubTeam')]
print(f"Found {len(primary_with_fallback)} primary team(s) with fallback:\n")
for pt in primary_with_fallback:
    print(f"  - {pt.get('name', pt.get('compID'))} → fallback: {pt.get('subTeamId')}")
    print(f"    Heroes: {', '.join([h['name'] for h in pt['heroes']])}")
    # Check if the fallback exists
    fallback_exists = any(st.get('compID') == pt['subTeamId'] for st in sub_teams)
    if fallback_exists:
        print(f"    ✓ Fallback sub-team EXISTS")
    else:
        print(f"    ✗ WARNING: Fallback sub-team NOT FOUND!")
    print()

print("\n=== TEST INSTRUCTIONS ===")
print("To see the fallback team:")
if primary_with_fallback:
    pt = primary_with_fallback[0]
    print(f"1. In the app, UNCHECK these heroes from '{pt.get('name')}':")
    for h in pt['heroes'][:2]:  # Show first 2 heroes
        print(f"   - {h['name']}")
    print("2. Click 'Recommend' button")
    print(f"3. You should see '{sub_teams[0].get('name')}' with '⚠️ Fallback Team' badge")
