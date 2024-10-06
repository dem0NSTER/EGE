f = open('9/34/1.txt')

c = 1

for i in f: 
    row  = list(map(int, i.split()))
    povt = [i for i in row if row.count(i) > 1]
    ne_povt = [i for i in row if row.count(i) == 1]
    if len(povt) == 2 and len(ne_povt) == 4: 
        if povt[0] >= (sum(ne_povt) / len(ne_povt)): 
            print(povt, ne_povt)
            print(c)
            break
    c += 1
