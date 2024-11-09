s = open('24/35/1.txt').readline().lower()

c = 0
for i in range(len(s) - 3): 
    if s[i] == 'g' and s[i + 2] == 'm' and s[i + 3] == 'e': 
        c += 1

print(c)
