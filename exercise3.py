#!/usr/bin/env python3


def decide_rps(player1, player2):

    options = {('Rock', 'Rock'): 0, ('Paper', 'Paper'): 0, ('Scissors', 'Scissors'): 0,
               ('Rock', 'Scissors'): 1, ('Paper', 'Rock'): 1, ('Scissors', 'Paper'): 1,
               ('Rock', 'Paper'): 2, ('Paper', 'Scissors'): 2, ('Scissors', 'Rock'): 2}

    choices = (player1, player2)

    if isinstance(player1, str) is False or isinstance(player2, str) is False:
        raise TypeError('Wrong data type, only strings are allowed as input.')

    else:

        if choices in options:

            if options[choices] == 0:
                return 0

            elif options[choices] == 1:
                return 1

            else:
                return 2

        else:
            raise ValueError('Invalid input, only the strings Rock, Paper, or Scissors are allowed.')

