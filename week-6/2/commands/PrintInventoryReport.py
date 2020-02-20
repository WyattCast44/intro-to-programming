class PrintInventoryReport:

    signature = 'print:inventory-report'

    description = 'Print a sortable inventory report for all machines'

    def __init__(self, application):
        self.application = application

    def handle(self):
        self.application.output().error('\nTODO\n')
