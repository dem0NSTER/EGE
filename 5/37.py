for n in range(1000, 1, -1): 
    n2 = bin(n)[2:]

    if n2.count('1') % 2 == 0: 
        n2 = '10' + n2[2:] + '0'
    else: 
        n2 = '11' + n2[2:] + '1'
    
    r = int(n2, 2)
    if r < 35: 
        print(n)
        break