from functools import lru_cache
from sys import setrecursionlimit
setrecursionlimit(10000)


def movies(h: int): 
    return h * 3, h + 1 


@lru_cache(None)
def game(h: int): 
    if h >= 2163: 
        return 'win'
    if any(game(m) == 'win' for m in movies(h)): 
        return 'win1'
    if all(game(m) == 'win1' for m in movies(h)): 
        return 'win2'
    if any(game(m) == 'win2' for m in movies(h)): 
        return 'win3'
    if all(game(m) == 'win3' or game(m) == 'win1' for m in movies(h)): 
        return 'win4'
    

for s in range(1, 2163): 
    if game(s) == 'win4': 
        print(s)