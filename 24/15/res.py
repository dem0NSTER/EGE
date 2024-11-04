s = open('24/15/1.txt').readline().lower()

while 'bb' in s : 
    s = s.replace('bb', '*')
while 'dd' in s: 
    s = s.replace('dd', '*')

s = s.replace('a')
s = s.split()

print(len(max(s, key=len)))

"""***************************************"""
s = open('24/15/1.txt').readline().lower()
m = [0] * len(s)

for i in range(1, len(s)): 
    if s[i - 1] + s[i] == 'bb' or s[i - 1] + s[i] == 'dd': 
        m[i] = m[i - 2] + 1

print(max(m))
