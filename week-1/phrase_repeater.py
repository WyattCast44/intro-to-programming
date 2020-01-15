# Header

"""
Week 1 Review - Part 4
Wyatt Castaneda
SWDV 600: INTRO TO PROGRAMMING
"""

# Problem 

"""
Write a program that repeats a phrase, given by a user, the number of times a user requests it be repeated.

For example, a user could input the phrase `Lazy harp seal has no job`. Then the user could input to repeat it `3` times. Given these inputs, the program should (1) output the phrase three times and (2) output which repetition this is by starting each line with the repetition number (note the `1`, `2`, and `3` below): 
"""

# Given

"""
Input your phrase: Lazy harp seal has no job
How many times should it be repeated? 3
1 Lazy harp seal has no job
2 Lazy harp seal has no job
3 Lazy harp seal has no job
"""

# Solution

print()
inputPhrase = input("Please enter a phrase to repeat: ")
print()
numRepitions = int(input("How many times should it be repeated? "))
print()

for loopNo in range(numRepitions):
    print(f'{loopNo + 1} {inputPhrase}')
