import sys
from ConsoleIO import *

ConsoleIO().title('\nMy Console App - v0.1.0', ['green'])
ConsoleIO().line('This is my console app, for helping you do things.')

ConsoleIO().sectionWithList('Usage:', [
    f"python {sys.argv[0]} 'command' [arguments]",
])

ConsoleIO().sectionWithList('Options:', [
    "Enter 'h' for application help",
    "Enter 'v' for version",
])

ConsoleIO().sectionWithList('Commands:', [
    "Enter 'resume' to resume a saved game",
    "Enter 'new' to start a new game",
])