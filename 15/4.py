def f(x, y, a):
    return (x + 2 * y < a) or (y > x) or (x > 32)


for a in range(1000): 
    if all(f(x, y, a) for x in range(1000) for y in range(1000)): 
        print(a)
        break