numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_numbers = [num for num in numbers if num <= 0]
print(filtered_numbers)

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [num for sublist in list_of_lists for nested_list in sublist for num in nested_list]
print(flattened_list)

tuples_list = [(i,) + tuple([j ** i for j in range(7)]) for i in range(11)]
print(tuples_list)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries = [[country.upper(), country[:3].upper(), city.upper()] for nested_list in countries for (country, city) in nested_list]
print(flattened_countries)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dict_countries = [{'country': country.upper(), 'city': city.upper()} for nested_list in countries for (country, city) in nested_list]
print(dict_countries)

names = [[('Precious', 'Atuonwu')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_names = [' '.join(name) for nested_list in names for name in nested_list]
print(concatenated_names)


linear_function = lambda x, m, b: m * x + b

# Example usage:
slope = linear_function(2, 3, 1)
print(f"Slope: {slope}")

y_intercept = linear_function(0, 2, -1)
print(f"Y-Intercept: {y_intercept}")