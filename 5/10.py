def f(n: int, base: int) -> str: 
    s = ''

    while n > 0: 
        s += str(n % base)
        n = n // base
    return s[::-1]


for n in range(1000, 1, -1): 
    n3 = f(n, 3)

    if n % 3 == 0: 
        n3 = '1' + n3 + '02'
    else: 
        n3 += f((n % 3) * 4, 3)

    r = int(n3, 3)

    if r < 199: 
        print(n)
        break