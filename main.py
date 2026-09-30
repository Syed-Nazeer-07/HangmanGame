import random
import os

# Hangman ASCII art stages corresponding to incorrect attempts left (0 to 6)
HANGMAN_PICS = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\  |
      / \  |
           |
    =========
    """
]

def load_high_score():
    """Reads the high score from a local text file."""
    try:
        with open("highscore.txt", "r") as file:
            return int(file.read().strip())
    except (FileNotFoundError, ValueError):
        return 0

def save_high_score(score):
    """Saves the highest win streak to a text file."""
    try:
        with open("highscore.txt", "w") as file:
            file.write(str(score))
    except IOError:
        print("\n[Warning] Could not save high score to file.")

def choose_word():
    """Returns a random word from a large categorized list."""
    words = [
        # Technology
        "algorithm", "database", "hardware", "python", "internet",
        "software", "keyboard", "monitor", "processor", "bluetooth",
        "firmware", "compiler", "debugger", "encryption", "bandwidth",
        "cybersecurity", "javascript", "framework", "terminal", "repository",
        # Animals
        "elephant", "kangaroo", "penguin", "dolphin", "cheetah",
        "giraffe", "platypus", "chameleon", "butterfly", "crocodile",
        "flamingo", "wolverine", "porcupine", "anaconda", "jellyfish",
        "armadillo", "chinchilla", "orangutan", "dragonfly", "hippopotamus",
        # Sports
        "basketball", "gymnastics", "swimming", "volleyball", "tennis",
        "badminton", "snowboard", "wrestling", "archery", "cricket",
        "lacrosse", "marathon", "fencing", "surfing", "handball",
        "bobsled", "triathlon", "waterpolo", "climbing", "cycling",
        # Countries
        "switzerland", "argentina", "australia", "canada", "japan",
        "portugal", "thailand", "colombia", "ethiopia", "indonesia",
        "philippines", "madagascar", "singapore", "venezuela", "guatemala",
        "mozambique", "kazakhstan", "cambodia", "mongolia", "nicaragua",
        # Food & Drinks
        "chocolate", "pancake", "spaghetti", "avocado", "pineapple",
        "croissant", "hamburger", "cinnamon", "broccoli", "blueberry",
        "watermelon", "mushroom", "sandwich", "espresso", "lemonade",
        "milkshake", "guacamole", "marmalade", "raspberry", "pistachio",
        # Science
        "molecule", "gravity", "asteroid", "nucleus", "volcano",
        "tsunami", "photosynthesis", "chromosome", "ecosystem", "telescope",
        "magnetism", "radiation", "atmosphere", "hypothesis", "specimen",
        "experiment", "chemistry", "evolution", "satellite", "laboratory",
        # Music
        "saxophone", "orchestra", "accordion", "harmonica", "symphony",
        "drumstick", "microphone", "acoustic", "classical", "melody",
        "trombone", "xylophone", "conductor", "amplifier", "baritone",
        # Geography
        "mountain", "waterfall", "peninsula", "continent", "archipelago",
        "glacier", "savannah", "plateau", "canyon", "rainforest",
        "coastline", "limestone", "tundra", "estuary", "fjord",
        # Professions
        "architect", "detective", "scientist", "astronaut", "librarian",
        "carpenter", "plumber", "journalist", "pharmacist", "electrician",
        "firefighter", "professor", "engineer", "diplomat", "surgeon",
        # Everyday Objects
        "umbrella", "backpack", "scissors", "calendar", "envelope",
        "blanket", "lantern", "compass", "staircase", "chandelier",
        "binoculars", "trampoline", "wardrobe", "doorbell", "bookshelf",
    ]
    return random.choice(words)

def display_word(secret_word, guessed_letters):
    """Builds and returns the display string for the hidden word."""
    display = [letter if letter in guessed_letters else '_' for letter in secret_word]
    return " ".join(display)

def play_game():
    """Handles a single round of Hangman. Returns True if the player won, False otherwise."""
    secret_word = choose_word()
    guessed_letters = []  # List to store all guessed letters in order
    max_attempts = 6
    wrong_attempts = 0
    total_guesses = 0
    hint_available = True
    
    print("\n" + "="*50)
    print("New Game Started!")
    print(f"The word has {len(secret_word)} letters.")
    print("="*50)

    while wrong_attempts < max_attempts:
        # Display current game state
        print(HANGMAN_PICS[wrong_attempts])
        print("Word: " + display_word(secret_word, guessed_letters))
        print(f"Remaining attempts: {max_attempts - wrong_attempts}")
        
        if guessed_letters:
            print("Guessed letters: " + ", ".join(guessed_letters))
            
        # Get user input
        prompt = "\nGuess a letter" + (" (or type 'hint'): " if hint_available else ": ")
        guess = input(prompt).lower().strip()
        
        if guess == 'hint':
            if hint_available:
                # Find letters that haven't been guessed yet
                missing_letters = [char for char in secret_word if char not in guessed_letters]
                if missing_letters:
                    hint_letter = random.choice(missing_letters)
                    guessed_letters.append(hint_letter)
                    print(f"\n[HINT USED] Revealed letter: '{hint_letter}'")
                    hint_available = False
                    total_guesses += 1
                
                # Check if the hint completed the word
                if all(letter in guessed_letters for letter in secret_word):
                    break # Break out to win condition
                continue
            else:
                print("\n*** You have already used your hint for this round! ***")
                continue

        if len(guess) != 1 or not guess.isalpha():
            print("\n*** Invalid input. Please enter a single letter. ***")
            continue
            
        if guess in guessed_letters:
            print(f"\n*** You have already guessed '{guess}'. Try a different letter. ***")
            continue
            
        # Process valid guess
        guessed_letters.append(guess)
        total_guesses += 1
        
        if guess in secret_word:
            print(f"\nGood job! '{guess}' is in the word.")
            
            # Check for win condition
            if all(letter in guessed_letters for letter in secret_word):
                break # Player won, exit loop
        else:
            print(f"\nSorry, '{guess}' is not in the word.")
            wrong_attempts += 1
            
    # Game over logic
    won = wrong_attempts < max_attempts
    
    print("\n" + "="*50)
    print(HANGMAN_PICS[wrong_attempts])
    
    if won:
        print(f"Congratulations! You guessed the word: '{secret_word}'")
        print("YOU WIN! \o/")
    else:
        print(f"Out of attempts! YOU LOSE! :(")
        print(f"The correct word was: '{secret_word}'")
        
    print("\n--- Round Statistics ---")
    print(f"Total guesses made: {total_guesses}")
    print(f"Incorrect guesses: {wrong_attempts}")
    print("="*50)
    
    return won

def main():
    print("Welcome to Python Hangman: Enhanced Edition!")
    high_score = load_high_score()
    print(f"Current High Score (Win Streak): {high_score}")
    
    current_streak = 0
    playing = True
    
    while playing:
        # Play a round
        won = play_game()
        
        # Update streak
        if won:
            current_streak += 1
            print(f"\nCurrent Win Streak: {current_streak}")
            if current_streak > high_score:
                print("*** NEW HIGH SCORE! ***")
                high_score = current_streak
                save_high_score(high_score)
        else:
            print(f"\nYour streak ended at {current_streak} wins.")
            current_streak = 0
            
        # Ask to play again
        while True:
            play_again = input("\nDo you want to play another round? (yes/no): ").lower().strip()
            if play_again in ['yes', 'y']:
                break
            elif play_again in ['no', 'n']:
                print("\nThanks for playing! Final High Score: ", high_score)
                playing = False
                break
            else:
                print("Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
