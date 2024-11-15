def div(n: int): 
    s = set()

    for i in range(2, int(n ** 0.5) + 1): 
        if n % i == 0: 
            s.add(i)
            s.add(n // i)
    return sorted(s)


a = [i for i in range(106732567, 152673836 + 1) if int(i ** 0.5) == i ** 0.5]

for n in a: 
    d = div(n)
    if len(d) == 3: 
        print(n, max(d))

