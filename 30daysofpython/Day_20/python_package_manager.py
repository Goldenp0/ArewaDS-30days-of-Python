import requests
from bs4 import BeautifulSoup
from collections import Counter

# Fetching the content from the URL
url = 'http://www.gutenberg.org/files/1112/1112.txt'
response = requests.get(url)
html_content = response.content

# Parsing the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
text = soup.get_text()

# Performing word frequency analysis
words = [word.lower() for word in text.split()]
word_counts = Counter(words)
most_frequent_words = word_counts.most_common(10)

print("10 Most Frequent Words:")
for word, count in most_frequent_words:
    print(f"{word}: {count}")