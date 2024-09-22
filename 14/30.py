def f(n, base):
    s = []

    while n > 0: 
        s.append(n % base)
        n = n // base
    return s[::-1]

for x in range(1, 1000): 
    a = 125 ** 200 - 5 ** x + 74
    b = f(a, 5)
    if b.count(4) == 100: 
        print(x)
        break