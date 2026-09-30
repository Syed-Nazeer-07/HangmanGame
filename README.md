# 🎮 Python Hangman: Enhanced Edition

A feature-rich console-based Hangman game built with Python. This project was developed as part of the **CodeAlpha Python Programming Internship – Task 1** and expands the traditional Hangman game with ASCII graphics, a hint system, win-streak tracking, and persistent high scores.

---

## 📖 Overview

Hangman is a classic word-guessing game where players attempt to uncover a hidden word one letter at a time. This implementation enhances the gameplay experience with:

- A large collection of words from multiple categories
- Visual Hangman ASCII art
- One-time hint system
- High score persistence
- Win streak tracking
- Input validation and error handling
- Round statistics and replay functionality

---

## ✨ Features

### 🎲 Random Word Selection
The game randomly selects a word from a diverse collection of categories:

- Technology
- Animals
- Sports
- Countries
- Food & Drinks
- Science
- Music
- Geography
- Professions
- Everyday Objects

### 🎨 ASCII Hangman Graphics
A visual Hangman figure is displayed and updated after each incorrect guess.

### 💡 Hint System
- One hint per round
- Reveals a random hidden letter
- Helps players when they're stuck

### 🏆 High Score Tracking
- Tracks highest consecutive win streak
- Saves high scores locally in `highscore.txt`
- Automatically loads previous records when the game starts

### 📊 Round Statistics
At the end of every round, the game displays:

- Total guesses made
- Incorrect guesses
- Win/Loss result

### 🔄 Replay Functionality
Play unlimited rounds without restarting the program.

### ✅ Input Validation
The game prevents:

- Empty inputs
- Multiple-character inputs
- Non-alphabetic characters
- Duplicate guesses

---

## 🛠 Technologies Used

- Python 3
- Random Module
- File Handling
- Exception Handling
- Lists
- Strings
- Functions
- Loops
- Conditional Statements

---

## 📂 Project Structure

```text
HangmanGame/
│
├── main.py
├── highscore.txt
└── README.md
```

---

## 🚀 Installation & Usage

### Clone the Repository

```bash
git clone https://github.com/Syed-Nazeer-07/HangmanGame.git
```

### Navigate to the Project Folder

```bash
cd HangmanGame
```

### Run the Program

```bash
python main.py
```

---

## 🎯 How to Play

1. Start the game.
2. A random word will be selected.
3. Guess one letter at a time.
4. Correct guesses reveal letters in the word.
5. Incorrect guesses reduce your remaining attempts.
6. Use the **hint** command once per round if needed.
7. Guess the entire word before all attempts are used.
8. Try to build the highest win streak possible.

---

## 📸 Sample Gameplay

```text
==================================================
New Game Started!
The word has 8 letters.
==================================================

Word: _ _ _ _ _ _ _ _
Remaining attempts: 6

Guess a letter: a

Good job! 'a' is in the word.

Word: _ a _ _ _ _ _ _
Remaining attempts: 6
```

---

## 🏅 Scoring System

### Win Streak
- Each successful round increases your streak by 1.
- Losing a round resets your streak.
- The highest streak achieved is stored permanently.

### High Score File
The game automatically creates and updates:

```text
highscore.txt
```

This file stores your best win streak between sessions.

---

## 🎓 Internship Task Information

### CodeAlpha Python Programming Internship

**Task 1: Hangman Game**

**Objective:**
Create a text-based Hangman game where the player guesses a word one letter at a time using Python fundamentals such as:

- Random module
- Loops
- Conditional statements
- Strings
- Lists
- Functions

This project fulfills and extends the internship requirements by adding additional gameplay features and persistent score tracking.

---

## 🌟 Future Enhancements

Potential improvements for future versions:

- Difficulty levels
- Category selection menu
- Leaderboard system
- Multiplayer mode
- Timer-based gameplay
- GUI version using Tkinter
- Sound effects
- Online score storage

---

## 👨‍💻 Author

**Syed Nazeer**

- GitHub Profile: https://github.com/Syed-Nazeer-07
- Repository: https://github.com/Syed-Nazeer-07/HangmanGame

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a Pull Request

---

## 📜 License

This project is open-source and available under the MIT License.

---

⭐ If you enjoyed this project, consider giving the repository a star on GitHub!
