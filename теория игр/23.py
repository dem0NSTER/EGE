from functools import lru_cache

def moves(h: int): 
    moves = [h - 1, h - 2, h - 3, h - 4, h - 5]
    if h % 2 == 0: 
        moves.append(h // 2)
    return moves
    

@lru_cache(None)
def game(s): 
    if s < 10: 
        return 'win'
    if any(game(m) == 'win' for m in moves(s)): 
        return 'win1'
    if all(game(m) == 'win1' for m in moves(s)): 
        return 'win2'
    if any(game(m) == 'win2' for m in moves(s)): 
        return 'win3'
    if all(game(m) == 'win1' or game(m) == 'win3' for m in moves(s)): 
        return 'win4'
    
for s in range(11, 50): 
    if game(s) == 'win4': 
        print(s)

