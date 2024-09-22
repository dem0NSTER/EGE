for i in range(41): 
    b2 = bin(i)[2:]

    if b2[-4:] == '1011': 
        print(i)