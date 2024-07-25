def f(n: int, base: int) -> str: 
    s = ''

    while n > 0: 
        s += str(n % base)
        n = n // base
    return s[::-1]

for n in range(1, 1000): 
    n5 = f(n, 5)

    if n % 7 == 0: 
        n5 += n5[-2:]
    else: 
        n5 += f((n % 7) * 7, 5)
    
    r = int(n5, 5)

    if r > 1234: 
        print(n)
        break

