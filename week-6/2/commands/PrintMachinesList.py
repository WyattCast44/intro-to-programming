class PrintMachinesList:

    signature = 'print:machines-list'

    description = 'Print a list of all your machines and thier information'

    def __init__(self, application):
        self.application = application

    def handle(self):
        self.application.output().error('\nTODO\n')
