import math


# Function to add two numbers
def add_two_numbers(num1, num2):
    return num1 + num2

# Function to calculate the area of a circle
def area_of_circle(radius):
    return math.pi * radius**2

# Function to add all numbers in the arguments
def add_all_nums(*args):
    if all(isinstance(num, (int, float)) for num in args):
        return sum(args)
    else:
        return "Not all list items are numbers."

# Function to convert Celsius to Fahrenheit
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to check the season based on the month
def check_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    elif month in [9, 10, 11]:
        return "Autumn"
    else:
        return "Invalid month"

# Function to calculate the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

# Function to solve a quadratic equation
def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        return "No real roots"

# Function to print each element of a list
def print_list(lst):
    for item in lst:
        print(item)

# Function to reverse an array
def reverse_list(arr):
    return arr[::-1]

# Function to capitalize each item in a list
def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]

# Function to add an item to the end of a list
def add_item(lst, item):
    lst.append(item)
    return lst

# Function to remove an item from a list
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

# Function to add all numbers in a range
def sum_of_numbers(n):
    return sum(range(n + 1))

# Function to add all odd numbers in a range
def sum_of_odds(n):
    return sum(x for x in range(n + 1) if x % 2 != 0)

# Function to add all even numbers in a range
def sum_of_even(n):
    return sum(x for x in range(n + 1) if x % 2 == 0)

# Function to count the number of evens and odds in a positive integer
def evens_and_odds(number):
    if number > 0:
        evens = sum(1 for digit in str(number) if int(digit) % 2 == 0)
        odds = len(str(number)) - evens
        return f"The number of odds are {odds}.\nThe number of evens are {evens}."
    else:
        return "Please provide a positive integer."

# Function to calculate the factorial of a number
def factorial(number):
    if number >= 0:
        result = 1
        for i in range(1, number + 1):
            result *= i
        return result
    else:
        return "Factorial is not defined for negative numbers."

# Function to check if a parameter is empty
def is_empty(parameter):
    return not bool(parameter)

# Functions to calculate mean, median, mode, range, variance, and standard deviation
def calculate_mean(lst):
    return sum(lst) / len(lst) if len(lst) > 0 else "List is empty."

def calculate_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    if n % 2 == 0:
        return (sorted_lst[n//2 - 1] + sorted_lst[n//2]) / 2
    else:
        return sorted_lst[n//2]

def calculate_mode(lst):
    from collections import Counter
    counts = Counter(lst)
    max_count = max(counts.values())
    mode = [item for item, count in counts.items() if count == max_count]
    return mode

def calculate_range(lst):
    return max(lst) - min(lst) if len(lst) > 0 else "List is empty."

def calculate_variance(lst):
    mean = calculate_mean(lst)
    squared_diff = [(x - mean)**2 for x in lst]
    variance = sum(squared_diff) / len(lst)
    return variance

def calculate_std(lst):
    return math.sqrt(calculate_variance(lst)) if len(lst) > 0 else "List is empty."

print(evens_and_odds(100))
print(factorial(5))
print(is_empty([]))
# Call other list-related functions with your lists

import math
import json
import os

# Get the absolute path to the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to the JSON file
json_file_path = os.path.join(script_dir, 'data', 'countries-data.json')

# Open the JSON file and load the data
with open(json_file_path) as f:
    data = json.load(f)



# Function to check if a number is prime
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

# Function to check if all items in a list are unique
def are_all_items_unique(lst):
    return len(lst) == len(set(lst))

# Function to check if all items in a list have the same data type
def are_all_items_same_data_type(lst):
    return all(isinstance(item, type(lst[0])) for item in lst)

# Function to check if a variable is a valid Python variable
def is_valid_variable(variable):
    import re
    return re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', variable) is not None

# Function to get the most spoken languages in the world
def most_spoken_languages(data, num_languages=10):
    sorted_languages = sorted(data['languages'], key=lambda x: x['speakers'], reverse=True)
    return sorted_languages[:num_languages]

# Function to get the most populated countries
def most_populated_countries(data, num_countries=10):
    sorted_countries = sorted(data['countries'], key=lambda x: x['population'], reverse=True)
    return sorted_countries[:num_countries]

# Example usage
print(is_prime(17))  # True
print(are_all_items_unique([1, 2, 3, 4]))  # True
print(are_all_items_same_data_type([1, 2, 'three']))  # False
print(is_valid_variable('valid_variable'))  # True
most_spoken = most_spoken_languages(data, num_languages=5)
most_populated = most_populated_countries(data, num_countries=5)
print(most_spoken)
print(most_populated)
