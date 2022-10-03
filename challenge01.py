##write a script to generate 10 random integers in the range 10 to 30.
## Find the minimum and maximum values
##Print each integer, and alongside print what percentage it is of the minimum value
##and what percentage of the maximum.
##Percentages should be shown to nearst 1 percent (no decimals)
##your output should be nealty aligned columns
import random
def generate_random_number():
    random_number=random.randint(10,30)
    return random_number
def collect_number_generated():
    numbers=[]
    for x in range(10):
        random_number=generate_random_number()
        numbers.append(random_number)
    return numbers
def find_minimum_value(numbers):
    min_value=30
    for number in numbers:
        if number<min_value:
            min_value=number
    return min_value
def find_maximum_value(numbers):
    min_value=0
    for number in numbers:
        if number>min_value:
            min_value=number
    return min_value
def print_output(numbers,min_number,max_number):
    for number in numbers:
        min_percentage=(number/min_number)*100
        max_percentage=(number/max_number)*100
        print(f"{number} is {int(min_percentage)}% of {min_number} and {int(max_percentage)}% of {max_number}")
def start_script():
    numbers=collect_number_generated()
    min_number=find_minimum_value(numbers)
    max_number=find_maximum_value(numbers)
    print_output(numbers,min_number,max_number)
start_script()