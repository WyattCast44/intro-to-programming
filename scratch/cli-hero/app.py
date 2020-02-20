from src import Application
from src.options import Help, Verbose
from src.commands import MakeCommand, MakeOption

Application({
    'name': 'My App',
    'description': 'My first CLI app!',
    'version': '4.2.0',
    'env': 'dev'
}).registerCommands([
    MakeOption,
    MakeCommand,
]).registerOptions([
    Help,
    Verbose
]).run()
