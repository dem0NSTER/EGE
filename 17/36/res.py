with open('17/36/1.txt') as file: 
    s1 = file.read().split()

s = list(map(int, s1))

res11 = []
res17 = []
for i in s: 
    if i % 17 == 0: 
        res17.append(i)
    if i % 11 == 0: 
        res11.append(i)
    
if len(res11) > len(res17): 
    print(len(res11), min(res11))
else: 
    print(len(res17), max(res17))
    