# Header

"""
Week 3 Review - Part 1
Wyatt Castaneda
SWDV 600: INTRO TO PROGRAMMING
"""

# Problem 

"""
In a graphics window, you are to draw an outdoor scene containing a house.

Your drawing should include at least the following shapes:

three rectangles - Need one more
two lines - need two
one circle
one text label - Need this
Your picture should not be boring black and white. It should include at least three colors, tastefully distributed to bring your house to life.

Finally, it should have some interactive feature such that when a user clicks on your picture something changes (e.g. a color changes, a tree falls over, the sun rises, a door opens). The change only has to happen once.
"""

# Solution

from graphics import *

# Window
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 300
WINDOW_CAPTION = "My House"
WINDOW_BACKGROUND_DAY = color_rgb(237, 235, 218)
WINDOW_BACKGROUND_NIGHT = color_rgb(52, 63, 138)

# Ground
GROUND_HEIGHT = 50
GROUND_COLOR = color_rgb(108, 166, 119) 

# House
HOUSE_WIDTH = 150
HOUSE_HEIGHT = 75
HOUSE_COLOR = color_rgb(166, 149, 108)

# Roof
ROOF_COLOR = color_rgb(181, 88, 65)

def percentWidth(percent):
    return WINDOW_WIDTH * (percent/100)

def percentHeight(percent):
    return WINDOW_HEIGHT * (percent/100)

def createRectangle(xStart, yStart, width, height):
    return Rectangle(Point(xStart, WINDOW_HEIGHT - yStart), Point(xStart + width, WINDOW_HEIGHT - (yStart +  height)))

def createWindow():
    win = GraphWin(WINDOW_CAPTION, WINDOW_WIDTH, WINDOW_HEIGHT)
    win.setBackground(WINDOW_BACKGROUND_DAY)
    return win

def drawGround(win):
    rect = createRectangle(0, 0, percentWidth(100), GROUND_HEIGHT)
    rect.setFill(GROUND_COLOR)
    rect.setWidth(0)
    rect.draw(win)
    return rect

def drawHouse(win):
    rect = createRectangle((WINDOW_WIDTH - HOUSE_WIDTH)/2, GROUND_HEIGHT, HOUSE_WIDTH, HOUSE_HEIGHT)
    rect.setFill(HOUSE_COLOR)
    rect.setWidth(0)
    rect.draw(win)
    return rect

def drawRoof(win):
    print('eh')

def waitForClick(win):
    win.getMouse()

def main():
    win = createWindow()
    ground = drawGround(win)
    house = drawHouse(win)
    roof = drawRoof(win)
    waitForClick(win)

main()