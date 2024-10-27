from functools import lru_cache

def moves(h: int): 
    moves = [h - 1]
    if h - 4 >= 0: 
        moves.append(h - 4)
    if h - 2 >= 0: 
        moves.append(h - 2)
    return moves


@lru_cache(None)
def game(h: int): 
    if h == 0: 
        return 'win'
    if any(game(m) == 'win' for m in moves(h)): 
        return 'win1'
    if all(game(m) == 'win1' for m in moves(h)): 
        return 'win2'
    if any(game(m) == 'win2' for m in moves(h)): 
        return 'win3'
    if all(game(m) == 'win3' or game(m) == 'win1' for m in moves(h)): 
        return 'win4'
    if any(game(m) == 'win4' for m in moves(h)): 
        return 'win5'
    if all(game(m) == 'win5' for m in moves(h)): 
        return 'win6'
         


for s in range(1, 15): 
    if game(s) == 'win2' or game(s) == 'win4'or game(s) == 'win6': 
        print(s)
