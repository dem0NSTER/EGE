s = open('24/50/556.txt').readline().lower()


m = [1] * len(s)

for i in range(1, len(s)): 
    if s[i] + s[i - 1] != 'ad' and s[i] + s[i - 1] != 'da': 
        m[i] = m[i - 1] + 1

print(max(m))


s = open('24/50/556.txt').readline().lower()
s = s.replace('ad', 'a d').replace('da', 'd a')
s = s.split()
print(len(max(s, key=len)))
