# Variables in Python

first_name = 'Precious'
last_name = 'Atuonwu'
country = 'Nigeria'
city = 'Lagos'
age = 100
is_married = True
is_true = True
is_light = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname':'Precious', 
    'lastname':'Atuonwu', 
    'country':'Nigeria',
    'city':'Lagos',
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Precious', 'Atuonwu', 'Nigeria', 100, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

## Exercises: Levels

# Declare variables
first_name = "Precious"
last_name = "Atuonwu"
num_one = 5
num_two = 4

# Task 1: Check the data type of all variables
print("Data type of first_name:", type(first_name))
print("Data type of last_name:", type(last_name))
print("Data type of num_one:", type(num_one))
print("Data type of num_two:", type(num_two))

# Task 2: Find the length of your first name
first_name_length = len(first_name)
print("Length of first name:", first_name_length)

# Task 3: Compare the length of your first name and your last name
last_name_length = len(last_name)
if first_name_length == last_name_length:
    print("Length of first name is equal to length of last name.")
else:
    print("Length of first name is not equal to length of last name.")

# Task 4-10: Perform arithmetic operations
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

# Task 11-12: Calculate area and circumference of a circle
radius_of_circle = 30
area_of_circle = 3.14 * radius_of_circle ** 2
circum_of_circle = 2 * 3.14 * radius_of_circle

# Task 13: Take radius as user input and calculate the area
user_radius = float(input("30: "))
user_area_of_circle = 3.14 * user_radius ** 2
print("Area of the circle with user input radius:", user_area_of_circle)

# Task 14-15: Get user input for first name, last name, country, and age
user_first_name = input("Precious: ")
user_last_name = input("Atuonwu: ")
user_country = input("Nigeria: ")
user_age = int(input("100: "))

# Task 16: Check Python reserved words or keywords
help('keywords')

