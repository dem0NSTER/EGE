def f(x, a):
    return ((x % a == 0) and (x % 320 == 0)) <= ((x % 80 == 0) and (a > 35))

for a in range(1, 1000):
    if all(f(x, a) for x in range(1, 1000)):
        print(a)
        break
