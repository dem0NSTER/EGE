def f(n, base): 
    s = []

    while n > 0: 
        s.append(n % base)
        n = n // base
    return s[::-1]


for n in range(2, 10):
    a = f(68, n)
    if len(a) == 4 and a[-1] == 2: 
        print(n)
        break