# hangman.py
import random

HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========="""
]

WORD_LIST = [
    "python", "computer", "hangman", "program", "developer",
    "algorithm", "function", "variable", "internet", "keyboard"
]

def choose_word(word_list):
    """Randomly pick a word from the list."""
    return random.choice(word_list).lower()

def display_state(missed_letters, correct_letters, secret_word):
    """Print current hangman picture, missed letters and the discovered letters of secret word."""
    print(HANGMAN_PICS[len(missed_letters)])
    print()
    print("Missed letters:", " ".join(missed_letters) if missed_letters else "None")
    print()

    # show blanks and found letters
    blanks = ["_" if ch not in correct_letters else ch for ch in secret_word]
    print("Word: ", " ".join(blanks))
    print()

def get_guess(already_guessed):
    """Ask player for a single letter guess and validate input."""
    while True:
        guess = input("Guess a letter: ").lower().strip()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif not guess.isalpha():
            print("Please enter a LETTER (a-z).")
        elif guess in already_guessed:
            print("You already guessed that letter. Try a different one.")
        else:
            return guess

def play_again():
    """Ask user if they want to play again."""
    return input("Play again? (y/n): ").lower().startswith("y")

def main():
    print("Welcome to Hangman!")
    while True:
        secret_word = choose_word(WORD_LIST)
        missed_letters = []
        correct_letters = []
        game_over = False

        while not game_over:
            display_state(missed_letters, correct_letters, secret_word)

            # get player's guess
            guess = get_guess(missed_letters + correct_letters)

            if guess in secret_word:
                correct_letters.append(guess)

                # Check if all letters found
                found_all = all(ch in correct_letters for ch in secret_word)
                if found_all:
                    print()
                    print("Yes! The word is:", secret_word)
                    print("You have WON! 🎉")
                    game_over = True
            else:
                missed_letters.append(guess)

                # Check if reached max mistakes
                if len(missed_letters) == len(HANGMAN_PICS) - 1:
                    display_state(missed_letters, correct_letters, secret_word)
                    print("You've run out of guesses!")
                    print("The word was '{}'.".format(secret_word))
                    game_over = True

        if not play_again():
            print("Thanks for playing. Goodbye!")
            break

if __name__ == "__main__":
    main()
