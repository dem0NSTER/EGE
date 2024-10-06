f = open('9/39/1.txt')

c = 0

for i in f: 
    row = list(map(int, i.split()))
    repeted = [i for i in row if row.count(i) > 1]
    not_repeted = [i for i in row if row.count(i) == 1]

    chet = [i for i in row if i % 2 == 0]
    not_chet = [i for i in row if i % 2 != 0]

    flag = 0

    if len(repeted) == 2: 
        flag += 1

    if len(chet) != 0: 
        chet_res = sum(chet) / len(chet)
    else: 
        chet_res = 0
    
    if len(not_chet) != 0: 
        not_chet_res = sum(not_chet) / len(not_chet)
    else: 
        not_chet_res = 0
    if abs(chet_res - not_chet_res) > 50: 
        flag += 1

    if flag == 1: 
        c += 1
        

print(c)
