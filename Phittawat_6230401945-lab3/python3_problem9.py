while True:
    number = int(input("Enter an integers:"))
    if number == 99:
        print("Exit program")
        break
    elif number % 2 == 0:
        print(number)
    else:
        pass
