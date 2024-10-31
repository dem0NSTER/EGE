with open('17/28/1.txt') as file: 
    s1 = file.read().split('\n')

s = [int(i) for i in s1]


def f(n: int, m: int, x: int): 
    return (n * m * x) % 7 == 0 and str(n + m + x)[-1] == '5'


res = []
for i in range(len(s) - 2): 
    if f(s[i], s[i + 1], s[i + 2]): 
        res.append(s[i] + s[i + 1] + s[i + 2])


print(len(res), max(res))
