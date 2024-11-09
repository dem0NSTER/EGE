import string

s = open('24/45/1.txt').readline().strip()

res = {x: 0 for x in string.ascii_uppercase}

for i in range(len(s) - 2): 
    if s[i] == s[i + 2]: 
        res[s[i + 1]] += 1


max_len = max(res.values())

for i in string.ascii_uppercase: 
    if res[i] == max_len: 
        print(i, res[i], sep='')
        break
