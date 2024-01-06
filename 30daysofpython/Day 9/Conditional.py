# Exercise: Level 1
# Task 1
   user_age = int(input("Enter your age: "))
if user_age >= 18:
    print("You are old enough to learn to drive.")
else:
    missing_years = 18 - user_age
    print(f"You need {missing_years} more years to learn to drive.")

# Task 2
my_age = 25  # Assuming my age is 25 for comparison
your_age = int(input("Enter your age: "))
if my_age > your_age:
    age_difference = my_age - your_age
    plural_s = 's' if age_difference > 1 else ''
    print(f"You are {age_difference} year{plural_s} older than me.")
elif my_age < your_age:
    age_difference = your_age - my_age
    plural_s = 's' if age_difference > 1 else ''
    print(f"I am {age_difference} year{plural_s} older than you.")
else:
    print("We are the same age.")

# Task 3
num_a = int(input("Enter number one: "))
num_b = int(input("Enter number two: "))
if num_a > num_b:
    print(f"{num_a} is greater than {num_b}.")
elif num_a < num_b:
    print(f"{num_a} is smaller than {num_b}.")
else:
    print(f"{num_a} is equal to {num_b}.")

# Exercise: Level 2
# Task 1
score = int(input("Enter your score: "))
if 80 <= score <= 100:
    grade = 'A'
elif 70 <= score <= 89:
    grade = 'B'
elif 60 <= score <= 69:
    grade = 'C'
elif 50 <= score <= 59:
    grade = 'D'
else:
    grade = 'F'
print(f"Your grade is {grade}.")

# Task 2
user_input = input("Enter a month: ").lower()
if user_input in ['september', 'october', 'november']:
    season = 'Autumn'
elif user_input in ['december', 'january', 'february']:
    season = 'Winter'
elif user_input in ['march', 'april', 'may']:
    season = 'Spring'
elif user_input in ['june', 'july', 'august']:
    season = 'Summer'
else:
    season = 'Unknown'
print(f"The season is {season}.")

# Task 3
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Enter a fruit: ").lower()
if new_fruit not in fruits:
    fruits.append(new_fruit)
    print("Modified List:", fruits)
else:
    print("That fruit already exists in the list.")

# Exercise: Level 3
# Task 1
if 'skills' in person:
    skills_list = person['skills']
    if len(skills_list) > 1:
        middle_skill_index = len(skills_list) // 2
        print("Middle Skill:", skills_list[middle_skill_index])

# Task 2
if 'skills' in person and 'Python' in person['skills']:
    print("The person has 'Python' skill.")

# Task 3
if 'skills' in person:
    skills_list = person['skills']
    if skills_list == ['JavaScript', 'React']:
        print("He is a front end developer.")
    elif 'Node' in skills_list and 'Python' in skills_list and 'MongoDB' in skills_list:
        print("He is a backend developer.")
    elif 'React' in skills_list and 'Node' in skills_list and 'MongoDB' in skills_list:
        print("He is a fullstack developer.")
    else:
        print("Unknown title")

# Task 4
if person.get('is_married') and person.get('country') == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
