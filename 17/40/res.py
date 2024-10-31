with open('17/40/1.txt') as file: 
    s1 = file.read().split()

s = [int(i) for i in s1]

del_35 = [i for i in s if i % 35 == 0]
sum_35 = 0

for num in del_35: 
    m = [int(i) for i in str(num)]
    sum_35 += sum(m)


def f(n, m): 
    if n > sum_35 and m < sum_35: 
        if hex(m)[-2:] == 'ef': 
            return True
    if n < sum_35 and m > sum_35: 
        if hex(n)[-2:] == 'ef': 
            return True


res = []
for i in range(len(s) - 1): 
    if f(s[i], s[i + 1]): 
        res.append(s[i] + s[i + 1])

print(len(res), min(res))       
