import random
import os

# Function to read the words from the file and store them in a list
def read_words_from_file(filename):
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' does not exist.")
        return []
    with open(filename, 'r') as file:
        words = file.readlines()
    return [word.strip().upper() for word in words if word.strip()]

# Function to choose a random word from the list
def choose_random_word(word_list):
    return random.choice(word_list)

# Function to display the current clue with correctly guessed letters
def display_clue(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

# Function to play one round of Hangman
def play_hangman(word_list):
    word = choose_random_word(word_list)
    guessed_letters = set()
    chances_left = 6

    print("\n>>> Welcome to Hangman!")
    print(display_clue(word, guessed_letters))

    while True:
        guess = input("\n>>> Guess your letter: ").upper()

        # Check for invalid input
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid letter.")
            continue

        # Check for repeated guesses
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try another letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("\nCorrect!")
        else:
            chances_left -= 1
            print(f"\nIncorrect! You left with {chances_left} chances to guess.")

        print(display_clue(word, guessed_letters))

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print(f"\n🎉 Congratulations! You guessed the word '{word}' correctly.")
            break

        # Check lose condition
        if chances_left == 0:
            print(f"\n💀 Sorry, you lost! The word was '{word}'.")
            break

# Function to start and manage the game loop
def start_game():
    filename = 'words.txt'
    word_list = read_words_from_file(filename)
    if not word_list:
        return

    while True:
        play_hangman(word_list)
        again = input("\nDo you want to play again? (y/n): ").lower()
        if again != 'y':
            print("Goodbye! Thanks for playing Hangman!")
            break

# Main function
if __name__ == "__main__":
    start_game()
