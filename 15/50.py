from itertools import combinations

def f(a1, a2, x): 
    a = a1 <= x <= a2
    b = 24 <= x <= 90
    c = 47 <= x <= 115
    return c <= (((not a) and b) <= (not c))


ox = [i / 4 for i in range(23 * 4, 116 * 4)]

res = []
for a1, a2 in combinations(ox, 2): 
    if all(f(a1, a2, x) for x in ox): 
        res.append(a2 - a1)


print(min(res))
