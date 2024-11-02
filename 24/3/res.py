s = open('24/3/1.txt').readline()

for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower(): 
    s = s.replace(i, ' ')

s = s.split()
print(len(max(s, key=len)))

"""**************************************************************************"""
s = open('24/3/1.txt').readline()
m = [0] * len(s)

for i in range(len(s)): 
    if s[i] in '0123456789': 
        m[i] = m[i - 1] + 1

print(max(m))
