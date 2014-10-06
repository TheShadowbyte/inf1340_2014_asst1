#!/usr/bin/env python3

""" Module to test exercise2.py """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line

# imports one per line
import pytest
from exercise2 import checksum


def test_checksum():
    """
    Inputs that are the correct format and length
    """
    assert checksum("786936224306") is True
    assert checksum("085392132225") is True
    assert checksum("717951000841") is False
    # other tests


def test_input():
    """
    Inputs that are the incorrect format and length
    """
    with pytest.raises(TypeError):
        checksum(1.0)
        checksum(786936224306)

    with pytest.raises(ValueError):
        checksum("1")
        checksum("1234567890")

        # other tests

    # add functions for any other tests


odd_positions = 0
even_positions = 0

if type(str(upc)) == type(upc):
    if len(upc) == 12:
        for x in range(0, len(upc) - 1):
            if x == 0:
                print
                "First element"
                odd_positions += int(upc[x])
            elif x % 2 != 0:
                print
                "Even element"
                even_positions += int(upc[x])
            else:
                print
                "Odd element"
                odd_positions += int(upc[x])

        odd_positions_multiplied = odd_positions * 3
        total_sum = odd_positions_multiplied + even_positions
        total_sum_modulo_ten = total_sum % 10
        final_check_sum = 10 - total_sum_modulo_ten

        if final_check_sum == upc[-1]:
            return True
        else:
            return False
    else:
        raise ValueError('The provided input must be exactly 12 characters long.')
else:
    raise TypeError('The provided input must be a string, please try again.')
