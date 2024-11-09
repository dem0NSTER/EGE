s = open('24/37/1.txt').readlines()

c = 0
for string in s: 
    if string.count('X') == string.count('S'): 
        c += 1 

print(c)
