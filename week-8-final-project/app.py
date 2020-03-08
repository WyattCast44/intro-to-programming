from cliff import Application
from commands import StartNewGame

Application({
    'name': 'The Adventures of Starman',
    'description': 'An interactive game for my final project',
    'version': '1.1.0',
    'interactive': True
}).registerCommands([
    StartNewGame
]).run()
