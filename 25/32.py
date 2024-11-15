def div(n: int): 
    d = set()

    for i in range(2, int(n ** 0.5) + 1): 
        if n % i == 0: 
            d.add(i)
            d.add(n // i)
    return sorted(d)


c = 0
for j in range(500001, 10 ** 100): 
    d = [i for i in div(j) if i != 8 and str(i)[-1] == '8']

    if len(d) > 0: 
        c += 1
        print(j, min(d))

    if c == 5: 
        break
