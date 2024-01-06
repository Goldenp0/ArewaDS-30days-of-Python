# Task 1
dog = {}

# Task 2
dog['name'] = 'Buddy'
dog['color'] = 'Brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 3

# Task 3
student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 22,
    'marital_status': 'Single',
    'skills': ['Python', 'JavaScript'],
    'country': 'USA',
    'city': 'New York',
    'address': '123 Main St'
}

# Task 4
length_of_student = len(student)
print("Length of Student Dictionary:", length_of_student)

# Task 5
skills_value = student['skills']
print("Skills Value:", skills_value)
print("Data Type of Skills:", type(skills_value))

# Task 6
student['skills'].extend(['HTML', 'CSS'])
print("Modified Skills Value:", student['skills'])

# Task 7
keys_list = list(student.keys())
print("Dictionary Keys as a List:", keys_list)

# Task 8
values_list = list(student.values())
print("Dictionary Values as a List:", values_list)

# Task 9
list_of_tuples = list(student.items())
print("Dictionary as a List of Tuples:", list_of_tuples)

# Task 10
del student['marital_status']

# Task 11
del student
print("Student Dictionary deleted.")
