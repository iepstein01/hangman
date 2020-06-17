# Hangman Game in Python

import random

lines = []

with open("./assets/words.txt") as fp:
    lines = fp.read().splitlines()
    fp.close()

word = lines[random.randrange(1, len(lines) + 1)]

letters = []

for i in range(0, len(word)):
    letters.append(word[i:i+1])

print(letters)