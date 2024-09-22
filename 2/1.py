print('x y z w')

for y in range(2):
    for x in range(2):
        for z in range(2):
            for w in range(2):
                f = (x or not(y)) and not(y == z) and w
                if f == 1: 
                    print(x, y, z, w)