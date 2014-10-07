#!/usr/bin/env python3

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module contains one function grade_to_gpa. It can be passed a parameter
that is an integer (0-100) or a letter grade (A+, A, A-, B+, B, B-, or FZ). All
other inputs will result in an error.

Example:
    $ python exercise1.py

"""

__author__ = 'Dimitar Jordanov & Jordan Rae'
__email__ = "jordanov@mail.utoronto.ca"

__copyright__ = "2014 Dimitar Jordanov"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line


def grade_to_gpa(grade):
    """
    Returns the UofT Graduate GPA for a given grade.

    :param:
        grade (integer or string): Grade to be converted
            If integer, accepted values are 0-100.
            If string, accepted values are A+, A, A-, B+, B, B-, FZ

    :return:
        float: The equivalent GPA
            Value is 0.0-4.0

    :raises:
        TypeError if parameter is not a string or integer
        ValueError if parameter is out of range
    """

    if type(grade) is str:

        if grade == "A+" or grade == "A":
            gpa = 4.0
            print(grade)
        elif grade == "A-":
            gpa = 3.7
        elif grade == "B+":
            gpa = 3.3
        elif grade == "B":
            gpa = 3.0
        elif grade == "B-":
            gpa = 2.7
        elif grade == "FZ":
            gpa = 0.0
        else:
            # Raise a ValueError if the input is not one of the possible letters.
            raise ValueError("Wrong input given for letter grades.")

    elif type(grade) is int:

        if 0 <= grade <= 69:
            gpa = 0.0
        elif grade <= 72:
            gpa = 2.7
        elif grade <= 76:
            gpa = 3.0
        elif grade <= 79:
            gpa = 3.3
        elif grade <= 84:
            gpa = 3.7
        elif 85 <= grade <= 100:
            gpa = 4.0
        else:
            # Raise a ValueError if the input is less than 0 or greater than 100.
            raise ValueError("Grade value outside range. Please use value between 0 and 100.")

    else:
        # raise a TypeError exception
        raise TypeError("Invalid type passed as parameter")

    return gpa
