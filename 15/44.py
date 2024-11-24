from itertools import combinations

def f(x, a1, a2): 
    p = 15 <= x <= 40
    q = 21 <= x <= 63
    a = a1 <= x <= a2
    return p <= ((q and (not a)) <= (not p))


ox = [i / 4 for i in range(14 * 4, 64 * 4)]

res = []
for a1, a2 in combinations(ox, 2): 
    if all(f(x, a1, a2) for x in ox): 
        res.append(a2 - a1)

print(min(res))
