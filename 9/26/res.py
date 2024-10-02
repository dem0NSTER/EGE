from itertools import permutations

with open('9/26/1.txt') as file: 
    s1 = file.read().split('\n')

table = []

for i in s1: 
    data = sorted(int(j) for j in i.split()) 
    table.append(data)



for row in table: 
    already = []
    for i in permutations(row): 
        first = sorted(row[:2])
        second = sorted(row[2:])
        if first + second not in already: 
            if second + first not in already: 
                already.append(first + second)
                print(first, second)

        