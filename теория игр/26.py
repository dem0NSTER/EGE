from functools import lru_cache

def movies(h: int): 
    movies = [h + 1]
    if h * 2 <= 60: 
        movies.append(h * 2)
    if h * 3 <= 60: 
        movies.append(h * 3)
    return movies


@lru_cache(None)
def game(s: int): 
    if 36 <= s <= 60: 
        return 'win'
    if any(game(m) == 'win' for m in movies(s)): 
        return 'win1'
    if all(game(m) == 'win1' for m in movies(s)): 
        return 'win2'
    if any(game(m) == 'win2' for m in movies(s)): 
        return 'win3'
    if all(game(m) == 'win3' or game(m) == 'win1' for m in movies(s)): 
        return 'win4'
    

for i in range(1, 36): 
    if game(i) == 'win4': 
        print(i)
