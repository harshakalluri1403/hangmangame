import random

# List of words for the game
word_list = ["python", "hangman", "programming", "challenge"]

def select_random_word():
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

def hangman():
    word_to_guess = select_random_word()
    guessed_letters = []
    max_attempts = 6

    while max_attempts > 0:
        print(display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word_to_guess:
            guessed_letters.append(guess)
            if set(guessed_letters) == set(word_to_guess):
                print(f"Congratulations! You guessed the word: {word_to_guess}")
                break
        else:
            max_attempts -= 1
            print(f"Wrong guess! You have {max_attempts} attempts left.")

    else:
        print(f"Sorry, you ran out of attempts. The word was: {word_to_guess}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        hangman()

if __name__ == "__main__":
    hangman()
