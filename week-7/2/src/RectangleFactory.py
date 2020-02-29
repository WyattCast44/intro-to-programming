import random
from .ShapeFactory import ShapeFactory


class RectangleFactory(ShapeFactory):

    def __init__(self, bounds=[500, 500]):
        self.color = None
        self.bounds = bounds
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

        self.leftPoint = f'{random.randint(0, self.bounds[0])}, {random.randint(0, self.bounds[0])}'

        return self

    def setRightPoint(self):

        self.rightPoint = f'{random.randint(0, self.bounds[0])}, {random.randint(0, self.bounds[0])}'

        return self

    def make(self):

        self.setColor().setLeftPoint().setRightPoint()

        return f'Rectangle; {self.leftPoint}; {self.rightPoint}; {self.color}'
