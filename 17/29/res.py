with open('17/29/1.txt') as file: 
    s1 = file.read().split('\n')

s = [int(i) for i in s1]


def f(x: int, y: int, z: int) -> bool: 
    return (x % 12 == 0 or y % 12 == 0 or z % 12 == 0) and (x % 3 == 0 and y % 3 == 0 and z % 3 == 0)


res = []
for i in range(len(s) - 2): 
    if f(s[i], s[i + 1], s[i + 2]): 
        res.append((s[i] + s[i + 1] + s[i + 2]) / 3)


print(len(res), min(res))
