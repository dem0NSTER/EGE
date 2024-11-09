s = open('24/34/1.txt').readline().lower()

c = 0
for i in range(len(s) - 3): 
    if s[i] + s[i + 1] + s[i + 2] + s[i + 3] == 'xxxx': 
        c += 1

print(c)
