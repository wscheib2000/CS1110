# Will Scheib (wms9gv)
"""
Defines two functions to manage a gradebook.
"""


gradebook_grade = {}
gradebook_weight = {}


def assignment(kind, grade, weight=1):
    """
    Adds an assignment to the gradebook.

    :param kind: The type of assignment
    :param grade: The grade the student got on the assignment
    :param weight: How much the assignment is worth compared to others of its type
    :return: Nothing
    """
    if kind in gradebook_grade:
        gradebook_grade[kind] = (gradebook_grade[kind] * gradebook_weight[kind] + grade * weight) / (gradebook_weight[kind] + weight)
        gradebook_weight[kind] = gradebook_weight[kind] + weight
    else:
        gradebook_grade[kind] = grade
        gradebook_weight[kind] = weight


def total(proportions):
    """
    Takes a dictionary of weights for the types of assignments and computes the student's total grade in the class.

    :param proportions: The dictionary of weights
    :return: The student's grade
    """
    grade = 0
    for i in proportions:
        if i in gradebook_grade:
            grade += gradebook_grade[i] * proportions[i]
    return grade
