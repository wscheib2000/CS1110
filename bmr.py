# Will Scheib wms9gv
"""
Defines functions to calculate Mifflin St Jeor, Harris Benedict, revised Harris Benedict, and Katch-McArdle estimates of
basal metabolic rate.
"""


def st_jeor(mass, height, age, sex):
    """
    Calculates a Mifflin St Jeor estimate of basal metabolic rate.

    :param mass: The mass of the person in kg
    :param height: The height of the person in cm
    :param age: Age of the person in years
    :param sex: Gender of the person (binary)
    :return: Mifflin St Jeor estimate of bmr
    """
    if sex == "male":
        s = 5
    else:
        s = -161
    estimate = round((10 * mass) + (6.25 * height) - (5 * age) + s, 3)

    return estimate


def harris_benedict(mass, height, age, sex):
    """
    Calculates a Harris Benedict estimate of basal metabolic rate.

    :param mass: The mass of the person in kg
    :param height: The height of the person in cm
    :param age: Age of the person in years
    :param sex: Gender of the person (binary)
    :return: Harris Benedict estimate of bmr
    """
    if sex == "male":
        a = 66.5
        b = 13.75
        c = 5.003
        d = 6.755
    else:
        a = 655.1
        b = 9.563
        c = 1.850
        d = 4.676
    estimate = round(a + (b * mass) + (c * height) - (d * age), 3)

    return estimate


def revised_harris_benedict(mass, height, age, sex):
    """
    Calculates a revised Harris Benedict estimate of basal metabolic rate.

    :param mass: The mass of the person in kg
    :param height: The height of the person in cm
    :param age: Age of the person in years
    :param sex: Gender of the person (binary)
    :return: Revised Harris Benedict estimate of bmr
    """
    if sex == "male":
        a = 88.362
        b = 13.397
        c = 4.799
        d = 5.677
    else:
        a = 447.593
        b = 9.247
        c = 3.098
        d = 4.330
    estimate = round(a + (b * mass) + (c * height) - (d * age), 3)

    return estimate


def katch_mcardle(mass, bodyfat_pct):
    """
    Calculates a Katch-McArdle estimate of basal metabolic rate.

    :param mass: The mass of the person in kg
    :param bodyfat_pct: Percent body fat of the person
    :return: Katch-McArdle estimate of bmr
    """
    if bodyfat_pct < 1:
        lean_body_mass = mass * bodyfat_pct
    else:
        lean_body_mass = mass * (bodyfat_pct / 100)

    estimate = round(370 + (21.6 * lean_body_mass))

    return estimate
