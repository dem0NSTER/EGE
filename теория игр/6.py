from functools import lru_cache 

@lru_cache(None)
def g(h: int, s: int): 
    if h + s >= 77: 
        return 'win'
    if g(h, s * 2) == 'win' or g(h * 2, s) == 'win': 
        return 'win1'
    if g(h, s * 2) == 'win1' and g(h * 2, s) == 'win1' and g(h + 1, s) == 'win1' and g(h, s + 1) == 'win1': 
        return 'win2'
    if g(h, s * 2) == 'win2' or g(h * 2, s) == 'win2' or g(h + 1, s) == 'win2' or g(h, s + 1) == 'win2': 
        return 'win3'
    if (g(h, s * 2) == 'win1' and g(h * 2, s) == 'win3' and g(h + 1, s) == 'win3' and g(h, s + 1) == 'win3') or \
    (g(h, s * 2) == 'win1' and g(h * 2, s) =='win1' and g(h + 1, s) == 'win3' and g(h, s + 1) == 'win3') or \
    (g(h, s * 2) == 'win3' and g(h * 2, s) == 'win1' and g(h + 1, s) == 'win3' and g(h, s + 1) == 'win3'):
        return 'win4'
    

for s in range(1, 70):
    if g(7, s) == 'win4': 
        print(s)
    