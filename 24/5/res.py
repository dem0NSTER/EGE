s = open('24/5/1.txt').readline()
s = s.replace('XY', 'X Y').replace('XZ', 'X Z')
s = s.split()
print(len(max(s, key=len)))

"""*****************************************************"""
s = open('24/5/1.txt').readline()
m = [1] * len(s)
for i in range(1, len(s)): 
    if s[i - 1] + s[i] != 'XZ' and s[i - 1] + s[i] != 'XY': 
        m[i] = m[i - 1] + 1

print(max(m))
