import random
from ShapeFactory import ShapeFactory


class RectangleFactory(ShapeFactory):

    def __init__(self):
        self.color = None
        self.leftPoint = None
        self.rightPoint = None
        return

    def setColor(self):

        if random.randint(0, 1):
            self.color = random.choice(self.colors)
        else:
            self.color = self.defaultColor

        return self

    def setLeftPoint(self):
        return self

    def setRightPoint(self):
        return self

    def make(self):

        self.setColor().setLeftPoint().setRightPoint()

        return f'Rectangle; {self.leftPoint}, {self.rightPoint}; {self.color}'
