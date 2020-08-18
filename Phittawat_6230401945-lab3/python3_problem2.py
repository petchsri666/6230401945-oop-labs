word = "kku"
turns = 3
while turns > 0:
    charac_input = str(input("Enter a word:"))
    if charac_input == word:
        print("Congrats that you can guess the secert word correctly")
        break
    else:
        turns -= 1
        print("Incorrect! You have", turns, "guesses left.")
        if turns == 0:
            print("Thanks for trying, but the secert word is actually kku")
