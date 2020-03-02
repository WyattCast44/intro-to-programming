class Item:

    def __init__(self, properties):

        self.name = properties['name']
        self.description = properties['desc']
        self.abilites = properties['abilities']

    def __str__(self):
        return f'\nName: {self.name}\nDescription: {self.description}\nAbilites: {self.abilites}'
