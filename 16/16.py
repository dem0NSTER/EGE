"""
Алгоритм вычисления значения функции F(n), где n - натуральное число, задан
следующими соотношениями:
F(n) = 2 при n < 3;
F(n) = F(n - 2) + F(n - 1) - n, если n ≥ 3 и при этом n — четно.
F(n) = F(n - 1) - F(n - 2) + 2 * n, если n ≥ 3 и при этом n — нечетно .
Чему равно значение функции F(32)?
"""

def f(n): 
    if n < 3: 
        return 2
    if n % 2 == 0:
        return f(n - 2)  + f(n - 1) - n 
    else: 
        return f(n - 1) - f(n - 2) + 2 *n
    
print(f(32))
