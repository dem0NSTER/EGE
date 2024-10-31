with open('17/31/1.txt') as file: 
    s1 = file.read().split('\n')

s = [int(i) for i in s1]


def f(x, y, z, w): 
    return (w <= z <= y <= x) and abs(w - x) > 1000


res = []
for i in range(len(s) - 3): 
    if f(s[i], s[i + 1], s[i + 2], s[i + 3]): 
        res.append(s[i] + s[i + 1] + s[i + 2] + s[i + 3])


print(len(res), min(res))
