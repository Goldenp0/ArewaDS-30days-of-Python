# Given set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# Task 1
length_of_set = len(it_companies)
print("Length of it_companies:", length_of_set)

# Task 2
it_companies.add('Twitter')
print("it_companies after adding 'Twitter':", it_companies)

# Task 3
additional_companies = {'LinkedIn', 'Tesla', 'Uber'}
it_companies.update(additional_companies)
print("it_companies after adding multiple companies:", it_companies)

# Task 4
it_companies.remove('Uber')  # Choose any company to remove
print("it_companies after removing a company:", it_companies)

# Task 5
# Difference between remove and discard:
# - `remove` raises a KeyError if the specified element is not found in the set.
# - `discard` does not raise an error if the specified element is not found; it simply does nothing.

# Example:
try:
    it_companies.remove('NonexistentCompany')
except KeyError as e:
    print(f"Error when using remove: {e}")

it_companies.discard('NonexistentCompany')  # No error will be raised
print("No error occurred with discard")

# level 2

# Given sets
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Task 1
joined_sets = A.union(B)
print("Join A and B:", joined_sets)

# Task 2
intersection_set = A.intersection(B)
print("Intersection of A and B:", intersection_set)

# Task 3
is_A_subset_of_B = A.issubset(B)
print("Is A subset of B?", is_A_subset_of_B)

# Task 4
are_disjoint = A.isdisjoint(B)
print("Are A and B disjoint sets?", are_disjoint)

# Task 5
joined_A_B = A.union(B)
joined_B_A = B.union(A)
print("Join A with B:", joined_A_B)
print("Join B with A:", joined_B_A)

# Task 6
symmetric_difference = A.symmetric_difference(B)
print("Symmetric Difference between A and B:", symmetric_difference)

# Task 7
del A, B
print("Sets A and B deleted.")

#level 3

# Given ages list
ages_list = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Task 1
ages_set = set(ages_list)
length_list = len(ages_list)
length_set = len(ages_set)

print("Length of Ages List:", length_list)
print("Length of Ages Set:", length_set)
print("Which one is bigger? ", "List" if length_list > length_set else "Set")

# Task 2
# Explanation of data types
string_explanation = "String is a sequence of characters, represented by text. It is immutable."
list_explanation = "List is an ordered collection of elements. It is mutable and can contain elements of different data types."
tuple_explanation = "Tuple is an ordered collection of elements. It is immutable, meaning its elements cannot be changed once assigned."
set_explanation = "Set is an unordered collection of unique elements. It does not allow duplicate values."

print("\nExplanation of Data Types:")
print("String:", string_explanation)
print("List:", list_explanation)
print("Tuple:", tuple_explanation)
print("Set:", set_explanation)

# Task 3
sentence = "I am a teacher and I love to inspire and teach people."
unique_words = set(sentence.split())
num_unique_words = len(unique_words)

print("\nNumber of Unique Words in the Sentence:", num_unique_words)
print("Unique Words:", unique_words)
