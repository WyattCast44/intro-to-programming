import random
from .ShapeFactory import ShapeFactory


class CircleFactory(ShapeFactory):

    def __init__(self, bounds=[500, 500]):
        self.color = None
        self.radius = None
        self.bounds = bounds
        self.centerPoint = None
        return

    def setColor(self):

        if random.randint(0, 1):
            self.color = random.choice(self.colors)
        else:
            self.color = self.defaultColor

        return self

    def setCenterPoint(self):

        self.centerPoint = f'{random.randint(0, self.bounds[0])}, {random.randint(0, self.bounds[0])}'

        return self

    def setRadius(self):

        self.radius = f'{random.randint(0, self.bounds[0]/2)}'

        return self

    def make(self):

        self.setColor().setCenterPoint().setRadius()

        return f'Circle; {self.centerPoint}; {self.radius}; {self.color}'
