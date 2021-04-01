# Will Scheib wms9gv
"""
Defines functions to calculate mean, median, root-mean-square, and median of the previous three values.
"""


def mean(a, b, c):
    """
    Computes the mean of three numbers.

    :param a: First number
    :param b: Second number
    :param c: Third number
    :return: Mean
    """
    mean_vals = (a + b + c) / 3
    return mean_vals


def median(a, b, c):
    """
    Computes the median of three numbers.

    :param a: First number
    :param b: Second number
    :param c: Third number
    :return: Median
    """
    if a - b * c - a <= 0:
        return a
    elif b - a * c - b <= 0:
        return b
    else:
        return c


def rms(a, b, c):
    """
    Computes the root-mean-square of three numbers.

    :param a: First number
    :param b: Second number
    :param c: Third number
    :return: Root-mean-square
    """
    rms_vals = (mean(a**2, b**2, c**2))**(1/2)
    return rms_vals


def middle_average(a, b, c):
    """
    Calculates the mean, median, and root-mean-square of three numbers and returns the median of those values.

    :param a: First number
    :param b: Second number
    :param c: Third number
    :return: Median of the mean, median, and root-mean-square of the numbers
    """
    mean_vals = mean(a, b, c)
    median_vals = median(a, b, c)
    rms_vals = rms(a, b, c)

    middle_average_vals = median(mean_vals, median_vals, rms_vals)
    return middle_average_vals
