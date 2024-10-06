from itertools import permutations

with open('9/26/1.txt') as file: 
    s1 = file.read().split('\n')

table = []

for i in s1: 
    data = sorted(int(j) for j in i.split()) 
    table.append(data)




        