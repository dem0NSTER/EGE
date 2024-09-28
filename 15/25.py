def f(x, y, a): 
    return (x > 39) or (y > 26) or (2 * x + 4 * y < a)


for a in range(-1000, 1000): 
    if all(f(x, y, a) for x in range(100) for y in range(100)): 
        print(a)
        break