import os
import re
from collections import Counter

def count_lines_and_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        lines = text.split('\n')
        words = re.findall(r'\b\w+\b', text)
    return len(lines), len(words)

# Exercise 1
obama_lines, obama_words = count_lines_and_words('./data/obama_speech.txt')
print(f"Obama's speech has {obama_lines} lines and {obama_words} words.")

michelle_lines, michelle_words = count_lines_and_words('./data/michelle_obama_speech.txt')
print(f"Michelle's speech has {michelle_lines} lines and {michelle_words} words.")

donald_lines, donald_words = count_lines_and_words('./data/donald_speech.txt')
print(f"Donald's speech has {donald_lines} lines and {donald_words} words.")

melania_lines, melania_words = count_lines_and_words('./data/melania_trump_speech.txt')
print(f"Melania's speech has {melania_lines} lines and {melania_words} words.")

# Exercise 2
import json

def most_spoken_languages(filename, n):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        languages = [country['languages'] for country in data]
        flat_languages = [lang.strip() for sublist in languages for lang in sublist]
        language_counts = Counter(flat_languages)
        return language_counts.most_common(n)

print(most_spoken_languages(filename='./data/countries_data.json', n=10))
print(most_spoken_languages(filename='./data/countries_data.json', n=3))

# Exercise 3
def most_populated_countries(filename, n):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        sorted_countries = sorted(data, key=lambda x: x['population'], reverse=True)
        return sorted_countries[:n]

print(most_populated_countries(filename='./data/countries_data.json', n=10))
print(most_populated_countries(filename='./data/countries_data.json', n=3))

# Exercise 4
def extract_emails(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        emails = re.findall(r'\S+@\S+', text)
    return emails

email_addresses = extract_emails('./data/email_exchange_big.txt')
print(email_addresses)

# Exercise 5
def find_most_common_words(file_path, n):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        words = re.findall(r'\b\w+\b', text.lower())
        word_counts = Counter(words)
        return word_counts.most_common(n)

print(find_most_common_words('./data/english_text.txt', 10))

# Exercise 6
def find_most_frequent_words(speech_file, n):
    with open(speech_file, 'r', encoding='utf-8') as file:
        text = file.read()
        words = re.findall(r'\b\w+\b', text.lower())
        word_counts = Counter(words)
        return word_counts.most_common(n)

obama_frequent_words = find_most_frequent_words('./data/obama_speech.txt', 10)
michelle_frequent_words = find_most_frequent_words('./data/michelle_obama_speech.txt', 10)
donald_frequent_words = find_most_frequent_words('./data/donald_speech.txt', 10)
melania_frequent_words = find_most_frequent_words('./data/melania_trump_speech.txt', 10)

print("Obama's most frequent words:", obama_frequent_words)
print("Michelle's most frequent words:", michelle_frequent_words)
print("Donald's most frequent words:", donald_frequent_words)
print("Melania's most frequent words:", melania_frequent_words)

# Exercise 7
def clean_text(text):
    stop_words = set(open('./data/stop_words.txt', 'r', encoding='utf-8').read().split())
    words = re.findall(r'\b\w+\b', text.lower())
    cleaned_words = [word for word in words if word not in stop_words]
    return ' '.join(cleaned_words)

def remove_support_words(text):
    stop_words = set(open('./data/stop_words.txt', 'r', encoding='utf-8').read().split())
    words = re.findall(r'\b\w+\b', text.lower())
    cleaned_words = [word for word in words if word not in stop_words]
    return cleaned_words

def check_text_similarity(text1, text2):
    cleaned_text1 = clean_text(text1)
    cleaned_text2 = clean_text(text2)
    words1 = remove_support_words(cleaned_text1)
    words2 = remove_support_words(cleaned_text2)
    
    common_words = set(words1) & set(words2)
    similarity = len(common_words) / max(len(set(words1)), len(set(words2)))
    
    return similarity

michelle_text = open('./data/michelle_obama_speech.txt', 'r', encoding='utf-8').read()
melania_text = open('./data/melania_trump_speech.txt', 'r', encoding='utf-8').read()

similarity_score = check_text_similarity(michelle_text)