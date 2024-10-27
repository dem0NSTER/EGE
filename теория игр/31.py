from functools import lru_cache

def movies(h: int, s: int, g: int): 
    return \
    (h + 3, s, g), (h, s + 3, g), (h, s, g + 3), \
    (h + 13, s, g), (h, s + 13, g), (h, s, g + 13), \
    (h + 23, s, g), (h, s + 23, g), (h, s, g + 23)


@lru_cache(None)
def game(h: int, s: int, g: int):
    if h + s + g >= 73: 
        return 'win'
    if any(game(m, n, v) == 'win' for m, n, v in movies(h, s, g)): 
        return 'win1'
    if all(game(m, n, v) == 'win1' for m, n, v in movies(h, s, g)): 
        return 'win2'
    if any(game(m, n, v) == 'win2' for m, n, v in movies(h, s, g)): 
        return 'win3'
    if all(game(m, n, v) == 'win3' or game(m, n, v) == 'win1' for m, n, v in movies(h, s, g)): 
        return 'win4'
    

for s in range(1, 23): 
    if game(2, s, 2 * s) == 'win4': 
        print(s)
        