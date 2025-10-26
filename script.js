let questions = [];       // Array to store all questions
let usedQuestions = [];   // To track shown questions

// Load questions from JSON
fetch('questions.json')
  .then(response => response.json())
  .then(data => {
    questions = data;
    populateFilters();   // Fill dropdowns
    showRandomQuestion(); // Show first question
  })
  .catch(error => console.error("Error loading questions:", error));

// Show random question function
function showRandomQuestion() {
  if (questions.length === 0) return;

  const selectedGenre = document.getElementById('genreFilter').value;
  const selectedSubgenre = document.getElementById('subgenreFilter').value;

  // Filter questions if filters exist
  let filtered = questions;
  if (selectedGenre) filtered = filtered.filter(q => q.genre === selectedGenre);
  if (selectedSubgenre) filtered = filtered.filter(q => q.subgenre === selectedSubgenre);

  if (filtered.length === 0) {
    document.getElementById('questionText').textContent = "No questions found.";
    return;
  }

  // Reset usedQuestions if all filtered questions were shown
  if (usedQuestions.length === filtered.length) usedQuestions = [];

  let randomIndex;
  do {
    randomIndex = Math.floor(Math.random() * filtered.length);
  } while (usedQuestions.includes(randomIndex));

  usedQuestions.push(randomIndex);

  document.getElementById('questionText').textContent = filtered[randomIndex].question;
}

// Button click
document.getElementById('nextBtn').addEventListener('click', showRandomQuestion);

// Populate genre/subgenre filters
function populateFilters() {
  const genreSet = [...new Set(questions.map(q => q.genre))].sort();
  const subgenreSet = [...new Set(questions.map(q => q.subgenre))].sort();

  const genreSelect = document.getElementById('genreFilter');
  const subgenreSelect = document.getElementById('subgenreFilter');

  // Clear old options except first
  genreSelect.length = 1;
  subgenreSelect.length = 1;

  // Populate genres
  genreSet.forEach(g => {
    const option = document.createElement('option');
    option.value = g;
    option.textContent = g;
    genreSelect.appendChild(option);
  });

  // Populate subgenres
  subgenreSet.forEach(sg => {
    const option = document.createElement('option');
    option.value = sg;
    option.textContent = sg;
    subgenreSelect.appendChild(option);
  });

  // Reset questions when filters change
  genreSelect.addEventListener('change', () => { usedQuestions = []; showRandomQuestion(); });
  subgenreSelect.addEventListener('change', () => { usedQuestions = []; showRandomQuestion(); });
}
