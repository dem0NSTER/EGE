s = open('24/33/1.txt').readline().lower()

c = 0
for i in range(len(s) - 2): 
    if s[i] + s[i + 1] + s[i + 2] == 'xix': 
        c += 1

print(c)
