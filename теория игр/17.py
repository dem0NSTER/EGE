from functools import lru_cache

def moves(s: int, last: int):
    if last == '*2':
        return [s + 1, '+1'] , [s + 2, '+2']
    if last == '+1':
         return [s * 2, '*2'] , [s + 2, '+2']
    if last == '+2':
        return [s * 2, '*2'] , [s + 1, '+1']
    return [s * 2, '*2'], [s + 1, '+1'], [s + 2, '+2'] 


@lru_cache(None)
def g(s: int, last):
    if s >= 83:
        return 'win'
    if any(g(m, l) == 'win' for m, l in moves(s, last)):
        return 'win1'
    if all(g(m, l) == 'win1' for m, l in moves(s, last)):
        return 'win2'
    if any(g(m, l) == 'win2' for m, l in moves(s, last)):
        return 'win3'
    if all(g(m, l) == 'win3' or g(m, l) == 'win1' for m, l in moves(s, last)):
        return 'win4'

for s in range(1, 83):
    if g(s, '') == 'win4':
        print(s, 'win4')
        
