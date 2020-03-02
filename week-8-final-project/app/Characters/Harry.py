from .Player import Player


class Harry(Player):

    def __init__(self):

        super().__init__({
            'health': 10,
            'name': "Harry Potter",
            'description': "You are a forth year gryffindor at Hogwarts.",
            'strengths': [
                'You are The-chosen-one',
                'Bravery'
            ],
            'weaknesses': [
                'Young'
            ]
        })

        return
