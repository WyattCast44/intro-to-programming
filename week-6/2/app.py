from cliff import Application
from options import (Help)
from commands import (ReportChooser)
from models import Machines

app = Application({
    'name': 'Vending Machine Inventory Management Tool',
    'description': 'A small tool to help keep track of your vending machine empire',
    'version': '1.2.0',
}).registerCommands([
    ReportChooser,
]).registerOptions([
    Help
]).setDefaultCommand(ReportChooser)

app.state().set('sources', [
    app.state().get("cwd") + '/data/REID_1F_20171004.json',
    app.state().get("cwd") + '/data/REID_2F_20171004.json',
    app.state().get("cwd") + '/data/REID_3F_20171004.json',
])

# machiness = Machines().loadSources(app.state().get('sources'))

# print(machiness, machiness.getMachines())

app.run()
