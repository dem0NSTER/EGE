with open('9/43/1.txt') as file: 
    s1 = file.read().split('\n')

table = []
for i in s1: 
    line = [int(x) for x in i.split()]
    table.append(line)


c = 0

for line in table: 
    line.sort()
    if line[0] != line[1]: 
        if line[0] - line[1] == line[1] - line[2]: 
            c += 1

print(c)
