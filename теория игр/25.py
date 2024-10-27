from functools import lru_cache


def moves(h: int): 
    return h + 1, h + 2, h + 3, h * 2


@lru_cache(None)
def game(s: int): 
    if s >= 34: 
        return 'win'
    if any(game(m) == 'win' for m in moves(s)): 
        return 'win1'
    if all(game(m) == 'win1' for m in moves(s)): 
        return 'win2'
    if any(game(m) == 'win2' for m in moves(s)): 
        return 'win3'
    if all(game(m) == 'win3' or game(m) == 'win1' for m in moves(s)): 
        return 'win4'
    

for i in range(1, 33): 
    if game(i) == 'win4': 
        print(i)
