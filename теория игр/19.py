from functools import lru_cache

def moves(h, s):
    return (h * 2, s), (h, s * 2), (h + 5, s), (h, s + 5)

@lru_cache(None)
def game(h, s):
    if h + s >= 115:
        return 'win'
    if any(game(m, n) == 'win' for m, n in moves(h, s)):
        return 'win1'
    if all(game(m, n) == 'win1' for m, n in moves(h, s)):
           return 'win2'
    if any(game(m, n) == 'win2' for m, n in moves(h, s)):
        return 'win3'
    if all(game(m, n) == 'win3' or game(m, n) == 'win1' for m, n in moves(h, s)):
        return 'win4'
    if any(game(m, n) == 'win' or game(m, n) == 'win2' or game(m, n) == 'win4' for m, n in moves(h, s)):
        return 'win5'


ctn = 0    
for s in range(1, 99):
    if game(15, s) == 'win5':
        print(s)
        ctn += 1
print(ctn)
