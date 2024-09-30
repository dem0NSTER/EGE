with open('D:\\Python_program\\ege\\9\\7\\1.txt') as file: 
    s1 = file.read().split('\n')

res_data = []

for i in s1: 
    data = [int(j) for j in i.split()]
    res_data.append(data)

c = 0

for row in res_data: 
    print(row)
    if row[0] == row[2] and row[1] == row[3] and row[0] != row[1]: 
        c += 1

print(c)