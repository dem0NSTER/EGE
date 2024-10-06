f = open('9/38/1.txt')

c = 0

for i in f: 
    row = list(map(int, i.split()))
    row.sort()
    repeted = [i for i in row if row.count(i) > 1]
    not_repeted = [i for i in row if row.count(i) == 1]
    if row[0] not in repeted: 
        if len(repeted) != 0: 
            if row[0] + row[-1] < sum(repeted): 
                c += 1

print(c)