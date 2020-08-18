sum = 0
round = 0
while True:
    number = int(input("Enter an integers:"))
    if number >= 0:
        round += 1
        sum = sum + number
    elif number < 0:
        if round == 0:
            print("You haven't entered a positive number")
            break
        elif round > 0:
            print("Average is", sum / round)
            break
