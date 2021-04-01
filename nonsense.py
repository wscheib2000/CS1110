# Will Scheib wms9gv
"""
Asks the user to input a word, prints the word 12 times, and says it doesn't sound like a word anymore.
"""

word = input("Please enter your favorite word: ")
for i in range(12):
    print(word, end=" ")
print("\n\"" + word + "\" doesn't even sound like a word anymore.")
