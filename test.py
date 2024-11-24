def factorial(n: int) -> int:
    """
    Calculate the factorial of a given integer.

    The factorial of a number is the product of all positive integers
    less than or equal to that number. For example, the factorial of 5
    is 1*2*3*4*5 = 120.

    :param n: the input number
    :return: the factorial of n
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(6))

def any_system(num: int, base: int) -> int:
    """
    Convert a given number from the decimal number system to any other.

    :param num: the number to convert
    :param base: the new base
    :return: the number in the new base
    """
    s = ''

    # take the remainder of the number divided by the base
    # and add it to the string
    while num > 0:
        s += str(num % base)
        # remove the last digit from the number
        num = num // base

    # reverse the string
    return int(s[::-1])


print(any_system(8, 2))
