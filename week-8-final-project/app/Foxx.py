class Foxx:

    max_parts = 6

    def __init__(self, game):

        self.game = game
        self.health = 100
        self.amuletCount = 0

    def subtractHealth(self, amount):

        self.health = self.health - amount

        if self.health <= 0:

            self.game.end()

        return

    def getHealth(self):

        return self.health

    def addAmuletPart(self):

        self.amuletCount = self.amuletCount + 1

        return

    def getAmuletCount(self):

        return self.amuletCount
