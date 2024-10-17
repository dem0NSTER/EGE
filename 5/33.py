for n in range(100, 1, -1): 
    n2 = bin(n)[2:]
    num2 = n2[::-1]
    r = int(num2, 2)
    if r == 13: 
        print(n)
        break