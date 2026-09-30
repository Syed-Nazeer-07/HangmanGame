# 🎮 Python Hangman: Enhanced Edition

A feature-rich console-based Hangman game built with Python. This project was developed as part of the **CodeAlpha Python Programming Internship (Task 1)** and expands upon the traditional Hangman game by adding hints, ASCII art, score tracking, and persistent high scores.

---

## 📌 Features

### 🎲 Random Word Selection

* Randomly selects a word from a large collection of categories:

  * Technology
  * Animals
  * Sports
  * Countries
  * Food & Drinks
  * Science
  * Music
  * Geography
  * Professions
  * Everyday Objects

### 🎨 ASCII Hangman Graphics

* Visual Hangman stages displayed after each incorrect guess.
* Provides a more engaging gameplay experience.

### 💡 Hint System

* One hint is available per round.
* Reveals a random hidden letter from the secret word.

### 📊 Round Statistics

Displays:

* Total guesses made
* Number of incorrect guesses
* Win/Loss result

### 🏆 High Score Tracking

* Tracks the highest consecutive win streak.
* Saves high scores locally using a text file.
* Automatically loads previous records when the game starts.

### 🔄 Replay Option

* Play multiple rounds without restarting the program.
* Maintains your current win streak across rounds.

### ✅ Input Validation

* Prevents invalid inputs.
* Detects duplicate guesses.
* Accepts both uppercase and lowercase letters.

---

## 🛠 Technologies Used

* Python 3
* Random Module
* File Handling
* Lists
* Functions
* Loops
* Conditional Statements
* Exception Handling

---

## 📂 Project Structure

```text
Hangman-Game/
│
├── main.py
├── highscore.txt
└── README.md
```

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Hangman-Game.git
```

### 2. Navigate to the Project Folder

```bash
cd Hangman-Game
```

### 3. Run the Program

```bash
python main.py
```

---

## 🎯 Gameplay Rules

1. A random word is selected.
2. The player guesses one letter at a time.
3. Each incorrect guess adds a part to the Hangman drawing.
4. The player has a maximum of 6 incorrect attempts.
5. One hint can be used per game.
6. Guess all letters before running out of attempts to win.

---

## 📸 Sample Gameplay

```text
Word: _ _ _ _ _ _
Remaining attempts: 6

Guess a letter: a

Good job! 'a' is in the word.

Word: _ a _ _ _ _
```

---

## 🎓 Internship Task

**CodeAlpha Python Programming Internship**

**Task 1: Hangman Game**

Goal:
Create a text-based Hangman game where the player guesses a hidden word one letter at a time using Python fundamentals such as loops, conditionals, lists, strings, and the random module.

---

## 🌟 Future Improvements

* Difficulty levels (Easy, Medium, Hard)
* Category selection by player
* Timer-based gameplay
* Leaderboard system
* Multiplayer mode
* GUI version using Tkinter or PyQt

---

## 👨‍💻 Author

Developed by **[Your Name]**

GitHub: https://github.com/your-username

---

## 📜 License

This project is open-source and available under the MIT License.
