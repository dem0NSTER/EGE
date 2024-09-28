from itertools import combinations 

def f(a1, a2, x):
    q = 32 <= x <= 60
    p = 21 <= x <= 48
    a = a1  <= x <= a2
    return q  <= (((not a) and p) <= (not p))


ox = [i / 4 for i in range(20 * 4 , 61 * 4)]
res = []

for a1, a2 in combinations(ox, 2):
    if all(f(a1, a2, x) for x in ox):
        res.append(a2 - a1)

print(min(res))
