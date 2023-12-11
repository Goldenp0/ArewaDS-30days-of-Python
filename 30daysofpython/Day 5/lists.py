# Task 1
empty_list = []

# Task 2
list_with_items = [1, 2, 'three', 4.0, True]

# Task 3
length_of_list = len(list_with_items)
print("Length of the list:", length_of_list)

# Task 4
first_item = list_with_items[0]
middle_item = list_with_items[length_of_list // 2]
last_item = list_with_items[-1]

print("First item:", first_item)
print("Middle item:", middle_item)
print("Last item:", last_item)

# Task 5
mixed_data_types = ['John', 25, 5.9, 'Single', '123 Main St']

# Task 6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Task 7
print("IT Companies:", it_companies)

# Task 8
num_of_companies = len(it_companies)
print("Number of companies in the list:", num_of_companies)

# Task 9
print("First company:", it_companies[0])
print("Middle company:", it_companies[num_of_companies // 2])
print("Last company:", it_companies[-1])

# Task 10
it_companies[0] = 'Meta'
print("List after modifying a company:", it_companies)

# Task 11
it_companies.append('LinkedIn')
print("List after adding an IT company:", it_companies)

# Task 12
it_companies.insert(num_of_companies // 2, 'Tesla')
print("List after inserting an IT company in the middle:", it_companies)

# Task 13
it_companies[2] = it_companies[2].upper()
print("List after changing one company to uppercase:", it_companies)

# Task 14
check_company = 'Google' in it_companies
print("Does 'Google' exist in the list?", check_company)

# Task 15
it_companies.sort()
print("List after sorting:", it_companies)

# Task 16
it_companies.reverse()
print("List in descending order:", it_companies)

# Task 17
first_three_companies = it_companies[:3]
print("First three companies:", first_three_companies)

# Task 18
last_three_companies = it_companies[-3:]
print("Last three companies:", last_three_companies)

# Task 19
middle_company = it_companies[num_of_companies // 2]
print("Middle company or companies:", middle_company)

# Task 20
it_companies.pop(0)
print("List after removing the first IT company:", it_companies)

# Task 21
it_companies.pop(num_of_companies // 2)
print("List after removing the middle IT company:", it_companies)

# Task 22
it_companies.pop()
print("List after removing the last IT company:", it_companies)

# Task 23
it_companies.clear()
print("List after removing all IT companies:", it_companies)

# Task 24
del it_companies
# it_companies is now undefined

# Task 25
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

# Task 26
full_stack = front_end + back_end

# Task 27
if 'SQL' in full_stack:
    full_stack.insert(full_stack.index('SQL') + 1, 'Python')
else:
    print("'SQL' not found in the list.")

print("Joined and modified list:", full_stack)

# EXECISES TWO
# Task 1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Task 2
ages.sort()
min_age = min(ages)
max_age = max(ages)

print("Sorted Ages:", ages)
print("Min Age:", min_age)
print("Max Age:", max_age)

# Task 3
ages.extend([min_age, max_age])
print("Ages after adding min and max age:", ages)

# Task 4
sorted_ages = sorted(ages)
middle_index = len(sorted_ages) // 2
median_age = (sorted_ages[middle_index - 1] + sorted_ages[middle_index]) / 2 if len(sorted_ages) % 2 == 0 else sorted_ages[middle_index]

print("Median Age:", median_age)

# Task 5
average_age = sum(ages) / len(ages)
print("Average Age:", average_age)

# Task 6
age_range = max(ages) - min(ages)
print("Range of Ages:", age_range)

# Task 7
min_average_diff = abs(min_age - average_age)
max_average_diff = abs(max_age - average_age)
print("Difference between min and average:", min_average_diff)
print("Difference between max and average:", max_average_diff)

# Task 8
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
middle_index_countries = len(countries) // 2
middle_country = countries[middle_index_countries] if len(countries) % 2 != 0 else [countries[middle_index_countries - 1], countries[middle_index_countries]]

print("Middle Country(ies):", middle_country)

# Task 9
if len(countries) % 2 == 0:
    first_half = countries[:middle_index_countries]
    second_half = countries[middle_index_countries:]
else:
    first_half = countries[:middle_index_countries + 1]
    second_half = countries[middle_index_countries + 1:]

print("First Half:", first_half)
print("Second Half:", second_half)

# Task 10
first_three, *scandic_countries = countries[:3], countries[3:]
print("First Three Countries:", first_three)
print("Scandic Countries:", scandic_countries)
