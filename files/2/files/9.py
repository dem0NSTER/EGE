with open('files/2/files/9.txt') as file: 
    s1 = file.read().split('\n')

table = []
for i in s1: 
    data = [int(x) for x in i.split()]
    table.append(data)


c = 0
for i in table: 
    i.sort()
    if i[0] == i[1] and i[2] == i[3]:
        print(i) 
        c += 1

print(c)
