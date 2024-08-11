althabet = '0 1 2 3 4 5 6 7 8 9 a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
althabet.reverse()

for x in althabet:
    if (int(f'gjs{x}2', 36) + int(f'{x}83j{x}', 36)) % 34 == 0:
        print(hex((int(f'gjs{x}2', 36) + int(f'{x}83j{x}', 36)) // 34)[2:])
        break

