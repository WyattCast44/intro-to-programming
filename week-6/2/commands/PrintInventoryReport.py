from models import InventoryItem, Machine
from .LoadMachinesIntoState import LoadMachinesIntoState


class PrintInventoryReport:

    items = {}

    signature = 'print:inventory-report'

    description = 'Print a sortable inventory report for all machines'

    def __init__(self, application):
        self.application = application

    def handle(self):

        # Ensure we load up the source files
        self.application.runUnregisteredCommand(LoadMachinesIntoState)

        machines = self.application.state().get('machines')

        # Loop through each machine and get the data
        for machine in machines.getMachines():

            print(type(item), item.getId())
