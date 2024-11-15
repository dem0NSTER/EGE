def div(n: int): 
    s = set()

    for i in range(2, int(n * 0.5) + 1): 
        if n % i == 0:
            s.add(i)
            s.add(n // i)

    return sorted(s)


c = 0
for n in range(500_000, 1, -1): 
    d = [i for i in div(n) if len(div(i)) == 0]
    s = sum(d)

    if s != 0 and s % 10 == 0: 
        c += 1
        print(n, s)
    
    if c == 7: 
        break
