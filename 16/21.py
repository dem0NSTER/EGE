from sys import setrecursionlimit
setrecursionlimit(10000)

def f(n: int):
    if n <= 15:
        return n
    if n % 4 == 0:
        return n + f(n // 4 + 2)
    else:
        return n + f(n +4)

for n in range(1, 11000):
    try:
        if f(n) > 1000:
            print(n)
            break
    except:
        continue
