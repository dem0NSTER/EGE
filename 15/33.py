from itertools import combinations

def f(a1, a2, x):
    a = a1 <= x <= a2
    q = 37 <= x <= 83
    p = 17 <= x <= 54
    return p <= ((q and (not a)) <= (not p))

ox = [i / 4 for i in range(16 * 4, 84 * 4)]
res = []

for a1, a2 in combinations(ox, 2):
    if all(f(a1, a2, x) for x in ox):
        res.append(a2 - a1)

print(min(res))
