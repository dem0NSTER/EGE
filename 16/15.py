"""
(ОСН 2022)
Алгоритм вычисления значенияфункции F(n), где n натуральное число, задан следующими соотношениями:
F(n) = 1 при n < 3;
F(n) = F(n - 1) + n - 1, если n ≥ 3 и при этом n — четно.
F(n) = F(n - 2) + 2 · n - 2, если n ≥ 3 и при этом n — нечетно .
Чему равно значениефункции F(35)? 
"""

def f(n): 
    if n < 3: 
        return 1    
    if n >= 3 and n % 2 == 0: 
        return f(n - 1) + n - 1
    else: 
        return f(n - 2) + 2 * n - 2
    
print(f(35))