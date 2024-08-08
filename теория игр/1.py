def game(s): 
    if s >= 31: 
        return 'win'
    if game(s * 2) == 'win': 
        return 'win1'
    if game(s * 2) == 'win1' and game(s + 1) == 'win1' and game(s + 4) == 'win1': 
        return 'win2'
    if game(s * 2) == 'win2' or game(s + 1) == 'win2' or game(s + 4) == 'win2': 
        return 'win3'
    if (game(s * 2) == 'win1' and game(s + 1) == 'win3' and game(s + 4) == 'win3') or \
       (game(s * 2) == 'win1' and game(s + 1) == 'win3' and game(s + 4) == 'win1'): 
        return 'win4'

    
for s in range(1, 31): 
    if game(s) == 'win4': 
        print(s, 'vanya 1 or 2')