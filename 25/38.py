def div(n: int): 
    s = set()

    for i in range(2, int(n ** 0.5) + 1): 
        if n % i == 0: 
            s.add(i)
            s.add(n // i)

    return sorted(s)


def f(n: int, div: list) -> list:
    for division in div: 
        first = n // division
        if first in div: 
            return sorted([first, division])
        

for n in range(125697, 125721 + 1): 
    d = [i for i in div(n) if len(div(i)) == 0]
    res = f(n, d)
    if res: 
        print(res[0], res[1])