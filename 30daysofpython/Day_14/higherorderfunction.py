# Given lists
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Exercises: Level 1
# 1. Explain the difference between map, filter, and reduce.
# Answer: map is used to apply a given function to all items in an iterable, filter is used to filter out elements based on a condition, and reduce is used to accumulate the result of a binary function on the items of an iterable.
# 2. Explain the difference between higher order function, closure, and decorator.
# Answer: A higher-order function takes one or more functions as arguments or returns a function as its result. A closure is a function object that has access to variables in its lexical scope, even when the function is called outside that scope. A decorator is a design pattern in Python that allows the behavior of a function or class to be altered without modifying its source code.
# 3. Define a call function before map, filter, or reduce, see examples.
# Answer: A `call` function before map, filter, or reduce would look like this:

def call(func, iterable):
    return func(iterable)

# Example usage:
result = call(len, countries)
print(result)  # Output: 6

# 4. Use for loop to print each country in the countries list.
for country in countries:
    print(country)

# 5. Use for to print each name in the names list.
for name in names:
    print(name)

# 6. Use for to print each number in the numbers list.
for number in numbers:
    print(number)

# Exercises: Level 2
# 1. Use map to create a new list by changing each country to uppercase in the countries list.
uppercase_countries = list(map(str.upper, countries))
print(uppercase_countries)

# 2. Use map to create a new list by changing each number to its square in the numbers list.
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)

# 3. Use map to change each name to uppercase in the names list.
uppercase_names = list(map(str.upper, names))
print(uppercase_names)

# 4. Use filter to filter out countries containing 'land'.
filtered_countries_land = list(filter(lambda country: 'land' not in country.lower(), countries))
print(filtered_countries_land)

# 5. Use filter to filter out countries having exactly six characters.
filtered_countries_six_chars = list(filter(lambda country: len(country) == 6, countries))
print(filtered_countries_six_chars)

# 6. Use filter to filter out countries containing six letters and more in the country list.
filtered_countries_six_letters = list(filter(lambda country: len(country) >= 6, countries))
print(filtered_countries_six_letters)

# 7. Use filter to filter out countries starting with an 'E'
filtered_countries_starting_with_e = list(filter(lambda country: country[0].lower() != 'e', countries))
print(filtered_countries_starting_with_e)

# 8. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
# Assuming we want to filter out countries with 'land' and convert them to uppercase
chained_result = list(map(str.upper, filter(lambda country: 'land' not in country.lower(), countries)))
print(chained_result)

# 9. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(lst):
    return list(filter(lambda item: isinstance(item, str), lst))

# 10. Use reduce to sum all the numbers in the numbers list.
from functools import reduce
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)

# 11. Use reduce to concatenate all the countries and to produce this sentence:
# Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries.
concatenated_countries_sentence = reduce(lambda x, y: f'{x}, {y}', countries)
print(f'{concatenated_countries_sentence} are north European countries.')

# 12. Declare a function called categorize_countries that returns a list of countries with some common pattern.
def categorize_countries(pattern):
    return list(filter(lambda country: pattern.lower() in country.lower(), countries))

# 13. Create a function returning a dictionary, where keys stand for starting letters of countries
# and values are the number of country names starting with that letter.
def count_countries_by_starting_letter():
    starting_letters = set(map(lambda country: country[0].upper(), countries))
    count_dict = {letter: len(list(filter(lambda country: country[0].upper() == letter, countries))) for letter in starting_letters}
    return count_dict

# 14. Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
def get_first_ten_countries():
    return countries[:10]

# 15. Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries():
    return countries[-10:]

# Exercises: Level 3
# Assuming you have access to the countries_data.py file
countries = [
    # ... (the list of countries you provided)
]

# Sort by name
sorted_countries_by_name = sorted(countries)

# Print the result
print("Sorted by Name:")
print(sorted_countries_by_name)
print()

# Sorting by capital or population would require specific data for each country.
# Assuming you have a list of dictionaries with country details including 'name', 'capital', and 'population':

country_details = [
    {'name': 'Afghanistan', 'capital': 'Kabul', 'population': 38041754},
    # ... (details for other countries)
]

# Sort by capital
sorted_countries_by_capital = sorted(country_details, key=lambda x: x['capital'])
print("Sorted by Capital:")
print([country['name'] for country in sorted_countries_by_capital])
print()

# Sort by population
sorted_countries_by_population = sorted(country_details, key=lambda x: x['population'])
print("Sorted by Population:")
print([country['name'] for country in sorted_countries_by_population])

# 1. Sort countries by name, by capital
