from itertools import permutations
c = 0


def f(n1: list) -> list: 
    s = []
    for i in permutations(n1, r=2):
        if i[0] == '0': 
            continue
        s.append(int(''.join(i)))

    return [min(s), max(s)] 


for n in range(300, 401): 
    n1 = [i for i in str(n)]
    minn, maxx = f(n1)
    r = maxx - minn 
    if r == 20: 
        c += 1
        print(n, c)
