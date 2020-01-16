# Header

"""
Week 2 Review - Part 2
Wyatt Castaneda
SWDV 600: INTRO TO PROGRAMMING
"""

# Problem 

"""
A franchise restaurant is attempting to understand if customers think their service is good day-to-day by summarizing a series of daily scores. The restaurant computes a daily score based on the number of positive comments and negative comments it receives that day. Each the score begins at 0. A positive comment adds 1 to the score, and a negative comment subtracts 1. So on a given day if there were 5 positive comments and 2 negative comments, the score for that day would be 3 (5 - 2).

Your task is to write a program that enables a restaurant manager to input these daily scores and report the total score for those days. For example, if the score on Monday is 3, Tuesday is 4, Wednesday is -2, and Thursday is 3, then the total score for those days would be 3 + 4 + (-2) + 3, which is 8. This would indicate the service is being positively reviewed over the past few days.

You program should prompt the user for how many days of scores they will be entering, and then prompt them for the score for each day. The score prompt should include the number of the day for which they entering a score (i.e., notice the `day 1` phrase in the prompt of the example below).

Once all the scores have been entered, it should then output the number total score for those days. 
"""

# Given 

"""
How many days of scores? 4
Enter score for day 1: 2
Enter score for day 2: 4
Enter score for day 3: -2
Enter score for day 4: 1
The total score of the 4 days is 5
"""

# Solution

import math

print()
inputNumDays = int(input("How many days of scores would you like to enter? "))
print()

def promptUserToEnterDailyScores(numberOfDays):
    result = 0

    for day in range(numberOfDays):
        result = result + int(input(f'Enter the score for day {day + 1}: '))
    
    return result

finalScore = promptUserToEnterDailyScores(inputNumDays)

print()
print(f'The total score of the {inputNumDays} days is {finalScore}.')
