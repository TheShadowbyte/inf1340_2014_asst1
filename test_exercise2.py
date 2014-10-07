#!/usr/bin/env python3

""" Module to test exercise2.py """

__author__ = 'Dimitar Jordanov & Jordan Rae'
__email__ = "jordanov@mail.utoronto.ca & jordan.rae@mail.utoronto.ca"

__copyright__ = "2014 Dimitar Jordanov & Jordan Rae"
__license__ = "MIT License"

__status__ = "Prototype"

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
    assert checksum("124578906532") is False
    assert checksum("001480098006") is True
    assert checksum("001570094004") is False

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
