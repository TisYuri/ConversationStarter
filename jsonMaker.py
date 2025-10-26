import json

# 1. Read the TXT file
with open("232_Questions.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# 2. Remove empty lines and strip whitespace
questions = [line.strip() for line in lines if line.strip()]

# 3. Convert to JSON
with open("questions.json", "w", encoding="utf-8") as json_file:
    json.dump(questions, json_file, ensure_ascii=False, indent=2)

print("questions.json created successfully!")
