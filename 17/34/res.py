with open('17/34/1.txt') as file: 
    s1 = file.read().split()

s = [int(i) for i in s1]
average = sum(s) / len(s)


def f(x, y, z): 
    return (x > average) + (y > average) + (z > average) > 1


res = []
for i in range(len(s) - 2): 
    if f(s[i], s[i + 1], s[i + 2]): 
        res.append(s[i] + s[i + 1] + s[i + 2])

print(len(res), max(res))
