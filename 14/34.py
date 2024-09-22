def f(n, base): 
    s = []

    while n > 0: 
        s.append(n % base)
        n = n // base
    return s[::-1]


a = 5 * 216**1156 - 4 * 36**1147 + 6**1153 - 875
b = f(a, 6)
print(b.count(5) - b.count(0))