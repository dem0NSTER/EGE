from functools import lru_cache

@lru_cache
def game(h, s):
    if h + s >= 84: 
        return 'win'
    if game(h * 2, s) == 'win' or game(h, s * 3) == 'win': 
        return 'win1'
    if game(h * 2, s) == 'win1' and game(h, s * 3) == 'win1' and game(h, s + 1) == 'win1' and game(h + 1, s) == 'win1': 
        return 'win2'
    if game(h * 2, s) == 'win2' or game(h, s * 3) == 'win2' or game(h + 1, s) == 'win2' or game(h, s + 1) == 'win2':
        return 'win3'
    if (game(h * 2, s) == 'win3' and game(h, s * 3) == 'win1' and game(h + 1, s) == 'win3' and game(h, s + 1) == 'win3') or \
    (game(h * 2, s) == 'win1' and game(h, s * 3) == 'win1' and game(h + 1, s) == 'win3' and game(h, s + 1) == 'win3'): 
        return 'win4'
    


for s in range(68, 1, -1):  
    if game(16, s) == 'win4': 
        print(s, 'vanya 1, 2')
        break