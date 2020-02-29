from ShapeFactory import ShapeFactory
from random import randint, choice


class CircleFactory(ShapeFactory):

    def __init__(self):
        self.color = None
        self.radius = None
        self.centerPoint = None
        return

    def setColor(self):

        if randint(0, 1):
            self.color = choice(self.colors)
        else:
            self.color = self.defaultColor

        return self

    def setCenterPoint(self):

        return self

    def setRadius(self):

        return self

    def make(self):

        self.setColor().setCenterPoint().setRadius()

        return f'Circle; {self.centerPoint}; {self.radius}; {self.color}'
