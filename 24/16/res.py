import string

s = open('24/16/1.txt').readline().lower()

s = s.replace('pc', '**').replace('csgo', '----')
s = s.replace('pc', '**').replace('csgo', '----')
for i in string.ascii_lowercase: 
    s = s.replace(i, ' ')

s = s.split()
# s = [i.replace('*', '**').replace('-', '----') for i in s]
a = max(s, key=len)
print(len(max(s, key=len)))
# print(a.count('*') * 2 + a.count('-') * 4)

"""***************************************************"""
s = open('24/16/1.txt').readline().lower()

m = [0] * len(s)

for i in range(1, len(s)): 
    if s[i - 1] + s[i] == 'pc': 
        m[i] = m[i - 2] + 2
    if i >= 3 and s[i - 3] + s[i - 2] + s[i - 1] + s[i] == 'csgo': 
        m[i] = m[i - 4] + 4

print(max(m))
