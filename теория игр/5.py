from functools import lru_cache

@lru_cache(None)
def g(s): 
    if s <= 10: 
        return 'win'
    if g(s // 2) == 'win' or g(s - 8) == 'win': 
        return 'win1'
    if g(s // 2) == 'win1' and g(s - 8) == 'win1': 
        return 'win2'
    if g(s // 2) == 'win2' or g(s - 8) == 'win2': 
        return 'win3'
    if g(s // 2) == 'win1' and g(s - 8) == 'win3': 
        return 'win4'
    
win4 = []
for s in range(100, 10, -1): 
    if g(s) == 'win4': 
        win4.append(s)

print(len(win4))
