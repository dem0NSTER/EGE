from fnmatch import fnmatch


def div(n: int): 
    s = set()

    for i in range(1, int(n ** 0.5) + 1): 
        if n % i == 0: 
            s.add(i)
            s.add(n // i)
    return sorted(s)


c = 0
for i in range(65001, 10 ** 100): 
    if fnmatch(str(i), '6*97*5?'): 
        d = [x for x in div(i) if x % 2 == 0]
        if len(d) > 3: 
            c += 1
            print(i, sum(d))
        
    if c == 7: 
        break
    