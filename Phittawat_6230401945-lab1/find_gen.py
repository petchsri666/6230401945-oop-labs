#Phittawat Champajan DME Y.2
import datetime
name = str(input("Enter your name: "))
born_year = int(input("Enter the year you were born: "))
time = datetime.datetime.now()
year_old = time.year-born_year
if year_old >= 73:
    print(name,"is",year_old, "years old.","You are genaration is", '"Builder"')
elif year_old >= 55:
    print(name,"is",year_old, "years old.","You are genaration is", '"Baby Boomer"')
elif year_old >= 40:
    print(name, "is", year_old, "years old.", "You are genaration is", '"X"')
elif year_old >= 25:
    print(name, "is", year_old, "years old.", "You are genaration is", '"Y"')
elif year_old >= 10:
    print(name, "is", year_old, "years old.", "You are genaration is", '"Z"')
elif year_old >= 1:
    print(name, "is", year_old, "years old.", "You are genaration is", '"Alpha"')
else :
    print("Sorry please check your born year")



