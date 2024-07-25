def f(n: int, base: int) -> str: 
    new = ''

    while n > 0: 
        num = n % base
        new += str(num)
        n = n // 2
    return new[::-1]

for n in range(4, 1000): 
    n2 = f(n, 2)
    
    if n % 3 == 0: 
        n2 += n2[-3:]
    else: 
        num = f((n % 3) * 3, 2)
        n2 += num
    
    r = int(n2, 2)

    if r > 99: 
        print(n)
        break
        
    