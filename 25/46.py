from fnmatch import fnmatch


def div(n: int): 
    s = set()

    for i in range(1, int(n ** 0.5) + 1): 
        if n % i == 0: 
            s.add(i)
            s.add(n // i)

    return sorted(s)


res = []
for i in range(10 ** 7, 1, -1): 
    if fnmatch(str(i), '9?*55*7'): 
        d = div(i)
        res.append([i, sum(d) % 21])

    if len(res) == 5: 
        break


for i in res[::-1]: 
    print(*i)
