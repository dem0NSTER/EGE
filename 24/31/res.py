s = open('24/31/1.txt').readline().lower()

s = s.replace('stock', '*')
print(s.count('ock'))


count = 0
for i in range(2, len(s) - 2): 
    if s[i - 2] + s[i - 1] + s[i] + s[i + 1] + s[i + 2] != 'stock': 
        if s[i] + s[i + 1] + s[i + 2] == 'ock': 
            count += 1

print(count)
