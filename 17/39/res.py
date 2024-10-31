with open('17/39/1.txt') as file: 
    s1 = file.read().split()

s = [int(i) for i in s1]


def f(n: int, m: int, z: int): 
    return not(n > 0 and str(n)[-1] == '9') and (m > 0 and str(m)[-1] == '9') and not(z > 0 and str(z)[-1] == '9')


res = []
for i in range(len(s) - 2): 
    if f(s[i], s[i + 1], s[i + 2]): 
        res.append(s[i] + s[i + 1] + s[i + 2])


print(len(res), max(res))
