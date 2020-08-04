#Phittawat Champajan DME Y.2
import random, statistics
first_random_number = random.randrange(1, 11)
second_random_number = random.randrange(1, 11)
average_value = statistics.mean((first_random_number,second_random_number))
standard_deviation_value =  statistics.stdev((first_random_number, second_random_number))
print("The average of",first_random_number,"and",second_random_number,"is",average_value)
print("The standard deviation of",first_random_number,"and",second_random_number,"is",standard_deviation_value)