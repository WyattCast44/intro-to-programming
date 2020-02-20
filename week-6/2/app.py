from cliff import Application
from options import Problem, Version
from commands import PrintInventoryReport, PrintMachinesList, PrintMachinesReport, ReadSourcesIntoState

app = Application({
    'name': 'Vending Machine Inventory Checker',
    'description': 'A small tool to help keep track of your vending machine empire',
    'version': '1.2.0',
}).registerCommands([
    PrintMachinesList,
    ReadSourcesIntoState,
    PrintMachinesReport,
    PrintInventoryReport,
]).registerOptions([
    Problem,
    Version
])

app.state().set('sources', [
    app.state().get("cwd") + '/data/REID_1F_20171004.json',
    app.state().get("cwd") + '/data/REID_2F_20171004.json',
    app.state().get("cwd") + '/data/REID_3F_20171004.json',
])

app.run()
