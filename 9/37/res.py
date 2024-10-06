f = open('9/37/1.txt')

c = 0

for i in f: 
    row = list(map(int, i.split()))
    repeted = [i for i in row if row.count(i) > 1]
    not_repeted = [i for i in row if row.count(i) == 1]
    if len(repeted) != 0 and len(not_repeted) != 0: 
        if (sum(not_repeted)/len(not_repeted)) < (sum(repeted)/len(repeted)): 
            c += 1

print(c)