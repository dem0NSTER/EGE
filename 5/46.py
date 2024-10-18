
def f(n1: list): 
    s = []
    for i in range(len(n1) - 1): 
        s.append(int(n1[i] + n1[i + 1]))
    return s


for n in range(10, 10000): 
    n1 = [i for i in str(n)]
    n2 = f(n1)
    minn = min(n2)
    maxx = max(n2)
    r = maxx - minn
    if r == 44: 
        print(n)
        break
