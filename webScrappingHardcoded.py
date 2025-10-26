import requests
from bs4 import BeautifulSoup
import json
import os

# --- Change this URL each time ---
url = "https://conversationstartersworld.com/would-you-rather-questions/"

# --- Hardcoded genre and subgenre ---
genre = "Would you rather"      # change as needed
subgenre = "Would you rather"   # change as needed

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
    return any(
        (isinstance(q, dict) and q.get("question") == q_text) or
        (isinstance(q, str) and q == q_text)
        for q in all_questions
    )

# Scrape the webpage
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Grab all questions from <li> inside any <ul> or <ol>
for list_tag in soup.find_all(["ul", "ol"]):
    for li in list_tag.find_all("li"):
        question_text = li.get_text(strip=True)
        # Only add if it looks like a real question (ends with ?)
        if question_text.endswith("?") and not question_exists(question_text):
            all_questions.append({
                "question": question_text,
                "genre": genre,
                "subgenre": subgenre
            })

# Save to JSON
with open("questions.json", "w", encoding="utf-8") as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=2)

print(f"Total questions saved: {len(all_questions)}")
