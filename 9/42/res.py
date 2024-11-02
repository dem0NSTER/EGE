with open('9/42/1.txt') as file: 
    s1 = file.read().split('\n')

table = []
for i in s1: 
    data = [int(j) for j in i.split()]
    table.append(data)


c = 0
for line in table: 
    line.sort()
    if max(line) < line[0] + line[1] + line[2]: 
        chet = [i for i in line if i % 2 == 0]
        ne_chet = [i for i in line if i % 2 != 0]
        if sum(chet) == sum(ne_chet): 
            c += 1

print(c)
