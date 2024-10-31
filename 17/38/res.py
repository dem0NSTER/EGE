with open('17/38/1.txt') as file:
    s1 = file.read().split()

s = [int(i) for i in s1]


def f(n: int, m: int) -> bool: 
    if n % 9 == 0 and m % 9 != 0: 
        if oct(m)[-1] == '3': 
            return True
    if n % 9 != 0 and m % 9 == 0: 
        if oct(n)[-1] == '3': 
            return True
    

res = []
for i in range(len(s) - 1): 
    if f(s[i], s[i + 1]): 
        res.append(s[i])
        res.append(s[i + 1])

print(len(res) // 2, max(res))
