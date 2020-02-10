# Header

"""
Week 6 Review - Part 1
Wyatt Castaneda
SWDV 600: INTRO TO PROGRAMMING
"""

# Problem 

"""
Recall, your work involves more than just correctness. Specifically, we will look for:

- appropriate separation of concerns (including classes)
- appropriate use of function interfaces (i.e., using parameters and return values, not using variables declared as part of a script to make them accessible in all function scopes)
- comments explaining the why behind more difficult areas of code
- documentation of classes/modules for explaining their purpose and usage
- good function, parameter, and variable names that communicate the purpose and make the program more readable

Please keep in mind there is no single correct answer for how you design the program: there are many good approaches that are worth full credit.

A unique list has no repeated items. For example, the list ['orange', 'juice', 'futures'] is unique because each item only appears one time. However, the list ['sell','mortimer','sell'] is not unique because the string 'sell' appears more than one time.

Write a program named `unique_list` where a user inputs a series of positive integers and, when finished, it reports whether or not the sequence of numbers input is unique or not. For example:

This program tests if the sequence of positive numbers you input are unique

Enter -1 to quit
Enter the first number: 9
Next: 5
Next: 3
Next: 6
Next: 23
Next: -1
The sequence [9, 5, 3, 6, 23] is unique!

This program tests if the sequence of positive numbers you input are unique

Enter -1 to quit
Enter the first number: 83
Next: 20
Next: 593
Next: 28
Next: 20
Next: 51
Next: -1

The sequence [83, 20, 593, 28, 20, 51] is NOT unique!
"""

# Solution

from helpers import *

def main():
    Console().sectionTitle('\nUnique List Finder - v0.1.0')

main()