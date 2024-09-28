from itertools import combinations

def f(a1, a2, x):
    p = 23 <= x <= 37
    q = 41 <= x <= 73
    a = a1 <= x <= a2
    return not( ((not p) <= q) <= a )

ox = [i / 4 for i in range(22 * 4, 74 * 4)]
res = []

for a1, a2 in combinations(ox, 2):
    if all(not(f(a1, a2, x)) for x in ox):
        res.append(a2 - a1)

print(min(res))
