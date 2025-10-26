let questions = [];       // Array to store all questions
let usedQuestions = [];   // To track shown questions

// 1️⃣ Load questions from JSON
fetch('questions.json')
  .then(response => response.json())
  .then(data => {
    questions = data;
    showRandomQuestion();  // Show a question when page loads
  })
  .catch(error => console.error("Error loading questions:", error));

// 2️⃣ Show random question function
function showRandomQuestion() {
  if (questions.length === 0) return;

  // Reset usedQuestions if all questions were shown
  if (usedQuestions.length === questions.length) {
    usedQuestions = [];
  }

  let randomIndex;
  do {
    randomIndex = Math.floor(Math.random() * questions.length);
  } while (usedQuestions.includes(randomIndex));

  usedQuestions.push(randomIndex);

  document.getElementById('questionText').textContent = questions[randomIndex];
}

// 3️⃣ Button click
document.getElementById('nextBtn').addEventListener('click', showRandomQuestion);
