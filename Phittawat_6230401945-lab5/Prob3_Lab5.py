import math


def hypotenuse(a, b):
    try:
        square_1 = math.sqrt(a ** 2 + b ** 2)
        return square_1
    except TypeError:
        return None

if __name__ == '__main__':
    print("hypotenuse({}, {}) is {}".format(3.0, 4.0, hypotenuse(3.0, 4.0)))
    print("hypotenuse({}, {}) is {}".format("3", "4", hypotenuse("3", "4")))
    print("hypotenuse({}, {}) is {}".format(3, "4.0", hypotenuse(3, "4.0")))