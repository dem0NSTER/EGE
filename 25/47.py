from fnmatch import fnmatch 


def div(n: int): 
    d = set()

    for i in range(1, int(n ** 0.5) + 1): 
        if n % i == 0: 
            d.add(i)
            d.add(n // i)

    return sorted(d)


c = 0
for x in range(8, 10 ** 100, 8): 
    if x % 6 == 0 and x % 7 == 0: 
        if fnmatch(str(x), '?6*6*?6'): 
            d = div(x)
            c += 1
            print(x, sum(d))

    if c == 7: 
        break
