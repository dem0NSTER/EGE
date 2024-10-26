from itertools import product
c = set()
for i in product('01', repeat=15): 
   c.add(i)

print(len(c)) 
