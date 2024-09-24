def f(x, y, a): 
    return ((x + y) <= 30) or (y <= (x + 2)) or (y >= a)

for a in range(10000, 0, -1): 
    if all(f(x, y, a) for x in range(1000) for y in range(1000)): 
        print(a)
        break