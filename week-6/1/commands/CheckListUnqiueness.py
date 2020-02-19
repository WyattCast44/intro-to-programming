from helpers import collect


class CheckListUnqiueness:

    signature = 'check-list'

    description = 'An interactive proccess to check a lists uniqueness'

    def __init__(self, application):
        self.application = application

    def handle(self):

        # Print instructions
        self.application.console().sectionWithList('List Input', [
            f'Enter -1 to finish entering items'
        ])

        # Accumulator
        items = []

        # First item
        item = self.application.console().ask('Enter the first item?')

        # Get more items
        while not item == '-1':
            items.append(item)

            item = self.application.console().ask('Enter the next item?')

        # Determine list uniqueness
        if collect(items).unique():
            self.application.console().success(
                f'\nThe sequence {items} is unique!')
        else:
            self.application.console().error(
                f'\nThe sequence {items} is not unique!')
