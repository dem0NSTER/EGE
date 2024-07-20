word = 'abbbcc'
c = 0 
for i in range(0, len(word) - 1): 
    if word[i] == word[i + 1]: 
        c += 1

print(c)
