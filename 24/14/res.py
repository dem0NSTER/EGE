s = open('24/14/1.txt').readline()

m = [1] * len(s)

for i in range(1, len(s)): 
    if s[i - 1] > s[i]: 
        m[i] = m[i - 1] + 1
    if m[i] == 9: 
        print(s[i - 9 + 1: i + 1 + 1])
