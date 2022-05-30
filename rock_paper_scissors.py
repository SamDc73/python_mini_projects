# scissors

import random


def play():
    human_player_choise = input(
        "Choos 'r' for rock, 'p' for paper or 's' for scissors\n"
    )
    coumputer_choise = random.choice(['r', 'p', 's'])

    if is_the_winner(human_player_choise, coumputer_choise):
        return "You Won"
    return "you lost"


def is_the_winner(human_player_choise, coumputer_choise):
    if (
        (human_player_choise == 'r' and coumputer_choise == 's')
        or (human_player_choise == 'p' and coumputer_choise == 'r')
        or (human_player_choise == 's' and coumputer_choise == 'p')
    ):
        return True


print(play())
