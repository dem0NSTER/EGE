def f(n, base): 
    s = []

    while n > 0: 
        s.append(n % base)
        n = n // base
    return s[::-1]

a = 51 * 7**12 - 7**3 - 22
b = f(a, 7)
print(sum(b))