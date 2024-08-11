from functools import lru_cache

def moves(h: int):
    return h  * 2, h + 3

@lru_cache(None)
def g(h: int):
    if h >= 33:
        return 'win'
    if any(g(m) == 'win' for m in moves(h)):
        return 'win1'
    if all(g(m) == 'win1' for m in moves(h)):
        return 'win2'
    if any(g(m) == 'win2' for m in moves(h)):
        return 'win3'
    if all(g(m) == 'win3' or g(m) == 'win1' for m in moves(h)):
        return 'win4'

for s in range(1, 33):
    if g(s) == 'win4':
        print(s, 'win4')
        
        
