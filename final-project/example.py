# My Libraries
from console import Application

# Options
from options import Help
from options import Version

# Commands
from commands import MakeView
from commands import MakeCommand

import commands

app = Application({
    'name': 'Invoice Calculator',
    'version': '0.1.0',
    'description': 'Summarize and get insights on your monthly sales invoices'
})

app.registerOptions([
    Help,
    Version
]).registerCommands([
    MakeView,
    MakeCommand
]).run()