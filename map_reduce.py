# Will Scheib wms9gv
"""
Defines two functions, one which applies a function to every argument in a list, and one which uses the function on
arguments of the list to combine them into one value.
"""


def mymap(func, lst):
    """
    Applies a function to each value in a list.

    :param func: The function to be applied
    :param lst: The list to apply the function to
    :return: List of results
    """
    new_lst = []
    for n in range(0, len(lst)):
        new_lst.append(func(lst[n]))
    return new_lst


def myreduce(func, lst):
    """
    Uses a function repeatedly to combine all elements of a list into a single value.

    :param func: The function to be applied
    :param lst: The list to apply the function to
    :return: The resultant value
    """
    val = lst[0]
    for x in lst[1:]:
        val = func(val, x)
    return val
