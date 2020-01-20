# Header

"""
Week 3 Review - Part 2
Wyatt Castaneda
SWDV 600: INTRO TO PROGRAMMING
"""

# Problem 

"""
In the picture above you will see a gradient bar. Gradients in computer graphics typically show a color progression. The example above is a progression of the green intensity from 0 to 255, with red and blue remaining at intensity 0 through the progression, spread across six rectangles. When you see graduated colors on your computer they are often created using this technique: having thinner and thinner rectangles makes a smoother gradient progression. For example, the gradient below is a green progression through 64 rectangles:

Your task is to draw a gradient bar. You can make the color progression as simple (e.g., just green intensities changing) or sophisticated (e.g., linear equations manipulating the red, green, and blue intensities independently) as you desire. Your main requirements are this:

The window you draw the bar in must be 400 pixels wide and the progression must be horizontal.
There can be no gaps or overlaps in the progression: no spaces between the rectangles, no spaces from the edges of the window, no bars drawn on top of one another.
The number of bars you use must be a multiple of 6 (i.e., 6 bars, 12 bars, 18 bars, etc.)
The bars must have no outline (hint: setWidth method)
All bars must have a width within one pixel of the same width. For example, if we have 6 bars in a 400-pixel window, then each bar should be 66 or 67 pixels wide. This goes along with the no overlaps constraint
It is strongly recommend that you first figure out how to draw rectangles that fill the window without gaps or overlaps. Then, if necessary, consider how you could reduce the redundancy of your work using repetition. Finally work on making the colors progress (hint: a loop variable can progress through a range of values enabling your progression).
"""

# Solution

import math
import random
import graphics as g

# Window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 200

# Bars
NUM_BARS = 6
BAR_WIDTHS = []

"""
Used to determine a the widths of an 
arbitary number of bars, in a window of
arbitaty with
"""
def determineBarWidths():
    nominalWidth = math.floor(WINDOW_WIDTH / NUM_BARS)

    # Set the nominal width for bars
    for bar in range(NUM_BARS):
        BAR_WIDTHS.append(nominalWidth)
    
    # Distribute the remainer into the bars 
    for index in range(WINDOW_WIDTH % NUM_BARS):
        BAR_WIDTHS[index] = BAR_WIDTHS[index] + 1
    
"""
Create the window
"""
def createWindow():
    win = g.GraphWin("My Gradient Bar", WINDOW_WIDTH, WINDOW_HEIGHT)
    return win    

"""
Tranlate a x coordinate to a percent width of window
"""
def percentWidth(width):
    return width/WINDOW_WIDTH

"""
Map a percent window width to a percent color scale
"""
def percentColor(percent):
    return math.floor(255 * percent)

"""
Draw the bars onto the window
"""
def drawBars(win):

    xStart = 0
    yStart = 0

    for bar in range(NUM_BARS):
        rect = g.Rectangle(g.Point(xStart, yStart), g.Point(xStart + BAR_WIDTHS[bar], WINDOW_HEIGHT))
        xStart = xStart + BAR_WIDTHS[bar]
        rect.setWidth(0)
        rect.setFill(g.color_rgb(percentColor(percentWidth(xStart)), 0, 0))
        rect.draw(win)

def printBarDetails():
    print()
    print(f'There will be {NUM_BARS} bars, the widths are listed below:')
    print()
    for index in range(NUM_BARS):
        print(f'Bar {index + 1} will be {BAR_WIDTHS[index]} pixels wide')
    print()
    print('Please click the window to exit the program...')

def main():
    determineBarWidths()
    win = createWindow()
    drawBars(win)
    printBarDetails()
    win.getMouse()

main()