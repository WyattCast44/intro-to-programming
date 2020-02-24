import json


class InventoryItem:

    def __init__(self, name):
        self.name = name
        self.totalSlots = 0
        self.totalStocked = 0
        self.totalInStock = 0

    def addToStocked(self, stockAmt):
        self.totalStocked = self.totalStocked + stockAmt

    def addToInStock(self, inStockAmt):
        self.totalInStock = self.totalInStock + inStockAmt

    def incrementSlots(self):
        self.totalSlots = self.totalSlots + 1

    def getNumberSold(self):
        return self.totalStocked - self.totalInStock

    def getSoldPct(self):
        return self.getNumberSold() / self.totalStocked

    def getStockNeed(self):
        return 8 * self.totalSlots - self.totalInStock

    def getName(self):
        return self.name

    def getNumberInStock(self):
        return self.totalInStock

    def __repr__(self):
        return '{} In Stock: {}, Stocked: {}, Slots: {}'.format(self.name, self.totalInStock, self.totalStocked, self.totalSlots)


class MachineStatus:

    currentStock = None
    totalSales = None
    percentSold = None


def choice1():
    print('w')


def choice2():
    print('e')


def main():

    options = {
        'm': choice1,
        'i': choice2
    }

    message = '\n> Which you like to view the (m)achine report or the (i)nventory report? '

    choice = input(message)

    while not choice in options:

        path = input(message)

    options[choice]()

    quit()

    # List of source files
    files = [
        "../data/REID_1F_20171004.json",
        "../data/REID_2F_20171004.json",
        "../data/REID_3F_20171004.json",
    ]

    # Map of item names to item classes
    items = {}

    for source in files:

        # Get the json from the source file
        data = json.loads(open(source, 'r').read())

        # Get the main content
        contents = data['contents']

        # Loop through the rows
        for row in contents:

            # Loop through the slots in each row
            for slot in row['slots']:

                # Get the name of the item in the slot
                name = slot['item_name']

                # Set/update the item in the items list
                item = items.get(name, InventoryItem(name))

                # Update item numbers
                item.addToStocked(slot['last_stock'])
                item.addToInStock(slot['current_stock'])
                item.incrementSlots()

                # Update the item in the items list
                items[name] = item

    # Set the initial sort
    sort = ''

    inventory = list(items.values())

    while sort != 'q':

        sort = input(
            '\nSort by (n)ame, (p)ct sold, (s)tocking need, or (q) to quit: ')

        if sort == 'n':
            # Sort by name
            inventory.sort(key=InventoryItem.getName)
        elif sort == 'p':
            # Sort by percent sold
            inventory.sort(key=InventoryItem.getSoldPct)
            inventory.reverse()
        elif sort == 's':
            # Sort by stock
            inventory.sort(key=InventoryItem.getStockNeed)
            inventory.reverse()

        print('\nItem Name            Sold     % Sold     In Stock Stock needs')

        for item in inventory:
            print('{:20} {:8} {:8.2f}% {:8} {:8}'.format(item.getName(), item.getNumberSold(), item.getSoldPct() * 100, item.
                                                         getNumberInStock(), item.getStockNeed()))

        print()


main()
