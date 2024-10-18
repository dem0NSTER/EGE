for n in range(2, 10000): 
    n1 = [i for i in str(n)]
    chet = [int(i) for i in n1 if int(i) % 2 == 0]
    on_chet = [int(n1[i]) for i in range(len(n1)) if i % 2 != 0]
    summ1 = sum(chet)
    summ2 = sum(on_chet)
    r = abs(summ1 - summ2)
    if r == 9: 
        print(n)
        break
