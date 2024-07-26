import random

def get_random_word(word_list):
    return random.choice(word_list).upper()

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word_list = ['PYTHON', 'JAVASCRIPT', 'DEVELOPER', 'HANGMAN', 'PROGRAMMING']
    word_to_guess = get_random_word(word_list)
    guessed_letters = set()
    incorrect_guesses = set()
    max_attempts = 6

    print("Welcome to guessgame!")

    while len(incorrect_guesses) < max_attempts and not set(word_to_guess).issubset(guessed_letters):
        print(f"\nWord to guess: {display_word(word_to_guess, guessed_letters)}")
        print(f"Incorrect guesses: {' '.join(incorrect_guesses)}")
        print(f"Attempts remaining: {max_attempts - len(incorrect_guesses)}")

        guess = input("Guess a letter: ").upper()

        if guess in guessed_letters or guess in incorrect_guesses:
            print("You've already guessed that letter. Try again.")
        elif guess in word_to_guess:
            guessed_letters.add(guess)
            print(f"Good job! {guess} is in the word.")
        else:
            incorrect_guesses.add(guess)
            print(f"Sorry, {guess} is not in the word.")

    if set(word_to_guess).issubset(guessed_letters):
        print(f"\nCongratulations! You've guessed the word: {word_to_guess}")
    else:
        print(f"\nGame Over! The word was: {word_to_guess}")

if __name__ == "__main__":
    hangman()
