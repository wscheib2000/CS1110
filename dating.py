# Will Scheib wms9gv
"""
Asks the user for their age and outputs a range of ages that they can date.
"""


age = int(input("How old are you? "))
boundLower = int((age / 2) + 7)
boundUpper = int((age * 2) - 13)

print("You can date people between " + str(boundLower) + " and " + str(boundUpper) + " years old")
