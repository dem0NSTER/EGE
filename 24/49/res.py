s = open('24/49/1.txt').readline().lower()
# s = 'abbssabbsbasassabccccc'

s = s.replace('ss', 's s')
s = s.split()
print(len(max(s, key=len)))


s = open('24/49/1.txt').readline().lower()
# s = 'abbssabbsbasassabccccc'

m = [1] * len(s)

for i in range(1, len(s)): 
    if s[i - 1] + s[i] != 'ss': 
        m[i] = m[i - 1] + 1

print(max(m))
