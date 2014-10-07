#!/usr/bin/env python3

""" Module to test exercise3.py """

__author__ = 'Dimitar Jordanov & Jordan Rae'
__email__ = "jordanov@mail.utoronto.ca & jordan.rae@mail.utoronto.ca"

__copyright__ = "2014 Dimitar Jordanov & Jordan Rae"
__license__ = "MIT License"

__status__ = "Prototype"

import pytest
from exercise3 import decide_rps


def test_checksum():
    """
    Inputs that are the correct format and length
    """
    assert decide_rps("Rock", "Paper") == 2
    assert decide_rps("Scissors", "Scissors") == 0
    assert decide_rps("Rock", "Scissors") == 1
    # other tests
    assert decide_rps("Rock", "Rock") == 0
    assert decide_rps("Paper", "Paper") == 0
    assert decide_rps("Paper", "Scissors") == 2
    assert decide_rps("Scissors", "Rock") == 2
    assert decide_rps("Paper", "Rock") == 1
    assert decide_rps("Scissors", "Paper") == 1


