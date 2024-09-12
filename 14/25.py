a = oct(64 ** 6 + 16 ** 56 + 8 ** 120 - 13)[2:]

s = 0

for i in a: 
    if i in '1357': 
        s += int(i)

print(s)