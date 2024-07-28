import sys

sys.setrecursionlimit(2000)

res = []

def f(n): 
    res.append(n)
    

    if n >= 7: 
        res.append(n * n)
        f(n - 1)
        f(n - 2)

    # return sum(res)


for n in range(1, 1500):
    res = []
    f(n)
    if sum(res) >= 1000000:
        print(n)
        break
