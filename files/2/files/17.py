s = [int(i) for i in open('files/2/files/17_8427.txt')]

min_3 = 10**10
for i in s: 
    if len(str(i)) == 3: 
        if str(i)[-1] == '3': 
            min_3 = min(min_3, i)


res = []
for i in range(len(s) - 1): 
    if (len(str(s[i])) == 4) + (len(str(s[i + 1])) == 4) == 1: 
        if (s[i] ** 2 + s[i + 1] ** 2) % min_3 == 0: 
            res.append(s[i] ** 2 + s[i + 1] ** 2)


print(len(res), max(res))