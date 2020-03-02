class Enemy:

    def __init__(properties):

        self.name = properties['name']
        self.health = properties['health']
        self.description = properties['desc']
        self.strengths = properties['strengths']
        self.weaknesses = properties['weaknesses']

        return

    def __str__(self):
        return f'\nName: {self.name}\nDescription: {self.description}\nStrengths: {self.strengths}\nWeaknesses: {self.weaknesses}'
