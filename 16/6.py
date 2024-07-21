import sys
sys.setrecursionlimit(2000)

def f(n): 
    if n == 0: 
        return 5
    if n > 0 and n % 2 == 0: 
        return 1 + f(n // 2)
    if n > 0 and n % 2 != 0: 
        return f(n // 2)

c = 0

for i in range(1, 1001): 
    if f(i) == 7: 
        c += 1

print(c)
