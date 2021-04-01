# Will Scheib wms9gv
"""
Defines two functions that convert the temperature from Celsius to Fahrenheit and Fahrenheit to Celsius, respectively.
"""


def c2f(temp):
    """
    This function converts a temperature in Celsius to Fahrenheit.

    :param temp: Temperature in Celsius
    :return: temperature in Fahrenheit
    """
    return round(temp * (9 / 5) + 32, 1)


def f2c(temp):
    """
    This function converts a temperature in Fahrenheit to Celsius.

    :param temp: Temperature in Celsius
    :return: temperature in Fahrenheit
    """
    return round((temp - 32) * (5 / 9), 1)
