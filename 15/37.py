from itertools import combinations

def f(x, a1, a2):
    p = 20 <= x <= 54
    q = 37 <= x <= 83
    a = a1 <= x <= a2
    return p <= ((q and (not a)) <= (not p))

ox = [i / 4 for i in range(19 * 4, 84 * 4)]
res = []

for a1, a2 in combinations(ox, 2):
    if all(f(x, a1, a2) for x in ox):
        res.append(a2 - a1)

print(min(res))

