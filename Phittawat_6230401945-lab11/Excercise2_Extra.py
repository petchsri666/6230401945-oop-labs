from functools import reduce
import sys

n = int(sys.argv[1])

number = list(range(1, n+1))
fac = lambda i : reduce(lambda x, y:x * y, range(1, i + 1))
a = list(map(fac, number))


print(f"With the argument as {sys.argv[1]}, the input list is {number}")
print(f"The factorial numbers are {a}")
