def f(n: int, base: int) -> str: 
    new = ''

    while n > 0: 
        num = n % base 
        new += str(num)
        n = n // base
    return new[::-1]

for n in range(1,  1000): 
    n3 = f(n, 3)

    if n % 3 == 0: 
        n3 += n3[-3:]
    else: 
        n3 += f(((n % 3) * 3), 3)
    
    r = int(n3, 3)

    if r > 150: 
        print(n, r)
        break
