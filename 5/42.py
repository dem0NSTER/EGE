for n in range(999, 100, -1): 
    n1 = [i for i in str(n)]
    n2 = [int(n1[0]) * int(n1[1]), int(n1[1]) * int(n1[2])]
    n2.sort(reverse=True)
    n3 = [str(i) for i in n2]
    r = ''.join(n3)
    if r == '240': 
        print(n)
        break 
    