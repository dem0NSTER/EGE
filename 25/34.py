def div(n: int): 
    s = set()

    for i in range(2, int(n ** 0.5) + 1): 
        if n % i == 0: 
            s.add(i)
            s.add(n // i)

    return sorted(s)


c = 0
for n in range(550001, 10 ** 10): 
    d = [i for i in div(n) if str(i)[-1] == '7']

    if len(d) == 3: 
        c += 1
        print(n, max(d))

    if c == 5: 
        break
    