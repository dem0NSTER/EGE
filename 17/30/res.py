def goto3(n: int): 
    s = ''

    while n > 0: 
        s += str(n % 3)
        n = n // 3
    return s[::-1]


def f(x: int, y: int, z: int): 
    return goto3(x)[-1] == '2' or goto3(y)[-1] == '2' or goto3(z)[-1] == '2'


with open('17/30/1.txt') as file: 
    s1 = file.read().split('\n')


s = [int(i) for i in s1]

res = []
c = 0
for i in range(len(s) - 2): 
    if f(s[i], s[i + 1], s[i + 2]): 
        c += 1
        res.append(min([s[i], s[i + 1], s[i + 2]]))
        

print(len(res), sum(res))
