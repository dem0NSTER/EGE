def f(x, y, a): 
    return (x >= 9) or (2 * x < y) or (x * y < a)

for a in range(1000): 
    if all(f(x, y, a) for x in range(100) for y in range(100)): 
        print(a)
        break