f = open('9/35/1.txt')

res = []

for i in f: 
    row = list(map(int, i.split()))
    povt = [i for i in row if row.count(i) > 1]
    ne_povt = [i for i in row if row.count(i) == 1]
    if len(povt) == 4 and len(set(povt)) == 2: 
        if max(row) not in povt: 
            res.append(row)

print(sum(res[0]))