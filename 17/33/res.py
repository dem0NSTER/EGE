with open('17/33/1.txt') as f: 
    s1 = f.read().split()

s = [int(i) for i in s1]


def f(n, m): 
    return (abs(n) + abs(m) <= 200) and (abs(n) + abs(m) >= 50)


res = []
for i in range(len(s1) - 1): 
    if f(s[i], s[i + 1]): 
        res.append(s[i])
        res.append(s[i + 1])

print(res)
