def f(n: int) -> int: 
    if n <= 18: 
        return n + 3
    if n > 18 and n % 3 == 0: 
        return (n // 3) * f(n // 3) + n - 12
    if n > 18 and n % 3 != 0: 
        return f(n - 1) + n ** 2 + 5


c = 0
for n in range(1, 1000 + 1): 
    num = f(n)
    nums = [i for i in str(num) if int(i) % 2 == 0]
    if len(str(num)) == len(nums):
        c += 1

print(c)
