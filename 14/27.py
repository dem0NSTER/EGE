def f(n, base): 
    s = []

    while n > 0: 
        s.append(n % base)
        n = n // base
    return s[::-1]


a = 3 * 16**8 - 4**5 + 3
a1 = f(a, 4)
print(a1.count(3))
