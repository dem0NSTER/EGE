s = open('24/36/1.txt').readline().lower()

c = 0
for i in range(len(s) - 4): 
    if s[i] == 'a' and s[i + 2] == 'a' and s[i + 4] == 'a': 
        c += 1

print(c)
