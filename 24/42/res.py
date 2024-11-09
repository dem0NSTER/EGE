s = open('24/42/1.txt').readline().lower()

'шалаш'
c = 0
for i in range(len(s) - 4): 
    if s[i] == s[i + 4]: 
        if s[i + 1] == s[i + 3]: 
            c += 1

print(c)
