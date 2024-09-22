def f(n, base): 
    s = []

    while n > 0: 
        s.append(n % base)
        n = n // base
    return s[::-1]


c = 0

for i in range(1, 10000): 
    num5 = f(i, 5)
    num2 = f(i, 2)
    num16 = f(i, 16)

    if len(num5) > 4: 
        continue
    if len(num2) < 5: 
        continue
    if num16[-1] != 12: 
        continue
    c += 1

print(c)