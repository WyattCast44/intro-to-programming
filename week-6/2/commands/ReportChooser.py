from .PrintInventoryReport import PrintInventoryReport
from .PrintMachinesReport import PrintMachinesReport


class ReportChooser:

    signature = 'reports:choose'

    description = 'Allows you to choose a report to view.'

    def __init__(self, application):
        self.application = application

    def handle(self):

        options = {
            'm': 'Enter `m` for the machines report',
            'i': 'Enter `i` for the inventory report',
        }

        choice = self.application.input().askWithOptions(
            'Please choose which report you would like to view:', options)

        if choice == 'm':
            self.application.runUnregisteredCommand(PrintMachinesReport)
        elif choice == 'i':
            self.application.runUnregisteredCommand(PrintInventoryReport)
