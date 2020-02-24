from models import InventoryItem, Machine
from .LoadMachinesIntoState import LoadMachinesIntoState


class PrintInventoryReport:

    items = {}

    signature = 'print:inventory-report'

    description = 'Print a sortable inventory report for all machines'

    def __init__(self, application):
        self.application = application

    def readMachinesIntoState(self):

        # Load the machines data files into the app state

        machines = []

        for path in self.application.state().get('sources'):

            machines.append(Machine().fromSource(path))

        self.application.state().set('machines', machines)

    def parseMachinesData(self):

        for machine in self.application.state('machines'):

            # Get the machines content
            contents = machine['contents']

            # Loop through the rows
            for row in contents:

                # Loop through the slots in each row
                for slot in row['slots']:

                    # Get the name of the item in the slot
                    name = slot['item_name']

                    # Set/update the item in the items list
                    item = self.items.get(name, InventoryItem(name))

                    # Update item numbers
                    item.addToStocked(slot['last_stock'])
                    item.addToInStock(slot['current_stock'])
                    item.incrementSlots()

                    # Update the item in the items list
                    items[name] = item

    def handle(self):

        # Ensure we load up the source files
        self.application.runUnregisteredCommand(LoadMachinesIntoState)

        # self.parseMachinesData()

        # Set the initial sort
        # sort = ''

        # inventory = list(items.values())

        # while sort != 'q':

        #   sort = input(
        #        '\nSort by (n)ame, (p)ct sold, (s)tocking need, or (q) to quit: ')

        #    if sort == 'n':
        #         # Sort by name
        #         inventory.sort(key=InventoryItem.getName)
        #     elif sort == 'p':
        #         # Sort by percent sold
        #         inventory.sort(key=InventoryItem.getSoldPct)
        #         inventory.reverse()
        #     elif sort == 's':
        #         # Sort by stock
        #         inventory.sort(key=InventoryItem.getStockNeed)
        #         inventory.reverse()

        #     print('\nItem Name            Sold     % Sold     In Stock Stock needs')

        #     for item in inventory:
        #         print('{:20} {:8} {:8.2f}% {:8} {:8}'.format(item.getName(), item.getNumberSold(), item.getSoldPct() * 100, item.
        #                                                      getNumberInStock(), item.getStockNeed()))

    def printReport(self):

        print()
