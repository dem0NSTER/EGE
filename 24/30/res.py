s = open('24/30/1.txt').readline().lower()

print(s.count('tik') + s.count('tok'))

count = 0

for i in range(len(s) - 2): 
    if s[i] + s[i + 1] + s[i + 2] == 'tik' or s[i] + s[i + 1] + s[i + 2] == 'tok': 
        count += 1

print(count)
