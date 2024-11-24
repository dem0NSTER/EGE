from fnmatch import fnmatch 


def summ(n: int): 
    s = [int(i) for i in str(n)]
    return sum(s)


c = 0
for n in range(700011, 10 ** 100, 13): 
    if fnmatch(str(n), '*0??3*'): 
        continue
    if fnmatch(str(n), '*4??2'): 
        continue
    if fnmatch(str(n), '*1*'): 
        continue
    
    print(n, summ(n))
    c += 1
    if c == 5: 
        break
