#Phittawat Champajan DME Y.2
import random,math
first_random_number = float(random.randint(1, 10))
second_random_number = float(random.randint(1, 10))
average_value = (first_random_number+second_random_number)/2
standard_deviation_value =  math.sqrt((((first_random_number-average_value)**2)+((second_random_number-average_value)**2))/2)
print("The average of",first_random_number,"and",second_random_number,"is",average_value)
print("The standard deviation of",first_random_number,"and",second_random_number,"is",standard_deviation_value)