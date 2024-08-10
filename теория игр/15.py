from functools import lru_cache

def moves(h):
    return h + 2, h + 4, h * 3

@lru_cache(None)
def game(h):
    if h >= 81:
        return 'win'
    if any(game(m) == 'win' for m in moves(h)):
        return 'win1'
    if all(game(m) == 'win1' for m in moves(h)):
        return 'win2'
    if any(game(m) == 'win2' for m in moves(h)):
        return 'win3'
    if all(game(m) == 'win3' or game(m) == 'win1' for m in moves(h)):
        return 'win4'

for s in range(1, 81):
    if game(s) == 'win4':
        print(s, 'win4')
