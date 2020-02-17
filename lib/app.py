from src import Application
from src.commands import MakeCommand, MakeOption


def setInteractive(app):
    app.state().upsert('config.interactive', True)


Application({
    'name': 'My App',
    'description': 'My first CLI app!',
    'version': '2.4.19'
}).registerCommands([
    MakeOption,
    MakeCommand,
]).registerOptions({
    '--i': setInteractive
}).run()
