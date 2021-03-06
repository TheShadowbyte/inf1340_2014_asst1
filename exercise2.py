#!/usr/bin/env python3

""" Assignment 1, Exercise 2, INF1340, Fall, 2014. UPC Checksum

    Perform a checksum on a UPC on numerical 12-digit strings.

    The checksum is implemented by adding the odd elements in the string, multiplying by 3,
    and then adding the even elements sum to that product. The last digit is omitted.
    Then a modulo is extracted from the total sum which is in turn subtracted from 10.
    Finally, a conditional checks whether the last digit matches the checksum.

"""

__author__ = 'Dimitar Jordanov & Jordan Rae'
__email__ = "jordanov@mail.utoronto.ca & jordan.rae@mail.utoronto.ca"

__copyright__ = "2014 Dimitar Jordanov & Jordan Rae"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line


def checksum(upc):
    """
    Checks if the digits in a UPC is consistent with checksum

    :param upc: a 12-digit universal product code
    :return:
        Boolean: True, checksum is correct
        False, otherwise
    :raises:
        TypeError if input is not a string
        ValueError if string is the wrong length (with error string stating how many digits are over or under
    """

    # Starting values for odd_positions and even_positions
    odd_positions = 0
    even_positions = 0

    # check type of input
    if type(str(upc)) == type(upc):
        # check length of string
        if len(upc) == 12:
            for x in range(0, len(upc) - 1):
                if x == 0:
                    # Append the value of the first position to the odd elements count.
                    odd_positions += int(upc[x])
                elif x % 2 != 0:
                    # Append the values of the second, fourth, etc. positions to the even elements count.
                    even_positions += int(upc[x])
                else:
                    # Append the values of the third, fifth, etc. positions to the odd elements count.
                    odd_positions += int(upc[x])

            odd_positions_multiplied = odd_positions * 3
            total_sum = odd_positions_multiplied + even_positions
            total_sum_modulo_ten = total_sum % 10
            final_check_sum = 10 - total_sum_modulo_ten

            # Check that the final_check_sum equals the last element in the input string.
            if final_check_sum == int(upc[-1]):
                return True
            else:
                return False
        else:
            # raise ValueError if not 12
            raise ValueError('The provided input must be exactly 12 characters long.')
    else:
        # raise TypeError if not string
        raise TypeError('The provided input must be a string, please try again.')
