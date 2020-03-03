from app.Spell import Spell


class Expelliarmus(Spell):

    def __init__(self):

        super().__init__({
            'incantation': 'expelliarmus',
            'description': 'A spell used to disarm another wizard.'
        })

    def cast(self, player):

        status = player.attemptToRemoveWand()

        if status:
            # success
        else:
            # nope
