from math import ceil
from functools import lru_cache


def movies(h, s): 
    movie = []
    if h != 1: 
        movie.append((ceil(h / 2), s))
    if s != 1: 
        movie.append((h, ceil(s / 2)))
    if h - 1 > 0: 
        movie.append((h - 1, s))
    if s - 1 > 0: 
        movie.append((h, s - 1))
    return movie


@lru_cache(None)
def game(h, s): 
    if h + s <= 20: 
        return 'win'
    if any(game(m, n) == 'win' for m, n in movies(h, s)): 
        return 'win1'
    if all(game(m, n) == 'win1' for m, n in movies(h, s)): 
        return 'win2'
    if any(game(m, n) == 'win2' for m, n in movies(h, s)): 
        return 'win3'
    if all(game(m, n) == 'win3' or game(m, n) == 'win1' for m, n in movies(h, s)): 
        return 'win4'
    

for s in range(11, 100): 
    if game(10, s) == 'win4': 
        print(s)