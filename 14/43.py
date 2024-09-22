def f(n, base): 
    s = []

    while n > 0: 
        s.append(n % base)
        n = n // base
    return s[::-1]


for i in range(10, 56):
    c = str(i)
    num = 6 * int(c[0]) + int(c[1])
    num5 = f(num, 5)
    if len(num5) != 3: 
        continue
    num11 = f(num, 11)
    if num11[-1] == 1: 
        print(i)
        print(num)
        print(num5)
        print(num11)
        print()

