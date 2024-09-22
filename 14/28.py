def f(n, base): 
    s = []

    while n > 0: 
        s.append(n % base)
        n = n // base
    return s[::-1]

a = 2 * 27**7 + 3 ** 10 - 9
a1 = f(a, 3)
print(a1.count(0))