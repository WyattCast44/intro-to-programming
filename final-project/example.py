# My Libraries
from console import Application

# Options
from options import Help
from options import Version

# Commands
from commands import MakeView
from commands import MakeCommand

tap(Application({
    'name': 'Invoice Calculator',
    'version': '0.1.0',
    'description': 'Summarize and get insights on your monthly sales invoices'
})).registerCommands([
    MakeView,
    MakeCommand
]).registerOptions([
    Help,
    Version
]).run()