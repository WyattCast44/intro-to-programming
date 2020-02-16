from helpers import *
from options import *
from commands import *

app = Application({
    'name': 'Vending Machine Inventory Checker',
    'description': 'A small tool to help keep track of your vending machine empire',
    'version': '0.1.2'
}).registerOptions([
    Help,
    Version,
    Problem, 
    Interactive
]).registerCommands([
    ReadSourcesIntoState
]).setDefaultCommand(Interactive)

app.state().set('sources', [
    app.config['cwd'] + '/data/REID_1F_20171004.json', 
    app.config['cwd'] + '/data/REID_2F_20171004.json',
    app.config['cwd'] + '/data/REID_3F_20171004.json',
])

app.run()