class PrintMachinesReport:

    signature = 'print:machines-report'

    description = 'Print a machine status report for all machines'

    def __init__(self, application):
        self.application = application

    def handle(self):
        self.application.output().error('\nTODO\n')
