count = 0
for s in open('24/39/1.txt'): 
    for i in range(len(s) - 3): 
        if s[i] == 'K' and s[i + 2] == 'G' and s[i + 3] == 'E':
            count += 1
            break

print(count)
