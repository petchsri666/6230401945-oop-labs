def factorial(number):
    if number <= 1:
        return 1
    else:
        return number*factorial(number-1)


def check_positive():
    try:
        int_input = int(input("Enter an integer:"))
        if int_input < 0:
            raise ValueError("{} is not a positive integer".format(int_input))
    except ValueError as err:
        print("Please enter a positive integer.,%s" %err)
    else:
        print("factorial(%d) is "%int_input,factorial(number=int_input))

if __name__ == '__main__':
    check_positive()