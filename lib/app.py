from src import Application
from src.options import Help
from src.commands import MakeCommand, MakeOption


def setInteractive(app):
    app.state().upsert('config.interactive', True)


Application({
    'name': 'My App',
    'description': 'My first CLI app!',
    'version': '4.2.0'
}).registerCommands([
    MakeOption,
    MakeCommand,
]).registerOptions([
    Help
]).run()
