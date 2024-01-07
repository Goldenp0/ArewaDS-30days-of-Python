# Iterate 0 to 10 using for loop
for i in range(11):
    print(i)

# Iterate 0 to 10 using while loop
i = 0
while i <= 10:
    print(i)
    i += 1

# Iterate 10 to 0 using for loop
for i in range(10, -1, -1):
    print(i)

# Iterate 10 to 0 using while loop
i = 10
while i >= 0:
    print(i)
    i -= 1

# Print a triangle using for loop
for i in range(1, 8):
    print('#' * i)

# Print a triangle using nested loops
for _ in range(8):
    for _ in range(8):
        print('#', end=' ')
    print()

# Print the multiplication table
for i in range(11):
    print(f"{i} x {i} = {i * i}")

# Iterate through a list and print items
tech_stack = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for tech in tech_stack:
    print(tech)

# Print even numbers from 0 to 100 using for loop
for i in range(0, 101, 2):
    print(i)

# Print odd numbers from 0 to 100 using for loop
for i in range(1, 101, 2):
    print(i)

# Sum of all numbers from 0 to 100
total_sum = 0
for i in range(101):
    total_sum += i
print(f"The sum of all numbers is {total_sum}.")

# Sum of even and odd numbers separately
sum_even = 0
sum_odd = 0

for i in range(101):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i

print(f"The sum of all evens is {sum_even}. And the sum of all odds is {sum_odd}.")

# countries.py
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']

# Loop through countries containing the word 'land'
countries_with_land = [country for country in countries if 'land' in country.lower()]
print("Countries containing the word 'land':", countries_with_land)

# Reverse the order of the fruit list
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []

for fruit in reversed(fruits):
    reversed_fruits.append(fruit)

print("Reversed fruit list:", reversed_fruits)

# countries_data.py
countries_data = [
    {'name': 'China', 'population': 1444216107, 'languages': ['Mandarin']},
    {'name': 'India', 'population': 1393409038, 'languages': ['Hindi', 'English']},
    # ... other country data
]

# Total number of languages
all_languages = set()
for country in countries_data:
    all_languages.update(country['languages'])

print("Total number of languages:", len(all_languages))

# Find the ten most spoken languages
all_languages_count = {}
for country in countries_data:
    for language in country['languages']:
        all_languages_count[language] = all_languages_count.get(language, 0) + 1

most_spoken_languages = sorted(all_languages_count.items(), key=lambda x: x[1], reverse=True)[:10]
print("Ten most spoken languages:", most_spoken_languages)

# Find the 10 most populated countries
most_populated_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)[:10]
print("Ten most populated countries:", most_populated_countries)
