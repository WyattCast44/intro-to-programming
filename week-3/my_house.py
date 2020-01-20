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

three rectangles ✅
two lines
one circle ✅
one text label ✅
Your picture should not be boring black and white. It should include at least three colors, tastefully distributed to bring your house to life.

Finally, it should have some interactive feature such that when a user clicks on your picture something changes (e.g. a color changes, a tree falls over, the sun rises, a door opens). The change only has to happen once.
"""

# Solution

import time
from graphics import *

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 300
WINDOW_CAPTION = "Mars Base 1"
WINDOW_BACKGROUND = color_rgb(45, 55, 72)

def percentWidth(percent):
    return WINDOW_WIDTH * (percent/100)

def percentHeight(percent):
    return WINDOW_HEIGHT * (percent/100)

def createRectangle(xStart, yStart, width, height):
    return Rectangle(Point(xStart, WINDOW_HEIGHT - yStart), Point(xStart + width, WINDOW_HEIGHT - (yStart +  height)))

def createWindow():
    win = GraphWin(WINDOW_CAPTION, WINDOW_WIDTH, WINDOW_HEIGHT)
    win.setBackground(WINDOW_BACKGROUND)
    return win

def drawSun(win):
    sun = Circle(Point(0,0), 50)
    sun.setFill(color_rgb(242, 219, 104))
    sun.setOutline(color_rgb(242, 219, 104))
    sun.draw(win)
    return sun

def drawMercury(win):
    mercury = Circle(Point(percentWidth(45), percentHeight(22)), 3)
    mercury.setFill(color_rgb(168, 164, 151))
    mercury.setOutline('black')
    mercury.draw(win)
    return mercury

def drawVenus(win):
    venus = Circle(Point(percentWidth(30), percentHeight(10)), 8)
    venus.setFill(color_rgb(224, 21, 2))
    venus.setOutline('black')
    venus.draw(win)
    return venus

def drawEarth(win):
    earth = Image(Point(percentWidth(75), percentHeight(30)), "earth.png")
    earth.draw(win)
    return earth

def drawMars(win):
    mars = Circle(Point(percentWidth(50),percentHeight(150)), 300)
    mars.setFill(color_rgb(194, 87, 0))
    mars.setOutline('black')
    mars.setWidth(1)
    mars.draw(win)
    return mars

def drawBase(win):
    dome = Circle(Point(percentWidth(50), percentHeight(75)), 30)
    dome.setFill(color_rgb(174, 218, 232))
    dome.setOutline(color_rgb(92, 131, 156))
    dome.setWidth(2)
    dome.draw(win)

    base = createRectangle(percentWidth(40), percentHeight(15), 100, 30)
    base.setFill(color_rgb(161, 170, 173))
    base.setOutline('black')
    base.setWidth(2)
    base.draw(win)

    door = createRectangle(percentWidth(48), percentHeight(15), 10, 18)
    door.setFill(color_rgb(64, 68, 71))
    door.setOutline('black')
    door.setWidth(1)
    door.draw(win)

def drawMessage(win):
    message = "Welcome to Mars Base 1. Click to Play."
    message = Text(Point(percentWidth(50), percentHeight(93)), message)
    message.setFill('black')
    # message.setStyle('bold')
    message.draw(win)
    return message

def drawLaunchPad(win):
    pad = createRectangle(percentWidth(64), percentHeight(20), 40, 10)
    pad.setFill(color_rgb(64, 68, 71))
    pad.setOutline('black')
    pad.setWidth(1)
    pad.draw(win)

    rocket1 = Image(Point(percentWidth(68), percentHeight(75)), "rocket.png")
    rocket1.draw(win)

    rocket2 = rocket1.clone()
    rocket2.draw(win)
    rocket2.move(12,0)

    rocket3 = rocket1.clone()
    rocket3.draw(win)
    rocket3.move(-12,0)

    return rocket1

def updateMessage(message, text):
    message.setText(text)

def launchRocket(win, rocket, message):
    rocket.move(0, -10)
    sleep(0.15)
    updateMessage(message, "Trajectory is nominal.")
    rocket.move(5, -20)
    sleep(0.15)
    rocket.move(10, -30)
    sleep(0.15)
    rocket.move(5, -10)
    sleep(0.15)
    updateMessage(message, "Earth orbit insertion burn complete.")
    rocket.move(6, -8)
    sleep(0.2)
    rocket.move(7, -10)
    sleep(0.1)
    rocket.move(8, -10)
    sleep(0.1)
    rocket.move(10, -10)
    sleep(0.1)
    rocket.move(10, -10)
    sleep(0.2)

def waitForClick(win):
    win.getMouse()

def sleep(seconds):
    time.sleep(seconds)

def main():

    # Setup the world
    win = createWindow()
    drawSun(win)
    drawMercury(win)
    drawVenus(win)
    drawEarth(win)
    drawMars(win)
    drawBase(win)

    message = drawMessage(win)
    rocket = drawLaunchPad(win)

    waitForClick(win)

    # Start the game
    updateMessage(message, "Your mission, should you choose to accept it.")
    sleep(1.7)
    updateMessage(message, "Will be to launch Starship to Earth.")
    sleep(1.7)
    updateMessage(message, "If you accept, simply click the window.")
    waitForClick(win)

    # Launch sequence
    sleep(1)
    updateMessage(message, "The launch director has cleared Starship for liftoff.")
    sleep(2)
    updateMessage(message, "Starship has begun it's startup sequence.")
    sleep(3.5)
    updateMessage(message, "Starship has trasitioned to internal power.")
    sleep(1.5)
    updateMessage(message, "Starship has completed it's internal inspection.")
    sleep(1.5)
    updateMessage(message, "All systems go for launch.")
    sleep(1.5)
    updateMessage(message, "Starting countdown. 5...")
    sleep(1)
    updateMessage(message, "4...")
    sleep(1)
    updateMessage(message, "3...")
    sleep(1)
    updateMessage(message, "2...")
    sleep(1)
    updateMessage(message, "1...")
    sleep(1)
    updateMessage(message, "Launch!")
    sleep(1)
    launchRocket(win, rocket, message)
    sleep(2)
    updateMessage(message, "Starship established in a safe orbit! Thanks for playing!")
    sleep(3)
    updateMessage(message, "Click to exit.")
    waitForClick(win)

main()