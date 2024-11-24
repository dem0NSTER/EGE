from itertools import combinations


def f(a1, a2, x): 
    a = a1 <= x <= a2
    p = 19 <= x <= 56
    q = 32 <= x <= 84
    return ((not a) and q) <= p


ox = [i / 4 for i in range(18 * 4, 85 * 4)]

res = []
for a1, a2 in combinations(ox, 2): 
    if all(f(a1, a2, x) for x in ox): 
        res.append(a2 - a1)

print(min(res))
