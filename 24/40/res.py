def count_aoa(s: str) -> int: 
    c = 0
    for i in range(len(s) - 2): 
        if s[i] + s[i + 1] + s[i + 2] == 'AOA': 
            c += 1

    return c


def count_oao(s: str) -> int: 
    c = 0
    for i in range(len(s) - 2): 
        if s[i] + s[i + 1] + s[i + 2] == 'OAO': 
            c += 1

    return c


count = 0
for s in open('24/40/1.txt'): 
    if count_aoa(s) > count_oao(s): 
        count += 1

print(count)
