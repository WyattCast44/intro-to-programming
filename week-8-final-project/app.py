from cliff import Application
from cliff.commands import MakeCommand

# Init the database
# db = TinyDB('db.json')

Application({
    'name': 'Final Project',
    'description': 'An interactive game for my final project',
    'version': '0.1.0'
}).registerCommands([
    MakeCommand
]).run()
