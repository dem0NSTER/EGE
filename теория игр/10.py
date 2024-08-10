from functools import lru_cache

def moves(s):
    return s + s, s + '111'

@lru_cache(None)
def game(s):
    if s.count('1') >= 60:
        return 'win'
    if any(game(m) == 'win' for m in moves(s)):
        return 'win1'
    if all(game(m) == 'win1' for m in moves(s)):
        return 'win2'
    if any(game(m) == 'win2' for m in moves(s)):
        return 'win3'
    if all(game(m) == 'win3' or game(m) == 'win1' for m in moves(s)):
        return 'win4'

for s in range(1, 58):
    s1 = '1' * s
    if game(s1) == 'win4':
        print(s, 'win4')

