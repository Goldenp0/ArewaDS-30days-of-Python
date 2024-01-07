# Task 1
empty_tuple = ()

# Task 2
sisters = ('Alice', 'Bob', 'Charlie')  # Replace with actual names
brothers = ('David', 'Eva', 'Frank')   # Replace with actual names

# Task 3
siblings = brothers + sisters

# Task 4
num_siblings = len(siblings)

print("Siblings:", siblings)
print("Number of Siblings:", num_siblings)

# Task 5
father_and_mother = ('John', 'Jane')  # Replace with actual names
family_members = siblings + father_and_mother

print("Family Members:", family_members)

# exercise two

# Task 1
siblings, parents = family_members[:num_siblings], family_members[num_siblings:]

# Task 2
fruits = ('Apple', 'Banana', 'Orange')
vegetables = ('Carrot', 'Broccoli', 'Spinach')
animal_products = ('Chicken', 'Beef', 'Milk')

# Task 3
food_stuff_tp = fruits + vegetables + animal_products

# Task 4
food_stuff_lt = list(food_stuff_tp)

# Task 5
middle_items_tp = food_stuff_tp[len(food_stuff_tp)//2]
middle_items_lt = food_stuff_lt[len(food_stuff_lt)//2]

print("Middle Items (Tuple):", middle_items_tp)
print("Middle Items (List):", middle_items_lt)

# Task 6
first_three_last_three_lt = food_stuff_lt[:3] + food_stuff_lt[-3:]

print("First Three and Last Three Items (List):", first_three_last_three_lt)

# Task 7
del food_stuff_tp

# Task 8
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

# Check if 'Estonia' is a nordic country
is_estonia_nordic = 'Estonia' in nordic_countries
print("Is Estonia a Nordic country?", is_estonia_nordic)

# Check if 'Iceland' is a nordic country
is_iceland_nordic = 'Iceland' in nordic_countries
print("Is Iceland a Nordic country?", is_iceland_nordic)
