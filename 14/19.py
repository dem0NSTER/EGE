def f(n: int, base: int) -> list:
    s = []

    while n > 0:
        s.append(n % base)
        n = n//base
    return s[::-1]
        
print(f(8, 2))

s1 = (99 + 3 * 9**3) * 9**3 + 99 + 9**9
print(s1)
print(f(s1, 9))
print(sum(f(s1, 9)))
