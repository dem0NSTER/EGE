from itertools import product

c = 0 

for i in product('ab123', repeat=8): 
    code = ''.join(i)

    count = 0
    for letter in code: 
        if letter in 'ab': 
            count += 1
    
    if count == 2: 
        c += 1

print(c)
    