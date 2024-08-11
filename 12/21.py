for n in range(4, 1000):
    s = '5' + n * '2'

    while '52' in s or '1122' in s or '2222' in s:
        if '52' in s:
            s = s.replace('52', '11', 1)
        if '2222' in s:
            s = s.replace('2222', '5', 1)
        if '1122' in s:
            s = s.replace('1122', '25', 1)

    res = 1
    
    for i in s:
        res *= int(i)
    if res == 10:
        print(n)
        break
        
