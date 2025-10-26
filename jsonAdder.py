import json
import os

# --- File with questions ---
input_file = "inputquestion.txt"  # each line is one question

# --- Hardcoded genre and subgenre ---
genre = "controversial"
subgenre = "Political"

# Load existing questions
if os.path.exists("questions.json"):
    with open("questions.json", "r", encoding="utf-8") as f:
        all_questions = json.load(f)
        # Convert old JSON format (list of strings) to new format
        if all_questions and isinstance(all_questions[0], str):
            all_questions = [
                {"question": q, "genre": "unknown", "subgenre": "unknown"} for q in all_questions
            ]
else:
    all_questions = []

# Helper to check duplicates
def question_exists(q_text):
    return any(q.get("question") == q_text for q in all_questions)

# Read questions from text file
with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        question_text = line.strip()
        if question_text and not question_exists(question_text):
            all_questions.append({
                "question": question_text,
                "genre": genre,
                "subgenre": subgenre
            })

# Save to JSON
with open("questions.json", "w", encoding="utf-8") as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=2)

print(f"Total questions saved: {len(all_questions)}")
