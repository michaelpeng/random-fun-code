from tqdm import *

n = 1000

pair_map = {}
used_dict = {}

for c in tqdm(range(1,n+1)):
  for d in range(1,n+1):
    result = c**3 + d**3
    pair = frozenset([c,d])

    if result in pair_map.keys() and pair not in pair_map[result]:
      pair_map[result].append(pair)
      used_dict[pair] = False
    else:
      pair_map[result] = [pair]
      used_dict[pair] = False

results = 0

for result, pairs in pair_map.items():
  for pair1 in pairs:
    used_dict[pair1] = True
    for pair2 in pairs:
      if pair1 != pair2 and not used_dict[pair2]:
        results += 1
        a, b = list(pair1)
        c, d = list(pair2)
        print("a=%-4i b=%-4i c=%-4i d=%-4i" % (a, b, c, d))

print(results)