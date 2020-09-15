import math


def hypotenuse(a, b):
    square_1 = math.sqrt(a ** 2 + b ** 2)
    print(f"Sqrt({a}^2 + {b}^2) = {square_1}")


if __name__ == '__main__':
    hypotenuse(3.0, 4.0)
    hypotenuse(3, 4)
    hypotenuse(3, 4.0)