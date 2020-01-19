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

three rectangles
two lines
one circle
one text label
Your picture should not be boring black and white. It should include at least three colors, tastefully distributed to bring your house to life.

Finally, it should have some interactive feature such that when a user clicks on your picture something changes (e.g. a color changes, a tree falls over, the sun rises, a door opens). The change only has to happen once.
"""

# Solution

import graphics as g

# Window
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 300
WINDOW_CAPTION = "My House"

def ptFromBottomLeft(x, y):
    # Used to reset the negative y axis
    return g.Point(x, WINDOW_HEIGHT - y)

# Ground
GROUND_HEIGHT = 50
GROUND_COLOR = g.color_rgb(108, 166, 119)

# House
HOUSE_WIDTH = 150
HOUSE_HEIGHT = 75
HOUSE_BOTTOM_LEFT = ptFromBottomLeft((WINDOW_WIDTH / 2) - (HOUSE_WIDTH / 2), GROUND_HEIGHT)
HOUSE_TOP_RIGHT = ptFromBottomLeft((WINDOW_WIDTH / 2) + (HOUSE_WIDTH / 2), GROUND_HEIGHT + HOUSE_HEIGHT)
HOUSE_COLOR = g.color_rgb(166, 149, 108)

def drawGround(win):
    ground = g.Rectangle(ptFromBottomLeft(0,0), ptFromBottomLeft(WINDOW_WIDTH, GROUND_HEIGHT))
    ground.setOutline(GROUND_COLOR)
    ground.setFill(GROUND_COLOR)
    ground.draw(win)

def drawHouse(win):
    house = g.Rectangle(HOUSE_BOTTOM_LEFT, HOUSE_TOP_RIGHT)
    house.setOutline(HOUSE_COLOR)
    house.setFill(HOUSE_COLOR)
    house.draw(win)

def main():
    win = g.GraphWin(WINDOW_CAPTION, WINDOW_WIDTH, WINDOW_HEIGHT)
    drawGround(win)
    drawHouse(win)
    win.getMouse()

main()

