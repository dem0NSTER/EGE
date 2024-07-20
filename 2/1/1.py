"""№ 15618
(x ∧ ¬y) ∨ (y ≡ z) ∨ ¬w, f == 0"""
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((x and (not(y))) or (y == z) or (not(w))) == 0:
                    print(x, y, z, w)
"""
x y z w
0 0 1 1
0 1 0 1
1 1 0 1
w, z, y, x
"""