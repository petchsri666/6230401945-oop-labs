ADD, SUB, MUL, DIV = range(4)


def calculator(a, b, operation=ADD, output_formal=float):
    if operation == ADD:
        result = a + b
    elif operation == SUB:
        result = a - b
    elif operation == MUL:
        result = a * b
    elif operation == DIV:
        result = a / b
    else:
        raise ValueError("Operation must be ADD, SUB, MUL or DIV. ")
    if output_formal == float:
        result = float(result)
    elif output_formal == int:
        result = round(result)
    else:
        raise ValueError("Format must be float or int. ")
    return result


def flexible_calculator(operation=ADD, output_formal=float, *number):
    result = 0
    for i in number:
        if operation == ADD:
            result += i
        elif operation == SUB:
            result -= i
        elif operation == MUL:
            result *= i
        elif operation == DIV:
            result /= i
        else:
            raise ValueError("Operation must be ADD, SUB, MUL or DIV. ")
        if output_formal == float:
            result = float(result)
        elif output_formal == int:
            result = round(result)
        else:
            raise ValueError("Format must be float or int. ")
        return result


if __name__ == '__main__':
    answer = calculator(2, 3)
    print("calculator(2, 3) = {}".format(answer))
    answer = calculator(2, 3, MUL)
    print("calculator(2, 3, MUL) = {}".format(answer))
    answer = calculator(2, 3, SUB, int)
    print("calculator(2, 3, SUB, int) = {}".format(answer))
    answer = flexible_calculator(ADD, int, 1, 2, 3)
    print("flexible_calculator(ADD, int, 1, 2, 3) = {}".format(answer))
    answer = flexible_calculator(ADD, int, 1, 2, 3, 4)
    print("flexible_calculator(ADD, int, 1, 2, 3, 4) = {}".format(answer))
    answer = flexible_calculator(SUB, float, 1, 2, 3, 4, 5)
    print("flexible_calculator(SUB, float, 1, 2, 3, 4, 5) = {}".format(answer))
    answer = flexible_calculator(ADD, int, 1)
    print("flexible_calculator(ADD, int, 1) = {}".format(answer))
    answer = flexible_calculator(MUL, int, 2, 3, 4)
    print("flexible_calculator(MUL, int, 2, 3, 4) = {}".format(answer))
    answer = flexible_calculator(DIV, float, 10, 5, 2)
    print("flexible_calculator(DIV, float, 10, 5, 2) = {}".format(answer))
    answer = flexible_calculator(DIV, float)
    print("flexible_calculator(DIV, float) = {}".format(answer))