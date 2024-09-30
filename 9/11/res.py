with open('9/11/1.txt') as file: 
    s1 = file.read().split('\n')

table = []
for i in s1: 
    row = [int(j) for j in i.split()]
    table.append(row)

c = 0

for row in table: 
    if sum(row) == 180: 
        if any([i > 90 for i in row]): 
            c += 1

print(c)
