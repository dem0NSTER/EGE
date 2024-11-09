s = open('24/32/1.txt').readline().lower()

count = 0

for i in range(1, len(s) - 4): 
    if s[i - 1] != 'j' and s[i + 4] != 'j': 
        if s[i] + s[i + 1] + s[i + 2] + s[i + 3] == 'boss': 
            count += 1

print(count)
