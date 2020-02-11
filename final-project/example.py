# My Libraries
from console import Application

# Commands
from commands import Help

app = Application({
    'name': 'Invoice Calculator',
    'version': '0.1.0',
    'description': 'Summarize and get insights on your monthly sales invoices'
})

app.registerOptions({
    'h': Help
}).registerCommands({
    'new': 'Record a new sale',
    'export': 'Export all sales to a csv',
}).run()