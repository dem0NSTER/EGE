from functools import lru_cache

def moves(h: int): 
    moves = [h - 2, h - 5, int(h / 3)]
    return moves

@lru_cache(None)
def game(h: int): 
    if h <= 19: 
        return 'win'
    if any(game(m) == 'win' for m in moves(h)): 
        return 'win1'
    if all(game(m) == 'win1' for m in moves(h)): 
        return 'win2'
    if any(game(m) == 'win2' for m in moves(h)):
        return 'win3'
    if all(game(m) == 'win3' or game(m) == 'win1' for m in moves(h)): 
        return 'win4'
    
    
for s in range(20, 100): 
    if game(s) == 'win4': 
        print(s)

