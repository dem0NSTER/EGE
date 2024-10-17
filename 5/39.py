def f(n: int, base: int): 
    s = ''

    while n > 0: 
        s += str(n % base)
        n = n // base
    return s[::-1]


res = []

for n in range(1, 10000): 
    n6 = f(n, 6)
    if n % 3 == 0: 
        n6 += n6[:2]
    else: 
        n6 += f(10 * (n % 3), 6)

    r = int(n6, 6)
    if r > 680: 
        res.append(r)

print(min(res))