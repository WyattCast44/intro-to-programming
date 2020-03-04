from .Spell import Spell


class Riddikulus(Spell):

    def __init__(self):

        super().__init__({
            'incantation': 'riddikulus',
            'description': 'A spell used when fighting a Boggart; causes the Boggart to transform into something the caster finds humorous.'
        })

    def cast(self, enemy):

        if enemy.name != "Dementor":
            return "Merlins beard, the spell had no effect!"
        else:
            print('TODO')
