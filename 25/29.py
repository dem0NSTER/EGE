def div(x: int) -> list: 
    d = set()

    for i in range(2, int(x ** 0.5) + 1): 
        if x % i == 0: 
            d.add(i)
            d.add(x // i)

    return sorted(d)


c = 0
for i in range(400_000_001, 10**100): 
    d = div(i)
    p = 0

    if len(d) >= 5: 
        p = d[0] * d[1] * d[2] * d[3] * d[4]
    
    if p != 0:
        if p <= i and str(p)[-2] + str(p)[-1] == '17': 
            print(p, d[4])
            c += 1
    
    if c == 5: 
        break
