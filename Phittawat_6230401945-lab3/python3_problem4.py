fact = 1
number = int(input("Enter a number to find factorial:"))
for i in range(1, number + 1):
    fact = fact * i
print("Factorial of", number, "is", fact)
