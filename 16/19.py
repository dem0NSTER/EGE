import sys

sys.setrecursionlimit(2000)

def f(n: int): 
    if n <= 15: 
        return n 
    if n % 4 == 0 and n > 15: 
        return n + f(n // 4 + 2)
    if n % 4 != 0 and n > 15:
        return n + f(n + 4)


for n in range(1, 1000): 
    try: 
        res = f(n)
        if res > 1000: 
            print(n)
            break
    except: 
        continue