# Header

"""
Week 5 Review - Part 1
Wyatt Castaneda
SWDV 600: INTRO TO PROGRAMMING
"""

# Problem 

"""
You have been contracted by a golf training company in need of a new golf club recommendation app for their clients.

Your new client is looking for an application where a user enters some information about their current golfing situation and the app replies with what club the person should use. They want to start simple first. The application should ask the user, in this order, if

they have hit the ball on the green (answer should be `y` or `n`)
how far they are from the hole 
If the ball is on the green, then the app should recommend using the 'Putter' club. Otherwise, if the distance is 200 yards or more, it should recommend the 'Driver', between 140 and 200 yards it should recommend the '5-Iron', between 100 and 140 yards the '9-Iron', and for any other distance it should recommend the 'Pitching Wedge'.

You are to write a program that makes those recommendations based on the user's input. You can assume the user will only enter valid values. Here are two examples:

Welcome to the Golf Club Helper!
Tell me your situation, and I'll recommend a club

Did you hit it on the green (y/n)? y
How far is the ball from the hole? 15

I recommend using your Putter

Welcome to the Golf Club Helper!
Tell me your situation, and I'll recommend a club

Did you hit it on the green (y/n)? n
How far is the ball from the hole? 110

I recommend using your 9-Iron
"""

# Solution

from helpers import *

def isBallOnGreen():
    print('\nIs the ball currently on the green?\n')
    print("Enter 'y' for yes...")
    print("Enter 'n' for no...\n")
    return input('> ')

def promptUserForDistanceToHole():
    print('\nHow far is the ball from the hole? (yards)\n')
    return float(input('> '))

def determineBestClub(distanceToHole):
    if distanceToHole >= 200:
        return 'Driver'
    elif distanceToHole < 200 and distanceToHole >= 140:
        return '5-Iron'
    elif distanceToHole < 140 and distanceToHole >= 100:
        return '9-Iron'
    else:
        return 'Pitching Wedge'

def main():
    print(success('\nWelcome to the Golf Club Helper! ⛳'))
    print(success('---------------------------------------------------'))
    print(info('Tell me your situation, and I\'ll recommend a club.\n'))

    if isBallOnGreen() == 'y':
        print('\nI recommend using the Putter. 🏌️')
        return

    distance = promptUserForDistanceToHole()
    club = determineBestClub(distance)
    print(f'\nI recommend using your {club} 🏌️')

main()