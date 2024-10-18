def f(n: list) -> int: 
    s = 1
    for i in n: 
        s *= i
    return s


n = 120
for m in range(1, 10000): 
    n1 = [i for i in str(n)]
    m1 = [i for i in str(m)]
    n_chet = [int(i) for i in n1 if int(i) % 2 == 0 and int(i) != 0]
    m_chet = [int(i) for i in m1 if int(i) % 2 == 0 and int(i) != 0]
    p1 = f(n_chet + m_chet)
    
    n_not_chet = [int(i) for i in n1 if int(i) % 2 != 0]
    m_not_chet = [int(i) for i in m1 if int(i) % 2 != 0]
    p2 = f(n_not_chet + m_not_chet)

    r = abs(p1 - p2)
    if r == 29: 
        print(m)
        break
