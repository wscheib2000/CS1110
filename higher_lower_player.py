# Will Scheib  wms9gv
"""
Plays a guessing game where the computer guesses a user-selected number between 1 and 100.
"""

print("Think of a number between 1 and 100 and I'll guess it.")
num_guesses = int(input("How many guesses do I get? "))
lower_bound = 0
upper_bound = 101

while num_guesses > 0:
    answer = input("Is the number higher, lower, or the same as " + str((lower_bound + upper_bound) // 2) + "? ")
    answer = answer.strip(" ")
    answer = answer.lower()
    num_guesses -= 1
    if answer == "same":
        num_guesses = -1
        print("I won!")
    elif answer == "lower":
        upper_bound = ((lower_bound + upper_bound) // 2)
    elif answer == "higher":
        lower_bound = ((lower_bound + upper_bound) // 2)

    if num_guesses == 0:
        num = int(input("I lost, what was the answer? "))
        if lower_bound < num < upper_bound:
            print("Well played!")
        elif num < lower_bound:
            print("That can't be, you said it was higher than " + str(lower_bound) + "!")
        else:
            print("That can't be, you said it was lower than " + str(upper_bound) + "!")

    if lower_bound + 1 >= upper_bound:
        num_guesses = 0
        print("Wait; how can it be both higher than " + str(lower_bound) + " and lower than " + str(upper_bound) + "?")
