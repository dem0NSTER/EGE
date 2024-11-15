def div(x: int) -> list: 
    d = set()

    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)


c = 0
for i in range(150000, 10**10): 
    s = 0
    if len(div(i)): 
        s = sum(div(i))
    
    if s % 13 == 10: 
        print(i, s)
        c += 1
    
    if c == 7: 
        break
