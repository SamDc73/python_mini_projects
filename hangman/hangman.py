from words import *
import random
import string
import argparse

parser = argparse.ArgumentParser(
    description="Play Hangman form the comfort of your Terminal"
)
parser.add_argument(
    '-c',
    '--category',
    choices=['others', 'countries', 'foods', 'others'],
    type=str,
    default='others',
    help='Wich category you would like to play on',
)
parser.add_argument(
    '-l',
    '--lives',
    type=int,
    default=5,
    help="number of tries you are alowed to have (default is 6)",
)
args = parser.parse_args()

# For choosing the category
if args.category == 'countries':
    words = countries
elif args.category == 'foods':
    words = foods
elif args.category == 'animals':
    words = animals


def get_valid_word(words):
    word = random.choice(words)
    while '_' in word or ' ' in word:
        word = random.choice(words)
    return word.lower()


def hangman(lives):
    word = get_valid_word(words)
    print(word)
    word_letters = list(set(word))
    alphabet = list(set(string.ascii_lowercase))
    used_letters = list(set())
    right_letters = list(set())

    # The main iteration (user entering letters)
    while sorted(right_letters) != sorted(word_letters) and lives > 0:
        # Show the gussed word (while guessing it) in the formt [t_st]
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(''.join(word_list))
        guessed_letter = input("Please guess a letter ").lower()

        if guessed_letter in used_letters:
            print("You already entered this letter ")
        elif guessed_letter in alphabet:
            used_letters.append(guessed_letter)
            if guessed_letter in word_letters:
                print("Right guess")
                right_letters.append(guessed_letter)
            else:
                print("Wrong guess ")
                lives = lives - 1
        else:
            print("please enter a valid cahrchter")
    if right_letters == used_letters:
        print(f"Your are a wizard, your guest the word {word} with no wrong guesses")
    elif right_letters in used_letters:
        print(f"Comgrats you won, you guessed the word {word}")
    else:
        print("you failed, good luck next time")


hangman(lives=args.lives)
