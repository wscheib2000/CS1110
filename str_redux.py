# Will Scheib and Nathan Barrington (wms9gv, ndb7ab)
"""
Defines functions to perform find and split on strings.
"""


def myfind(string, search):
    """
    This function finds the first appearance of a string inside of a larger string. If it does not appear in the larger
    string, the function returns -1.

    :param string: The big string
    :param search: The small string
    :return: Location of first appearance or -1
    """
    if search not in string:
        return -1
    h = 0
    while string[h:h + len(search)] != search:
        h += 1
    return h


def mysplit(string, split_on=" "):
    """
    This function returns pieces of a string separated by a given smaller string.

    :param string: The big string
    :param split_on: The small string
    :return: Pieces of the string after being separated on the given values
    """
    vals = []
    while myfind(string, split_on) != -1:
        location = myfind(string, split_on)
        if location == 0 or len(string) == 1:
            vals.append("")
        else:
            vals.append(string[0:location])
        string = string[location + len(split_on):len(string)]
    vals.append(string)
    return vals
