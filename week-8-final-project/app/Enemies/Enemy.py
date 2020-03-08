class Enemy:

    def __init__(self, healthPoints, attackPoints):

        self.healthPoints = healthPoints
        self.attackPoints = attackPoints

        return self

    def attack(self, player):
