months = ["January", "Febuary", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_input = input("Enter month:")
zip_dict = dict(zip(months, days))
print(f"Number of days in {month_input} is {zip_dict[month_input]}")
