from .LoadMachinesIntoState import LoadMachinesIntoState


class PrintMachinesReport:

    signature = 'print:machines-report'

    description = 'Print a machine status report for all machines'

    def __init__(self, application):
        self.application = application

    def handle(self):

        # Ensure we load up the source files
        self.application.runUnregisteredCommand(LoadMachinesIntoState)

        # Loop through each machine get the data, and build the line to print
        lines = []

        for machine in self.application.state().get('machines'):

            lines.append(
                f'{machine.getName()}     {machine.getPercentSold()}%     ${machine.getTotalSales()}')

        self.application.output().sectionWithList(
            'Label       % Sold     Total Sales', lines, '')
