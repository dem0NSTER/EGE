from fnmatch import fnmatch 


def div(n: int): 
    s = set()

    for i in range(1, int(n ** 0.5) + 1): 
        if n % i == 0: 
            s.add(i)
            s.add(n // i)

    return sorted(s)


res = []
for n in range(9999794, 1, -217):
    if fnmatch(str(n), '14?4*'): 
        d = [i for i in div(n) if i % 2 != 0]
        res.append([n, sum(d)])

    if len(res) == 7: 
        break


for num in res[::-1]: 
    print(*num)
