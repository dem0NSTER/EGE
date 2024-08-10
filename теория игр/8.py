from functools import lru_cache

def moves(h: int):
    return h + 2, h + 3, h * 2

@lru_cache(None)
def game(h: int):
    if h >= 60:
        return 'win'
    if any(game(n) == 'win' for n in moves(h)):
        return 'win1'
    if all(game(n) == 'win1' for n in moves(h)):
        return 'win2'
    if any(game(n) == 'win2' for n in moves(h)):
        return 'win3'
    if all(game(n) == 'win3' or game(n) == 'win1' for n in moves(h)):
        return 'win4'

for s in range(1, 60):
    if game(s) == 'win4':
        print(s, 'win4')


        
