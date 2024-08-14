with open('17_Demo22.txt') as file: 
    s = file.read().split('\n')
s1 = [int(i) for i in s]

maxs = max(s1)
res = []

for i in range(len(s1) - 1):
    if (s1[i] % 3 == 0 or s1[i+1] % 3 == 0) and (s1[i] + s1[i+1] <= maxs):
        res.append(s1[i] + s1[i + 1])

print(len(res), max(res)) # 2439 998


    
