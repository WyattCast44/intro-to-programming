from .Item import Item


class InvisibilityCloak(Item):

    def __init__(self):

        super().__init__({
            'name': 'Cloak of Invisibility',
            'desc': 'A somewhat ragged looking cloak, that will make you invisible to enemies for three turns. Use it wisely...',
            'abilities': [
                'Wear',
                'Remove',
            ]
        })

        return
