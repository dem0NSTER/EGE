from functools import lru_cache

@lru_cache(None)
def g(h, s): 
    if h + s >= 67: 
        return 'win'
    if g(h * 3, s) == 'win' or g(h, s * 3) == 'win' or g(h + 1, s) == 'win' or g(h, s + 1) == 'win': 
        return 'win1'
    if g(h * 3, s) == 'win1' and g(h, s * 3) == 'win1' and g(h + 1, s) == 'win1' and g(h, s + 1) == 'win1': 
        return 'win2'
    if g(h * 3, s) == 'win2' or g(h, s * 3) == 'win2' or g(h + 1, s) == 'win2' or g(h, s + 1) == 'win2': 
        return 'win3'
    if (g(h, s * 3) == 'win1' and g(h * 3, s) == 'win3' and g(h + 1, s) == 'win3' and g(h, s + 1) == 'win3') or \
    (g(h, s * 3) == 'win1' and g(h * 3, s) == 'win1' and g(h + 1, s) == 'win3' and g(h, s + 1) == 'win3') or \
    (g(h, s * 3) == 'win3' and g(h * 3, s) == 'win1' and g(h + 1, s) == 'win3' and g(h, s + 1) == 'win3'):
        return "win4" 

win3 = []
for s in range(1, 61): 
    print(s)
    if g(6, s) == 'win4': 
        win3.append(s)

print(win3)
