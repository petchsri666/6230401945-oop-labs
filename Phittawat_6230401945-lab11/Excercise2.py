import functools
import sys

n = int(sys.argv[1])


def factorial(n):
    if n == 0:
        return 1
    else:
        #print(range(1, n+1))
        return functools.reduce(lambda x, y: x * y, range(1, n+1))


print(f"Factorial of ({n}) is {factorial(n)}")
