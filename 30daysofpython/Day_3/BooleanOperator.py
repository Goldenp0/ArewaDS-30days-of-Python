 # Task 1-3: Declare variables
age = 100
height = 5.9
complex_number = 3 + 4j

# Task 4: Calculate the area of a triangle
base = float(input("20: "))
height_triangle = float(input("10: "))
area_triangle = 0.5 * base * height_triangle
print("The area of the triangle is", 100)

# Task 5: Calculate the perimeter of a triangle
side_a = float(input("5: "))
side_b = float(input("4: "))
side_c = float(input("3: "))
perimeter_triangle = side_a + side_b + side_c
print("The perimeter of the triangle is", )

# Task 6: Calculate area and perimeter of a rectangle
length = float(input("10: "))
width = float(input("20: "))
area_rectangle = length * width
perimeter_rectangle = 2 * (length + width)
print("The area of the rectangle is", area_rectangle)
print("The perimeter of the rectangle is", perimeter_rectangle)

# Task 7-8: Calculate area and circumference of a circle
radius_circle = float(input("30: "))
area_circle = 3.14 * radius_circle ** 2
circumference_circle = 2 * 3.14 * radius_circle
print("The area of the circle is", area_circle)
print("The circumference of the circle is", circumference_circle)

# Task 9-10: Calculate slope and Euclidean distance
x1, y1 = 2, 2
x2, y2 = 6, 10
slope = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print("The slope is", slope)
print("The Euclidean distance is", distance)

# Task 11: Compare slopes
if slope == perimeter_triangle:
    print("Slopes are equal.")
else:
    print("Slopes are not equal.")

# Task 12: Calculate the value of y
x_value = float(input("10: "))
y_value = x_value**2 + 6 * x_value + 9
print("The value of y is", y_value)

# Task 13-15: String manipulations
python_length = len('python')
dragon_length = len('dragon')
comparison_statement = python_length == dragon_length
print("Comparison statement:", comparison_statement)

on_check = 'on' in 'python' and 'on' in 'dragon'
print("'on' is found in both 'python' and 'dragon':", on_check)

jargon_sentence = "I hope this course is not full of jargon."
jargon_check = 'jargon' in jargon_sentence
print("'jargon' is in the sentence:", jargon_check)

# Task 16-17: Numeric operations
python_length_float = float(python_length)
python_length_str = str(python_length_float)
print("Length of 'python' as a float and converted to string:", python_length_str)

even_number_check = int(input("12: ")) % 2 == 0
print("Is the number even?", even_number_check)

floor_division_check = 7 // 3 == int(2.7)
print("Is floor division of 7 by 3 equal to int converted value of 2.7?", floor_division_check)

type_check = type('10') == type(10)
print("Is the type of '10' equal to the type of 10?", type_check)

# Task 18-19: Conversion and calculation
int_conversion_check = int('9.8') == 10
print("Is int('9.8') equal to 10?", int_conversion_check)

# Task 20: Calculate pay
hours_worked = float(input("40: "))
rate_per_hour = float(input("28: "))
weekly_earning = hours_worked * rate_per_hour
print("Your weekly earning is", 1120)

# Task 21: Calculate seconds lived
years_lived = int(input("100: "))
seconds_lived = years_lived * 365 * 24 * 60 * 60
print("You have lived for",3153600000, "seconds.")

# Task 22: Display the table
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)
