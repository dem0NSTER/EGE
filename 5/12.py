for n in range(1, 10000): 
    n8 = oct(n)[2:]
    summ_oct = n8.count('1') * n
    summ_hex = hex(summ_oct)[2::]
    res = summ_hex.count('4')
    if res == 2: 
        print(n)
        break