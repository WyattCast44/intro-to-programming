class Foxx:

    def __init__(self, game):

        self.game = game
        self.health = 100
        self.keys = []

    def subtractHealth(self, amount):

        self.health = self.health - amount

        if self.health <= 0:

            self.game.end()

        return
