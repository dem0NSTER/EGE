def div(x: int) -> list: 
    d = set()

    for i in range(2, int(x ** 0.5) + 1): 
        if x % i == 0: 
            d.add(i)
            d.add(x // i)

    return sorted(d)


c = 0
for i in range(250201, 10**100): 
    d = div(i)
    s = 0
    if d: 
        s = min(d) + max(d)
    if s % 123 == 17: 
        print(i, s)
        c += 1

    if c == 5: 
        break
    