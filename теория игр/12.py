from functools import lru_cache

def moves(h: int):
    return h * 3, h + 4

@lru_cache(None)
def game(h):
    if h >= 382:
        return 'win'
    if any(game(m) == 'win' for m in moves(h)):
        return 'win1'
    if all(game(m) == 'win1' for m in moves(h)):
        return 'win2'
    if any(game(m) == 'win2' for m in moves(h)):
        return 'win3'
    if all(game(m) == 'win3' or game(m) == 'win1' for m in moves(h)):
        return 'win4'

for s in range(1, 381):
    # print(s)
    if game(s) == 'win3':
        print(s, 'win3')
        
