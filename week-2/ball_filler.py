# Header

"""
Week 2 Review - Part 1
Wyatt Castaneda
SWDV 600: INTRO TO PROGRAMMING
"""

# Problem 

"""
You have been contracted by a bowling ball manufacturer to write a program that estimates the amount of ball "filler" they will need to order for a new line of bowling balls.

Each spherical bowling ball has a diameter that can vary from 8.4 to 8.6 inches. Inside that ball there are two things: (1) a uniquely shaped metal object called the core that affects the spin of the ball, and (2) stuff packed around the core making the ball's spherical shape called the filler. Given the intended diameter of a bowling ball, the volume of the ball's core, and the number of bowling balls to produce, your program should calculate the amount of filler the company should order.

For example, let assume a company wants to produce 100 bowling balls with a diameter of 8.5 inches. Each of these balls will contain a core that has a volume of 124 inches cubed. Then each ball will require 197.55 inches cubed of filler (i.e., the total volume of the spherical ball (Links to an external site.) containing no core, which can be computed with the formula LaTeX: V=\frac{4}{3}\pi r^3V = 4 3 π r 3, minus the volume of the core). If each ball needs 197.55 inches cubed of filler, and the company is producing 100 balls, then in total they will need ~19,755 inches cubed of filler. 

You program should prompt a user to input in this order: the number of balls to manufacture, the diameter of each ball in inches, and the volume of the core in inches cubed. It should then compute and output the total amount of filler required.
"""

# Given 

"""
How many bowling balls will be manufactured? 100
What is the diameter of each ball in inches? 8.5
What is the core volume in inches cubed? 124
You will need 19755.509806430524 inches cubed of filler
"""

# Solution

import math

print()
inputNumBalls = int(input("How many bowling balls will be manufactured? "))
inputBallDiameter = float(input("What is the diameter of each ball in inches? "))
inputBallVolume = float(input("What is the core volume in inches cubed? "))
print()

def sphereVolume(diameter):
    result = (4/3) * math.pi * (diameter/2) ** 3
    return result

fillableVolumePerBall = sphereVolume(inputBallDiameter) - inputBallVolume

totalUnfilledVolume = inputNumBalls * fillableVolumePerBall

print(f'You will need {totalUnfilledVolume} inches cubed of filler.')
