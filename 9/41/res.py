with open('9/41/1.txt') as file: 
    s1 = file.read().split('\n')

s2 = [i.split() for i in s1]
s = []
for i in range(len(s2)): 
    g = [int(j) for j in s2[i]]
    s.append(g)


c = 0
for i in s: 
    i.sort()
    if 2 * (i[-1] + i[-2]) > 3 * (i[0] + i[1] + i[2]): 
        if ((str(i[0])[-1] == '5') + (str(i[1])[-1] == '5') + (str(i[2])[-1] == '5') + (str(i[3])[-1] == '5') + (str(i[4])[-1] == '5')) > 1: 
            c += 1

print(c)
