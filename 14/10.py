def f(s1: int) -> bool: 
    for i in range(2, s1): 
        if s1 % i == 0: 
            return False
    return True

althabet = '0 1 2 3 4 5 6 7 8 9 a b c d e f'.split()
althabet.reverse()

for x in althabet: 
    s = int(f'109{x}', 16) + int(f'12{x}7', 16)
    if f(s): 
        print(x, s)
        break
