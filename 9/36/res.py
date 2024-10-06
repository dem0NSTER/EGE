f = open('9/36/1.txt')

c = 0

for i in f: 
    row = list(map(int, i.split()))
    row.sort()
    repeted = [i for i in row if row.count(i) > 1]
    not_repeted = [i for i in row if row.count(i) == 1]
    if len(not_repeted) == len(row): 
        if 2 * (row[0] + row[-1]) <= 3 * (row[1] + row[2] + row[3]): 
            c += 1

print(c)
