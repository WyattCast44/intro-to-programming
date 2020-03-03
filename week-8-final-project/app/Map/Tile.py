class Tile:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        return

    def message(self):
        raise Exception("You did not implement a message method.")
