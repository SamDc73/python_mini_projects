import random


def guess(x):
    random_number = random.randint(1, x)
    guessed_number = 0
    while guessed_number != random_number:
        guessed_number = int(input(f"Enter a number between 1 and {x}:  "))
        if guessed_number not in range(1, x):
            print(f"Please Enter between 1 and {x}")
        elif random_number < guessed_number:
            print("the number you entered is too high, please enter another guess")
        elif random_number > guessed_number:
            print("The number you entered is too low, please enter another guess")
    print(f"indeed {random_number} is right, Great guessing !!")
    print("Do you like to replay the game again ? ")

    # To Ask the user wether they like to rerun the game agian :
    def repeat_the_game():
        repeat_status = input(
            "A. yes, this game is alot of fun    B. No, I got bored.\n"
        )
        if repeat_status.lower() in ["a", "yes", "A. yes, this game is alot of fun"]:
            guess(x)
        elif repeat_status.lower() in ["b", "no", "B. No, I got bored."]:
            print("Well, see you later then. ")
        else:
            print("Sorry, I couldn't understand you")
            repeat_status()

    repeat_the_game()


guess(10)
