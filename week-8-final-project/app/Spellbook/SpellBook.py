from .Stupify import Stupify
from .Riddikulus import Riddikulus
from .Expelliarmus import Expelliarmus


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

            spell = spell()

            incantation = self.application.output().format('green', spell.incantation)

            items.append(f'{incantation} {spell.description}')

        self.application.output().sectionWithList('Spellbook:', items, ' ')
