from cliff import Application
from commands import ResumeGame, StartNewGame, ShowCredits

Application({
    'name': 'The Adventures of Starman - Final Project',
    'description': 'An interactive game for my final project',
    'version': '1.1.0',
    'interactive': True
}).registerCommands([
    StartNewGame,
    ShowCredits
]).run()
