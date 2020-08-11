def get_temp():
    tempf = False
    while not tempf:
        try:
            tempf = float(input("Enter a temperature Fahrenheit: "))
            tempc = (5 / 9) * (tempf - 32)
            print("Temperature %.2f" % tempf, "in Fahrenheit is %.2f" % tempc,
                  "in Celsius")
        except ValueError:
            print("Please enter a valid floating point for the temperature.")
        else:
            tempf = True


if __name__ == '__main__':
    get_temp()