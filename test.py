# from itertools import combinations

# a = [1, 2, 3, 4, 5]
# for first in combinations(a, 2): 
#     for second in combinations(a, 2): 
#         if any(first[i] in second for i in range(len(first))):
#             continue
#         print(first, second)

from itertools import permutations

a = [1, 2, 3, 4]

for i in permutations(a): 
    first = sorted(i[:2])
    second = sorted(i[2:])
    print(first, second)


