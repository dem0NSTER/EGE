strs = open('24/47/1.txt').readlines()

max_q = 0
max_s = ''
for s in strs: 
    count_q = s.count('Q')
    if count_q >= max_q: 
        max_q = count_q
        max_s = s

max_s = max_s.strip()
res = {x: max_s.count(x) for x in sorted(set(max_s))}

min_len = min(res.values())
for v in res:
    if res[v] == min_len: 
        letter = v
        break

string = ''.join(strs)
print(letter, string.count(letter), sep='')
