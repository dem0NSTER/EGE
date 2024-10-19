def f(n: int) -> int: 
    if n <= 1: 
        return n
    if n > 1 and n % 3 == 0: 
        return n + f(n / 3)
    if n > 1 and n % 3 != 0: 
        return n + f(n + 3)


for хуй in range(1, 100):
    try:  
        if f(хуй) > 100: 
            print(хуй)
            break
    except RecursionError: 
        continue
