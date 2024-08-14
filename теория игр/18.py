from functools import lru_cache

def moves(h: int, s: int):
    return [h, h + s], [h + s, s]


@lru_cache(None)
def g(h: int, s: int):
    if h + s >= 79:
        return 'win'
    if any(g(m, n) == 'win' for m, n in moves(h, s)):
        return 'win1'
    if all(g(m, n) == 'win1' for m, n in moves(h, s)):
        return 'win2'
    if any(g(m, n) == 'win2' for m, n in moves(h, s)):
        return 'win3'
    if all(g(m, n) == 'win1' or  g(m, n) == 'win3' for m, n in moves(h, s)):
        return 'win4'

for s in range(1, 79):
    if g(12, s) == 'win4':
        print(s, 'win4')
