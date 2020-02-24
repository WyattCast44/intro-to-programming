import json
from models import InventoryItem
from .LoadMachinesIntoState import LoadMachinesIntoState


class PrintInventoryReport:

    signature = 'print:inventory-report'

    description = 'Print a sortable inventory report for all machines'

    def __init__(self, application):
        self.application = application

    def handle(self):

        # Ensure we load up the source files
        self.application.runUnregisteredCommand(LoadMachinesIntoState)

        # Map of item names to item classes
        items = {}

        for machine in self.application.state().get('machines'):

            # Loop through the slots
            for slot in machine.getSlots():

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

            sort = self.application.input().askWithOptions(
                'How would you like to sort the data?', {
                    'n': "Enter `n` to sort by item name",
                    'p': "Enter `p` to sort by percent of items sold",
                    's': "Enter `s` to sort by stock needs",
                    'q': "Enter `q` to quit"
                })

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

            lines = []

            for item in inventory:
                lines.append('{:20} {:8} {:8.2f}% {:8}   {:8}'.format(item.getName(), item.getNumberSold(), item.getSoldPct() * 100, item.
                                                                      getNumberInStock(), item.getStockNeed()))

            self.application.output().sectionWithList(
                'Item Name                Sold    % Sold       In-Stock   Stock-needs', lines, '')
