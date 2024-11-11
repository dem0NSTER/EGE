def f(x, y, a): 
    return not((x + 5 < a) <= (y > a)) or (x * y >= 76)


for a in range(1, 100): 
    if all(f(x, y, a) for x in range(1, 1000) for y in range(1, 1000)): 
        print(a)
        break