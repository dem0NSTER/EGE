with open('9/19/1.txt') as file: 
    s1 = file.read().split('\n')

table = []

for i in s1: 
    data = [int(j) for j in i.split()]
    table.append(data)

c = 0

for row in table: 
    x1 = row[0]
    y1 = row[1]
    x2 = row[2]
    y2 = row[3]

    if x1 == 0 or y1 == 0: 
        if x2 == 0 or y2 == 0: 
            c += 1

print(c)
