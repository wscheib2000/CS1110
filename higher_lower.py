# Will Scheib  wms9gv
"""
Plays a guessing game where the user has to guess a number between 1 and 100.
"""

import random


num = int(input("What should the answer be? "))
if num == -1:
    num = random.randrange(1, 101)
num_guesses = int(input("How many guesses? "))
while num_guesses < 1:
    print("Sorry, that's not a positive number.")
    num_guesses = int(input("How many guesses? "))

while num_guesses > 0:
    guess = int(input("Guess a number: "))
    num_guesses -= 1
    if num == guess:
        num_guesses = 0
        print("You win!")
    elif num_guesses == 0:
        print("You lose; the number was " + str(num) + ".")
    elif num < guess:
        print("The number is lower than that")
    elif num > guess:
        print("The number is higher than that.")
