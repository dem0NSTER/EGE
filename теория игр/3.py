from functools import lru_cache

@lru_cache(None)
def game(h, s): 
    if h + s >= 77: 
        return 'win'
    if game(h, s * 2) == 'win' or game(h * 2, s) == 'win': 
        return 'win1'
    if game(h, s * 2) == 'win1' and game(h * 2, s) == 'win1' and game(h + 1, s) == 'win1' and game(h, s + 1) == 'win1': 
        return 'win2'  
    if game(h, s * 2) == 'win2' or game(h * 2, s) == 'win2' or game(h + 1, s) == 'win2' or game(h, s + 1) == 'win2': 
        return 'win3'
    if (game(h, s * 2) == 'win1' and game(h * 2, s) == 'win3' and game(h + 1, s) == 'win3' and game(h, s + 1) == 'win3') or \
    (game(h * 2, s) == 'win1' and game(h, s * 2) == 'win1' and game(h + 1, s) == 'win3' and game(h, s + 1) == 'win3') or \
    (game(h * 2, s) == 'win1' and game(h, s * 2) == 'win3' and game(h + 1, s) == 'win3' and game(h, s + 1) == 'win3'): 
        return 'win4'

for s in range(1, 70): 
    if game(7, s) == 'win4': 
        print(s, 'vanay 1 2')
        break
        