strs = open('24/48/1.txt').readlines()
# strs = ['ZZQABA', 'ZALAAC', 'QRAQUT']


max_c = 0
max_s = ''
for s in strs: 
    c = 1

    for i in range(len(s) - 1): 
        if s[i] == s[i + 1]: 
            c += 1
            if c > max_c: 
                max_c = c
                max_s = s
        else: 
            c = 1

max_s = max_s.strip()

res = {x: max_s.count(x) for x in sorted(set(max_s))}


max_len_s = max(res.values())
for i in res: 
    if max_len_s == res[i]: 
        letter = i
        break

string = ''.join(strs)
print(letter, string.count(letter), sep='')
