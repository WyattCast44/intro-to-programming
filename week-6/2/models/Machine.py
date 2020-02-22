import json


class Machine:

    attributes = {}

    source, rawContents, jsonContents = None, None, None

    def fromSource(self, path):
        self.source = path

        self.loadSource().parseContents()

        return self

    def loadSource(self):
        # Read the file into memory
        self.rawContents = open(self.source, 'r').read()

        return self

    def parseContents(self):

        # Get the raw json
        self.jsonContents = json.loads(self.rawContents)

        # Grab the id
        self.attributes['id'] = self.jsonContents['machine_id']

        # Grab the name
        self.attributes['name'] = self.jsonContents['machine_label']

        # Grab the content
        self.attributes['contents'] = self.jsonContents['contents']

        # Set the initial row count
        self.attributes['rowCount'] = 0

        for row in self.attributes['contents']:

            self.incrementRowCount()

            for slot in row['slots']:
                # each row has 9 slots
                p = 1

        # Need to parse the rows
        # in the rows, need to parse the slots
        # in the slots, need to parse the
        # - item name
        # - last stock
        # - current stock
        # Machine need to know how many slots it has

        return self

    def incrementRowCount(self):

        self.attributes['rowCount'] = self.attributes['rowCount'] + 1

    def __del__(self):

        print(self.attributes["id"], self.attributes["name"])

##
# A machine has rows
# A row has slots (9)
# A slot can hold up to 8 items
##


class InventoryReport:

    def __init__(self, machines):
        pass

    def handle(self):

        inventory = []

        sortChoice = ''

        while sortChoice != 'q':

            sortChoice = input(
                'Sort by (n)ame, (p)ercent sold, (s)tocking need, or (q) to quit: ')

            if sortChoice == 'n':

                inventoryItemsList.sort(key=InventoryItem.getName)
            elif sortChoice == 'p':
                inventoryItemsList.sort(key=InventoryItem.getSoldPct)
                inventoryItemsList.reverse()
            elif sortChoice == 's':
                inventoryItemsList.sort(key=InventoryItem.getStockNeed)
                inventoryItemsList.reverse()

            print('Item Name            Sold     % Sold     In Stock Stock needs')

            for item in inventoryItemsList:
                print('{:20} {:8} {:8.2f}% {:8} {:8}'.format(item.getName(), item.getNumberSold(), item.getSoldPct() * 100, item.
                                                             getNumberInStock(), item.getStockNeed()))

            print()
