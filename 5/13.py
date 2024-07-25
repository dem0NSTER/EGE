for n in range(1, 10000): 
    n2 = bin(n)[2:]

    n2 = n2.replace('1', '*')
    n2 = n2.replace('0', '.')
    n2 = n2.replace('*', '0')
    n2 = n2.replace('.', '1')

    n10 = int(n2, 2)
    r = n - n10

    if r == 1443: 
        print(n)
        break

