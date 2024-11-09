import string

s = open('24/46/1.txt').readline()

res = {f'CB{x}BC': 0 for x in string.ascii_uppercase}

for i in range(len(s) - 4): 
    if s[i] + s[i + 1] == 'CB': 
        if s[i + 3] + s[i + 4] == 'BC':
            res[s[i:i + 5]] += 1


max_len = max(res.values())
for i in string.ascii_uppercase: 
    if res[f'CB{i}BC'] == max_len:
        print(i, res[f'CB{i}BC'], sep='')
