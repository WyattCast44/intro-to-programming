# My Libraries
from console import Application

# Options
from options import Help

# Commands
from commands import Version

# app = Application({
#     'name': 'Invoice Calculator',
#     'version': '0.1.0',
#     'description': 'Summarize and get insights on your monthly sales invoices'
# })

# app.registerOptions([
#     Help,
#     Version,
# ]).registerCommands({
#     'new': 'Record a new sale',
#     'export': 'Export all sales to a csv',
# }).run()

app = Application()

app.run()