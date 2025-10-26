import json
from collections import Counter

with open('questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)  # data is already a list

genres = Counter(q['genre'] for q in questions)
subgenres = Counter(q['subgenre'] for q in questions)

print("Genres:", genres)
print("Subgenres:", subgenres)
