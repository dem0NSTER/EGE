from itertools import combinations

def f(x, a1, a2): 
    p = 5 <= x <= 100
    q = 15 <= x <= 25
    r = 35 <= x <= 50
    a = a1 <= x <= a2
    return (p <= q) or ((not a) <= r)


ox = [i / 4 for i in range(3 * 4, 101 * 4)]
res = []

for a1, a2 in combinations(ox, 2):
    if all(f(x, a1, a2) for x in ox): 
        res.append(a2-a1)

print(min(res))