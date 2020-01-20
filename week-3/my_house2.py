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

import graphics as g

# Window
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 300
WINDOW_CAPTION = "My House"
WINDOW_BACKGROUND_DAY = g.color_rgb(237, 235, 218)
WINDOW_BACKGROUND_NIGHT = g.color_rgb(52, 63, 138)

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

# Roof
ROOF_COLOR = g.color_rgb(181, 88, 65)

def createWindow():
    win = g.GraphWin(WINDOW_CAPTION, WINDOW_WIDTH, WINDOW_HEIGHT)
    win.setBackground(WINDOW_BACKGROUND_DAY)
    return win

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

def drawRoof(win):
    roof = g.Polygon(g.Point(0,0), g.Point(HOUSE_WIDTH,0), g.Point(HOUSE_WIDTH/2, -35), g.Point(0,0))
    roof.setFill(ROOF_COLOR)
    roof.setOutline(ROOF_COLOR)
    roof.move((WINDOW_WIDTH / 2) - (HOUSE_WIDTH / 2), HOUSE_TOP_RIGHT.getY())
    roof.draw(win)

def drawSun(win):
    sun = g.Circle(g.Point(0,0), 50)
    sun.setFill(g.color_rgb(242, 219, 104))
    sun.setOutline(g.color_rgb(242, 219, 104))
    sun.draw(win)
    return sun

def changeToNightOnClick(win):
    win.getMouse()
    win.setBackground(WINDOW_BACKGROUND_NIGHT)
    
def changeSunToMoon(sun):
    sun.setFill(g.color_rgb(177, 181, 204))
    sun.setOutline(g.color_rgb(177, 181, 204))

def main():
    win = createWindow()
    drawGround(win)
    drawHouse(win)
    drawRoof(win)
    sun = drawSun(win)
    changeToNightOnClick(win)
    changeSunToMoon(sun)
    win.getMouse()

main()

