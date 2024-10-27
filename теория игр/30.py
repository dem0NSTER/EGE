from functools import lru_cache

def movies(h: int, s: int): 
    return (h + 1, s), (h, s + 1), (h * 2, s), (h, s * 2)


@lru_cache(None)
def game(h: int, s: int): 
    if h * s >= 63: 
        return 'win'
    if any(game(m, n) == 'win' for m, n in movies(h, s)): 
        return 'win1'
    if all(game(m, n) == 'win1' for m, n in movies(h, s)): 
        return 'win2'
    if any(game(m, n) == 'win2' for m, n in movies(h, s)): 
        return 'win3'
    if all(game(m, n) == 'win3' or game(m, n) == 'win1' for m, n in movies(s, h)): 
        return 'win4'


for s in range(1, 31): 
    if game(2, s) == 'win4': 
        print(s)
