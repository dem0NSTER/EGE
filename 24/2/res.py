s = open('24/2/1.txt').readline()
s = s.replace('A', ' ').replace('B', ' ').replace('C', ' ')
s = s.split()
print(len(max(s, key=len)))

"""***********************************************************************"""
s = open('24/2/1.txt').readline()
m = [0] * len(s)

for i in range(len(s)): 
    if s[i] in '123': 
        m[i] = m[i - 1] + 1

print(max(m))
