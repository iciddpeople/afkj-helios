import json

with open(r'c:\Users\Ilir\Desktop\AFK\comps\battle-drills\verdshroom\endboss\comps.json') as f:
    data = json.load(f)

print(f"Total teams: {len(data['teams'])}\n")

for i, t in enumerate(data['teams']):
    name = t.get('name', t.get('compID', 'NO NAME'))
    is_sub = t.get('isSubTeam', False)
    sub_id = t.get('subTeamId', None)
    print(f"{i}: {name}")
    print(f"   isSubTeam: {is_sub}")
    print(f"   subTeamId: {sub_id}")
    print()
