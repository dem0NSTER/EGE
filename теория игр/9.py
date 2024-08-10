from functools import lru_cache

def moves(h: int, s: int):
    return [h * 2, s], [s * 2, h], [h + 1, s], [s + 1, h]

@lru_cache(None)
def game(h, s):
    if h + s >= 231:
        return 'win'
    if any(game(m, n) == 'win' for m, n in moves(h, s)):
        return 'win1'
    if all(game(m, n) == 'win1' for m, n in moves(h, s)): 
       return 'win2'
    if any(game(m, n) == 'win2' for m, n in moves(h, s)):
        return 'win3'
    if all(game(m, n) == 'win3' or game(m, n) == 'win1' for m, n in moves(h, s)):
        return 'win4'

for s in range(1, 214):
    if game(17, s) == 'win4':
        print(s, 'win4')
    
