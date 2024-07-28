def f(n: int, base: int) -> str: 
    s = ''

    while n > 0: 
        s += str(n % base)
        n = n // base
    return s[::-1]

for n in range(1, 1000): 
    n3 = f(n, 3)

    if n % 3 == 0: 
        n3 += n3[-3:]
    else: 
        ost = (n % 3) * 3
        n3 += f(ost, 3)

    r = int(n3, 3)

    if r > 150: 
        print(n)
        break
