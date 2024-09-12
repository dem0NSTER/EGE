from functools import lru_cache

def m(h, s):
    return (h, 3*s), (h*3, s), (h+3, s), (h, s +3), (h +2, s), (h, s + 2), (h + 1, s), (h, s + 2)


@lru_cache(None)
def g(h, s): 
    if h + s >= 145: 
        return 'w'
    if any(g(m, n) == 'w' for m, n in m(h, s)): 
        return 'w1'
    if all(g(m, n) == 'w1' for m, n in m(h, s)):
        return 'w2'
    if any(g(m, n) == 'w2' for m, n in m(h, s)):
        return 'w3'
    if all(g(m, n) == 'w1' or g(m, n) == 'w3' for m, n in m(h, s)):
        return 'w4'
    
for i in range(1, 134): 
    if g(11, i) == 'w4': 
        print(i)
