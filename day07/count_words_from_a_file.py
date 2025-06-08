import sys
from collections import Counter

filepath = sys.argv[1]

with open(filepath, 'r') as file:
    plain_text = file.read().lower()
    words_sep = plain_text.split()
    sort_words = sorted(words_sep)
    word_counts = Counter(sort_words)


for word, counts in word_counts.items():
    print(f"{word}: {counts}")