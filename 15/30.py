def f(x, y, a):
    return (2*x + y != 70) or (x < y) or (x < a)


for a in range(1000):
    if all(f(x, y, a) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break