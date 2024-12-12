n = 6666
f = open('26/2/1.txt')

data = [int(i) for i in f]
data.sort()

arhive_1 = []
arhive_2 = []
flag = True

while len(data) > 0: 
    arhive_1 += [data.pop(-1)]

    while sum(arhive_1) >= sum(arhive_2): 
        arhive_2 += [data.pop(0)]
        

print(len(arhive_1), len(arhive_2))
