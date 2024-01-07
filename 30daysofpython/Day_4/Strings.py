# Task 1
str1 = 'Thirty'
str2 = 'Days'
str3 = 'Of'
str4 = 'Python'
result_str = str1 + ' ' + str2 + ' ' + str3 + ' ' + str4
print(result_str)

# Task 2
str5 = 'Coding'
str6 = 'For'
str7 = 'All'
result_str2 = str5 + ' ' + str6 + ' ' + str7
print(result_str2)

# Task 3
company = "Coding For All"
print(company)

# Task 4
print("Length of company string:", len(company))

# Task 5
print("Uppercase:", company.upper())

# Task 6
print("Lowercase:", company.lower())

# Task 7
print("Capitalize:", company.capitalize())
print("Title:", company.title())
print("Swapcase:", company.swapcase())

# Task 8
sliced_company = company.split(' ')[1:]
print("Sliced out first word:", ' '.join(sliced_company))

# Task 9
print("Contains 'Coding'?", 'Coding' in company)

# Task 10
company = company.replace('Coding', 'Python')
print("Replaced 'Coding' with 'Python':", company)

# Task 11
splitted_company = company.split(' ')
print("Splitting using space as separator:", splitted_company)

# Task 12
tech_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
split_tech_companies = tech_companies.split(', ')
print("Split at the comma:", split_tech_companies)

# Task 13-15
print("Character at index 0:", company[0])
print("Last index of 'Coding For All':", company.rindex('l'))
print("Character at index 10:", company[10])

# Task 16-17
acronym1 = ''.join(word[0] for word in 'Python For Everyone'.split())
acronym2 = ''.join(word[0] for word in 'Coding For All'.split())
print("Acronym for 'Python For Everyone':", acronym1)
print("Acronym for 'Coding For All':", acronym2)

# Task 18-19
c_position = company.find('C')
f_position = company.find('F')

print("Position of first occurrence of 'C':", c_position if c_position != -1 else "Not found")
print("Position of first occurrence of 'F':", f_position if f_position != -1 else "Not found")

# Task 20-21
sentence = 'You cannot end a sentence with because because because is a conjunction'
print("Position of first occurrence of 'because':", sentence.index('because'))
print("Position of last occurrence of 'because':", sentence.rindex('because'))

# Task 22-23
phrase = sentence[sentence.index('because'):sentence.rindex('because')+len('because because because')]
print("Sliced phrase:", phrase)

# Task 24
print("Position of first occurrence of 'because':", sentence.find('because'))

# Task 25
phrase2 = sentence[sentence.find('because'):sentence.find('because') + len('because because because')]
print("Sliced phrase:", phrase2)

# Task 26-27
print("Starts with 'Coding'?", company.startswith('Coding'))
print("Ends with 'coding'?", company.endswith('coding'))

# Task 28
trimmed_str = '   Coding For All      '.strip()
print("Trimmed string:", trimmed_str)

# Task 29
var1 = '30DaysOfPython'
var2 = 'thirty_days_of_python'
print("Is '30DaysOfPython' an identifier?", var1.isidentifier())
print("Is 'thirty_days_of_python' an identifier?", var2.isidentifier())

# Task 30
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_libraries = ' # '.join(libraries)
print("Joined with hash and space:", joined_libraries)

# Task 31
sentences_with_newline = "I am enjoying this challenge.\nI just wonder what is next."
print("Sentences with new line:", sentences_with_newline)

# Task 32
lines_with_tab = "Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
print("Lines with tab:", lines_with_tab)

# Task 33
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

# Task 34-35
print(f"{8} + {6} = {8+6}")
print(f"{8} - {6} = {8-6}")
print(f"{8} * {6} = {8*6}")
print(f"{8} / {6} = {8/6:.2f}")
print(f"{8} % {6} = {8%6}")
print(f"{8} // {6} = {8//6}")
print(f"{8} ** {6} = {8**6}")
