s = open('24/4/1.txt').readline()
while 'PP' in s: s = s.replace('PP', 'P P')

s = s.split()
print(len(max(s, key=len)))
"""***************************************************************************"""
s = open('24/4/1.txt').readline()
m = [1] * len(s)

for i in range(1, len(s)): 
    if s[i] + s[i - 1] != 'PP': 
        m[i] = m[i - 1] + 1

print(max(m))
