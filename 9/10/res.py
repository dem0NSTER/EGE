with open('9/10/1.txt') as file: 
    s1 = file.read().split('\n')

table = []

for i in s1: 
    data = [int(j) for j in i.split()]
    table.append(data)

c = 0
r = 0

for row in table: 
    if sum(row) == 180:
        r += 1
        if len(set(row)) == 2 or len(set(row)) == 1: 
            c += 1


print((c / r) * 100)