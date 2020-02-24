from options import Help
from cliff import Application
from commands import ReportChooser

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

app.run()
