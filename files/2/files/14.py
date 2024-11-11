def f(n: int, base: int): 
    s = []

    while n > 0: 
        s.append(n % base)
        n = n // base
    return s


for n in range(1, 1000): 
    if len(f(n, 7)) == 2: 
        if len(f(n, 6)) == 3: 
            if f(n, 13)[0] == 3: 
                print(n)
                