# Will Scheib wms9gv
"""
Defines a function to test whether it is creepy if two people date each other. Includes commented out improvements
which make order of ages irrelevant and account for cases where one partner is younger than 14. Works for fractional
ages.
"""


def creepy(age1, age2):
    """
    This function tests whether it is creepy if two people date each other.

    :param age1: Age of the first person
    :param age2: Age of the second person
    :return: TRUE if it is creepy, FALSE if it is not.
    """
    return age1 < int((age2 / 2) + 7)  # or age2 < int((age1 / 2) + 7) \
            # or ((age1 < 14 or age2 < 13) and (age2 > age1 + 1 or age1 > age2 + 1))
