#!/usr/bin/env python3

""" Assignment 1, Exercise 3, INF1340, Fall, 2014. Rock-Paper-Scissors Game

    A rock / paper / scissors game that takes string inputs from 2 players.

    The 2-player input is stored in a tuple which is compared against all
    possible combinations within the options dictionary. The keys for the
    dictionary are also tuples which allows the user input to match one
    of the possible combinations. The following returns are given, based on
    the input from the 2 players:

    Tie: Return 0
    Player 1 Wins: Return 1
    Player 2 Wins: Return 2

"""

__author__ = 'Dimitar Jordanov & Jordan Rae'
__email__ = "jordanov@mail.utoronto.ca & jordan.rae@mail.utoronto.ca"

__copyright__ = "2014 Dimitar Jordanov & Jordan Rae"
__license__ = "MIT License"

__status__ = "Prototype"


def decide_rps(player1, player2):

    # All possible inputs in dictionary format
    options = {('Rock', 'Rock'): 0, ('Paper', 'Paper'): 0, ('Scissors', 'Scissors'): 0,
               ('Rock', 'Scissors'): 1, ('Paper', 'Rock'): 1, ('Scissors', 'Paper'): 1,
               ('Rock', 'Paper'): 2, ('Paper', 'Scissors'): 2, ('Scissors', 'Rock'): 2}

    # The 2 players' provided inputs
    choices = (player1, player2)

    if isinstance(player1, str) is False or isinstance(player2, str) is False:
        raise TypeError('Wrong data type, only strings are allowed as input.')

    else:

        # Check if the user input exists within the possible options.
        # Then run conditionals that check if the input tuple exists
        # within the options dictionary keys, which are also tuples.
        if choices in options:

            if options[choices] == 0:
                return 0

            elif options[choices] == 1:
                return 1

            else:
                return 2

        else:
            # ValueError is raised if the arguments given are not one of the three possible choices.
            raise ValueError('Invalid input, only the strings Rock, Paper, or Scissors are allowed.')

