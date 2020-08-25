import sys
import pdb


def divide(dividend, divisor):
    return dividend / divisor


while True:
    try:
        dividend = int(input("Please enter the dividend:"))
        if dividend < 0:
            break
        divisor = int(input("Please enter the divisor:"))
        if divisor < 0:
            break
        answer = divide(dividend, divisor)
        print('The answer is: {}'.format(answer))
    except ZeroDivisionError:
        print("Can not devide by zero")
    except ValueError:
        break