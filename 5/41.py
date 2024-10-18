for n in range(9999, 1000, -1): 
    n1 = [i for i in str(n)]
    n2 = [int(n1[0]) * int(n1[1]), int(n1[2]) * int(n1[3])]
    n2.sort()
    n3 = [str(i) for i in n2]
    r = ''.join(n3)
    if r == '1214': 
        print(n)
        break
