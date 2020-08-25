def check(msg):
    while True:
        checking_quit = input(msg)
        if checking_quit == "quit":
            break
        elif checking_quit != "quit":
            try:
                checking_quit = int(checking_quit)
            except ValueError:
                pass
            else:
                return checking_quit
            print("Please enter a number")


def processing():
    while True:
        try:
            first_number = check("Enter first operand:")
            second_number = check("Enter second operand:")
            operator = str(input("Enter the operator (+, -, *, /):"))
        except ValueError:
            print("Please enter a number")
            pass
        else:
            if operator == "+":
                print("Results of", first_number, operator, second_number,
                      "is", first_number + second_number)
            elif operator == "-":
                print("Results of", first_number, operator, second_number,
                      "is", first_number - second_number)
            elif operator == "*":
                print("Results of", first_number, operator, second_number,
                      "is", first_number * second_number)
            elif operator == "/":
                try:
                    print("Results of", first_number, operator, second_number,
                          "is", first_number / second_number)
                except ZeroDivisionError:
                    print("Can not divide by Zero")
            elif operator == "%":
                print("Results of", first_number, operator, second_number,
                      "is", first_number % second_number)
            else:
                print("Unknown Operator")


if __name__ == '__main__':
    processing()

