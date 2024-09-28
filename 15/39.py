from itertools import combinations

def f(x, a1, a2):
    a = a1 <= x <= a2
    q = 33 <= x <= 98
    p = 20 <= x <= 67
    return p <= ((q and (not a)) <= (not p))

ox = [i / 4 for i in range(19 * 4, 99 * 4)]
res = []

for a1, a2 in combinations(ox, 2):
    if all(f(x, a1, a2) for x in ox):
        res.append(a2 - a1)

print(min(res))
