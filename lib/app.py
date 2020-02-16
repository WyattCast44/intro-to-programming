from src import Application
from src.commands import MakeCommand, MakeOption
import commands

Application({
    'name': 'My App',
    'description': 'My first CLI app!',
    'version': '2.4.19'
}).registerCommands([
    MakeOption,
    MakeCommand,
    MyCommand
]).run()
