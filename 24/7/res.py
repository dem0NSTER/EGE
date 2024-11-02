s = open('24/7/1.txt').readline().lower()
s = s.replace('npo', '*').replace('pno', '*')
s = s.replace('n', ' ').replace('o', ' ').replace('p', ' ')
s = s.split()
print(len(max(s, key=len)))

"""****************************************"""
s = open('24/7/1.txt').readline().lower()
m = [0] * len(s)

for i in range(2, len(s)): 
    if s[i - 2] + s[i - 1] + s[i] == 'npo' or s[i - 2] + s[i - 1] + s[i] == 'pno': 
        m[i] = m[i - 3] + 1
print(max(m))
