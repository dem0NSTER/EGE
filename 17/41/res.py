with open('17/41/1.txt') as file: 
    s1 = file.read().split()

nums = [int(i) for i in s1]

max_13 = 0
for i in nums: 
    if str(i)[-2:] == '13': 
        max_13 = max(max_13, i)


def f(n: int, m: int, z: int): 
    if (n % 2 == 0 and m % 2 == 0 and z % 2 == 0) or (len(str(n)) == 2 or len(str(m)) == 2 or len(str(z)) == 2):
        if n + m + z <= max_13: 
            return True


res = []
for i in range(len(nums) - 2): 
    if f(nums[i], nums[i + 1], nums[i + 2]): 
        res.append(nums[i] + nums[i + 1] + nums[i + 2])

print(len(res), int(sum(res) / len(res)))