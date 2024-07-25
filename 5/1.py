def f(n: int): 
    number = bin(n)[2:]
    if n % 2 == 0:
        number += '10'
    else: 
        number += '01'
        
    
    return int(number, 2)
        

if __name__ == '__main__': 
    for i in range(200): 
        if f(i) > 200: 
            print(i)
            break