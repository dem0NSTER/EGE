def div(x: int): 
    d = set()

    for i in range(2, int(x ** 0.5) + 1): 
        if x % i == 0: 
            d.add(i)
            d.add(x // i)

    return sorted(d)


c = 0
for i in range(550000, 10 ** 100): 
    d = div(i)
    f = 0
    if d: 
        f = int(sum(d) / len(d))
    
    if f % 31 == 13: 
        print(i, f)
        c += 1

    if c == 5: 
        break
