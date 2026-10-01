<div align="center">

# Hangman 🎯

### A classic word-guessing game in a single Python file — no dependencies, runs in the terminal

![Python](https://img.shields.io/badge/python-3.x-3776AB?logo=python&logoColor=white)
![Dependencies](https://img.shields.io/badge/dependencies-none-2ea44f)
![Type](https://img.shields.io/badge/project-beginner%20friendly-6f42c1)

</div>

---

Guess the hidden word one letter at a time. You get **6 wrong guesses** before
the game is over. A small, readable example of loops, conditionals and string
handling in plain Python — a nice first project to read or tinker with.

## Play

```bash
git clone https://github.com/harshakalluri1403/hangmangame.git
cd hangmangame
python hangman.py
```

No installs needed — only the Python standard library.

## How it plays

```
_ _ _ _ _ _
Guess a letter: e
Wrong guess! You have 5 attempts left.
_ _ _ _ _ _
Guess a letter: o
_ o _ _ _ _
...
```

- A random word is chosen and shown as underscores.
- Enter one letter per turn. A correct letter is revealed in every position it
  appears; a wrong one costs an attempt.
- Guess the whole word before running out of attempts to **win**. Run out and
  the word is revealed.
- Choose to play again when a round ends.

## Under the hood

All the logic lives in [`hangman.py`](hangman.py):

- `select_random_word()` — picks a word from the built-in list
- `display_word()` — renders the masked word from the letters guessed so far
- `hangman()` — the main game loop (input validation, scoring, replay)

Want to make it yours? Extend `word_list` in [`hangman.py`](hangman.py), or add
difficulty levels, categories, or a score counter.
