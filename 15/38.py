from itertools import combinations

def f(x, a1, a2):
    q = 32 <= x <= 60
    p = 21 <= x <= 48
    a = a1 <= x <= a2
    return q <= (((not a) and p) <= (not q))

ox = [i / 4 for i in range(20 * 4, 61 * 4)]
res = []

for a1, a2 in combinations(ox, 2):
    if all(f(x, a1, a2) for x in ox):
        res.append(a2 - a1)

print(min(res))
