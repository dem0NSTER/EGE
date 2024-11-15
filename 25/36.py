def div(n: int): 
    s = set()

    for i in range(2, int(n ** 0.5) + 1): 
        if n % i == 0: 
            s.add(i)
            s.add(n // i)

    return sorted(s)


for n in range(25317, 51237 + 1): 
    d = [i for i in div(n) if len(div(i)) == 0]
    if len(d) > 5: 
        print(n, max(d))
        