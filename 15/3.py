def f(x, y, a): 
    return (x >= 12) or (3 * x < y) or (x * y < a)


for a in range(0, 1000): 
    if all(f(x, y, a) for x in range(1000) for y in range(1000)): 
        print(a)
        break