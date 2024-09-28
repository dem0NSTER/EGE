def f(x, a): 
    return (x in (2, 4, 6, 8, 10, 12)) <= (((x in (3, 6, 9, 12, 15)) and (not(x in a))) <= (not(x in (2, 4, 6, 8, 10, 12))))

a = [12, 6]
for x in range(1, 1000): 
    if not f(x, a): 
        print(1)
        a.append(x)

print(set(a))