s = open('24/9/1.txt').readline().lower()
s = s.replace('b', 'a').replace('2', '1')
s = s.replace('11a', '*')
s = s.replace('a', ' ').replace('1', ' ')
s = s.split()
print(len(max(s, key=len)))

"""********************************************"""
s = open('24/9/1.txt').readline().lower()
s = s.replace('b', 'a').replace('2', '1')
m = [0] * len(s)

for i in range(2, len(s)): 
    if s[i - 2] + s[i - 1] + s[i] == '11a': 
        m[i] = m[i - 3] + 1

print(max(m))
