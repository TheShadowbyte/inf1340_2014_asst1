#!/usr/bin/env python3


def decide_rps(player1, player2):

    options = {'Rock': 1, 'Paper': 2, 'Scissors': 3}

    if isinstance(player1, str) is False or isinstance(player2, str) is False:
        raise TypeError('Wrong data type, only strings are allowed as input.')
    else:
        p1_capitalized = player1.capitalize()
        p2_capitalized = player2.capitalize()
        if p1_capitalized in options and p2_capitalized in options:
            if options[player1] == options[player2]:
                print "Tie."
            elif options[player1] > options[player2]:
                print "Player 1 wins."
            else:
                print "Player 2 wins."
        else:
            raise ValueError('Invalid input, only the strings Rock, Paper, or Scissors are allowed.')

    return 1

decide_rps("Rock", "Paper")
decide_rps("Rock", "Rock")
decide_rps("Scissors", "Rock")