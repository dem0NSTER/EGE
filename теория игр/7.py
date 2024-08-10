from functools import lru_cache


@lru_cache(None)
def g(s: int): 
    if s >= 36: 
        if s >= 60: 
            return 'lose'
        return 'win'
    
    if g(s * 3) == 'win' or g(s * 2) == 'win' or g(s + 1) == 'win': 
        return 'win1'
    
    if (g(s * 3) == 'win1' or g(s * 3) == 'lose') and\
        (g(s * 2) == 'win1' or g(s * 2) == 'lose') and\
        (g(s + 1) == 'win1' or g(s + 1) == 'lose'): 
        return 'win2'
    
    if g(s * 3) == 'win2' or g(s * 2) == 'win2' or g(s + 1) == 'win2': 
        return 'win3'
    
    if ((g(s * 3) == 'win1' or g(s * 3) == 'lose') and \
        (g(s * 2) == 'win1' or g(s * 2) == 'lose') and \
        g(s + 1) == 'win3') or\
        ((g(s * 3) == 'win1' or g(s * 3) == 'lose') and \
        (g(s * 2) == 'win3' or g(s * 2) == 'lose') and g(s + 1) == 'win3'): 
        return 'win4'
    
res = []
for s in range(1, 36): 
    if g(s) == 'win4': 
        res.append(s)

print(min(res), max(res))
