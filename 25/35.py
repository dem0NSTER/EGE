def div(n: int): 
    s = set()

    for i in range(2, int(n ** 0.5) + 1): 
        if n % i == 0: 
            s.add(i)
            s.add(n // i)

    return sorted(s)


for n in range(6080068, 6080176 + 1): 
    d = div(n)
    if len(d) == 0: 
        print(n)
