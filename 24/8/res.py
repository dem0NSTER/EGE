s = open('24/8/1.txt').readline().lower()
s = s.replace('o', 'a')
s = s.replace('c', 'b').replace('d', 'b')
s = s.replace('ba', '*')
s = s.replace('b', ' ').replace('a', ' ')
s = s.split()
print(len(max(s, key=len)))

"""******************************************************************"""
s = open('24/8/1.txt').readline().lower()
m = [0] * len(s)
s = s.replace('o', 'a')
s = s.replace('c', 'b').replace('d', 'b')

for i in range(1, len(s)): 
    if s[i - 1] + s[i] == 'ba': 
        m[i] = m[i - 2] + 1

print(max(m))
