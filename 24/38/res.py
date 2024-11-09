c = 0
for s in open('24/38/1.txt'): 
    if (s.count('B') / s.count('A')) * 100 >= 105:
        c += 1

print(c)
