with open('17/21/1.txt') as file: 
    s1 = file.read().split('\n')

s = [int(i) for i in s1]


def f(num: int): 
    return num % 3 == 0 and \
        num % 7 != 0 and \
        num % 17 != 0 and \
        num % 19 != 0 and \
        num % 27 != 0


res = []
for num in s: 
    if f(num): 
        res.append(num)

print(len(res), max(res))
