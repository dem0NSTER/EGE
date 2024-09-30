with open('9/20/1.txt') as file: 
    s1 = file.read().split('\n')

table = []

def my_len(x, y): 
    return (x**2 + y**2)**0.5

for i in s1: 
    data = [int(j) for j in i.split()]
    table.append(data)

c = 0

for row in table: 
    x1 = row[0]
    y1 = row[1]
    x2 = row[2]
    y2 = row[3]

    if my_len(x2 - x1, y2 - y1) > 5: 
        continue
    
    if (x1 < 0 and x2 < 0) or (x1 > 0 and x2 > 0):
        if (y1 < 0 and y2 < 0) or (y1 > 0 and y2 > 0):
            continue
    c += 1

print(c)
