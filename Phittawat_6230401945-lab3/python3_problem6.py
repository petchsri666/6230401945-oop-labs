months = ["January", "Febuary", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dict = {}
for i in range(0, 12):
    dict[months[i]] = days[i]
month_input = input("Enter month:")
print(f"Number of days in {month_input} is {dict[month_input]}")
