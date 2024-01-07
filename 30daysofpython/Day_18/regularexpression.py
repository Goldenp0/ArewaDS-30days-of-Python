import re
from collections import Counter

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

# Clean the paragraph by removing non-alphabetic characters and converting to lowercase
cleaned_paragraph = re.sub(r'[^a-zA-Z\s]', '', paragraph).lower()

# Tokenize the cleaned paragraph into words
words = cleaned_paragraph.split()

# Use Counter to count the occurrences of each word
word_counts = Counter(words)

# Find the most common word
most_common_word = word_counts.most_common(1)

print("The most frequent word is:", most_common_word)

points = ['-12', '-4', '-3', '-1', '0', '4', '8']

# Convert the points to integers and sort them
sorted_points = sorted(map(int, points))

# Calculate the distance between the two furthest particles
distance = sorted_points[-1] - sorted_points[0]

print("The distance between the two furthest particles is:", distance)
