def output(num):
    int_float = input("Enter output format (float, int):")
    if int_float.lower() == "float":
        num = float(num)
    elif int_float.lower() == "int":
        num = int(num)
    else:
        num = float(num)
    return num


def robust_calculator():
    while True:
        try:
            first_number = input("Enter the first operand ('q' to quit):")
            if first_number.lower() == "q":
                break
            else:
                first_number = float(first_number)
            second_number = float(input("Enter second operand:"))
            operator = str(input("Enter the operation ('+','-','*','/'):"))
        except ValueError:
            pass
        if operator == "+":
            print(first_number, operator, second_number, "=",
                  output(num = first_number + second_number))
        elif operator == "-":
            print(first_number, operator, second_number, "=",
                  output(num = first_number - second_number))
        elif operator == "*":
            print(first_number, operator, second_number, "=",
                  output(num = first_number * second_number))
        elif operator == "/":
            try:
                print(first_number, operator, second_number, "=",
                      output(num = first_number / second_number))
            except ZeroDivisionError:
                print("Can not divide by Zero")
        elif operator == "%":
            print(first_number, operator, second_number, "=",
                  output(num = first_number % second_number))
        else:
            print("Unknown Operator")

if __name__ == '__main__':
    robust_calculator()