# Hangman Game in Python
### Description
This is a simple Hangman game implemented in Python. The goal of the game is for the player to guess the secret word, one letter at a time, within a certain number of attempts. If the player guesses the word correctly before running out of attempts, they win. Otherwise, they lose and the word is revealed.

### Features
1. Random word selection from a predefined word list.
2. Player guesses one letter at a time.
3. Display of the current state of the word with correctly guessed letters.
4. Display of incorrect guesses and remaining attempts.
5. Win or lose notification at the end of the game.

### Prerequisites
Python 3.x installed on your machine.

### How to Run the Game
1. Clone the Repository
```
git clone https://github.com/yourusername/hangmangame
```
2. Navigate to the Game Directory
```
cd hangmangame
```
3. Run the script
```
python hangman.py
```

### How to Play
1. A word is randomly selected, and the number of letters in the word is shown as underscores (_).
2. The player guesses a letter:
If the letter is in the word, all occurrences of the letter are revealed in the correct positions.
If the letter is not in the word, the number of remaining attempts decreases.
3. The player continues guessing letters until:
They correctly guess the word (win).
They run out of attempts (lose).
4. At the end of the game, the player can choose to play again or exit.

### Sample Gameplay
```
Copy code
Welcome to Hangman!
You have 6 attempts remaining.
_ _ _ _ _ _

Guess a letter: e
Incorrect! You have 5 attempts remaining.
_ _ _ _ _ _

Guess a letter: o
Correct!
_ o _ _ _ _
...
```
