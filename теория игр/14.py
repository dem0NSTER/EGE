from functools import lru_cache

def moves(h):
    moves = []
    if h + 1 <= 70: moves.append(h + 1)
    if h + 3 <= 70: moves.append(h + 3)
    if h * 2 <= 70: moves.append(h * 2)
    return moves

@lru_cache(None)
def game(h):
    if h >= 52:
        return 'win'
    if any(game(m) == 'win' for m in moves(h)):
        return 'win1'
    if all(game(m) == 'win1' for m in moves(h)):
        return 'win2'
    if any(game(m) == 'win2' for m in moves(h)):
        return 'win3'
    if all(game(m) == 'win3' or game(m) == 'win1' for m in moves(h)):
        return 'win4'
    if any(game(m) == 'win4' or game(m) == 'win2' for m in moves(h)):
        return 'win5'
    if all(game(m) == 'win5' or game(m) == 'win3' or game(m) == 'win1' for m in moves(h)):
        return 'win6'

for s in range(1, 52):
    if game(s) == 'win6':
        print(s, 'win6')


