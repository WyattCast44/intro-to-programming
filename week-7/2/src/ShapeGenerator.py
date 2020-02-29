import random
from .CircleFactory import CircleFactory
from .RectangleFactory import RectangleFactory


class ShapeGenerator:

    shapes = {
        'Circle': CircleFactory,
        'Rectangle': RectangleFactory
    }

    def random(self):

        shape = random.choice(list(self.shapes.keys()))

        return self.shapes[shape]().make()
