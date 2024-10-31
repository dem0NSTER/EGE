with open('17/35/1.txt') as file: 
    s1 = file.read().split()

s = [int(i) for i in s1]
max_19_all = []
for i in s: 
    if i % 19 == 0: 
        max_19_all.append(i)

max_19 = max(max_19_all)


def f(n, m): 
    return (n > max_19) + (m > max_19) > 0


res = []
for i in range(len(s) - 1): 
    if f(s[i], s[i + 1]): 
        res.append(s[i] + s[i + 1])

print(len(res), min(res))
