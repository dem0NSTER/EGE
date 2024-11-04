from functools import lru_cache

def moves(h: int, s: int): 
    return (h + 1, s), (h, s + 1), (h * 3, s), (h, s * 3)


@lru_cache(None)
def game(h: int, s: int): 
    if h + s >= 175: 
        return 'win'
    if any(game(m, n) == 'win' for m, n in moves(h, s)): 
        return 'win1'
    if all(game(m, n) == 'win1' for m, n in moves(h, s)): 
        return 'win2'
    if any(game(m, n) == 'win2' for m, n in moves(h, s)): 
        return 'win3'
    if all(game(m, n) == 'win3' or game(m, n) == 'win1' for m, n in moves(h, s)): 
        return 'win4'
    

for s in range(1, 154): 
    if game(19, s) == 'win4': 
        print(s)
        break
