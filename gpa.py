# Will Scheib wms9gv
"""
Defines three functions to track GPA and credits taken by a student.
"""


current_gpa = 0
current_credit_total = 0


def add_course(grade, num_credit=3):
    """
    This function adds a class to the gpa and credit_total variables, with credits defaulting to 3.

    :param grade: Grade in the class
    :param num_credit: How many credits the class was worth
    :return: Does not return any values
    """
    global current_gpa, current_credit_total
    current_gpa = (current_gpa * current_credit_total + grade * num_credit) / (current_credit_total + num_credit)
    current_credit_total = current_credit_total + num_credit


def gpa():
    """
    This function returns the current GPA.

    :return: Current GPA, rounded to 2 decimal places
    """
    return round(current_gpa, 2)


def credit_total():
    """
    This function returns the current credit total.

    :return: Current credit total
    """
    return current_credit_total
