from functools import lru_cache

def moves(h, s):
    return [h, s * 3], [h * 3, s], [h + 2, s], [h, s + 2]

@lru_cache(None)
def game(h, s):
    if h >= 60 or s >= 60:
        return 'win'
    if any(game(m, n) == 'win' for m, n in moves(h, s)):
        return 'win1'
    if all(game(m, n) == 'win1' for m, n in moves(h, s)):
        return 'win2'
    if any(game(m, n) == 'win2' for m, n in moves(h, s)):
        return 'win3'
    if all(game(m, n) == 'win3' or game(m, n) == 'win1' for m, n in moves(h, s)):
        return 'win4'

for s in range(1, 43):
    if game(19, s) == 'win4':
        print(s, 'win4')
