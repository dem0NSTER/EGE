with open('9/44/1.txt') as file: 
    s1 = file.read().split('\n')

table = []
for line in s1: 
    data = [int(i) for i in line.split()]
    table.append(data)


c = 0
for line in table: 
    line.sort()
    if line[-1] < line[0] + line[1] + line[2]:
        if len(set(line)) == 3: 
            c += 1

print(c)
