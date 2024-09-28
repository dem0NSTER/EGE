from itertools import combinations

def f(x, a1, a2):
    a = a1 <= x <= a2
    p = 24 <= x <= 77
    q = 47 <= x <= 92
    r = 82 <= x <= 116
    return (not(q <= (p or r))) <= ((not a) <= (not q))

ox = [i / 4 for i in range(23 * 4, 117 * 4)]
res = []

for a1, a2 in combinations(ox, 2):
    if all(f(x, a1, a2) for x in ox):
        res.append(a2 - a1)

print(min(res))
