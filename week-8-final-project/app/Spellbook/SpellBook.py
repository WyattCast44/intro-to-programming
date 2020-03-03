from app.Stupify import Stupify
from app.Riddikulus import Riddikulus
from app.Expelliarmus import Expelliarmus


class SpellBook:

    spells = [
        Stupify,
        Riddikulus,
        Expelliarmus
    ]

    def __init__(self, application):

        self.application = application

        return

    def read(self):

        items = []

        for spell in self.spells:

            incantation = self.application.output().format('green', spell.incantation)

            items.append(f'{incantation} {spell.description}')

        self.application.output().sectionWithList('Spellbook:', items, ' ')
