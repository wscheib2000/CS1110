# Will Scheib wms9gv
"""
Asks the user for the temperature in Celsius and outputs the temperature in Fahrenheit.
"""


tempC = float(input("What is the temperature in Celsius? "))
tempF = tempC * (9 / 5) + 32

print("It is " + str(round(tempF, 1)) + " degrees Fahrenheit")
