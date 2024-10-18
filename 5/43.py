for n in range(100, 999): 
    n1 = [i for i in str(n)]
    n2 = [int(n1[0]) ** 2 + int(n1[1]) ** 2, int(n1[1]) ** 2 + int(n1[2]) ** 2]
    n2.sort(reverse=True)
    n3 = [str(i) for i in n2]
    r = ''.join(n3)
    if r == '9010': 
        print(n)
        break
