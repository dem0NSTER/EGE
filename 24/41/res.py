s = open('24/41/1.txt').readline().lower()

c = 0

for i in range(len(s) - 6): 
    if s[i] == 'a' and s[i + 6] == 'f': 
        c += 1

for i in range(len(s) - 7): 
    if s[i] == 'a' and s[i + 7] == 'f': 
        c += 1

for i in range(len(s) - 8): 
    if s[i] == 'a' and s[i + 8] == 'f': 
        c += 1

for i in range(len(s) - 9): 
    if s[i] == 'a' and s[i + 9] == 'f': 
        c += 1


print(c)
