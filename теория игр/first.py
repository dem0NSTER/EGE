from functools import lru_cache

@lru_cache(None)
def game(h): 
    if h >= 91: 
        return 'win'
    if game(h * 3) == 'win' or game(h + 4) == 'win' or game(h + 1) == 'win': 
        return 'win1'
    if game(h * 3) == 'win1' and game(h + 4) == 'win1' and game(h + 1) == 'win1': 
        return 'win2'
    if game(h * 3) == 'win2' or game(h + 4) == 'win2' or game(h + 1) == 'win2': 
        return 'win3'
    if (game(h * 3) == 'win1' and game(h + 4) == 'win3' and game(h + 1) == 'win3') or \
        (game(h * 3) == 'win1' and game(h + 4) == 'win1' and game(h + 1) == 'win3'):
        return 'win4'



p1 = []
v1 = []
p2 = []
v12 = []

for s in range(100, 1, -1): 
    if game(s) == 'win1': 
        p1.append(s)
    if game(s) == 'win2': 
        v1.append(s)
    if game(s) == 'win3': 
        p2.append(s)
    if game(s) == 'win4': 
        v12.append(s)

p1.sort()
v1.sort()
p2.sort()
v12.sort()

print('19:', p1[0])
print('20:', p2[0], p2[1])
print('21:', v12[0])
    