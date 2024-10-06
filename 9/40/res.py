f = open('9/40/1.txt')

c = 0

for i in f: 
    row = list(map(int, i.split()))

    del3 = [i for i in row if i % 3 == 0]
    not_del3 = [i for i in row if i % 3 != 0]

    row.sort()

    if len(del3) == 3: 
        razm = row[-1] - row[0]
        if razm <= sum(del3): 
            c += 1

print(c)