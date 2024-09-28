def f(x, a):
    return ((x % 35 != 0) and (x % a == 0)) <= ((x % 21 == 0) or (x % a != 0))

for a in range(1, 1000):
    if all(f(x, a) for x in range(1, 1000)):
        print(a)
        break
