def f(a, x): 
    return (x % a == 0) or ((70 <= x <= 90) <= (x % 27 != 0))


for a in range(1000, 1, -1): 
    if all(f(a, x) for x in range(1000)): 
        print(a)
        break