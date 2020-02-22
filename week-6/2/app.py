from cliff import Application
from options import Problem, Version
from commands import PrintInventoryReport, PrintMachinesList, PrintMachinesReport, ReadSourcesIntoState

app = Application({
    'name': 'Vending Machine Inventory Management Tool',
    'description': 'A small tool to help keep track of your vending machine empire',
    'version': '1.2.0',
    'interactive': True
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

""""

Outline:

- Need to get parse each data file and create a machine from it
- For each machine, need to parse the given JSON file and determine inner state
    - percent sold
    - total sales
    - rows count
    - items stocked
    - count of each item stocked

- Need a way for all machine to still report the general inventory

- Machine
- Inventory

"""
