# Header

"""
Week 6 Review - Part 1
Wyatt Castaneda
SWDV 600: INTRO TO PROGRAMMING
"""
from helpers import *
from options import *
from commands import *

Application({
    'name': 'Unique List Finder',
    'description': 'A small tool to help you determine if a list of items is unique',
    'version': '1.0.0'
}).registerOptions([
    Help,
    Version,
    Problem
]).registerCommands([
    CheckListUnqiueness,
]).run()
