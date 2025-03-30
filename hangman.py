"""hangman game with python !"""
import random

words = [
    "Python",
    "Java",
    "JavaScript",
    "MySql",
    "C",
    "C#",
    "C++",
    "React",
    "Angular",
    "Django",
    "Flask",
    "Ruby",
    "PHP",
    "Go",
    "Kotlin"
]

# randomly select a word from the list
chosen_word = random.choice(words) 
word_display = ["_" for _ in chosen_word] # create a list of underscores with the same lenght as the chosen word
attempts = 6

print(""""
    _______________________
   |  Welcome to Hangman!  |
    _______________________ 
""")

# Game loop
while attempts > 0 and "_" in word_display:
    print("\nWord:"," ".join(word_display))
    guess = input("Guess a letter: ").lower()

    if guess in chosen_word.lower():
        for index , letter in enumerate(chosen_word.lower()):
            if letter == guess:
                word_display[index] = guess
    else:
        print("\nWrong guess!")
        attempts -= 1
        print(f"You have {attempts} attempts left.")

# Game over condition
if attempts == 0:
    print(f"\nGame over! The word was '{chosen_word}'\n")

# Game conclusion
if "_" not in word_display:
    print("\nCongratulations! You've guessed the word!")
