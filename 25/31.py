def div(x: int) -> list: 
    s = set()

    for i in range(2, int(x ** 0.5) + 1): 
        if x % i == 0: 
            s.add(i)
            s.add(x // i)

    return sorted(s)


for i in range(1204300, 1204380): 
    s = [i for i in div(i) if i % 2 == 0]
    
    if s and sum(s) % 10 == 0: 
        print(i, sum(s))        
