def f(x, y, a): 
    return (x * y > a) and (x > y) and (x < 8)


for a in range(-100, 100): 
    if all(f(x, y, a) == 0 for x in range(100) for y in range(100)): 
        print(a)
        break