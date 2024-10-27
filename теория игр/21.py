from functools import lru_cache

def moves(h: int): 
    moves = [h + 1]
    if h * 2 < 73: 
        moves.append(h * 2)
    if h * 3 < 73: 
        moves.append(h * 3)
    return moves


@lru_cache(None)
def game(h): 
    if 43 <= h <= 72: 
        return 'win'
    if any(game(m) == 'win' for m in moves(h)): 
        return 'win1'
    if all(game(m) == 'win1' for m in moves(h)): 
        return 'win2'
    if any(game(m) == 'win2' for m in moves(h)): 
        return 'win3'
    if all(game(m) == 'win3' or game(m) == 'win1' for m in moves(h)): 
        return 'win4'
    


for i in range(1, 42): 
    if game(i) == 'win4': 
        print(i)
