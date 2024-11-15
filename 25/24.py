def div(x): 
    d = set()

    for i in range(2, int(x ** 0.5) + 1): 
        if x % i == 0: 
            d.add(i)
            d.add(x // i)

    return sorted(d)


for i in range(81234, 132689 + 1): 
    d = div(i)
    if len(d) == 3: 
        print(*d)
        