with open('17-4.txt') as file:
    s1 = file.read().split('\n')

s = [int(i) for i in s1]

sr = sum(s) / len(s)
res = []

for i in s:
    if abs(i - sr) <= 670:
        if oct(i).count('3') > 1 and oct(i).count('4') > 0:
            res.append(i)

print(min(res), len(res))
    

