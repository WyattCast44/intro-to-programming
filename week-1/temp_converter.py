# Header

"""
Week 1 Review - Part 1
Wyatt Castaneda
SWDV 600: INTRO TO PROGRAMMING
"""

# Problem 

"""
Write a temperature converter program called `temp_converter` that enables a user to input a temperature in Celsius and output a temperature in Fahrenheit. The program should allow the user to do three temperature conversions.

Modify the temperature converter we developed in 1.10 Together Project: A Temperature Converter to now convert from Fahrenheit to Celsius. A user should now input a temperature in Fahrenheit and the program should output the equivalent temperature in Celsius. Modify the input prompts and the output message as appropriate.
"""

# Given

"""
- program name = temp_converter
- we want to convert Fahrenheit to Celcius
- we want the user to be able to input up to 3 values for coversion
- Conversion equations:
    - Degrees F = ((deg C) * 9)/5)) + 32
    - Degrees C = (((deg F) - 32) * 5)/9
"""

# Solution

def promptUserInput(inputFormat):
    return input(f'Please enter the temperature in degrees {inputFormat}: ')

def convertCelciusToFahrenheit(degCel):
    return ((float(degCel) * 9)/5) + 32

def convertFahrenheitToCelcius(degFah):
    return ((float(degFah) - 32) * 5)/9

def printConvertedValue(inputFormat, degrees):
    if inputFormat == "Celcius":
        message = f'The temperature in Fahrenheit is {degrees} degrees'
    else:
        message = f'The temperature in Celcius is {degrees} degrees'

    print(message)
    print()

print()
numRepitions = int(input("How many temperatures would you like to convert? Enter as whole number: "))
print()

for rounds in range(numRepitions):
    inputFormat = "Celcius"
    inputDegrees = promptUserInput(inputFormat)
    if inputFormat == "Celcius":
        printConvertedValue(
            inputFormat,
            convertCelciusToFahrenheit(inputDegrees)
            )
    else:
        printConvertedValue(
            inputFormat,
            convertFahrenheitToCelcius(inputDegrees)
            )

print("Thanks for using this tool :)")