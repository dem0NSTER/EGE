from itertools import permutations


def f(n1: list): 
    s = []
    for i in permutations(n1, r=2): 
        if i[0] == '0': 
            continue
        s.append(int(''.join(i)))
        
    return [min(s), max(s)]


for n in range(100, 999): 
    n1 = [i for i in str(n)]
    minn, maxx = f(n1)
    r = maxx - minn
    if r == 5: 
        print(n)
