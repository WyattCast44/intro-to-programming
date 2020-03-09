from time import sleep


class Foxx:

    def __init__(self, game, application):

        self.game = game
        self.health = 100
        self.amuletCount = 0
        self.application = application

    def subtractHealth(self, amount):

        self.health = self.health - amount

        if self.health <= 0:

            self.application.output().typed('You have died!', 0.05, 'red')

            sleep(1.5)

            self.game.end()

        return

    def getHealth(self):

        return self.health

    def addAmuletPart(self):

        self.amuletCount = self.amuletCount + 1

        totalAmulets = self.application.state().get('puzzle').amuletCount

        if self.amuletCount == totalAmulets:
            self.game.end(didWin=True)

        return

    def getAmuletCount(self):

        return self.amuletCount
