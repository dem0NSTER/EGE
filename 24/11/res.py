s = open('24/11/1.txt').readline().lower()
while 'xx' in s or 'yy' in s or 'zz' in s: 
    s = s.replace('xx', 'x x').replace('yy', 'y y').replace('zz', 'z z')

s = s.split()
print(len(max(s, key=len)))

"********************************************************"
s = open('24/11/1.txt').readline().lower()
m = [1] * len(s)

for i in range(1, len(s)): 
    if s[i - 1] != s[i]: 
        m[i] = m[i - 1] + 1

print(max(m))
