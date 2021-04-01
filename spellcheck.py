# Will Scheib wms9gv

"""
Checks an inputted line of text for spelling errors.
"""

import urllib.request

link = "http://cs1110.cs.virginia.edu/files/words.txt"
file = urllib.request.urlopen(link)
words = []
for line in file:
    words.append(line.decode("utf-8").lower().strip())

print("Type text; enter a blank line to end.")
input_line = input()
while input_line != "":
    words_in_phrase = input_line.split()
    for word in words_in_phrase:
        if word.lower().strip(".?!,()'\"") not in words and word.lower().strip(".?!,()'\"") != "":
            print("MISSPELLED: " + word.strip(".?!,()'\""))
    input_line = input()
