from itertools import product 

print('a b c d')
for a, b, c, d in product([0, 1], repeat=4): 
    f = ((a and b) == (not c)) and (b <= d)
    if f == 1: 
        print(a, b, c, d)
