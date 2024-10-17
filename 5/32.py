def f(n: int, base: int): 
    s = ''

    while n > 0: 
        s += str(n % base)
        n = n // base
    return s[::-1]


res = []

for n in range(1, 1000): 
    n3 = f(n, 3)
    n3 += str(n % 3)
    r = int(n3, 3)
    if 100 <= r <= 999: 
        res.append(r)

print(min(res))
