for n in range(1, 10000): 
    n2 = bin(n)[2:]
    nuls = 0
    once = 0
    for i in range(len(n2)): 
        if (i + 1) % 2 == 0 and n2[i] == '1': 
            once += 1
        elif (i + 1) % 2 != 0 and n2[i] == '0': 
            nuls += 1

    r = abs(nuls - once)
    if r == 5: 
        print(n)
        break