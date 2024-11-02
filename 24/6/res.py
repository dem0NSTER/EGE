s = open('24/6/1.txt').readline().lower()
s = s.replace('xzzy', 'xzz zzy')
s = s.split()
print(len(max(s, key=len)))

"""***********************************************"""
s = open('24/6/1.txt').readline().lower()
m = [3] * len(s)

for i in range(3, len(s)): 
    if s[i - 3] + s[i - 2] + s[i - 1] + s[i] != 'xzzy': 
        m[i] = m[i - 1] + 1

print(max(m))
