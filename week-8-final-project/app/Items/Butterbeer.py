from .Item import Item


class Butterbeer(Item):

    def __init__(self):

        super().__init__({
            'name': 'Butterbeer',
            'desc': 'An old butterbeer bottle, there seems to be more than a few floating items in it...',
            'abilities': [
                'Drink'
            ]
        })

        return
