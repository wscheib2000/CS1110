# Will Scheib wms9gv
"""
Defines a function to evaluate strings representing simple mathematical expressions. Uses while loops because I was
attempting to make it work for more than 1 operator. Doesn't work, though.
"""


def binop(string):
    string = string.replace(" ", "")
    while "*" in string:
        index = string.find("*")
        num1 = int(string[0:index])
        num2 = int(string[index + 1:len(string)])
        string = string.replace(str(num1) + "*" + str(num2), str(num1 * num2))
    while "/" in string:
        index = string.find("/")
        num1 = int(string[0:index])
        num2 = int(string[index + 1:len(string)])
        string = string.replace(str(num1) + "/" + str(num2), str(num1 / num2))
    while "+" in string:
        index = string.find("+")
        num1 = int(string[0:index])
        num2 = int(string[index + 1:len(string)])
        string = string.replace(str(num1) + "+" + str(num2), str(num1 + num2))
    while "-" in string[1:len(string)]:
        index = string.find("-")
        if index == 0:
            chunk = string[1:len(string)]
            index_chunk = chunk.find("-")
            num1 = int(string[0:index_chunk + 1])
            num2 = int(string[index_chunk + 2:len(string)])
        else:
            num1 = int(string[0:index])
            num2 = int(string[index + 1:len(string)])
        string = string.replace(str(num1) + "-" + str(num2), str(num1 - num2))
    if "." in string:
        return float(string)
    else:
        return int(string)
