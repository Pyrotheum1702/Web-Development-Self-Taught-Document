# Factorial recursion function
# Return the factorial value of the `n` argument
def factorial(n):
    if n < 1:
        print('argument must be positive numbers')
    if n == 1:
        return 1
    return n * factorial(n-1)


# Factorial function test:
print(factorial(5))
# Result : 5x4x3x2x1 = 120

print(factorial(10))
# Result : 10x9x8x7x6x5x4x3x2x1 = 3628800

print(factorial(15))
# Result : 15x14x13x12x11x10x9x8x7x6x5x4x3x2x1 = 1307674368000
