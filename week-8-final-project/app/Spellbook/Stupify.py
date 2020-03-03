from app.Spell import Spell


class Stupify(Spell):

    def __init__(self):

        super().__init__({
            'incantation': 'stupify',
            'description': 'A spell used to temporarily stun a victim.'
        })

    def cast(self, enemy):

        print('TODO')
