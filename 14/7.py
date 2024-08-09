for p in range(5, 37): 
    for x in range(p): 
        for y in range(p): 
            if (1 * p ** 1 + 2) * (3 * p ** 1 + 4) == (x * p ** 2 + y * p ** 1 + 2): 
                print(p, x, y)
                print(y * p ** 1 + x)
            if int('12', p) * int('34', p) == int(f'{x}{y}2', p): 
                print(p, x, y)
                print(int(f'{y}{x}',p))
