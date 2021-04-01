# Will Scheib  wms9gv
"""
Defines a function to test the validity of a credit card number.
"""


def check(num):
    """
    Checks the validity of a credit card number.

    :param num: The credit card number
    :return: True if it is valid, False if it is not
    """
    num = str(num)
    sum_every_second = 0
    sum_digits_of_doubles = 0
    for i in num[-1::-2]:
        sum_every_second += int(i)
    for i in num[-2::-2]:
        doubled = str(int(i) * 2)
        for j in doubled:
            sum_digits_of_doubles += int(j)

    return (sum_every_second + sum_digits_of_doubles) % 10 == 0
