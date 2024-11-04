s = open('24/17/1.txt').readline().lower()

m = [0] * len(s)

for i in range(2, len(s)): 
    if s[i - 2] == 'a' and s[i] == 'a' or s[i - 2] == 'c' and s[i] == 'c': 
        m[i] = m[i - 3] + 1

print(max(m))
