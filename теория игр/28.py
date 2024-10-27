from functools import lru_cache

def movies(s: int, h: int): 
    return (s + 1, h), (s, h + 1), (s * 2, h), (s, h * 2)


@lru_cache(None)
def game(s: int, h: int): 
    if s + h >= 77: 
        return 'win'
    if any(game(m, n) == 'win' for m, n in movies(s, h)): 
        return 'win1'
    if all(game(m, n) == 'win1' for m, n in movies(s, h)): 
        return 'win2'
    if any(game(m, n) == 'win2' for m, n in movies(s, h)): 
        return 'win3'
    if all(game(m, n) == 'win3' or game(m, n) == 'win1' for m, n in movies(s, h)): 
        return 'win4'

for i in range(1, 69): 
    if game(7, i) == 'win4': 
        print(i)
        