def processing():
    while True:
        try:
            first_number = float(input("Enter first number:"))
            second_number = float(input("Enter second number:"))
            operator = str(input("Enter the operator:"))
        except ValueError:
            break
        if operator == "+":
            print(first_number, operator, second_number, "=",
                  first_number + second_number)
        elif operator == "-":
            print(first_number, operator, second_number, "=",
                  first_number - second_number)
        elif operator == "*":
            print(first_number, operator, second_number, "=",
                  first_number * second_number)
        elif operator == "/":
            try:
                print(first_number, operator, second_number, "=",
                    first_number / second_number)
            except ZeroDivisionError:
                print("Can not divide by Zero")
        elif operator == "%":
            print(first_number, operator, second_number, "=",
                  first_number % second_number)
        else:
            print("Unknown Operator")


if __name__ == '__main__':
    processing()

