def f(s1: int) -> bool: 
    for i in range(2, s1): 
        if s1 % i == 0: 
            return False
    return True

print(f(11))