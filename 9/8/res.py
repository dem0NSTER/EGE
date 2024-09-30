with open('9/8/1.txt') as file: 
    s1 = file.read().split('\n')

res_data = []

for i in s1: 

    data = [int(j) for j in i.split()]
    res_data.append(data)

c = 0

for row in res_data: 
    if len(set(row)) == 2: 
        c += 1

print(c)