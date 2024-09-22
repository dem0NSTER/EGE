from itertools import product

print('y w z x')

for x, y, z, w in product([1, 0], repeat=4): 
    f = (x <= (y and not(z))) or w
    if f == 0: 
        print(y, w, z, x)
